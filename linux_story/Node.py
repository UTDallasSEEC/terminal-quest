"""
* Copyright (C) 2014 Kano Computing Ltd
* License: GNU General Public License v2 http://www.gnu.org/licenses/gpl-2.0.txt
*
* Author: Caroline Clark <caroline@kano.me>
* Emulate file system in a tree class
"""


class Node:
    def __init__(self, identifier, path="", is_dir=True):
        self.__identifier = identifier
        self.__path = path
        self.__children = []
        self.__parent = None
        self.__is_dir = is_dir

    @property
    def identifier(self):
        return self.__identifier

    @property
    def children(self):
        return self.__children

    @property
    def parent(self):
        return self.__parent

    @property
    def path(self):
        return self.__path

    @property
    def is_dir(self):
        return self.__is_dir

    def add_child(self, identifier):
        self.__children.append(identifier)

    def add_parent(self, identifier):
        self.__parent = identifier

    def add_path(self, identifier):
        self.__path = identifier

    def set_as_dir(self, is_dir):
        self.__is_dir = is_dir
