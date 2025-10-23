import mlx_whisper
from pydub import AudioSegment
import numpy as np

# 音声ファイルを指定して文字起こし
audio_file_path = "output_audio.wav"


def audio_file_to_text(file_path: str):
    """
    音声ファイルを受け取り文字起こしを行う関数。

    Args:
        audio_file_path: 文字起こしする音声ファイルのパス。

    Returns:
        文字起こしされたテキスト。
    """
    result = mlx_whisper.transcribe(
        file_path, path_or_hf_repo="mlx-community/whisper-base-mlx"
    )
    # print (result["text"]+"_____が出力されました")
    return result["text"]

# 音声データを指定して文字起こし
def preprocess_audio(sound):
    """
    pydubのAudioSegmentをWhisperが推奨する形式 (16kHz, 16bit, Mono) に変換する。
    """
    if sound.frame_rate != 16000:
        sound = sound.set_frame_rate(16000)
    if sound.sample_width != 2:
        sound = sound.set_sample_width(2)
    if sound.channels != 1:
        sound = sound.set_channels(1)
    return sound

audio_data = []


# 音声データを音声ファイルから読み取る
def audio_data_to_text(audio_file_path: str):
    """
    音声データを音声ファイルから読み取り文字起こしを行う関数。
    
    Args:
        audio_file_path: 文字起こしする音声ファイルのパス。

    Returns:
        文字起こしされたテキスト。
    """

    audio_data.append(AudioSegment.from_file(audio_file_path, format="wav"))

    for data in audio_data:
        sound = preprocess_audio(data)
        # Metal(GPU)が扱えるNumpy Array形式に変換
        arr = np.array(sound.get_array_of_samples()).astype(np.float32) / 32768.0
        result = mlx_whisper.transcribe(
            arr, path_or_hf_repo="mlx-community/whisper-base-mlx"
        )
        # print (result["text"]+"_____が出力されました")
        return result["text"]