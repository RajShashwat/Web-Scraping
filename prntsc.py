#Coded by Shashwat Raj
#Program to extract images from prnt.sc

import requests
from bs4 import BeautifulSoup
import os

#Header contains the user-agent
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}

#This function provide the next code for the URL
def next_code(code):
    code_int = int(code, base)
    return code_gen(code_int + 1, base)

#This function generater the new code by incrementing the current code
def code_gen(code_num, base):
    (q, r) = divmod(code_num, base)
    if q > 0:
        return code_gen(q, base) + digit_to_char(r)
    return digit_to_char(r)

#This function converts the code digits to charactere
def digit_to_char(digit):
    if digit < 10:
        return str(digit)
    return chr(ord('a') + digit - 10)

#This function finds the image and saves the image to the defined location
def get_img(path,code):
    html = requests.get(site_url+code, headers=headers).text
    soup = BeautifulSoup(html,'lxml')
    img_urls = soup.find_all('img')
    url = img_urls[0]['src']
    response = requests.get(url)
    with open(path+".png", 'wb') as img:
        img.write(response.content)

if __name__ == '__main__':
     
    base = 36
    site_url = "http://prnt.sc/"
    
    print("Code is a 6 Character string consisting of lowercase characters and integers.")
    code = input("Enter the Code: ")
    if len(code) !=6:
        print("The Code you enter is not proper.")
        if len(code) < 6:
            print("Default code is being applied!!!")
            code = 'asd123'
        print("Your code is Updated!!!\nCode: "+code)
        code = code[:6]
    if not code.islower():
        code = code.lower()
        
    count=int(input("No of Images: "))
    output_path ='output/'

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for i in range(count):
        try:
            get_img(output_path + "/"+code,code)
            print("Image saved ("+str(i+1)+"/"+str(count)+") \t [Name: "+code+".png ] ")
        except:
            print("Error: Image not found [URL: "+site_url+code+"]")
        code = next_code(code)