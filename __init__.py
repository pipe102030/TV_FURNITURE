# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

# Mycroft libraries
from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

import requests


__author__ = 'pipe102030'

LOGGER = getLogger(__name__)

class IotTVSkill(MycroftSkill):


    def __init__(self):
        super(IotTVSkill, self).__init__(name="IotTVSkill")
		
    def initialize(self):
	self.load_data_files(dirname(__file__))

        TV_command_intent = IntentBuilder("TVCommandIntent").require("TVKeyword").require("Action").build()
        self.register_intent(TV_command_intent, self.handle_TV_command_intent)

    def handle_TV_command_intent(self, message):
        action_word = message.data.get("Action")
        LOGGER.info("Command word: " + action_word )
        if action_word == "show" :
		    self.speak_dialog("show.tv")
		    r = requests.get('http://ip_here/lamp?cmd=1')
            
	elif action_word == "hide":
		self.speak_dialog("hide.tv")
		r = requests.get('http://ip_here/lamp?cmd=0')
	else:
		self.speak("not sure about that")  	

    def stop(self):
        pass

def create_skill():
    return IotTVSkill()
