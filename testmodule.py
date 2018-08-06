class songs:

  def __init__(dracula, songname, singer, vartuple):
    dracula.songname = songname
    dracula.singer = singer
    dracula.vartuple = vartuple
    for var in dracula.vartuple:
    	print(var)
	# def myfunc(self):
	# 	print("my fav song is " + self.songname)
	# 	self.mviname = mviname
	# 	self.seriesnum = seriesnum
# p1 = songs("IDFC_I DON'T FUCKING CARE", '1')
# p1.myfunc()				
song = songs("BATTLE SYMPHONY", "CHESTER BENNINGTON" , 'abc' , 'cde' , 'efg' ,'sss')
# print("\n")

print("song name is ", song.songname)
print("singer ", song.singer)

# print("=" *40)
# songs("shining", "Atif", 7,8,9,0,6,5,4,3,3,2,2,2)
# s1 = songs("THIS IS WHAT YOU CAME FOR", "RIHANNA")
# print("song name is ", s1.songname)
# print("singer name ", s1.singer)
# s1.songname = "tera ghata"
# print(s1.songname)
# print("=" *40)

# s2 = songs("NEVER FORGET YOU", "ZARA LARSSON")
# print("song name is ", s2.songname)
# print("singer name", s2.singer)

# print("-" *90)

# def greeting(name):
#   print("Hello, " + name)

# person1 = {
#   "name": "John",
#   "age": 36,
#   "country": "Norway"
# }