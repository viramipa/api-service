import os
import json
from datetime import datetime
from typing import Any, Dict, Optional

def read_json_file(file_path: str) -> Optional[Dict[str, Any]]:
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as file:
        return json.load(file)

def write_json_file(file_path: str, data: Dict[str, Any]) -> None:
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def ensure_directory_exists(dir_path: str) -> None:
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def sanitize_filename(filename: str) -> str:
    return "".join([c for c in filename if c.isalnum() or c in (' ', '.', '_', '-')]).rstrip()