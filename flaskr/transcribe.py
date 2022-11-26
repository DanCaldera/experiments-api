from flask import Blueprint
import pytube
import whisper

bp = Blueprint('transcribe', __name__)


@bp.route('/transcribe')
def transcribe():
    url = "https://www.youtube.com/watch?v=UuTcTAu__pY"
    model = whisper.load_model("tiny")
    youtube_vid = pytube.YouTube(url)
    youtube_vid.streams.get_audio_only().download(filename='audio.mp4')
    result = model.transcribe('audio.mp4')
    return result
