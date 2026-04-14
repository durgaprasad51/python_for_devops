# import shutil, os, datetime or as below

import shutil
import datetime
import os


def backup_files(source,destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination, f"backup_{today}") 
    shutil.make_archive(backup_file_name, 'gztar' , source )
    print(f"Backup created: {backup_file_name}.tar.gz")


source = "/home/dp/Documents/Work/Labs/Python4devops"
destination = "/home/dp/Documents/Work/Labs/Python4devops/backups"
backup_files(source,destination)
