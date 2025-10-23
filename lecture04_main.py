import recorder
import audio_to_text

if __name__ == "__main__":
    audio_file_path = recorder.record_audio
    audio_to_text.audio_data_to_text(audio_file_path)