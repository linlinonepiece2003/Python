def draw_square(size, filling): 
    for i in range(size):
        if filling == "filled" or i == 0 or i == size - 1:
            print("*" * size)
        else:
            print("*" + " " * (size - 2) + "*")

def draw_triangle(size, filling):
    if filling == "filled":
        for i in range(1, size + 1):
            print("*" * i)
    else:
        print("*")
        for i in range(2, size):
            print("*" + " " * (i - 2) + "*")
        print("*" * size)
def main():
 while True:
   shape = input("Enter shape to draw: ").lower()
   if shape in ("square", "triangle"):
     break
   print("Invalid input. Try again.")

 while True:
   filling = input("Filled or unfilled? ").lower()
   if filling in ("filled", "unfilled"):
     break
   print("Invalid input. Try again.")

 while True:
   try:
     size = int(input("Size: "))
     if 1 <= size <= 20:
       break
     print("Invalid input. Try again.")
   except ValueError:
     print("Invalid input. Try again.")

 print()  

 if shape == "square":
   draw_square(size, filling)
 else:
   draw_triangle(size, filling)

main()