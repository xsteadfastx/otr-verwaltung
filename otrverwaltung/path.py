# -*- coding: utf-8 -*-
### BEGIN LICENSE
# Copyright (C) 2010 Benjamin Elbers <elbersb@gmail.com>
#This program is free software: you can redistribute it and/or modify it 
#under the terms of the GNU General Public License version 3, as published 
#by the Free Software Foundation.
#
#This program is distributed in the hope that it will be useful, but 
#WITHOUT ANY WARRANTY; without even the implied warranties of 
#MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR 
#PURPOSE.  See the GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License along 
#with this program.  If not, see <http://www.gnu.org/licenses/>.
### END LICENSE

import sys
import os.path
from xdg import BaseDirectory

data_dir = '../data'

def getdatapath(*args):
    """Retrieve otrverwaltung data path

    This path is by default <otrverwaltung_lib_path>/../data/ in trunk
    and /usr/share/otrverwaltung in an installed version but this path
    is specified at installation time.
    """
    return os.path.join(os.path.dirname(__file__), data_dir, *args)
      
def get_storage_dir(filename=""):
    return os.path.join(BaseDirectory.xdg_data_home, "otrverwaltung", filename)

def get_config_dir(filename=""):
    return os.path.join(BaseDirectory.xdg_config_home, "otrverwaltung", filename)

def get_path(filename=""):
    return os.path.join(sys.path[0], "otrverwaltung", filename)

def get_plugin_paths():
    plugins_home = get_storage_dir("plugins") 
    plugins_usr = '/usr/share/otrverwaltung/plugins'
    return plugins_home, plugins_usr
    
def get_gui_path(filename=''):
    return os.path.join(get_path(), "gui", filename)
    
def get_image_path(filename=""):
    return getdatapath("media", filename)
