from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_restful import Resource

## owned packages
from work_files import WorkFiles
from sky_biometry import SkyBiometry
from face_streaming import FaceStreaming

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    biometry = SkyBiometry()
    try:
        sky_resultados = biometry.listAllData()
    except:
        sky_resultados = []
    
    if len(sky_resultados) == 0:
        return render_template('vazia.html', title='Home', label='Perfis', texto='Sem dados sobre os perfis')
    else:
        return render_template('index.html', title='Home', dados=sky_resultados)

@app.route('/cluster')
def cluster():
    wf = WorkFiles()
    try:
        clusters = wf.listAllClusters()
        pastas = []
        total_frames = 0
        for k, v in clusters.items():
            pastas.append(k)
            total_frames += len(v)
    except:
        clusters = []
        
    if len(clusters) == 0:
        return render_template('vazia.html', title='Cluster', label='Clusters', texto='Sem dados sobre os clusters')
    else:
        return render_template('cluster.html', title='Cluster', clusters=clusters, quantidade=len(pastas), total_frames=total_frames)

@app.route('/cluster/<pasta>')
def cluster_pasta(pasta):
    wf = WorkFiles()
    imagens = wf.listImagesFromCluster(pasta)
    return render_template('pasta.html', title='Pasta', imagens=imagens, pasta=pasta)


@app.route('/camera/', methods=['POST'])
def camera():
    streaming = FaceStreaming()
    if streaming.faceFromStreamingVideo():
        return render_template('resultado.html', title='Camera', label='Camera', texto='Frames capturados e clusterizados com sucesso')
    else:
        return render_template('resultado.html', title='Erro', label='Camera', texto='Não foi possível capturar os frames')
        
@app.route('/push', methods=['POST'])
def push_firebase():
    wf = WorkFiles()

    if wf.loadAllImagesToFirebase():
        return cluster()
    else:
        return render_template('resultado.html', title='Erro', label='Clusters', texto='Clusters não identificados')
    

## RUNNING AND DEBUGGING
if __name__ == '__main__':
    app.run(debug=True)