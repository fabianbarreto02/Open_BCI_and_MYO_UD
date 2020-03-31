import threading

def printit():
  threading.Timer(0.005, printit).start()
  print ("Hello, World!")

printit()
