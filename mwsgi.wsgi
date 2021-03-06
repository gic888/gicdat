#!/usr/bin/env python -3
# encoding: utf-8

#Created by Graham Cummins on Jun 10, 2011

# Copyright (C) 2011 Graham I Cummins
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later 
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT 
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS 
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 59 Temple
# Place, Suite 330, Boston, MA 02111-1307 USA
#

import sys, os

thisdir = os.path.split(__file__)[0]
if not thisdir in sys.path:
    sys.path.append(thisdir)

gdfs = os.path.join(thisdir, 'gdfs')
#os.environ["GICDAT_FSTORE_DIR"] = gdfs
import fstore
from srv import application

