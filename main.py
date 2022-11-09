from uuid import uuid4

from flask import Flask, send_from_directory, jsonify, send_file, request, redirect
import os

from pydub import AudioSegment

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route("/")
def index():
    # return render_template("index.html")
    return jsonify({"api": "ok"})


@app.route('/audio', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect('/')

        file = request.files['file']
        new_filename = str(uuid4()) + '.mp3'

        if file.filename == '':
            print('No selected file')
            return redirect('/')
        elif file and file.filename.rsplit('.', 1)[1].lower() == 'mp3':
            # If is mp3 no need to convert
            # file.save(new_filename)
            # return send_file(new_filename, as_attachment=True)
            return jsonify({"status": "ok", "filename": new_filename})
        elif file and 'audio' in file.mimetype:
            try:
                song = AudioSegment.from_file(file)
                # Save Converted File
                # song.export(new_filename, format="mp3")
                # return send_file(new_filename, as_attachment=True)
                return jsonify({"status": "ok", "filename": new_filename})
            except Exception as e:
                print(e)
                # Save Original File
                # file.save(new_filename)
                # Return File
                # return send_file(new_filename, as_attachment=True)
                return jsonify({"status": "ok", "filename": new_filename})
        else:
            print('File type not allowed')
            return redirect('/audio')
    return '''
    <!doctype html>
    <body style="background-color:black;">
        <title">MP3 Audio Conversor</title>
        <h1 style="color:white;">MP3 Audio Conversor</h1>
        <form method=post enctype=multipart/form-data>
        <input style="color:white;" type=file name=file>
        <input type=submit value=Upload>
        </form>
    </body>
    '''


if __name__ == '__main__':
    # To run in server
    # app.run(debug=True, port=os.getenv("PORT", default=5000), host='0.0.0.0')
    # To run in local
    app.run(debug=True, port=os.getenv("PORT", default=5000))
