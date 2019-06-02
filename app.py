from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_restful import Resource

## owned packages
from work_files import WorkFiles
from sky_biometry import SkyBiometry

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
        return render_template('vazia.html', title='Home', label='Perfis', texto='Dados sobre os perfis')
    else:
        return render_template('index.html', title='Home', dados=sky_resultados)

@app.route('/cluster')
def cluster():
    wf = WorkFiles()
    try:
        clusters = wf.listAllClusters()
        pastas = []
        for k, v in clusters.items():
            pastas.append(k)
    except:
        clusters = []
        
    if len(clusters) == 0:
        return render_template('vazia.html', title='Cluster', label='Clusters', texto='Rostos separados por pessoa')
    else:
        return render_template('cluster.html', title='Cluster', clusters=clusters, quantidade=len(pastas))

@app.route('/cluster/<pasta>')
def cluster_pasta(pasta):
    wf = WorkFiles()
    imagens = wf.listImagesFromCluster(pasta)
    return render_template('pasta.html', title='Pasta', imagens=imagens, pasta=pasta)






## RUNNING AND DEBUGGING
if __name__ == '__main__':
    app.run(debug=True)