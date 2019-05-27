from flask_restful import Resource
from sky_biometry import SkyBiometry

class Sky(Resource):
    def post(self, url):
        biometry = SkyBiometry(url)
        print(url)
        return biometry.skyBiometry()
        # return SkyBiometry(url).skyBiometry(), 200
    
    def get(self, url):
        # biometry = SkyBiometry(url)
        print('url')
        return print(url)
        # return biometry.skyBiometry()
        # return SkyBiometry(url).skyBiometry(), 200