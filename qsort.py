'''
Author:		Ryan Wagner
Date:		August 26, 2014
Description:	Quicksort() program in python for dailyprogrammer #177.
I/O:		User inputs a string of numbers to sort,
		Program outputs the resulting sorted string.
Credits:	L/R recursion logic by /u/CatatonicMan
'''
counter = 0
def _quicksort_( int_list ):
	global counter
	counter += 1
	if( len( int_list ) <= 1 ):
		return int_list

	pivot = int_list[ ( len( int_list ) // 2 ) ]

	l = [ i for i in int_list if i < pivot ]
	r = [ i for i in int_list if i > pivot ]
	c = [ i for i in int_list if i == pivot ]
	return _quicksort_( l ) + c + _quicksort_( r )

while True:	
	try:
		int_string = str( raw_input( "Enter a number (666 exits): " ) )
		int_list = [ int( i ) for i in int_string ]
		if int( int_string ) != 666:
			print( _quicksort_( int_list ) )
			print "Sorted in %i iterations." % ( counter )
			counter = 0
		else:
			print "Exit condition met."
			break
	except ValueError:
		print( "Enter a valid integer value." )
