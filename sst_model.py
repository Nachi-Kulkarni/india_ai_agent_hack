import torch
import torchaudio
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC

# Load the processor and model
processor = Wav2Vec2Processor.from_pretrained("nvidia/parakeet-tdt-0.6b-v3")
model = Wav2Vec2ForCTC.from_pretrained("nvidia/parakeet-tdt-0.6b-v3").to("cpu")

# Load and preprocess the audio file
waveform, sr = torchaudio.load("audio_output/kokoro_af_bella_output.wav")
if sr != 16000:
    waveform = torchaudio.functional.resample(waveform, sr, 16000)

input_values = processor(waveform[0].numpy(), sampling_rate=16000, return_tensors="pt").input_values

# Perform transcription
with torch.no_grad():
    logits = model(input_values).logits
predicted_ids = torch.argmax(logits, dim=-1)
transcription = processor.batch_decode(predicted_ids)[0]
print("Transcription:", transcription)
