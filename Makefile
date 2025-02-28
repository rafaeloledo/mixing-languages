compile:
	gcc -shared -o libutil.so -fPIC hello.c

run:
	python main.py

useful:
	readelf -d libutil.so
	nm libutil.so
	readelf -s libutil.so
	objdump -s libutil.sso
