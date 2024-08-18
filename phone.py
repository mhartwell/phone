import re

def extract_phone(input):
	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	match = phone_regex.search(input)
	if match:
		return match.group()  
	else:
		return None


def extract_all_phone(input):
	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	return phone_regex.findall(input)

def is_valid_phone(input):
	if extract_phone(input):
		return True
	else:
		return False



print(extract_phone("my number is 123 456-7891"))
print(extract_phone("my number is 123 456-789101234"))
print(is_valid_phone('123 456-7891'))
print(is_valid_phone('123 456-78'))