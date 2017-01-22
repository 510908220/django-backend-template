# -*- encoding: utf-8 -*-

"""项目升级脚本.

Usage:
  updater.py  <source_zip> 
  updater.py (-h | --help)
  updater.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --source_zip  7z file.
"""
import shutil
import os
import subprocess
import time
from docopt import docopt
import importlib

CUR_DIR = os.path.abspath(os.path.dirname(__file__))


def extract(archive_file, dest_dir):
    """
    archive_file:待解压的压缩文件
    dest_dir: 压缩文件解压到的目录
    """
    cmd = "7z x {archive_file} -o{dest_dir} -y".format(
        dest_dir=dest_dir,
        archive_file=archive_file,
    )
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    _, err = p.communicate()
    return p.returncode == 0, err, cmd


def main(arguments):
    source_tmp_dir = os.path.join(CUR_DIR, str(int(time.time())))
    success, err, _ = extract(arguments["<source_zip>"], source_tmp_dir)
    if not success:
        raise Exception(err)
    source_dir_name = os.listdir(source_tmp_dir)[0]
    source_path = os.path.join(source_tmp_dir, source_dir_name)
    
    # 更新升级逻辑脚本
    source_update_imp = os.path.join(source_path, "updater", "updater_imp.py")
    dst_update_imp = os.path.join(CUR_DIR, "updater", "updater_imp.py")
    shutil.copyfile(source_update_imp, dst_update_imp)
    
    # 载入升级函数
    m = importlib.import_module("updater.updater_imp")
    update_func = getattr(m, 'update')
    update_func(source_path)
    shutil.rmtree(source_tmp_dir)


if __name__ == "__main__":
    arguments = docopt(__doc__, version='updater 1.0')
    main(arguments)
