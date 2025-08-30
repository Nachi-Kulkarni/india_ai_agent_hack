#!/usr/bin/env python3
"""
Direct Kokoro TTS Implementation
Using the model directly from HuggingFace without complex dependencies.
"""

import os
import sys
from pathlib import Path
import numpy as np

# Set environment variables to avoid some import issues
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

class DirectKokoroTTS:
    """Direct Kokoro TTS implementation."""

    def __init__(self):
        """Initialize the TTS system."""
        self.output_dir = Path("audio_output")
        self.output_dir.mkdir(exist_ok=True)
        self.model = None
        self.pipeline = None
        self._initialize_model()

    def _initialize_model(self):
        """Initialize the Kokoro model."""
        try:
            # Try to import and initialize Kokoro
            from kokoro import KPipeline
            self.pipeline = KPipeline(lang_code='a')
            print("✓ Kokoro TTS model initialized successfully")
            return True
        except Exception as e:
            print(f"✗ Failed to initialize Kokoro TTS: {e}")
            print("Please ensure you have:")
            print("1. pip install kokoro>=0.9.2")
            print("2. pip install torch")
            print("3. pip install transformers")
            print("4. pip install numpy soundfile")
            return False

    def generate_speech(self, text, voice="af_bella", output_file=None):
        """Generate speech from text."""
        if not self.pipeline:
            print("✗ TTS not initialized")
            return None

        try:
            if not output_file:
                output_file = self.output_dir / f"kokoro_{voice}_output.wav"

            print(f"Generating speech for: '{text}'")
            print(f"Using voice: {voice}")

            # Generate speech
            generator = self.pipeline(text, voice=voice)

            audio_chunks = []
            for i, (gs, ps, audio) in enumerate(generator):
                print(f"Processing chunk {i}: {gs}")
                audio_chunks.append(audio)

            if audio_chunks:
                # Concatenate audio chunks
                audio_data = np.concatenate(audio_chunks)

                # Save to file
                import soundfile as sf
                sf.write(output_file, audio_data, 24000)

                print(f"✓ Audio saved to: {output_file}")
                print(f"  Duration: {len(audio_data)/24000:.2f}s")
                return str(output_file)
            else:
                print("✗ No audio generated")
                return None

        except Exception as e:
            print(f"✗ Error generating speech: {e}")
            return None

    def list_voices(self):
        """List available voices."""
        voices = {
            'af_heart': 'Heart (Female) - Warm, natural female voice',
            'af_bella': 'Bella (Female) - Clear, professional female voice',
            'af_sarah': 'Sarah (Female) - Friendly, approachable female voice',
            'af_nicole': 'Nicole (Female) - Confident, strong female voice',
            'af_sky': 'Sky (Female) - Youthful, energetic female voice',
            'am_michael': 'Michael (Male) - Professional, clear male voice',
            'am_fenrir': 'Fenrir (Male) - Deep, authoritative male voice',
            'am_adam': 'Adam (Male) - Natural, conversational male voice',
            'am_levi': 'Levi (Male) - Young, friendly male voice',
        }

        print("\nAvailable voices:")
        print("-" * 50)
        for voice_id, description in voices.items():
            print(f"{voice_id:12} | {description}")
        print()

        return voices

def main():
    """Main function."""
    print("🔊 Direct Kokoro TTS Implementation")
    print("=" * 40)

    tts = DirectKokoroTTS()

    if not tts.pipeline:
        print("\nPlease fix the installation issues above and try again.")
        return 1

    # List available voices
    tts.list_voices()

    # Generate test speech
    text = "Hello! This is a test of the Kokoro text-to-speech system using the hexgrad/Kokoro-82M model from HuggingFace."
    result = tts.generate_speech(text)

    if result:
        print(f"\n✓ Test completed successfully!")
        print(f"Audio file: {result}")
    else:
        print("\n✗ Test failed")

    return 0

if __name__ == "__main__":
    sys.exit(main())
