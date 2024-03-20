def view_classlist():
    with open("classlist.txt" , "r") as f:
        file_contents = f.read()
        print(file_contents)        

 