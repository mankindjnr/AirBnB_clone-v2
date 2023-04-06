#!/usr/bin/python3
"""
 generating a tgz file with the contents of a web static folder
"""


from fabric.api import *
from datetime import datetime

def do_pack():
    """
    this is an archive of the contents in web static folder
    """
    current = datetime.now()
    fileArchive = "versions/web_static_{}{}{}{}{}{}.tgz".format(current.year,
                                                             current.month,
                                                             current.day,
                                                             current.hour,
                                                             current.minute,
                                                             current.second)
    print("Packing web_static to versions/{}".format(fileArchive))
    """creation of the directory versions
    """
    local("mkdir -p versions")
    result = local("tar -cvzf {} web_static".format(fileArchive))
    if result.succeeded:
        return (fileArchive)
    else:
        return None
