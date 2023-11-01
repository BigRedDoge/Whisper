from recorder import AudioRecorder
from transcriber import transcribe
import dotenv 
import queue
import os
import openai


dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def main():
    # Queue for audio frames
    audio_queue = queue.Queue()
    # thread for recording audio
    recorder = AudioRecorder(audio_queue, record_length=5, audio_path="recording.wav")
    # transcribes audio
    audio_path = "recording.wav"

    recorder.start()
    try:
        while True:
            # get audio frames from queue
            frames = audio_queue.get(block=True)
            # transcribe audio
            text = transcribe(frames, audio_path)
            print("transcribed text: ", text)

    except KeyboardInterrupt:
        recorder.stop()


if __name__ == '__main__':
    main()