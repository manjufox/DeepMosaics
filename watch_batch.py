import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:
    DIRECTORY_TO_WATCH = r'.\result_converted'  # 監視するディレクトリのパス

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_created(event):
        if not event.is_directory:
            # 新しいファイルが作成されたときの処理
            print(f"Received created event - {event.src_path}.")
            # deepmosaic.pyスクリプトを実行
            os.system(f"python deepmosaic.py --media_path {event.src_path} --model_path ./pretrained_models/mosaic/clean_youknow_video.pth --gpu_id 0")

if __name__ == '__main__':
    w = Watcher()
    w.run()
