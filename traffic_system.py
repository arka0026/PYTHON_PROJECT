#Traffic Light Console Simulator

while True:
    
    supplier=str(input("I'm a traffic light stand.Tell me colour plz:-")).capitalize()

    if supplier == "Red":
      print("Kindly stop sir.Now vehicals r continuing")
      continue
    elif supplier =="Yellow":
      print("Wait some more time plz sir")
      continue
    elif supplier == 'Green':
      print("Now you can go sir.Wish you a safe day")
      continue
    else:
      print("Techniqual problem.")
      print('thank you sir ')

      break

    

"""

- Runs in an infinite loop, repeatedly asking for a color.

- .capitalize() makes the input case-insensitive 
  (e.g. "red", "RED", "reD" all become "Red").

- Any other input - treated as invalid/technical error, 
  prints a message and ends the program (break)

"""





