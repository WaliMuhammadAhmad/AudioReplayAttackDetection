import librosa

def get_audio_info(audio_path):
    try:
        audio_data, sr = librosa.load(audio_path, sr=None)
        num_channels = audio_data.shape[0] if len(audio_data.shape) > 1 else 1
        bit_depth = audio_data.dtype.itemsize * 8  # Calculate bit depth

        print("Audio Information:")
        print("File:", audio_path)
        print("Sample Rate:", sr, "Hz")
        print("Channels:", "Mono" if num_channels == 1 else "Stereo")
        print("Bit Depth:", bit_depth, "bits")
    except Exception as e:
        print(f"Error loading audio file {audio_path}: {e}")

audio_path = r"dataset\raw\Real.wav"
get_audio_info(audio_path)