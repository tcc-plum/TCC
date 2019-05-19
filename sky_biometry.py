# libraries
from PIL import Image
import requests
from io import BytesIO
import pyrebase
import datetime
import json
import os


class SkyBiometry:
    # constants
    SKY_API_KEY = "cqm6psmc935f0svh5igl162kc9"
    SKY_API_SECRET = "vj06aa6179mffof6h9mfvkrhcm"
    FIREBASE_KEY = "AIzaSyBYZqhEllq8-vN0XN_yBpav54CCVGRHq9E"
    FIREBASE_AUTH = "teste-tcc-2c7b3.firebaseapp.com"
    FIREBASE_DATABASE = "https://teste-tcc-2c7b3.firebaseio.com/"
    FIREBASE_STORAGE = "teste-tcc-2c7b3.appspot.com"

    def __init__(self, url_image):
        self.url_image = url_image

    # setting up Firebase application
    k_fields = ["apiKey", "authDomain", "databaseURL", "storageBucket"]
    v_fields = [FIREBASE_KEY, FIREBASE_AUTH, FIREBASE_DATABASE, FIREBASE_STORAGE]

    config = dict(zip(k_fields, v_fields))

    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    f_db = firebase.database()

    def getCurrentDateAsId(self):
        cur_date_str = json.dumps(datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'))
        cur_date_str = cur_date_str.replace('"', '')
        return cur_date_str

    # load image to Firebase storage
    def loadToFirebaseStorage(self, image, filename, f_key, f_storage):
        # load image to Firebase storage
        l_storage_file = filename + ".jpg"
        f_storage_path = "sky/" + l_storage_file

        if not os.path.exists('./img'):
            os.makedirs('./img')

        l_storage_path = './img/' + l_storage_file

        image.save(l_storage_path, "JPEG")

        result = f_storage.child(f_storage_path).put(l_storage_path, f_key)

        # remove picture from the local storage
        os.remove(l_storage_path)

        return result

    # load json to Firebase database
    def loadToFirebaseDatabase(self, f_db, json_file):
        result_db = f_db.child("sky").push(json_file)
        return result_db

    def skyBiometry(self):
        # read image from url
        image_http = requests.get(self.url_image)
        image = Image.open(BytesIO(image_http.content))

        # using Sky Biometry API for face detect
        url_sky_biometry = [
            "https://api.skybiometry.com/fc/faces/detect.json?api_key=" + self.SKY_API_KEY +
            "&api_secret=" + self.SKY_API_SECRET +
            "&urls=" + self.url_image + "&attributes=all"]
        sky_biometry = requests.get(url_sky_biometry[0]).json()
        # sky_biometry_json = sky_biometry.json()

        sky_biometry['cur_date'] = self.getCurrentDateAsId()
        sky_biometry['dev_type'] = 'entrance'

        pid = sky_biometry['operation_id']

        self.loadToFirebaseStorage(image, pid, self.FIREBASE_KEY, self.storage)
        self.loadToFirebaseDatabase(self.f_db, sky_biometry)

        print(sky_biometry)

