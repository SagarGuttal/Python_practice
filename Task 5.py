dict1 = { 
   "april_batch":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "python":80,
            "maths":70
         }
      }
   }
}


#access "Mike"
print(dict1["april_batch"]["student"]["name"])

#access 80
print(dict1["april_batch"]["student"]["marks"]["python"])

#change "Mike" to "Your name"change "Mike" to "Your name"
dict1["april_batch"]["student"]["name"]="sagar"
print(dict1)

#add ML = 80 and DL = 80 inside marks
dict1["april_batch"]["student"]["marks"]={"ML":80,"DL":70}
print(dict1)
