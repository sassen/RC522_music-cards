#!/usr/bin/env python
import RPi.GPIO as GPIO
import MFRC522
MIFAREReader = MFRC522.MFRC522()
def readCard():
	while True:
		# Scan for cards
		(status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
		# If a card is found
		if status == MIFAREReader.MI_OK:
			print "Card detected"
			break

	# Get the UID of the card
	(status,uid) = MIFAREReader.MFRC522_Anticoll()
	if uid:
		#print uid
		return uid

print 'Ready: place a card on top of the reader'

while True:
	try:
		card = readCard()
		print card
	except KeyboardInterrupt:
		GPIO.cleanup()
		sys.exit(0)
