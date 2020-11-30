# sha256brute


sha256brute.py is a CPU powered SHA256 multicore alphabetic password bruteforcer
This means that it will check every possible password in SHA256 until it finds a match.
To speed things up I added multiple modes to the bruteforcing tool:
Mode 1: numeric mode
  Aliases: 1, number
  Description: will go through every possible numeric password
Mode 2: letter mode 
  Aliases: 2, letter
  Description: will go through the alphabet in uppercase and lowercase
Mode 3: lower mode 
  Aliases: 3, lower
  Description: will go through the alphabet in lowercase
Mode 4: upper mode 
  Aliases: 4, upper
  Description: will go through the alphabet in uppercase
Mode 5: all mode 
  Aliases: 5, all
  Description: will go through all characters (the alphabet in lower and uppercase and all numbers) also the slowest variant

