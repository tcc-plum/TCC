from sky_biometry import SkyBiometry
import requests

biometry = SkyBiometry()

url_sky = "https://api.skybiometry.com/fc/faces/detect.json?api_key=3ogvrg5ej8thp4r1lpa97tbhg9&api_secret=l9kus97mjm2cs0d5jup2ird06m&attributes=all"

retorno = requests.post(url_sky, files = {'media': open('./cluster/face_1/face_20190601210021837430.jpg', 'rb')})
print(retorno.json())
