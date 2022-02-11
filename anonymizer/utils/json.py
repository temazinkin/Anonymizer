import json


def write_to_json(
        data: dict,
        filename: str
) -> str:

    """
    Записывает данные в .json файл
    и возвращает путь к файлу
    """
    filename = _get_json_filename(filename)

    with open(filename, 'w', encoding='UTF-8') as json_file:
        json.dump(
            data,
            json_file,
            indent=4,
            ensure_ascii=False,
            sort_keys=True
        )
    return filename


def _get_json_filename(filename: str):
    """
    Добавляет расширение .json при необходимости
    """
    filename = '.json' == str(filename)[-5:] and filename or f'{filename}.json'
    return filename
