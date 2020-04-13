# TRIQS application maxent
# Copyright (C) 2018 Gernot J. Kraberger
# Copyright (C) 2018 Simons Foundation
# Authors: Gernot J. Kraberger and Manuel Zingl
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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


def application_pytriqs_import(name, *args, **kwargs):
    if name.startswith('@package_name@'):
        name = name[len('@package_name@') + 1:]
    return builtin_import(name, *args, **kwargs)

import builtins
builtins.__import__, builtin_import = application_pytriqs_import, builtins.__import__
