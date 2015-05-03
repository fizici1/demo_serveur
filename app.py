# -*-coding:utf-8 -*

from flask import Flask, render_template, Response
import gestionIO
import grovepi
from camera_pi import Camera

gestionIO.setupIO()

app = Flask(__name__)


@app.route('/')
@app.route('/donnees')
def index():
    return render_template('donnees.html')

@app.route('/controle')
def controleur():
    return render_template('controle.html')

@app.route('/streaming')
def materiel():
    return render_template('streaming.html')

@app.route('/description')
def logiciel():
    return render_template('description.html')

@app.route('/applications')
def applications():
    return render_template('applications.html')

@app.route('/applications/<app>/<etat>/<p1>/<p2>')
def active_applications(app,etat,p1,p2):
    gestionIO.lumiere(int(p1), int(p2), int(etat))
    return render_template('applications.html')

@app.route('/sensor_request')
def sensorRefresh():
    return gestionIO.readData()

@app.route('/<nom>/<etat>')
def controle(nom, etat):
    gestionIO.controle(nom, int(etat))
    

@app.route('/RGB/<rouge>/<vert>/<bleu>')
def RGB(rouge, vert, bleu):
    gestionIO.RGB(int(rouge), int(vert), int(bleu))
    

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
    app.run(host='192.168.1.32', port=5000)
