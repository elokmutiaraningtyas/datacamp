# list of function:
# max(list) | round(number, ndigits=None)


# ----------------------------------------------------------------------------------------------------------

# Familiar functions
# Out of the box, Python offers a bunch of built-in functions to make your life as a data scientist easier. You already know two such functions: print() and type(). There are also functions like str(), int(), bool() and float() to switch between data types. You can find out about them here. These are built-in functions as well.

# Calling a function is easy. To get the type of 3.0 and store the output as a new variable, result, you can use the following:

# result = type(3.0)

# Instructions
# 100 XP
# Use print() in combination with type() to print out the type of var1.
# Use len() to get the length of the list var1. Wrap it in a print() call to directly print it out.
# Use int() to convert var2 to an integer. Store the output as out2.

# script.py

# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)

# output ----------

# <class 'list'>
# 4

# ----------------------------------------------------------------------------------------------------------

# Help!
# Maybe you already know the name of a Python function, but you still have to figure out how to use it. Ironically, you have to ask for information about a function with another function: help(). In IPython specifically, you can also use ? before the function name.

# To get help on the max() function, for example, you can use one of these calls:

# help(max)
# ?max
# Use the IPython Shell to open up the documentation on pow(). Do this by typing ?pow or help(pow) and hitting Enter.

# Which of the following statements is true?

# answer:                                                                                                                                 
# pow() requires base and exp arguments; mod is optional.   

# ----------------------------------------------------------------------------------------------------------

# Multiple arguments
# In the previous exercise, you identified optional arguments by viewing the documentation with help(). You'll now apply this to change the behavior of the sorted() function.

# Have a look at the documentation of sorted() by typing help(sorted) in the IPython Shell.

# You'll see that sorted() takes three arguments: iterable, key, and reverse. In this exercise, you'll only have to specify iterable and reverse, not key.

# Two lists have been created for you.

# Can you paste them together and sort them in descending order?

# Instructions
# 100 XP
# Use + to merge the contents of first and second into a new list: full.
# Call sorted() and on full and specify the reverse argument to be True. Save the sorted list as full_sorted.
# Finish off by printing out full_sorted.

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)

# output ----------

# [20.0, 18.0, 11.25, 10.75, 9.5]

# ----------------------------------------------------------------------------------------------------------

# String Methods
# Strings come with a bunch of methods. Follow the instructions closely to discover some of them. If you want to discover them in more detail, you can always type help(str) in the IPython Shell.

# A string place has already been created for you to experiment with.

# Instructions
# 0 XP
# Use the .upper() method on place and store the result in place_up. Use the syntax for calling methods that you learned in the previous video.
# Print out place and place_up. Did both change?
# Print out the number of o's on the variable place by calling .count() on place and passing the letter 'o' as an input to the method. We're talking about the variable place, not the word "place"!


# There

# string to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count('o'))

# output ----------

# poolhouse
# POOLHOUSE
# 3


# ----------------------------------------------------------------------------------------------------------


# List Methods
# Strings are not the only Python types that have methods associated with them. Lists, floats, integers and booleans are also types that come packaged with a bunch of useful methods. In this exercise, you'll be experimenting with:

# .index(), to get the index of the first element of a list that matches its input and
# .count(), to get the number of times an element appears in a list.
# You'll be working on the list with the area of different parts of a house: areas.

# Instructions
# 100 XP
# Use the .index() method to get the index of the element in areas that is equal to 20.0. Print out this index.
# Call .count() on areas to find out how many times 9.50 appears in the list. Again, simply print out this number.


# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))


# Print out how often 9.50 appears in areas
print(areas.count(9.50))

# output ----------

# 2
# 1


# ----------------------------------------------------------------------------------------------------------

# List Methods (2)
# Most list methods will change the list they're called on. Examples are:

# .append(), that adds an element to the list it is called on,
# .remove(), that removes the first element of a list that matches the input, and
# .reverse(), that reverses the order of the elements in the list it is called on.
# You'll be working on the list with the area of different parts of the house: areas.

# Instructions
# 100 XP
# Use .append() twice to add the size of the poolhouse and the garage again: 24.5 and 15.45, respectively. Make sure to add them in this order.
# Print out areas
# Use the .reverse() method to reverse the order of the elements in areas.
# Print out areas once more.


# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size

areas.append(24.5)
areas.append(15.45)

# Print out areas

print(areas)

# Reverse the orders of the elements in areas

areas.reverse()


# Print out areas

print(areas)

# output ----------

# <script.py> output:
#     [11.25, 18.0, 20.0, 10.75, 9.5, 24.5, 15.45]
#     [15.45, 24.5, 9.5, 10.75, 20.0, 18.0, 11.25]



# ----------------------------------------------------------------------------------------------------------


# Import package
# Let's say you wanted to calculate the circumference and area of a circle. Here's what those formulas look like:


# Rather than typing the number for pi, you can use the math package that contains the number

# For reference, ** is the symbol for exponentiation. For example 3**4 is 3 to the power of 4 and will give 81.

# Instructions
# 100 XP
# Import the math package.
# Use math.pi to calculate the circumference of the circle and store it in C.
# Use math.pi to calculate the area of the circle and store it in A.


# Import the math package
import math

# Calculate C
C = 2 * 0.43 * math.pi

# Calculate A
A = math.pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))


# output :

# Circumference: 2.701769682087222
# Area: 0.5808804816487527


# ----------------------------------------------------------------------------------------------------------


# Selective import
# General imports, like import math, make all functionality from the math package available to you. However, if you decide to only use a specific part of a package, you can always make your import more selective:

# from math import pi
# Try the same thing again, but this time only use pi.

# Instructions
# 100 XP
# Perform a selective import from the math package where you only import the pi function.
# Use pi to calculate the circumference of the circle and store it in C.
# Use pi to calculate the area of the circle and store it in A.


# Import pi function of math package
from math import pi

# Calculate C
C = 2 * 0.43 * pi

# Calculate A
A = pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))

# output: 

# Circumference: 2.701769682087222
# Area: 0.5808804816487527



# ----------------------------------------------------------------------------------------------------------


# In [1]:
# help(str)
# Help on class str in module builtins:

