# module for youtube
from pytube import YouTube

#taking video url for download
print("----------------------------------------------")
url=input("please enter  youtube vedio url : \n")
print("----------------------------------------------")

#method for getting all strams which are available
vedios=YouTube(url).streams.all()
number=1

#for Clear view of streams with choice no
for vedio in vedios:
    print(f"{number} for {vedio}")
    print(" ")
    number+=1

#Option for user choise by no
user_input=int(input("enter your choise "))

vedios=vedios[user_input-1]
#file loacation to download
vedios.download("download")

#file Downloaded messege
print(" file downloaded successfullyl")



