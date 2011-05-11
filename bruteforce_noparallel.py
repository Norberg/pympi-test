import hashlib
from find_password import find_password

if __name__=="__main__":
	passwd = find_password(hashlib.sha256("simon22").hexdigest(), 0, 1)
	print passwd
