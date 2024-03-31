"""

Part 3 - Coding Exercise: Decoding a Message from a Text File

In this exercise, you will develop a function named decode(message_file). This function should read an encoded message from a .txt file and return its decoded version as a string.

Note that you can write your code using any language and IDE you want (Python is preferred if possible, but not mandatory).

Your function must be able to process an input file with the following format:

3 love
6 computers
2 dogs
4 cats
1 I
5 you

In this file, each line contains a number followed by a word. The task is to decode a hidden message based on the arrangement of these numbers into a "pyramid" structure. The numbers are placed into the pyramid in ascending order, with each line of the pyramid having one more number than the line above it. The smallest number is 1, and the numbers increase consecutively, like so:

  1
 2 3
4 5 6

The key to decoding the message is to use the words corresponding to the numbers at the end of each pyramid line (in this example, 1, 3, and 6). You should ignore all the other words. So for the example input file above, the message words are:

1: I
3: love
6: computers

and your function should return the string "I love computers".

"""

# Decode message_file using staircase decoder

def decode(message_file):

  # Create dictionary from text file

  def create_dictionary_from_text_file(file_path):
    """Creates a dictionary from a text file.

    Args:
      file_path: The path to the text file.

    Returns:
      A dictionary containing the key-value pairs from the text file.
    """

    with open(file_path, "r") as f:
      lines = f.readlines()

    dictionary = {}
    for line in lines:
      key, value = line.strip().split(" ")
      dictionary[key] = value

    # Convert dictionary keys to int
      
    dictionary_int = {int(k) : v for k, v in dictionary.items()}

    # Sort dictionary by key ascending numerically

    dictionary_sorted = dict(sorted(dictionary_int.items()))

    return dictionary_sorted

  # Create dictionary from solution file

  my_dictionary = create_dictionary_from_text_file(message_file)

  # Create list of dictionary keys

  my_dictionary_keys = list(my_dictionary.keys())

  # Create staircase of nums length

  def create_staircase(nums):
    step = 1
    subsets = []
    while len(nums) != 0:
      if len(nums) >= step:
        subsets.append(nums[0:step])
        nums = nums[step:]
        step += 1
      else:
        return False
        
    return subsets

  # Create staircase from dictionary keys

  my_staircase = create_staircase(my_dictionary_keys)

  # Create list of last element in each sub-list

  def get_last_elements(list_of_lists):
    last_elements = []
    for sublist in list_of_lists:
      last_elements.append(sublist[-1])
    return last_elements

  # Get last elements of staircase

  last_elements = get_last_elements(my_staircase)

  # Given a list of keys, find each associated value in a given dictionary

  def get_values(dict, keys):
    """Return a list of values associated with the given keys in the given dictionary.

    Args:
      dict: A dictionary.
      keys: A list of keys.

    Returns:
      A list of values.
    """

    values = []
    for key in keys:
      if key in dict:
        values.append(dict[key])
    return values

  """
  For each element in last_elements:
    find that key in my_dictionary
    print associated value
  """

  values = get_values(my_dictionary, last_elements)

  print(values)

decode("coding_qual_input.txt")
