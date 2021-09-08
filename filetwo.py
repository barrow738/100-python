# importing the whole file
import converters

print(converters.convert_to_pounds(450))


# Or specific sections of the module
from converters import convert_to_kgs
print(convert_to_kgs(20320))