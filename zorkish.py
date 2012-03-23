import sublime, sublime_plugin



class ZorkishTextCommand(sublime_plugin.WindowCommand):

	def run(self):
		self.window.show_input_panel("?","", self.on_done, None, None)


	def on_done(self, cmd):
		self.window.active_view().run_command("zork_process_cmd", {"cmd":cmd})
		if cmd <> "quit":
			sublime.active_window().run_command("zork_text")
		else:
			WarnUser("Good-bye!")



class ZorkishProcessCmdCommand(sublime_plugin.TextCommand):

	def run(self, edit, cmd):
		print "running"
		zp = ZorkishParser()
		zp.Parse(cmd)








########################################
#     ____                             #
#    / __ \____ ______________  _____  #
#   / /_/ / __ `/ ___/ ___/ _ \/ ___/  #
#  / ____/ /_/ / /  (__  )  __/ /      #
# /_/    \__,_/_/  /____/\___/_/       #
########################################	                                   



class ZorkishParser():
	def __init__(self):
		pass


	def Parse(self,cmd):
		print "in parse"
		splitCmd = self.split(cmd)
		if len(splitCmd) == 1:
			#must be an action or an error
			for cmdName, cmdAlias in MOVE_CMDS.iteritems():
				for alias in cmdAlias:
					if alias.lower() == splitCmd[0]:
						self.executeMove(cmdName)
						# have a winnner
		else:
			print "Error!"
			#error invalid input


	def executeMove(self, cmd):
		print "Moving " + MOVE_CMDS[cmd][0]
		pass

	def split(self, cmd):
		splitStr = cmd.lower().split(" ")
		return splitStr


MOVE_CMDS = {
	 "n" :	["North", "n"],
	 "s" :	["South", "s"],
	 "e" :	["East", "e"],
	 "w" :	["West", "w"],
	 "ne" : ["Northeast", "ne"],
	 "nw" :	["Northwest", "nw"],
	 "se" :	["Southeast", "se"],
	 "sw" :	["Southwest", "sw"],
	 "u" :	["Up", "u"],
	 "d" :	["Down", "d"],
	 "l" :	["Look"],
	 "save" :	["save"],
	 "restore" :	["restore"]
}

#  $i = item, $c = container, $l = location, $e = exit, $r = control
#  $o = object, $m = mob/creature, $d
ITM_CMDS = [
	 "take $i",
	 "take all",
	 "put $i in $c", 
	 "throw $1 at $l", 
	 "open $c", 
	 "open $e", 
	 "read $i", 
	 "drop $i",
	 "put $i in $c", 
	 "turn $r with $i", 
	 "turn on $i", 
	 "turn off $i",
	 "move $o", 
	 "attack $m with $i", 
	 "examine $o", 
	 "inventory",
	 "eat $i", 
	 "shout", 
	 "close", 
	 "tie $i to $o", 
	 "close $o", 
	 "kill self with $i",
	 "go $d"
 ]

