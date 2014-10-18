#!/usr/bin/python
# -*- coding: utf-8 -*-

# freeseer - vga/presentation capture software
#
#  Copyright (C) 2014  Free and Open Source Software Learning Centre
#  http://fosslc.org
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

# For support, questions, suggestions or any other inquiries, visit:
# http://wiki.github.com/Freeseer/freeseer/

import json
import os
import signal

from flask import Blueprint
from flask import request

from freeseer import settings, logging
from freeseer.framework.multimedia import Multimedia
from freeseer.framework.plugin import PluginManager
from freeseer.frontend.controller import app
from freeseer.frontend.controller import validate
from freeseer.frontend.controller.server import HTTPError
from freeseer.frontend.controller.server import ServerError
from freeseer.frontend.controller.server import http_response

log = logging.getLogger(__name__)
configuration = Blueprint('configuration', __name__)

plugins_map = {
    "audioinput": "AudioInput",
    "audiomixer": "AudioMixer",
    "videoinput": "VideoInput",
    "videomixer": "VideoMixer",
    "importer": "Importer",
    "output": "Output"
}

@configuration.before_app_first_request
def configure_configuration():
    """
    Initializes the profile, configuration, and plugin manager.
    Runs on first call to server.
    """
    signal.signal(signal.SIGINT, teardown_configuration)
    configuration.profile = settings.profile_manager.get()
    configuration.config = configuration.record_profile.get_config('freeseer.conf',
                                                                   settings.FreeseerConfig,
                                                                   storage_args=['Global'],
                                                                   read_only=True)
    configuration.plugin_manager = PluginManager(configuration.profile)


def teardown_configuration(signum, frame):
    """
    Teardown method for configuration api.
    """
    pass


@configuration.route('/configuration/general', methods=['GET'])
@http_response(200)
def get_general_configuration():
    """
    Returns the general configuration.
    """
    log.debug('GET /configuration/general')
    return {}


@configuration.route('/configuration/general', methods=['PUT'])
@http_response(200)
def put_general_configuration():
    """
    Writes to the general configuration.
    """
    log.debug('PUT /configuration/general')


@configuration.route('/configuration/recording', methods=['GET'])
@http_response(200)
def get_recording_configuration():
    """
    Returns the recording configuration.
    """
    log.debug('GET /configuration/recording')
    return {}


@configuration.route('/configuration/recording', methods=['PUT'])
@http_response(200)
def put_recording_configuration():
    """
    Writes to the recording configuration.
    """
    log.debug('PUT /configuration/recording')


@configuration.route('/configuration/recording/<string:plugins>', methods=['GET'])
@http_response(200)
def get_plugins(plugins):
    """
    Returns available plugins for :plugins type {audio, video, file, stream}.
    """
    plugins_type = plugins_map[plugins]
    available = configuration.plugin_manager.get_plugins_of_category(plugins_type)
    log.debug('GET /configuration/recording/{0}', plugins)
    return { 'plugins': available }


@configuration.route('/configuration/recording/<string:plugins>', methods=['PUT'])
@http_response(200)
def select_plugin(plugins):
    """
    Selects a plugin for :plugins type {audio, video, file, stream}.
    """
    log.debug('PUT /configuration/recording/{0}', plugins)


@configuration.route('/configuration/recording/<string:plugins>/<string:plugin>', methods=['GET'])
@http_response(200)
def get_plugin(plugins, plugin):
    """
    Returns the configuration for a :plugin of :plugins type.
    """
    log.debug('GET /configuration/recording/{0}/{1}', plugins, plugin)
    return {}


@configuration.route('/configuration/recording/<string:plugins>/<string:plugin>', methods=['PUT'])
@http_response(200)
def put_plugin(plugins, plugin):
    """
    Writes the configuration for a :plugin of :plugins type.
    """
    log.debug('PUT /configuration/recording/{0}/{1}', plugins, plugin)







