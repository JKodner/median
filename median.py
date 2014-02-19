def median(lst):
	"""Finds the median of a sequence of numbers."""
	status = True
	for i in lst:
		if type(i) != int:
			status = False
	if status:
		lst.sort()
		if len(lst) % 2 == 0:
			num = len(lst) / 2
			num2 = (len(lst) / 2) + 1
			avg = float(lst[num - 1] + lst[num2 - 1]) / 2
			median = {"median": avg, "positions": [lst[num - 1], lst[num2 - 1]]}
		elif len(lst) % 2 != 0:
			num = (len(lst) + 1) / 2
			median = {"median": lst[num - 1], "position": num}
		return median
	else:
		raise ValueError("Inappropriate List")