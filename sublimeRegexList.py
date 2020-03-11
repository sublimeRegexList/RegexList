# -*- coding: utf-8 -*-
"""
    sublimeRegexList.py(regexlistCommand)

    This plug-in will output common regex list in a new view.

    ver 0.0.1 - 2020.3.11
"""

import sublime
import sublime_plugin

class regexlistCommand(sublime_plugin.TextCommand):
    def run(self, edit, seconds=10):
        regex_view = self.view.window().new_file()
        self.print_seconds(regex_view, seconds,"\\d [[:digit:]]")
        self.print_seconds(regex_view, seconds,"\\l [[:lower:]]")
        self.print_seconds(regex_view, seconds,"\\s [[:space:]]")
        self.print_seconds(regex_view, seconds,"\\u [[:upper:]]")
        self.print_seconds(regex_view, seconds,"\\w [[:word:]]")
        self.print_seconds(regex_view, seconds,"\\D [^[:digit:]]")
        self.print_seconds(regex_view, seconds,"\\L [^[:lower:]]")
        self.print_seconds(regex_view, seconds,"\\S [^[:space:]]")
        self.print_seconds(regex_view, seconds,"\\U [^[:upper:]]")
        self.print_seconds(regex_view, seconds,"\\W [^[:word:]]")

    def print_seconds(self, view, seconds, text):
        if seconds > 0:
            if seconds == 5:
                sublime.set_timeout_async(lambda: self.print_seconds(view, seconds - 1), 1000)
        else:
            text = 'Time over!'
        view.run_command('append', { 'characters': text + '\n', 'scroll_to_end': True })