# class str(object)
#  |  str(object='') -> str
#  |  str(bytes_or_buffer[, encoding[, errors]]) -> str
#  |
#  |  Create a new string object from the given object. If encoding or
#  |  errors is specified, then the object must expose a data buffer
#  |  that will be decoded using the given encoding and error handler.
#  |  Otherwise, returns the result of object.__str__() (if defined)
#  |  or repr(object).
#  |  encoding defaults to sys.getdefaultencoding().
#  |  errors defaults to 'strict'.
#  |
#  |  Methods defined here:
#  |
#  |  __add__(self, value, /)
#  |      Return self+value.
#  |
#  |  __contains__(self, key, /)
#  |      Return bool(key in self).
#  |
#  |  __eq__(self, value, /)
#  |      Return self==value.
#  |
#  |  __format__(self, format_spec, /)
#  |      Return a formatted version of the string as described by format_spec.
#  |
#  |  __ge__(self, value, /)
#  |      Return self>=value.
#  |
#  |  __getitem__(self, key, /)
#  |      Return self[key].
#  |
#  |  __getnewargs__(...)
#  |
#  |  __gt__(self, value, /)
#  |      Return self>value.
#  |
#  |  __hash__(self, /)
#  |      Return hash(self).
#  |
#  |  __iter__(self, /)
#  |      Implement iter(self).
#  |
#  |  __le__(self, value, /)
#  |      Return self<=value.
#  |
#  |  __len__(self, /)
#  |      Return len(self).
#  |
#  |  __lt__(self, value, /)
#  |      Return self<value.
#  |
#  |  __mod__(self, value, /)
#  |      Return self%value.
#  |
#  |  __mul__(self, value, /)
#  |      Return self*value.
#  |
#  |  __ne__(self, value, /)
#  |      Return self!=value.
#  |
#  |  __repr__(self, /)
#  |      Return repr(self).
#  |
#  |  __rmod__(self, value, /)
#  |      Return value%self.
#  |
#  |  __rmul__(self, value, /)
#  |      Return value*self.
#  |
#  |  __sizeof__(self, /)
#  |      Return the size of the string in memory, in bytes.
#  |
#  |  __str__(self, /)
#  |      Return str(self).
#  |
#  |  capitalize(self, /)
#  |      Return a capitalized version of the string.
#  |
#  |      More specifically, make the first character have upper case and the rest lower
#  |      case.
#  |
#  |  casefold(self, /)
#  |      Return a version of the string suitable for caseless comparisons.
#  |
#  |  center(self, width, fillchar=' ', /)
#  |      Return a centered string of length width.
#  |
#  |      Padding is done using the specified fill character (default is a space).
#  |
#  |  count(...)
#  |      S.count(sub[, start[, end]]) -> int
#  |
#  |      Return the number of non-overlapping occurrences of substring sub in
#  |      string S[start:end].  Optional arguments start and end are
#  |      interpreted as in slice notation.
#  |
#  |  encode(self, /, encoding='utf-8', errors='strict')
#  |      Encode the string using the codec registered for encoding.
#  |
#  |      encoding
#  |        The encoding in which to encode the string.
#  |      errors
#  |        The error handling scheme to use for encoding errors.
#  |        The default is 'strict' meaning that encoding errors raise a
#  |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
#  |        'xmlcharrefreplace' as well as any other name registered with
#  |        codecs.register_error that can handle UnicodeEncodeErrors.
#  |
#  |  endswith(...)
#  |      S.endswith(suffix[, start[, end]]) -> bool
#  |
#  |      Return True if S ends with the specified suffix, False otherwise.
#  |      With optional start, test S beginning at that position.
#  |      With optional end, stop comparing S at that position.
#  |      suffix can also be a tuple of strings to try.
#  |
#  |  expandtabs(self, /, tabsize=8)
#  |      Return a copy where all tab characters are expanded using spaces.
#  |
#  |      If tabsize is not given, a tab size of 8 characters is assumed.
#  |
#  |  find(...)
#  |      S.find(sub[, start[, end]]) -> int
#  |
#  |      Return the lowest index in S where substring sub is found,
#  |      such that sub is contained within S[start:end].  Optional
#  |      arguments start and end are interpreted as in slice notation.
#  |
#  |      Return -1 on failure.
#  |
#  |  format(...)
#  |      S.format(*args, **kwargs) -> str
#  |
#  |      Return a formatted version of S, using substitutions from args and kwargs.
#  |      The substitutions are identified by braces ('{' and '}').
#  |
#  |  format_map(...)
#  |      S.format_map(mapping) -> str
#  |
#  |      Return a formatted version of S, using substitutions from mapping.
#  |      The substitutions are identified by braces ('{' and '}').
#  |
#  |  index(...)
#  |      S.index(sub[, start[, end]]) -> int
#  |
#  |      Return the lowest index in S where substring sub is found,
#  |      such that sub is contained within S[start:end].  Optional
#  |      arguments start and end are interpreted as in slice notation.
#  |
#  |      Raises ValueError when the substring is not found.
#  |
#  |  isalnum(self, /)
#  |      Return True if the string is an alpha-numeric string, False otherwise.
#  |
#  |      A string is alpha-numeric if all characters in the string are alpha-numeric and
#  |      there is at least one character in the string.
#  |
#  |  isalpha(self, /)
#  |      Return True if the string is an alphabetic string, False otherwise.
#  |
#  |      A string is alphabetic if all characters in the string are alphabetic and there
#  |      is at least one character in the string.
#  |
#  |  isascii(self, /)
#  |      Return True if all characters in the string are ASCII, False otherwise.
#  |
#  |      ASCII characters have code points in the range U+0000-U+007F.
#  |      Empty string is ASCII too.
#  |
#  |  isdecimal(self, /)
#  |      Return True if the string is a decimal string, False otherwise.
#  |
#  |      A string is a decimal string if all characters in the string are decimal and
#  |      there is at least one character in the string.
#  |
#  |  isdigit(self, /)
#  |      Return True if the string is a digit string, False otherwise.
#  |
#  |      A string is a digit string if all characters in the string are digits and there
#  |      is at least one character in the string.
#  |
#  |  isidentifier(self, /)
#  |      Return True if the string is a valid Python identifier, False otherwise.
#  |
#  |      Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
#  |      such as "def" or "class".
#  |
#  |  islower(self, /)
#  |      Return True if the string is a lowercase string, False otherwise.
#  |
#  |      A string is lowercase if all cased characters in the string are lowercase and
#  |      there is at least one cased character in the string.
#  |
#  |  isnumeric(self, /)
#  |      Return True if the string is a numeric string, False otherwise.
#  |
#  |      A string is numeric if all characters in the string are numeric and there is at
#  |      least one character in the string.
#  |
#  |  isprintable(self, /)
#  |      Return True if the string is printable, False otherwise.
#  |
#  |      A string is printable if all of its characters are considered printable in
#  |      repr() or if it is empty.
#  |
#  |  isspace(self, /)
#  |      Return True if the string is a whitespace string, False otherwise.
#  |
#  |      A string is whitespace if all characters in the string are whitespace and there
#  |      is at least one character in the string.
#  |
#  |  istitle(self, /)
#  |      Return True if the string is a title-cased string, False otherwise.
#  |
#  |      In a title-cased string, upper- and title-case characters may only
#  |      follow uncased characters and lowercase characters only cased ones.
#  |
#  |  isupper(self, /)
#  |      Return True if the string is an uppercase string, False otherwise.
#  |
#  |      A string is uppercase if all cased characters in the string are uppercase and
#  |      there is at least one cased character in the string.
#  |
#  |  join(self, iterable, /)
#  |      Concatenate any number of strings.
#  |
#  |      The string whose method is called is inserted in between each given string.
#  |      The result is returned as a new string.
#  |
#  |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
#  |
#  |  ljust(self, width, fillchar=' ', /)
#  |      Return a left-justified string of length width.
#  |
#  |      Padding is done using the specified fill character (default is a space).
#  |
#  |  lower(self, /)
#  |      Return a copy of the string converted to lowercase.
#  |
#  |  lstrip(self, chars=None, /)
#  |      Return a copy of the string with leading whitespace removed.
#  |
#  |      If chars is given and not None, remove characters in chars instead.
#  |
#  |  partition(self, sep, /)
#  |      Partition the string into three parts using the given separator.
#  |
#  |      This will search for the separator in the string.  If the separator is found,
#  |      returns a 3-tuple containing the part before the separator, the separator
#  |      itself, and the part after it.
#  |
#  |      If the separator is not found, returns a 3-tuple containing the original string
#  |      and two empty strings.
#  |
#  |  removeprefix(self, prefix, /)
#  |      Return a str with the given prefix string removed if present.
#  |
#  |      If the string starts with the prefix string, return string[len(prefix):].
#  |      Otherwise, return a copy of the original string.
#  |
#  |  removesuffix(self, suffix, /)
#  |      Return a str with the given suffix string removed if present.
#  |
#  |      If the string ends with the suffix string and that suffix is not empty,
#  |      return string[:-len(suffix)]. Otherwise, return a copy of the original
#  |      string.
#  |
#  |  replace(self, old, new, count=-1, /)
#  |      Return a copy with all occurrences of substring old replaced by new.
#  |
#  |        count
#  |          Maximum number of occurrences to replace.
#  |          -1 (the default value) means replace all occurrences.
#  |
#  |      If the optional argument count is given, only the first count occurrences are
#  |      replaced.
#  |
#  |  rfind(...)
#  |      S.rfind(sub[, start[, end]]) -> int
#  |
#  |      Return the highest index in S where substring sub is found,
#  |      such that sub is contained within S[start:end].  Optional
#  |      arguments start and end are interpreted as in slice notation.
#  |
#  |      Return -1 on failure.
#  |
#  |  rindex(...)
#  |      S.rindex(sub[, start[, end]]) -> int
#  |
#  |      Return the highest index in S where substring sub is found,
#  |      such that sub is contained within S[start:end].  Optional
#  |      arguments start and end are interpreted as in slice notation.
#  |
#  |      Raises ValueError when the substring is not found.
#  |
#  |  rjust(self, width, fillchar=' ', /)
#  |      Return a right-justified string of length width.
#  |
#  |      Padding is done using the specified fill character (default is a space).
#  |
#  |  rpartition(self, sep, /)
#  |      Partition the string into three parts using the given separator.
#  |
#  |      This will search for the separator in the string, starting at the end. If
#  |      the separator is found, returns a 3-tuple containing the part before the
#  |      separator, the separator itself, and the part after it.
#  |
#  |      If the separator is not found, returns a 3-tuple containing two empty strings
#  |      and the original string.
#  |
#  |  rsplit(self, /, sep=None, maxsplit=-1)
#  |      Return a list of the substrings in the string, using sep as the separator string.
#  |
#  |        sep
#  |          The separator used to split the string.
#  |
#  |          When set to None (the default value), will split on any whitespace
#  |          character (including \n \r \t \f and spaces) and will discard
#  |          empty strings from the result.
#  |        maxsplit
#  |          Maximum number of splits.
#  |          -1 (the default value) means no limit.
#  |
#  |      Splitting starts at the end of the string and works to the front.
#  |
#  |  rstrip(self, chars=None, /)
#  |      Return a copy of the string with trailing whitespace removed.
#  |
#  |      If chars is given and not None, remove characters in chars instead.
#  |
#  |  split(self, /, sep=None, maxsplit=-1)
#  |      Return a list of the substrings in the string, using sep as the separator string.
#  |
#  |        sep
#  |          The separator used to split the string.
#  |
#  |          When set to None (the default value), will split on any whitespace
#  |          character (including \n \r \t \f and spaces) and will discard
#  |          empty strings from the result.
#  |        maxsplit
#  |          Maximum number of splits.
#  |          -1 (the default value) means no limit.
#  |
#  |      Splitting starts at the front of the string and works to the end.
#  |
#  |      Note, str.split() is mainly useful for data that has been intentionally
#  |      delimited.  With natural text that includes punctuation, consider using
#  |      the regular expression module.
#  |
#  |  splitlines(self, /, keepends=False)
#  |      Return a list of the lines in the string, breaking at line boundaries.
#  |
#  |      Line breaks are not included in the resulting list unless keepends is given and
#  |      true.
#  |
#  |  startswith(...)
#  |      S.startswith(prefix[, start[, end]]) -> bool
#  |
#  |      Return True if S starts with the specified prefix, False otherwise.
#  |      With optional start, test S beginning at that position.
#  |      With optional end, stop comparing S at that position.
#  |      prefix can also be a tuple of strings to try.
#  |
#  |  strip(self, chars=None, /)
#  |      Return a copy of the string with leading and trailing whitespace removed.
#  |
#  |      If chars is given and not None, remove characters in chars instead.
#  |
#  |  swapcase(self, /)
#  |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
#  |
#  |  title(self, /)
#  |      Return a version of the string where each word is titlecased.
#  |
#  |      More specifically, words start with uppercased characters and all remaining
#  |      cased characters have lower case.
#  |
#  |  translate(self, table, /)
#  |      Replace each character in the string using the given translation table.
#  |
#  |        table
#  |          Translation table, which must be a mapping of Unicode ordinals to
#  |          Unicode ordinals, strings, or None.
#  |
#  |      The table must implement lookup/indexing via __getitem__, for instance a
#  |      dictionary or list.  If this operation raises LookupError, the character is
#  |      left untouched.  Characters mapped to None are deleted.
#  |
#  |  upper(self, /)
#  |      Return a copy of the string converted to uppercase.
#  |
#  |  zfill(self, width, /)
#  |      Pad a numeric string with zeros on the left, to fill a field of the given width.
#  |
#  |      The string is never truncated.
#  |
#  |  ----------------------------------------------------------------------
#  |  Static methods defined here:
#  |
#  |  __new__(*args, **kwargs)
#  |      Create and return a new object.  See help(type) for accurate signature.
#  |
#  |  maketrans(...)
#  |      Return a translation table usable for str.translate().
#  |
#  |      If there is only one argument, it must be a dictionary mapping Unicode
#  |      ordinals (integers) or characters to Unicode ordinals, strings or None.
#  |      Character keys will be then converted to ordinals.
#  |      If there are two arguments, they must be strings of equal length, and
#  |      in the resulting dictionary, each character in x will be mapped to the
#  |      character at the same position in y. If there is a third argument, it
#  |      must be a string, whose characters will be mapped to None in the result.
