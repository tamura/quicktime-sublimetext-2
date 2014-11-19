import sublime, sublime_plugin, subprocess
# from subprocess import Popen, PIPE


#  ctr + F1 Start Current Movie - Plays the frontmost window in Quicktime Player after rewinding it by two seconds.
#  ctr + F2 Stop Current Movie - Stops all movies in Quicktime Player.
#  ctr + F3 Rewind Current Movie - Rewinds the frontmost window in Quicktime Player to the beginning.
# http://stackoverflow.com/questions/2940916/how-do-i-embed-an-applescript-in-in-a-python-script
#  http://www.salling.com/forums/viewtopic.php?t=5424

class QuicktimeCommand(sublime_plugin.WindowCommand):
	def run(self):


		# Play at normal speed.scpt
		# Play faster.scpt
		# Play or Pause.scpt
		# Play slower.scpt
		# Step backward.scpt
		# Step forward.scpt

		# script_Start
		# script_Stop

		# ...
		# if keyCode is in rewindKeys then
		# tell application "QuickTime Player"
		# tell movie 1
		# set steps to duration / 50
		# if steps < 6000 then set steps to 6000
		# set current time to (current time - steps)
		# end tell
		# end tell
		# else if keyCode is in forwardKeys then
		# tell application "QuickTime Player"
		# tell movie 1
		# set steps to duration / 50
		# if steps < 6000 then set steps to 6000
		# set current time to (current time + steps)
		# end tell
		# end tell
		# else if keyCode is in volumeUpKeys then
		# ... 


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

		# args = ['2', '2']

		# p = subprocess.Popen(["osascript", "-"] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
		# p = subprocess.Popen(["osascript", "-"], stdin="PIPE", stdout="PIPE", stderr="PIPE")
		p = subprocess.Popen(['ls','.'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
		stdout, stderr = p.communicate(script_Rewind)

		# ret = p.returncode
		ret = stdout
		# ret = stderr
		# p.stdout.read() ..... p.stderr.read()

		output_view = self.window.get_output_panel("textarea")
		self.window.run_command("show_panel", {"panel": "output.textarea"})
		output_view.set_read_only(False)
		edit = output_view.begin_edit()
		output_view.insert(edit, output_view.size(), script_Rewind)
		# output_view.insert(edit, output_view.size(), ret)
		output_view.end_edit(edit)
		output_view.set_read_only(True)

