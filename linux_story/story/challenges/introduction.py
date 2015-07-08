#!/usr/bin/env python
#
# Copyright (C) 2014, 2015 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#
# A chapter of the story

import os
from linux_story.Terminal import Terminal
from linux_story.story.challenges.challenge_1 import Step1 as NextChallengeStep


class StepTemplateLs(Terminal):
    challenge_number = 0


class Step1(StepTemplateLs):
    story = [
        "Hello",
        "Welcome to Terminal Quest.",
        "You've entered a perilous world where words "
        "wield power, and you are going to learn to harness this power!",
        "Ready?  Press {{gb:Enter}} to begin."
    ]
    start_dir = "~/my-house/my-room"
    end_dir = "~/my-house/my-room"

    def next(self):
        NextChallengeStep()
