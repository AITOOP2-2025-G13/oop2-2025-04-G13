"""
recorder.py 作業者1

10秒間マイクから音声を録音し、WAVファイルとして保存するモジュール。
macOSのAVFoundationを使用。

- ファイル名：recorder.py
- 関数名：record_audio()
- 出力ファイル名：record_audio.wav 
- 戻り値：ファイルパス
- 録音時間：10秒固定
- マイクデバイスID：macOS用に ":0" を指定
"""

import ffmpeg

def record_audio(output_path="record_audio.wav", duration=10, device_id=":1"):
    """
    指定したマイクから音声を録音する。

    Args:
        output_path (str): 保存するファイル名（例: "recorded.wav"）
        duration (int): 録音時間（秒）
        device_id (str): AVFoundationのデバイスID（macOS用）

    Returns:
        str: 保存されたファイルパス
    """
    try:
        print(f"{duration}秒間、マイクからの録音を開始します...")
        (
            ffmpeg
            .input(device_id, format='avfoundation', t=duration)
            .output(output_path, acodec='pcm_s16le', ar='44100', ac=2)  # ac=2でステレオに変更
            .run(overwrite_output=True)
        )
        print(f"録音が完了しました。{output_path}に保存されました。")
        return output_path

    except ffmpeg.Error as e:
        if e.stderr:
            try:
                print(f"FFmpegエラー詳細: {e.stderr.decode()}")
            except Exception:
                print("FFmpegエラーが発生しました（詳細のデコードに失敗）")
        else:
            print(f"FFmpegエラーが発生しました: {e}")
        return None
    except Exception as e:
        print(f"予期せぬエラー: {e}")
        return None

# テスト実行用（このファイルを直接実行したときのみ録音）
if __name__ == "__main__":
    record_audio()
