all: contrast

contrast: contrast.py 
	python contrast.py -g reverse.csv -i large-E.jpg

greyimage: greyimage.py
	python greyimage.py

clean: 
	rm -f cdata-* 

