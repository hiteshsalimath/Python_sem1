#class variables are common for all the objects whereas instance variables are not

# class cat:
#     tail = 1
#     wiskers  = 11
#     eyes = 2
#     legs = 4
#     ears = 2
#     def __init__(self):
#         self.color = "Black"
#         print("object is created")

# tom = cat()
# angela = cat()

# #chaging the variable value of one object does not alter the valu of other objects

# tom.color = "white" #tom color is changed

# print("Angela color = ",angela.color)
# print("Tom color = ",tom.color)




class cat:
    tail = 1
    wiskers  = 11
    eyes = 2
    legs = 4
    ears = 2
    def __init__(self,color):
        self.color = color
        print("object is created")


tom = cat("grey")
angela = cat("black")

print(tom.color)
print(angela.color)
