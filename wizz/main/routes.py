import os
import secrets
from docx2pdf import convert
from PIL import Image
from . import main
from ..models import Document, NewDocument
from ..email import send_mail
from wizz import db
from flask import json, render_template, redirect, request, current_app, url_for, abort, send_from_directory, flash, jsonify
from werkzeug.utils import secure_filename

try:
    import pythoncom
except Exception as e:
    pass

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@main.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template("Dashboard.html")

@main.route('/select-document/<pdf>', methods=['GET', 'POST'])
def selectDocument(pdf):
    document = NewDocument.query.filter_by(name=pdf).first()
    link = "http://localhost:5000/clientCreate/" + document.name
    print(link)
    return render_template("select-document.html", link=link, pdf=document.name, document=document)

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

@main.route('/clientCreate/<image>', methods=['GET', 'POST'])
def clientCreate(image):
    imagePdf = NewDocument.query.filter_by(name=image).first()
    return render_template("create.html", imagePdf=imagePdf.name)


@main.route('/upload', methods=['GET', 'POST'])
def getFile():
    if request.method == "POST":
        uploaded_file = request.files["file"]
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in current_app.config['UPLOAD_EXTENSIONS']:
                print("Abort 400")
                abort(400)
            if file_ext != ".pdf" and file_ext in current_app.config["WORD_EXTENSIONS"]:
                picture_file = save_picture(uploaded_file)
                picture_path = os.path.join(
                                current_app.root_path, 'static/images', picture_file)
                try:
                    pythoncom.CoInitialize()
                except Exception as e:
                    raise e
                convert(picture_path)
                pdf_file_name = picture_file.split(".")[0]
                pdf_file_with_ext = pdf_file_name + ".pdf"
                print(pdf_file_with_ext)
                document = Document(image_file=pdf_file_with_ext, name="Adegoke Bright")
                db.session.add(document)
                db.session.commit()
                print("File uploaded successfully...............")
                flash('Your file has been successfully uploaded!', 'success')
                return redirect(url_for("main.create", image=pdf_file_with_ext))


            elif file_ext != ".pdf" and file_ext in current_app.config["PICTURE_EXTENSIONS"]:
                picture_file = save_picture(uploaded_file)
                picture_path = os.path.join(
                                current_app.root_path, 'static/images', picture_file)
                image1 = Image.open(picture_path)
                im1 = image1.convert('RGB')
                pdf_file_name = picture_file.split(".")[0]
                pdf_file_with_ext = pdf_file_name + ".pdf"
                new_picture_path = os.path.join(
                                current_app.root_path, 'static/images', pdf_file_with_ext)
                im1.save(new_picture_path)
                print(pdf_file_with_ext)
                document = Document(image_file=pdf_file_with_ext, name="Adegoke Bright")
                db.session.add(document)
                db.session.commit()
                print("File uploaded successfully...............")
                flash('Your file has been successfully uploaded!', 'success')
                return redirect(url_for("main.create", image=pdf_file_with_ext))
            else:
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
    # information = request.data
    # print("information -", information, type(information))
    document = Document.query.filter_by(image_file=filename).first()
    document.saved_image_file = document.image_file
    db.session.commit()
    print("File saved successfully...............")
    return redirect(request.referrer)


@main.route('/uploadForClient', methods=['GET', 'POST'])
def uploadForClient():
    if request.method == "POST":
        uploaded_file = request.files["file"]
        print(uploaded_file)
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in current_app.config['AGENT_UPLOAD_EXTENSIONS']:
                print("Abort 400")
                abort(400)
            picture_file = save_picture(uploaded_file)
            document = NewDocument(name=picture_file)
            db.session.add(document)
            db.session.commit()
            flash('Your file has been successfully uploaded!', 'success')
            return redirect(url_for("main.selectDocument", pdf=picture_file))
    
    
    return render_template("fill.html")

   

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
            current_app.root_path, 'static/images', picture_fn)
    form_picture.save(picture_path)

    return picture_fn


# href="mailto:brightaverix@gmail.com?subject=HI&body={{link}}"