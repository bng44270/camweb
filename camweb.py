from pywebcam import PyWebCam
import os
from re import match as regex_match
from flask import Flask, render_template, send_file, request, make_response

class CamWeb(Flask):
  def __del__(self):
    super().__del__()
    camfiles = [a for a in os.listdir('/tmp') if regex_match(r'^pycam-',a)]

    for thisfile in camfiles:
      os.remove('/tmp/' + thisfile)

app = CamWeb(__name__)

cam = PyWebCam()

@app.route("/")
def GetRoot():
  camlist = cam.GetCams()
  return render_template('camview.html',cams = camlist)
  
@app.route("/<camera>.jpg")
def GetImageFile(camera):
  filepath = cam.Capture(camera)
  return send_file(filepath)

app.run("0.0.0.0",8080)
