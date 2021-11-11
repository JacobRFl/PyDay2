def crowd_test(l):
 if len(l) > 3:
  print("Its crowded in here")
 else:
  print("Its not very crowded in here")
l=["sam","ren","jean","bennett"]
print(len(l))
crowd_test(l)
l.remove("sam")
print(l)
l.remove("ren")
crowd_test(l)
print(l)

def mob_test(l):
 if len(l)>5:
  print("there is a mob in here")
 elif len(l) >= 3:
  print("Its crowded in here")
 elif len(l) >= 1:
  print("Its not very crowded in here")
 else:
  print("room is empty")
l=["sam","ren","jean","bennett","tod","james"]
print(len(l))
mob_test(l)
l.remove("sam")
print(l)
l.remove("ren")
mob_test(l)
print(l)
l=[]
mob_test(l)