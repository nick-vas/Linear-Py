class Vector(object):
	#Creates a vector based on input of coordinates
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
			#Sets the dimension of space the vector lives in
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

	#prints the coordinates of the vector 
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

	#Compare 2 vectors and return bool of their equality 
    def __eq__(self, v):
		#Compares amount of change
        return self.coordinates == v.coordinates

    #Add 2 vectors and return their sum
    def __add__(self,v):
        return [x+y for x,y in zip(self.coordinates, v.coordinates)]

    #Substract 2 vectors and return the result
    def __sub__(self,v):
        return [x-y for x,y in zip(self.coordinates, v.coordinates)]

    #Multiply a vector by a Scalar and return the result
    def __scale__(self,scalar):
        return [scalar*x for x in self.coordinates]

#Tests
my_vector = Vector([1,2,3])
print (my_vector)
my_vector2 = Vector([1,2,3])
my_vector3 = Vector([-1,2,3])
#Equality tests
print (my_vector == my_vector2)
print (my_vector == my_vector3)

#Sum, Sub and Scalar tests
print (my_vector.__add__(my_vector))
print (my_vector.__sub__(my_vector))
print (my_vector.__scale__(2))