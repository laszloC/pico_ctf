#!/usr/bin/python3 -u
import os.path

KEY_FILE = "key"
KEY_LEN = 50000
FLAG_FILE = "flag"

FLAG_LEN = 0

def startup(key_location):
	global FLAG_LEN
	flag = open(FLAG_FILE).read()
	print(len(flag))
	FLAG_LEN = len(flag)
	kf = open(KEY_FILE, "rb").read()

	start = key_location
	stop = key_location + len(flag)

	key = kf[start:stop]
	key_location = stop

	print(key)

	result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), flag, key))
	print("This is the encrypted flag!\n{}\n".format("".join(result)))

	return key_location

def encrypt(key_location):
	# ui = input("What data would you like to encrypt? ").rstrip()
	ui = (b"\x00" * KEY_LEN).decode()
	if len(ui) == 0 or len(ui) > KEY_LEN:
		return -1

	start = key_location
	stop = key_location + len(ui)

	kf = open(KEY_FILE, "rb").read()

	if stop >= KEY_LEN:
		stop = stop % KEY_LEN
		key = kf[start:] + kf[:stop]
	else:
		key = kf[start:stop]
	key_location = stop

	result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), ui, key))

	print("Here ya go!\n{}\n".format("".join(result)[-(FLAG_LEN * 2):]))

	return key_location


print("******************Welcome to our OTP implementation!******************")
c = startup(0)
# while c >= 0:
c = encrypt(c)
# to_encrypt = b"\x00" * KEY_LEN
# encrypt(to_encrypt)

