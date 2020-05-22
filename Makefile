# MacOS file location

timesbee.out: timesbee.py
	cat /usr/share/dict/words | python3 $< > $@

lint: timesbee.py
	pycodestyle timesbee.py
