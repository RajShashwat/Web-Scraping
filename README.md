# Web-Scrapping
This is a code to extract billions of free images form internet. 

So there is a website called prnt.sc which contains more than a billion images from different source. This site allow user to easilly upload the images through different sources as web interface and screen capture tools. They are freely available to download.

The amount of images provided on the website can be really usefull, specially for someone working with images, ML, DL, or AI. This collection is a very intresting because the images are randomly scattered and there is no structure in them. There ia a great variance among the images there. Simply we can say that its the treasure for developers, just we need to extract it.

I developed a tool to extract images from this site so it can be used by developers.

How this site works:

 This the the URL for the site : prnt.sc/
 
 Now after this the images canbe found by entring a 6 character string consisting of only lowercase character and digits.
 Examples:
 prnt.sc/asd123
 
 Now just like this every images is stored at a unique aaddress. So to get the image u will have tyo enter the 6 character string after prnt.sc/ every time to get a new image.
 
So here I have the code to automate the process of generating the 6 character string and then downloading the images from the website.
