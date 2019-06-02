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




# @app.route("/")
# @app.route("/home")
# @app.route("/index")
# def index():
#     return render_template('index.html', title='Home')

# @app.route("/sky")
# def skypage():
#     return render_template('skypage.html', title= 'API')

# @app.route("/consulta", methods=['POST'])
# def consultaSky():
#     url = request.form['url']
#     biometry = SkyBiometry().skyBiometry(url)
    
#     #biometry = {'status': 'success', 'photos': [{'url': 'http://www.wallpapermaiden.com/image/2016/11/10/redhead-model-smiling-blue-eyes-bare-shoulders-pink-lipstick-open-mouth-girls-9129.jpg', 'pid': 'F@03d1a5d56d64bc036f9e45253715b9ab_44aad7d559364', 'width': 2048, 'height': 1362, 'tags': [{'uids': [], 'label': None, 'confirmed': False, 'manual': False, 'width': 29.35, 'height': 39.43, 'yaw': -9, 'roll': -3, 'pitch': -15, 'attributes': {'face': {'value': 'true', 'confidence': 72}, 'gender': {'value': 'female', 'confidence': 100}, 'glasses': {'value': 'false', 'confidence': 100}, 'dark_glasses': {'value': 'false', 'confidence': 69}, 'smiling': {'value': 'true', 'confidence': 20}, 'age_est': {'value': '23', 'confidence': 50}, 'mood': {'value': 'neutral', 'confidence': 80}, 'lips': {'value': 'parted', 'confidence': 89}, 'eyes': {'value': 'open', 'confidence': 100}, 'neutral_mood': {'value': 'true', 'confidence': 80}, 'anger': {'value': 'false', 'confidence': 45}, 'disgust': {'value': 'false', 'confidence': 0}, 'fear': {'value': 'false', 'confidence': 0}, 'happiness': {'value': 'true', 'confidence': 62}, 'sadness': {'value': 'false', 'confidence': 0}, 'surprise': {'value': 'true', 'confidence': 73}}, 'points': None, 'similarities': None, 'tid': 'TEMP_F@03d1a5d56d64bc036f9e4525042b01f8_44aad7d559364_52.10_37.00_0_1', 'recognizable': True, 'center': {'x': 52.1, 'y': 37.0}, 'eye_left': {'x': 61.28, 'y': 23.35, 'confidence': 94, 'id': 449}, 'eye_right': {'x': 47.31, 'y': 24.89, 'confidence': 97, 'id': 450}, 'mouth_center': {'x': 54.79, 'y': 44.86, 'confidence': 93, 'id': 615}, 'nose': {'x': 56.49, 'y': 38.62, 'confidence': 93, 'id': 403}}]}], 'usage': {'used': 15, 'remaining': 85, 'limit': 100, 'reset_time': 1559007639, 'reset_time_text': 'Tue, 28 May 2019 01:40:39 +0000'}, 'operation_id': 'bae90d1b92e94e548f5ec8b1fb7e9e40', 'cur_date': '20190527223748571517', 'dev_type': 'entrance'}
#     return render_template('gallery.html', data=biometry, title='API')
#     # return redirect(url_for('gallery'data=biometry))


# @app.route("/teste", methods=['POST'])
# def ListaTodos():
#     biometry = SkyBiometry().listAllData()
#     return render_template('teste.html', data=biometry, title='API')