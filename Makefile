all: contrast

contrast: contrast.py 
	python contrast.py -g gamma -i large-E.jpg

clean: 
	rm -f cdata-* 

