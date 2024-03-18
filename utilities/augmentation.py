from pydub import AudioSegment
import os
import random

def create_short_clips(audio, clip_length, num_clips):
    output_path = r"dataset\replay\replay_22050Hz"
    os.makedirs(output_path, exist_ok=True)

    audio_duration = len(audio)

    for i in range(num_clips):
        if audio_duration <= clip_length:
            break  # Audio duration is shorter than clip length, stop creating clips

        start_time = random.randint(0, audio_duration - clip_length)
        end_time = start_time + clip_length

        clip = audio[start_time:end_time]

        output_file = os.path.join(output_path, f"replay_{i}.wav")
        clip.export(output_file, format="wav")

def main():
    audio_path = r"dataset\raw\Replay(22050).wav"

    # Load the original audio
    original_audio = AudioSegment.from_file(audio_path)

    # Set the desired clip length in milliseconds (10 seconds)
    clip_length_ms = 10000

    # Set the number of clips you want to generate
    num_clips = 100

    create_short_clips(original_audio, clip_length_ms, num_clips)

if __name__ == "__main__":
    main()
