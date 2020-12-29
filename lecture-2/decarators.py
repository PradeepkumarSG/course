def dec(f):
  def wrapper():
    print("this is a wrapper of the function")
    f()
    print("the wrap function ends")
  return wrapper

@dec
def hello():
  print("Function")

hello()