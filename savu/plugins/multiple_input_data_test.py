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
.. module:: multiple_input_data_test
   :platform: Unix
   :synopsis: Plugin to test multiple input data sets are passed to process 
   
.. moduleauthor:: Nicola Wadeson <scientificsoftware@diamond.ac.uk>

"""
from savu.plugins.plugin import Plugin
from savu.plugins.utils import register_plugin
from savu.plugins.driver.cpu_plugin import CpuPlugin


@register_plugin
class MultipleInputDataTest(Plugin, CpuPlugin):
    """
    The base class from which all plugins should inherit.
    :param in_datasets: Create a list of the dataset(s) to process. Default: [].
    :param out_datasets: Create a list of the dataset(s) to process. Default: [].
    """

    def __init__(self):
        super(MultipleInputDataTest, self).__init__("MultipleInputDataTest")

    def process_frames(self, data, frame_list):
        return data[0] + data[1]
#        in_data = self.get_data_objects(self.exp.index, "in_data")
#        out_data = self.get_data_objects(self.exp.index, "out_data")
#
#        in_data = in_data[0]
#        out_data = out_data[0]
#
#        slice_list = in_data.single_slice_list()
#        count = 0
#        for sl in slice_list:
#            temp = in_data.data[sl]
#            out_data.data[sl] = temp
#            count = count + 1
#
#        print "plugin complete"

#    def setup(self):
#        in_datasets, out_datasets = self.get_datasets()
#        in_pData, out_pData = self.get_plugin_datasets()
##         print in_pData[0].meta_data.get_meta_data('SINOGRAM')#
#        tobecorrected = in_datasets[0]
#        monitor = in_datasets[1]
#        corrected = out_datasets[0]
#        corrected.create_dataset(tobecorrected)
#        in_pData, out_pData = self.get_plugin_datasets()
#        in_pData[0].plugin_data_setup('SINOGRAM', self.get_max_frames())
#        in_pData[1].plugin_data_setup('SINOGRAM', self.get_max_frames())
#        out_pData[0].plugin_data_setup('SINOGRAM', self.get_max_frames())

    def setup(self):
        """
        Initial setup of all datasets required as input and output to the
        plugin.  This method is called before the process method in the plugin
        chain.
        """
        in_datasets, out_datasets = self.get_datasets()
        in_pData, out_pData = self.get_plugin_datasets()

        in_pData[0].plugin_data_setup('SINOGRAM', self.get_max_frames())
        print in_datasets[0].get_data_patterns()
        #slice_dirs = in_pData[0].get_slice_directions()
        #print "BEFORE", slice_dirs
        #in_pData[0].set_fixed_directions(slice_dirs, [0, 0])
        #print "AFTER", in_pData[0].get_slice_directions()

        in_pData[1].plugin_data_setup('SINOGRAM', self.get_max_frames())
        #in_pData[1].set_fixed_directions(slice_dirs, [0, 0])

        out_datasets[0].create_dataset(in_datasets[0])
        out_pData[0].plugin_data_setup('SINOGRAM', self.get_max_frames())

    def nInput_datasets(self):
        return 2

    def nOutput_datasets(self):
        return 1

    def get_max_frames(self):
        return 8
