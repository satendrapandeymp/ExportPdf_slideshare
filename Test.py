import requests, os
from fpdf import FPDF

def download_file(add, name):
	request = requests.get(add, timeout=60, stream=True)
	#Open the output file and make sure we write in binary mode
	flag = 0
	with open(name, 'wb') as fh:
	    # Walk through the request response in chunks of 1024 * 1024 bytes, so 1MiB
	    for chunk in request.iter_content(1024 * 1024):
	        # Write the chunk to the file
    		flag += 1
    		if flag > 10:
    			Log_file.write("This file is bigger than 10MB so download it if you want-- " + add + '\n\n')
    			break
            fh.write(chunk)

# Fill the image location as given in this example

#add = "https://image.slidesharecdn.com/moleculardrivingforcebykenadillsarinabromberg-160126115055/95/molecular-driving-force-by-ken-a-dill-sarina-bromberg-"

add = raw_input("type image location as described in Readme.md : ")

add1 = "-1024.jpg?cb=1453809353"

pdf = FPDF()

# No of pages = 661

pages = raw_input("Type Number of pages : ")
pdfname = raw_input("Type name of pdf with .pdf in last like xyz.pdf : ")

pages = int(pages)

for i in range(pages):
    i += 1
    link = add + str(i) + add1
    name = str(i) + ".jpg"

    try:

        download_file(link, name)
        pdf.add_page()
        pdf.image(name,0,0,210,297)
        os.remove(name)

    except:

        print "Error at adding Page No. " + str(i)

pdf.output(pdfname, "F")
