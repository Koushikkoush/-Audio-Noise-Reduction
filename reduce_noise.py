import noisereduce as nr
import numpy as np
import soundfile as sf
import librosa
import sys

# Function to reduce noise from an audio file
def reduce_noise(audio_path, output_path):
    try:
        # Load the audio file
        audio, sample_rate = librosa.load(audio_path, sr=None)

        # Apply noise reduction
        reduced_noise_audio = nr.reduce_noise(y=audio, sr=sample_rate)

        # Save the output
        sf.write(output_path, reduced_noise_audio, sample_rate)
        print(f"Noise reduced audio saved to: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if the user provided input and output file paths
    if len(sys.argv) != 3:
        print("Usage: python reduce_noise.py <input_audio_file> <output_audio_file>")
        sys.exit(1)

    input_audio_file = sys.argv[1]
    output_audio_file = sys.argv[2]

    # Call the noise reduction function
    reduce_noise(input_audio_file, output_audio_file)
