from sympy.combinatorics import Permutation
from SymmetricGroupGeneratorsConstructor import SymmetricGroupGeneratorsConstructor
from math import sqrt, ceil


class AntiMagicSquareGenerator(object):

    # As we will need to go through all possible permutations of a square with numbers,
    # we will initiate the class by identifying a Symmetric Group of degree equal to
    # the multitude of the possible numbers in the square.
    #
    # See the SymmetricGroupGeneratorsConstructor class and its references for more
    # information on why the generators can be a 2 and 3 order elements.
    def __init__(self, degree_or_generators):
        error_class_start = 'Error at initiating the class: '
        # The parameter can either be the degree (integer) or the generators (tuple of Permutations)
        if isinstance(degree_or_generators, int):
            degree = degree_or_generators
            # Validate the degree
            if degree < 1:
                raise RuntimeError(error_class_start + 'Degree needs to be greater than 0.')
            # Construct the generators
            constructor = SymmetricGroupGeneratorsConstructor(degree)
            generators = constructor.construct()
        elif isinstance(degree_or_generators, tuple):
            generators = degree_or_generators
            # Validate the generators
            if len(generators) != 2 or not isinstance(generators[0], Permutation) or not isinstance(generators[1], Permutation):
                raise RuntimeError(error_class_start + 'Generators need to be a tuple of two Permutations.')
            if generators[0].size != generators[1].size:
                raise RuntimeError(error_class_start + 'Generators need to have the same degree.')
            # Get the degree from a generator
            degree = generators[0].size
        else:
            raise RuntimeError(
                error_class_start + 'Provide either a positive integer or a tuple of the two Permutation generators')

        # The Symmetric Group defined needs to represent a Square
        order = sqrt(degree)
        if ceil(order) != order:
            raise RuntimeError(error_class_start + 'Degree needs to be a square number.')

        # Set the Symmetric Group's degree and generators that identify it
        self.degree = degree
        self.generators = generators
        self.order = ceil(order)

    def is_magic_square(self, el):
        # Get the Magic Constant, i.e. the number to which all columns, rows and diagonals are equal
        magic = 0
        for i in range(self.order):
            magic += el(i)
        # Initialise diagonal numbers.
        magic_diag_ford = 0
        magic_diag_back = 0
        # Start iterating one dimension of the square.
        for i in range(self.order):
            # Initialise the row and column numbers.
            magic_row = 0
            magic_col = 0
            # Start iterating the second dimension of the square.
            for j in range(self.order):
                # We build the row and column magic number by using the order of the square (which
                # is also the size of a row/column) to iterate through the columns of the square.
                magic_row += el(i*self.order+j)
                magic_col += el(j*self.order+i)
            if magic_row != magic or magic_col != magic:
                return False
            # To build the diagonal magic number we only need one dimension.
            magic_diag_ford += el(i*(self.order+1))
            magic_diag_back += el((i+1)*(self.order-1))
        if magic_diag_ford != magic or magic_diag_back != magic:
            return False
        return True
