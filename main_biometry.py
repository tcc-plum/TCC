from sky_biometry import SkyBiometry
import requests

biometry = SkyBiometry()

# url_sky = "https://api.skybiometry.com/fc/faces/detect.json?api_key=3ogvrg5ej8thp4r1lpa97tbhg9&api_secret=l9kus97mjm2cs0d5jup2ird06m&attributes=all"

# retorno = requests.post(url_sky, files = {'media': open('./cluster/face_1/face_20190601210021837430.jpg', 'rb')})
# print(retorno.json())


# resultado = biometry.listAllData()

# for chave, valor in resultado.items():
#     print(chave + ' ' + str(valor['photos'][0]['tags']))
    

# resultado = biometry.listData('-LgOpu-ulAxWJzMwQxnF')
# print(resultado)

# resultado = biometry.skyBiometry('./cluster/face_1/face_20190602171650671726.jpg', 
#                      'https://firebasestorage.googleapis.com/v0/b/teste-tcc-2c7b3.appspot.com/o/cluster%2Fface_20190602171650671726.jpg?alt=media&token=AIzaSyBYZqhEllq8-vN0XN_yBpav54CCVGRHq9E',
#                      'face_1_20190602171732514400')
# print(resultado)
