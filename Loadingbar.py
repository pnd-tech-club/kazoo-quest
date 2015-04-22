from __future__ import print_function
desu = []
global wait
wait = 0
while len(desu) < 20:
	wait += 1
	if wait >= 300000:
		desu.extend('|')
		wait = 0
	if wait >= 3000000:
		desu.extend('|')
		wait = 0
	if wait >= 5000000:
		desu.extend('|')
		wait = 0
	if wait >= 100000:
		desu.extend('|')
		wait = 0
	if wait >= 1000000:
		desu.extend('|')
		wait = 0
	if wait >= 9000000:
		desu.extend('|')
		wait = 0
	if wait >= 100000:
		desu.extend('|')
		wait = 0
	if wait >= 2500000:
		desu.extend('|')
		wait = 0
	if wait >= 1337000:
		desu.extend('|')
		wait = 0
	if wait >= 420000:
		desu.extend('|')
		wait = 0
	print(''.join(desu), end = '\r')
print('\n')
import kazooquest
