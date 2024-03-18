import os
import librosa

dataset_directory = r"dataset/raw"
audio_files = [os.path.join(dataset_directory, file) for file in os.listdir(dataset_directory) if file.endswith(".wav")]
for audio_file in audio_files:
    try:
        audio_data, sr = librosa.load(audio_file, sr=None)
        if sr != 22050:
            print(f"Deleting {audio_file} (Sample Rate: {sr} Hz)")
            # os.remove(audio_file)
    except Exception as e:
        print(f"Error processing {audio_file}: {e}")
