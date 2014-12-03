#!/usr/bin/env python
#
# Copyright (C) 2014 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#
# Author: Caroline Clark <caroline@kano.me>
# A chapter of the story

import os
import sys

dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
if __name__ == '__main__' and __package__ is None:
    if dir_path != '/usr':
        sys.path.insert(1, dir_path)
        print sys.path

from linux_story.Step import Step
from linux_story.challenges.challenge_1.terminals import Terminal1
from linux_story.challenges.challenge_2.terminals import Terminal2


class Step_Template1(Step):
    def __init__(self):
        Step.__init__(self, Terminal1)


class Step_Template2(Step):
    def __init__(self):
        Step.__init__(self, Terminal2)


class Step1(Step_Template1):
    story = [
        "You are in the home directory.",
        "You remember the rabbit's note, "
        "which told you to look harder in this directory"
    ]
    start_dir = "~"
    end_dir = "~"
    command = "ls -a"
    hints = [
        "You decide that the rabbit meant that you should look "
        "for hidden files and folders in this directory",
        "To see any hidden folders or files you need to "
        "{{yl}}i{{ys}}t {{ya}}ll the files and folders",
        "The command {{yls -a}} lists all files and folders in the directory you are in",
        "Type {{yls -a}} and press ENTER"
    ]

    def next(self):
        Step2()


class Step2(Step_Template1):
    story = [
        "You see a small shady {{b.hidden-path}} you didn't notice before.",
        "Can you see what's down the path?"
    ]
    start_dir = "~"
    end_dir = "~"
    command = [
        "ls .hidden-path",
        "ls .hidden-path/",
        "ls -a .hidden-path",
        "ls -a .hidden-path/"
    ]
    hints = [
        "The command {{yls <Directory name>}} lets you look into a directory",
        "To look down the hidden path, type {{yls .hidden-path}}",
        "Type {{yls .hidden-path}} and press ENTER"
    ]

    def next(self):
        Step3()


class Step3(Step_Template2):
    story = [
        "Squinting, you can just about see the path "
        "leading to a dense thicket of woodland",
        "You decide to walk down the path",
        "You need to use the command {{ycd}} to {{yc}}hange {{yd}}irectory",
        "First, use {{y cd .hidden-path}} to go on the {{b.hidden-path}}"
    ]
    start_dir = "~"
    end_dir = ".hidden-path"
    command = ""
    hints = [
        "You want to {{yc}}hange your {{yd}}irectory so are in the .hidden-path "
        "directory",
        "You want to use the command {{ycd <path to directory>}} "
        "to get into the directory",
        "Use the command {{ycd .hidden-path}}"
    ]

    def next(self):
        Step4()


class Step4(Step_Template2):
    story = [
        "Have another look around"
    ]
    start_dir = ".hidden-path"
    end_dir = ".hidden-path"
    command = ["ls", "ls -a"]
    hints = [
        "To look around, you need to {{yl}}i{{ys}}t all the files in the directory",
        "Use {{yls}} to look around you.",
        "Type {{yls}} and press Enter"
    ]

    def next(self):
        Step5()


class Step5(Step_Template2):
    story = [
        "You are on the narrow dusty path leading into the woods",
        "You decide to walk into the woods"
    ]
    start_dir = ".hidden-path"
    end_dir = "woods"
    command = ""
    hints = [
        "Remember, you want to {{yc}}hange your {{yd}}irectory to the {{bwoods}} "
        "directory",
        "Type {{ycd woods}} and press Enter"
    ]

    def next(self):
        Step6()


class Step6(Step_Template2):
    story = [
        "Have a look around."
    ]
    start_dir = "woods"
    end_dir = "woods"
    command = ["ls", "ls -a"]
    hints = [
        "To look around, you need to use the command {{yls}}"
    ]

    def next(self):
        Step7()


class Step7(Step_Template2):
    story = [
        "You see you're surrounded by a lot of plants, trees and shrubbery.",
        "There's a lot of stuff here, but you have sharp eyes and take a good look round "
        "you",
        "You're looking for a hidey-hole for a rabbit",
        "When you find it, you want to enter it"
    ]
    start_dir = "woods"
    end_dir = "rabbithole"
    command = ""
    hints = [
        "Remember, {{bdirectories show up in blue}}",
        "If you scroll through the elements in this directory, you should be able to "
        "spot the rabbit's because it will be the only {{bblue}} one",
        "Remember, you want to {{yc}}hange the {{yd}}irectory to the directory you find."
    ]

    def next(self):
        Step8()


class Step8(Step_Template2):
    story = [
        "You entered the rabbithole",
        "The rabbit who dug it must be huge, the rabbithole is bigger than the average "
        "man",
        "Let's clear the terminal to end this challenge"
    ]
    start_dir = "woods"
    end_dir = "woods"
    command = "clear"
    hints = [
        "Type {{yclear}} and press Enter to clear the terminal"
    ]