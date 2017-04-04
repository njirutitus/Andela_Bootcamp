def data_type(value):
	if isinstance(value,str):
		return len(value)
	if value is None:
		return "no value"
	if isinstance(value,int):
		if isinstance(value, bool):
			return value
		else:
			if value == 100:
				return 'equal to 100'
			if value < 100:
				return 'less than 100'
			if value > 100:
				return 'more than 100'
	if isinstance(value, bool):
		return value
	if isinstance(value, list):
		if len(value) >= 3:
			return value[2]
		else:
			return None