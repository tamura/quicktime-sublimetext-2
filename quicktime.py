import sublime, sublime_plugin
import subprocess
from subprocess import Popen, PIPE


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
				end tell
			on error error_quit
			end try
		end tell
		'''

		p = subprocess.Popen(["osascript", "-"], stdin=PIPE, stdout=PIPE, stderr=PIPE)

		stdout, stderr = p.communicate(script_Rewind)


