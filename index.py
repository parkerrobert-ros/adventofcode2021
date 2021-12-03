 #!/usr/bin/env python3                                                      
 
 print("hello world")
 with open('index.txt') as f:
     lines = f.readlines()
 count = 0
 is_started = False
 prev_number = 0
 for number in lines:
     number = int(number)
     if is_started:
         if number > prev_number:
              count += 1
         prev_number = number
      else:
         is_started = True
      print(number)
     print(type(number))
  
  print(f"the answer is: {count}")