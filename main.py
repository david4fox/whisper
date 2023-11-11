import whisper

model = whisper.load_model("base")
result = model.transcribe("audio_prueba.mp3")
print(result["text"])