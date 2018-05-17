from ctypes import Structure, windll, c_uint, sizeof, byref

class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]

def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0


if __name__ == '__main__':
	from pynput.keyboard import Controller as KeyControl, Key
	import sys, time, datetime
	
	keyboard = KeyControl()
	
	try:
		IDLE_TIMIT = int(sys.argv[1])
	except:
		IDLE_TIMIT = 60
	print 'IDLE Limit: {}'.format(IDLE_TIMIT)
		
	try:
		interval = int(sys.argv[2])
	except:
		interval = 30
	print 'Checking Interval: {}'.format(interval)
		
	try:
		key_to_press = sys.argv[3]
	except:
		key_to_press = Key.up
	print 'Key to Press: {}'.format(key_to_press.upper())
	start_time = datetime.datetime.now()
	while True:
		idle_seconds = get_idle_duration()
		if idle_seconds > IDLE_TIMIT:
			keyboard.press(key_to_press)
			print 'Pressed {} on {} idle seconds'.format(key_to_press.upper(), IDLE_TIMIT)
		time.sleep(interval)
		print 'Time: {} \tIdle: {} secs'.format(datetime.datetime.now() - start_time, idle_seconds)
		
		
		
		