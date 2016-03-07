# Copyright 2014 Diamond Light Source Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
.. module:: create_autosummary
   :platform: Unix
   :synopsis: A module to automatically update a Sphinx API

.. moduleauthor:: Nicola Wadeson <scientificsoftware@diamond.ac.uk>

"""
import os


def list_of_packages(base_path):
    pkg_list = []
    for entry in os.listdir(base_path):
        entry_path = os.path.join(base_path, entry)
        if not os.path.isfile(entry_path):
            pkg_list.append(entry_path)
    return pkg_list


def add_package_entry(f, root, dirs, files, output):
    pkg_path = root.split('Savu/')[1]
    module_name = pkg_path.replace('/', '.')
    f.write(module_name +
            '\n------------------------------------------------------------\n')
    f.write('\n.. currentmodule::' + module_name)
    f.write('\n.. autosummary::')
#    f.write('\n   :toctree: ' + output + '/' + pkg_path + '\n\n')
    f.write('\n   :toctree: api\n\n')

    for fi in files:
        file_path = module_name + '.' + fi
        f.write('   ' + file_path.split('.py')[0] + '\n')
    f.write('\n\n')


def list_of_files(package):
    pass


if __name__ == "__main__":

    # determine Savu base path
    savu_base_path = os.path.abspath('../')
    out_folder = '_autosummary'

    # open the autosummary file
    f = open(savu_base_path + '/doc/source/autosummary.rst', 'w')

    # add header
    f.write('Autosummary \n==============\n')
    f.write('Information on specific functions, classes, and methods.\n \n')

    base_path = savu_base_path + '/savu'
    # create entries in the autosummary for each package

    exclude_dir = ['__pycache__', 'test']
    exclude_file = ['__init__.py']
    for root, dirs, files in os.walk(base_path, topdown=True):
        dirs[:] = [d for d in dirs if d not in exclude_dir]
        files[:] = [fi for fi in files if fi.split('.')[-1] == 'py']
        files[:] = [fi for fi in files if fi not in exclude_file]
        if '__' not in root:
            add_package_entry(f, root, dirs, files, out_folder)
