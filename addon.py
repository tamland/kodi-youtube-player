# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 Thomas Amland
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

import sys
import xbmc
import xbmcplugin
from xbmcgui import ListItem
from lib import pafy

handle = int(sys.argv[1])


def play(video_id):
    video = pafy.new(video_id)
    url = video.getbest().url
    xbmcplugin.setResolvedUrl(handle, True, ListItem(path=url))


if __name__ == '__main__':
    url = sys.argv[0]
    if len(sys.argv) == 3:
        url += sys.argv[2]

    path = url.split('plugin://plugin.video.youtube/')[1]

    if path.startswith('play/'):
        play(path.split('play/'))
    elif path.startswith('?action=play_video&videoid='):
        play(path.split('?action=play_video&videoid=')[1])
    else:
        xbmc.log("[youtube] unknown argument '%s'" % path, xbmc.LOGERROR)

