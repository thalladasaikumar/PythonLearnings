from fpdf import FPDF
import os
 
def add_image(image_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.image(image_path, x=10, y=8, w=100)
    pdf.set_font("Arial", size=12)
    pdf.ln(85)  # move 85 down
    pdf.cell(200, 10, txt="{}".format(image_path), ln=1)
    pdf.output("excel.pdf")
 
if __name__ == '__main__':
    print('present working dir :'+os.getcwd())
    os.chdir(r'E:/Learning/nabihbawazir/Excel Tips/')
    for fl, subfl, fileNames in os.walk(os.getcwd()):
        #add_image('')
        for eachFile in fileNames:
            if eachFile.endswith('.png'):
                print(eachFile)
                add_image(eachFile)