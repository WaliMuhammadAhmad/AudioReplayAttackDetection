import os
from pydub import AudioSegment

def check_audio_properties(file_path):
    audio = AudioSegment.from_file(file_path)
    
    if audio.channels != 1:
        return "Audio is Stereo audio (should be mono)"
    
    if audio.frame_rate != 22050:
        return f"Sample rate is {audio.frame_rate} Hz (should be 44100 Hz)"
     
    if audio.frame_rate * audio.frame_width * 8 != audio.frame_rate * audio.sample_width * audio.channels * 8:
        return "Audio codec is not pcm_s16le"
    
    return None

def main():
    folder_path = input("Enter the folder path containing .wav files: ")
    
    audio_files = [file for file in os.listdir(folder_path) if file.lower().endswith(".wav")]
    print(f"Total {len(audio_files)} .wav files found in the folder.")

    for file in audio_files:
        file_path = os.path.join(folder_path, file)
        violation = check_audio_properties(file_path)
        if violation:
            print(f"File: {file}, Violation: {violation}")

if __name__ == "__main__":
    main()