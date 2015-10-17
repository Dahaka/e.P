import re,urllib
import urllib.request

programmIsActive= True;




while programmIsActive:

  
 zipCode = input("Enter zip code:\n");
 
     
 
 url= "http://www.uszip.com/zip/" + zipCode;

 try:

    print("making the connection ...");

    print("\n");
    u=urllib.request.urlopen(url);
    text=u.read();
   
    Population = re.findall(r'Total population</dt><dd>(.*?)<span', str(text));

    
    print("Total population : " + Population[0]);

    HousingUnits = re.findall(r'<dt>Housing units</dt><dd>(.*?)<',str(text));

    print("Housing units : " + HousingUnits[0]);

    LandArea = re.findall(r'Land area<br><span class="stype">\(sq. miles\)</span></dt><dd>(.*?)<',str(text));

    print("Land area : " + LandArea[0]);

    Density = re.findall(r'Density<br><span class="stype">\(people per sq. mile\)</span></dt><dd>(.*?)<',str(text));

    print("Density : " + Density[0]);

    WaterArea = re.findall(r'Water area<br><span class="stype">\(sq. miles\)</span></dt><dd>(.*?)<',str(text));

    print("Water area : " + WaterArea[0] + " \n" );
    

 except:
    print("This zip code does not exist in the US\n");

    

 choice = input("would you like to search again? y/n: ")
 if choice == "n":
     print("Ok Good bye :) ");
     programmIsActive=False;
 elif choice =="y":
     programmIsActive=True;
 else:
     print("i guess not .. bye bye :)");
     programmIsActive=False;
         
     

