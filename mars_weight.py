# Milestone #1: Mars Weight
# A few years ago, NASA made history with the first controlled flight on another planet. Its latest Mars Rover, Perseverance, has onboard a 50cm high helicopter called Ingenuity. Ingenuity made its third flight, during which it flew faster and further than it had on any of its test flights on Earth. Interestingly, Ingenuity uses Python for some of its flight modeling software!
# Ingenuity on the surface of Mars (source: NASA)
# When programming Ingenuity, one of the things that NASA engineers need to account for is the fact that due to the weaker gravity on Mars, an Earthling's weight on Mars is 37.8% of their weight on Earth. Write a Python program that prompts an Earthling to enter their weight on Earth and prints their calculated weight on Mars.
# The output should be rounded to two decimal places when necessary. Python has a round function which can help you with this. You pass in the value to be rounded and the number of decimal places to use. In the example below, the number 3.1415926 is rounded to 2 decimal places which is 3.14.

#------------------------------------------------------------------------------------------------------------

    
Mars_CONSTANT = 37.8 
    

def get_mars_weight():
    # MIlstone 1 : get user weight

  try:
    user_weight: float = float(input("What is your weight on earth? "))
  except ValueError:
        return "Invalid input! Please enter a valid number for your weight."

    #Milestone 2 : get planet Name
  planet_name :str = input("What is your planet Name? ")

    # Milestone 3 : which planet is constant
  gravity_constant = 0
  if planet_name == "mars":
    gravity_constant = Mars_CONSTANT

    #Milestone 2: Find user weight on Mars
   
  weight = round((user_weight * Mars_CONSTANT /100), 2) # Now Mars_CONSTANT is a float
    
  return f"your weight on {planet_name.lower()} is {weight} kg is"

  

print(get_mars_weight())



