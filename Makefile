compile_c:
	gcc --shared -o libutil.so -fPIC hello.c

run:
	python main.py
