from class3 import program

def d():
	
	def local():
		drac = "track1"

	def dglobal():
		global drac
		drac = "track2"

	def dnonlocal():
		nonlocal drac
		drac = "track3"
	
	drac = "local tracks"	
	local()
	print("when you play 'PROMISE NOT TO FALL' it's called", drac)
	dglobal()
	print("when you play 'THE NIGHT WE MET' it's called", drac)
	dnonlocal()
	print("when you play 'NEVER FORGET YOU' it's called", drac)
d()
# print("favourate song 'READY TO RUN' comes under", drac)