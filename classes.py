# a = 8
# b = 4
# print(a+b)
# print(a.__add__(b))

# class kettle(object):
# 	power_source = "electricity"
# 	def __init__(self, make, price):
# 		self.make = make
# 		self.price = price
# 		self.on = False

# kenwood = kettle("kenwood", 8.99)
# print(kenwood.make)
# print(kenwood.price)

# print("=" *40)

# kenwood.price= 12.56
# print(kenwood.make)
# print(kenwood.price)
# print(kenwood.on)


# print("=" *40)

# hemilton = kettle("hemilton", 14.98)
# print(hemilton.make)
# print(hemilton.price)

# print("models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hemilton.make, hemilton.price))

# print("*" *40)

# kenwood.power = 1.32
# print(kenwood.power)
# print(kenwood.power_source) 
# print(hemilton.power_source)
# print(kattle.power_source)
# # print(kettle.__dict__)
# # print(kenwood.__dict__)
# # print(hamelton.__dict__)
# class Snake:
# 	pass
# 	name = "python"

# 	def change_name(self, new_name):
# 		self.name = new_name
# snake = Snake()
# print(snake.name)
# snake.change_name("deepesh")
# print(snake.name)



	
# class MyClass:
#     """A simple example class"""
#     i = 12345

#     def f(self):
#         return 'hello world'
class songs:

	def __init__(dracula, songname, singer):
		dracula.songname = songname
		dracula.singer = singer
	# def myfunc(self):
	# 	print("my fav song is " + self.songname)
	# 	self.mviname = mviname
	# 	self.seriesnum = seriesnum
# p1 = songs("IDFC_I DON'T FUCKING CARE", '1')
# p1.myfunc()				
song = songs("BATTLE SYMPHONY", "CHESTER BENNINGTON")
print("\n")

print("song name is ", song.songname)
print("singer ", song.singer)

print("=" *40)

s1 = songs("THIS IS WHAT YOU CAME FOR", "RIHANNA")
print("song name is ", s1.songname)
print("singer name ", s1.singer)
s1.songname = "tera ghata"
print(s1.songname)
print("=" *40)

s2 = songs("NEVER FORGET YOU", "ZARA LARSSON")
print("song name is ", s2.songname)
print("singer name", s2.singer)

print("-" *90)