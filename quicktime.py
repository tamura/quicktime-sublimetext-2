import sublime, sublime_plugin
import subprocess
# from subprocess import Popen, PIPE


class QuicktimeCommand(sublime_plugin.WindowCommand):
	def run(self):

		script_Rewind = '''
		tell application "QuickTime Player"
			try
				if not (exists document 1) then error
				tell document 1
					set rate_temp to the rate
					set current time to current time - 8
					play
					set the rate to rate_temp
		current time
				end tell
			on error error_quit
			end try
		end tell
		'''

		p = subprocess.Popen(["osascript", "-"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

		stdout, stderr = p.communicate(script_Rewind)


		output_view = self.window.get_output_panel("textarea")
		self.window.run_command("show_panel", {"panel": "output.textarea"})
		output_view.set_read_only(False)
		edit = output_view.begin_edit()
		output_view.insert(edit, output_view.size(), stdout)

		output_view.end_edit(edit)
		output_view.set_read_only(True)

# import sys, sublime, sublime_plugin
# from optparse import OptionParser

# platform = sys.platform

# if platform == "win32":
#     import win32com.client
#     qtp = win32com.client.gencache.EnsureDispatch("QuickTimePlayerX.Application")
# else:
#     from Foundation import *
#     from ScriptingBridge import *
#     qtp = SBApplication.applicationWithBundleIdentifier_("com.apple.QuickTimePlayerX")



# class QuicktimeCommand(sublime_plugin.WindowCommand):
# 	def run(self):

		# qtp.playpause()


