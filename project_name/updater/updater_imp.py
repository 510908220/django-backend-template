# -*- encoding: utf-8 -*-
"""
实现具体的升级逻辑.
"""
import shutil
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 升级文件列表
UPDATE_LIST = [
    ("docker-compose.yml", "file"),
    ("Dockerfile", "file"),
    ("src", "dir")
]

def update_item(source_dir, item):
    file_name, file_type = item
    src_file = os.path.join(source_dir, file_name)
    dst_file = os.path.join(ROOT_DIR, file_name)
    if file_type == 'file':
        shutil.copyfile(src_file, dst_file)
    elif file_type == "dir":
        for root, dirs, files in os.walk(src_file):
            for f in files:
                src_f = os.path.join(root, f)
                dst_f = src_f.replace(src_file, dst_file)
                shutil.copyfile(src_f, dst_f)
                
def update(source_path):
    for item in UPDATE_LIST:
        update_item(source_path, item)
