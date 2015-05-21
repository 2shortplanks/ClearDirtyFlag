import sublime, sublime_plugin
import os.path

class ClearDirtyFlag(sublime_plugin.ApplicationCommand):
    def run(self):
        for window in sublime.windows():
            views = window.views()
            for view in views:
                if view.is_dirty():
                    filename = view.file_name()
                    if filename and os.path.isfile(filename):
                        on_disk_contents = open(filename).read()
                        in_buffer_contents = view.substr(sublime.Region(0, view.size()))
                        if on_disk_contents == in_buffer_contents:
                            print("%s isn't really dirty" % filename)
                            view.run_command("revert")