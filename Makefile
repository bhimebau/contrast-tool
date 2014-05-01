all: contrast

contrast: contrast.py 
#	python contrast.py -g gammatable.csv -i COAS_300-Landolt_C_small.jpg
#	python contrast.py -g gammatable.csv -i COAS_600px-Landolt_Cv2.jpg 
	python contrast.py -g gammatable.csv -i large-E.jpg
greyimage: greyimage.py
	python greyimage.py

clean: 
	rm -f cdata-* 

