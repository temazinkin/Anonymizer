from pathlib import Path

from anonymizer.config import (
    CONFIDENTIAL_DATA_FOLDER,
    ALLOWED_EXTENSIONS,
)


def confidential_file_tree_generator(
        folder: str = CONFIDENTIAL_DATA_FOLDER,
        extensions: list = ALLOWED_EXTENSIONS,
) -> list:

    """
    Формирует список путей к файлам,
    подходящим по маскам extensions,
    из каталога folder и всех подкаталогов
    """

    all_confidential_files = set()

    for extension in extensions:
        all_confidential_files.update(
            Path(folder).rglob(extension)
        )

    return sorted(all_confidential_files)
