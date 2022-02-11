from pathlib import Path


# Основной каталог
BASE_DIR = Path(__file__).resolve().parent.parent

# Каталоги конфиденциальных файлов
# Вложенные каталоги учитываются автоматически
CONFIDENTIAL_DATA_FOLDERS = [
    BASE_DIR / 'secret',
]

# Каталог сохранения обезличенных файлов
SAVE_PATH = BASE_DIR / 'no_secret'

# Поддерживаемые расширения
ALLOWED_EXTENSIONS = [
    '*.xls?',
]
