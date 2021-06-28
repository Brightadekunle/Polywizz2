import os
from io import StringIO
import secrets
from . import main
from ..models import Document
from wizz import db
from flask import json, render_template, redirect, request, current_app, url_for, abort, send_from_directory, flash, jsonify
from werkzeug.utils import secure_filename



@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@main.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template("Dashboard.html")

@main.route('/view-status', methods=['GET', 'POST'])
def viewStatus():
    return render_template("view-status.html")

@main.route('/select-document', methods=['GET', 'POST'])
def selectDocument():
    return render_template("select-document.html")

@main.route('/process-history', methods=['GET', 'POST'])
def processHistory():
    return render_template("process-history.html")

@main.route('/all-history', methods=['GET', 'POST'])
def allHistory():
    return render_template("all-history.html")


@main.route('/create/<image>', methods=['GET', 'POST'])
def create(image):
    imagePdf = Document.query.filter_by(image_file=image).first()
    return render_template("create.html", imagePdf=imagePdf.image_file)


@main.route('/upload', methods=['GET', 'POST'])
def getFile():
    
    if request.method == "POST":
        uploaded_file = request.files["file"]
        print(uploaded_file)
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in current_app.config['UPLOAD_EXTENSIONS']:
                print("Abort 400")
                abort(400)
            picture_file = save_picture(uploaded_file)
            document = Document(image_file=picture_file, name="Adegoke Bright")
            db.session.add(document)
            db.session.commit()
            print("File uploaded successfully...............")
            flash('Your file has been successfully uploaded!', 'success')
            return redirect(url_for("main.create", image=picture_file))
    
    
    return render_template("add-new.html")


@main.route('/save/<filename>', methods=['GET', 'POST'])
def download(filename):
    document = Document.query.filter_by(image_file=filename).first()
    # picture_file = save_picture(filename)
    document.saved_image_file = document.image_file
    db.session.commit()
    print("File saved successfully...............")
    return redirect(request.referrer)
    # picture_path = os.path.join(
    #         current_app.root_path, 'static/images')
    # return send_from_directory(directory=picture_path, filename=filename)


@main.route('/send/<filename>', methods=['GET', 'POST'])
def sendFile(filename):
    document = Document.query.filter_by(saved_image_file=filename).first()
    print(document.saved_image_file)
    return redirect(url_for("main.selectDocument"))

    


    
# @main.route('/save/<filename>', methods=['GET', 'POST'])
# def download(filename):
#     picture_path = os.path.join(
#             current_app.root_path, 'static/images')
#     return send_from_directory(directory=picture_path, filename=filename)
   

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
            current_app.root_path, 'static/images', picture_fn)
    form_picture.save(picture_path)

    return picture_fn