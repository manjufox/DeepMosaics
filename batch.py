# globモジュールをインポート
import os
import glob

# フォルダのパスと拡張子を指定
folder_path = r'.\result'
result_dir = r".\clean"
move_dir = r".\move"

# フォルダ内の指定した拡張子のファイルの一覧を取得
file_list = glob.glob(os.path.join(folder_path))

# ファイルの一覧をループしてコマンドを実行
for file_path in file_list:
    # コマンドを実行
    os.system(f"python deepmosaic.py --media_path {file_path} --result_dir {result_dir} --mask_threshold 30 --model_path ./pretrained_models/mosaic/clean_youknow_video.pth --gpu_id 0")
    os.move(file_path,move_dir)
