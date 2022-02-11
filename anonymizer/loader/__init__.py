from pathlib import Path

from anonymizer.config import (
    CONFIDENTIAL_DATA_FOLDERS,
    ALLOWED_EXTENSIONS,
)


def confidential_file_tree_generator(
        folders: list = CONFIDENTIAL_DATA_FOLDERS,
        extensions: list = ALLOWED_EXTENSIONS,
) -> list:

    """
    Формирует список путей к файлам,
    подходящим по маскам extensions,
    из всех каталогов и подкаталогов folders
    """

    all_confidential_files = set()

    for folder in folders:
        for extension in extensions:
            all_confidential_files.update(
                Path(folder).rglob(extension)
            )

    return sorted(all_confidential_files)
