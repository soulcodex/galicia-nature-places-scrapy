from typing import Text, List
from pathlib import Path


def plain_text_file_as_list(path: Text) -> List[Text]:
    file_path = Path(path)
    if not file_path.exists():
        return []

    content = []
    with file_path.open(mode='r') as file:
        for line in file:
            content.append(line.rstrip())

    return content
