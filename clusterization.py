# pip install pyfacy

from pyfacy import face_clust
import os


class FaceClusterization:

    def __init__(self):
        __self__ = self

    def cluster(self, from_path, to_path):
        if not os.path.exists(from_path):
            print('O caminho informado não existe')
            return False

        if not os.path.exists(to_path):
            os.makedirs(to_path)

        try:
            cluster = face_clust.Face_Clust_Algorithm(from_path)
            cluster.load_faces()
            cluster.save_faces(to_path)
        except:
            print('Não foi possível clusterizar')
            return False

        return True
