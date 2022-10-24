from watchdog.events import FileSystemEventHandler
from pathlib import Path
import re

class FileTracking(FileSystemEventHandler):
    
    def on_created(self, event):
        file_name :str = Path(event.src_path).stem #получил имя, из пути файла, вызвавшего событие

        for letter in list(file_name):

            vowel_letter :re = re.match('а|о|у|ы|э|е|ё|и|ю|я|a|e|i|o|u|y', letter, re.IGNORECASE)

            if vowel_letter:
                print(letter.lower())

            else:
                print(letter.upper())