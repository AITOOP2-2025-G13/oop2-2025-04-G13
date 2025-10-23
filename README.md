# oop2-2025-04-G13

## 作業者
リーダー：加藤慶悟 <br>
作業者１：鎌田隼澄 <br>
作業者２：河合星実 <br>
作業者３：加藤璃空 <br>

## リポジトリの目的
プログラムを起動したら10秒間音声を録音し，録音された内容を文字起こしして，テキストファイルに保存するアプリケーションを作成するためのリポジトリである。

## 実行するのに必要なモジュール
whisper-base-mlx：音声を認識し、文字起こしを行うため。
pydub：録音した音声データを取り扱うため。

## 実行手順
①. 

## リポジトリのコミットログ（コミットログを追加したコミットログはない）
* commit 9236fa3c605764eb38216980ea5b5980d90956fc (HEAD -> main, origin/main, origin/HEAD)
| Author: Karotte-23 <kgkarotte23can@gmail.com>
| Date:   Thu Oct 23 16:09:45 2025 +0900
| 
|     main.pyを更新
| 
* commit b74b4eaf64cbb078e9796eeb4ccb080f2a7652fa
| Author: Karotte-23 <kgkarotte23can@gmail.com>
| Date:   Thu Oct 23 16:09:22 2025 +0900
| 
|     main.pyを更新
| 
* commit 4bb555e5463f67dc9b26ea3cdcdf73e9db2c6d54
| Author: Karotte-23 <kgkarotte23can@gmail.com>
| Date:   Thu Oct 23 16:04:56 2025 +0900
| 
|     README.mdを更新
|     
|     必要なモジュールに、pydubを追加
|   
*   commit ec9877062ca70a659096a8c78a11a5d45b289419
|\  Merge: 35ea27a d63a2d9
| | Author: Karotte-23 <kgkarotte23can@gmail.com>
| | Date:   Thu Oct 23 16:01:51 2025 +0900
| | 
| |     Merge pull request #2 from AITOOP2-2025-G13/hoshimi
| |     
| |     「音声ファイルもしくは音声データを受け取り文字起こしする処理」を作成した
| | 
| * commit d63a2d95a4860e810e24e80de8a8db6d4e941923 (origin/hoshimi)
| | Author: kurageoO <rayn.am1004@gmail.com>
| | Date:   Thu Oct 23 15:55:57 2025 +0900
| | 
| |     「音声ファイルもしくは音声データを受け取り文字起こしする処理」を作成した
| | 
* | commit 35ea27a21e51496fa2f08e1041d13368bfdf467f
| | Author: Karotte-23 <kgkarotte23can@gmail.com>
| | Date:   Thu Oct 23 15:59:51 2025 +0900
| | 
| |     lecture04_main.pyを更新
| |     
| |     lecture04_main.pyに、recorder.pyによって音声を録音するコードを実装した。
| |   
* |   commit ca2f00fa4476c2560dce516a3b5e894ca598c548
|\ \  Merge: 682e191 92fdfd6
| | | Author: Karotte-23 <kgkarotte23can@gmail.com>
| | | Date:   Thu Oct 23 15:56:36 2025 +0900
| | | 
| | |     Merge pull request #1 from AITOOP2-2025-G13/recorder
| | |     
| | |     録音処理と録音ファイルの作成ができる
| | | 
| * | commit 92fdfd6d984182f3925b796416743d09bb2ac397 (origin/recorder)
| |/  Author: 1500hayao <kamata1500@gmail.com>
| |   Date:   Thu Oct 23 15:48:12 2025 +0900
| |   
| |       録音処理と録音ファイルの作成ができる
| | 
* | commit 682e1911aa74fdf1180e1061351dc39a1e9a77aa
| | Author: Karotte-23 <kgkarotte23can@gmail.com>
| | Date:   Thu Oct 23 15:54:11 2025 +0900
| | 
| |     README.mdの更新｜lecture04_main.pyの追加
| |     
| |     lecture04_main.pyにて実行を行うので、用意を行なった。
| |     
| |     README.md内でモジュールを追加した。実行手順の項目に①を追加した。コミットログの項目を追加した。
| | 
* | commit a39cf6b32ee3534ccc39f619e9551e2410fde7c1 (origin/lecture04_main, lecture04_main)
|/  Author: Karotte-23 <kgkarotte23can@gmail.com>
|   Date:   Thu Oct 23 15:09:00 2025 +0900
|   
|       README.mdの更新
|       
|       このリポジトリの目的について、修正した。
| 
* commit 4d47400a35c95efff561911af89258633e779c12
| Author: Karotte-23 <kgkarotte23can@gmail.com>
| Date:   Thu Oct 23 15:02:16 2025 +0900
| 
|     README.mdの更新
|     
|     作業者欄の表示を修正
| 
* commit 8d68976b274fb57fb0545f3ecdc0d3e5a0bc63d9
| Author: Karotte-23 <kgkarotte23can@gmail.com>
| Date:   Thu Oct 23 15:00:12 2025 +0900
| 
|     README.mdを更新
|     
|     作業者名を確定し、内容を更新した。
| 
* commit a9c0fe431438f6b7302896f5159c8a34ae7d01b1
| Author: Karotte-23 <kgkarotte23can@gmail.com>
| Date:   Thu Oct 23 14:46:57 2025 +0900
| 
|     README.mdを更新
|     
|     README.mdを更新し、雛形を作成した。
| 
* commit f19f1828e04c4d13d40ea100c67824ef2ffe0627
  Author: Karotte-23 <kgkarotte23can@gmail.com>
  Date:   Thu Oct 23 14:37:59 2025 +0900
  
      Initial commit
