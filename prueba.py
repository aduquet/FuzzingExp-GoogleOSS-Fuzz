import sys
import zlib

import atheris

# @atheris.instrument_func
# def TestOneInput(data): 
# 	print(data.decode(errors='ignore'))
# 	try:# Our entry point
# 		if len(data) != 8:
# 		        return
# 		if chr(data[0]) == "d":
# 		   if chr(data[1]) == "e":
# 		      if chr(data[2]) == "a":
# 		          if chr(data[3]) == "d":
# 		             if chr(data[4]) == "b":
# 		                if chr(data[5]) == "e":
# 		                   if chr(data[6]) == "e":
# 		                      if chr(data[7]) == "f":
# 		                         raise RuntimeError("Error input found!")

# 	except zlib.error:
# 		pass   
# atheris.Setup(sys.argv, TestOneInput)
# atheris.Fuzz()

# @atheris.instrument_func
# def TestOneInput(a, b): 
# 	print(a.decode(errors='ignore'))
# 	print(b.decode(errors='ignore'))
# 	try:# Our entry point
# 		return a + b
# 		# if len(data) != 8:

# 		#         return a + b
# 		# if chr(data[0]) == "d":
# 		#    if chr(data[1]) == "e":
# 		#       if chr(data[2]) == "a":
# 		#           if chr(data[3]) == "d":
# 		#              if chr(data[4]) == "b":
# 		#                 if chr(data[5]) == "e":
# 		#                    if chr(data[6]) == "e":
# 		#                       if chr(data[7]) == "f":
# 		#                          raise RuntimeError("Error input found!")

# 	except zlib.error:
# 		pass   
# atheris.Setup(sys.argv,TestOneInput)
# atheris.Fuzz()
@atheris.instrument_func
def calc(a,b):

	return a+b

	

def TestOneInput(data): 
	fdp = atheris.FuzzedDataProvider(data)
	a = fdp.ConsumeInt(2)
	fdp_b = atheris.FuzzedDataProvider(data)
	b = fdp_b.ConsumeInt(3)
	print('a: ', a)
	print('b: ', b)
	print('====')
	try:
		print(calc(a,b))
	
	except zlib.error:
  		pass


		# # if len(data) != 8:

		# #         return a + b
		# # if chr(data[0]) == "d":
		# #    if chr(data[1]) == "e":
		# #       if chr(data[2]) == "a":
		# #           if chr(data[3]) == "d":
		# #              if chr(data[4]) == "b":
		# #                 if chr(data[5]) == "e":
		# #                    if chr(data[6]) == "e":
		# #                       if chr(data[7]) == "f":
		# #                          raise RuntimeError("Error input found!")
  #  except zlib.error:
		# pass   
atheris.Setup(sys.argv,TestOneInput)
atheris.Fuzz()