try:
    
    with open("my_file.txt", "w") as file:
       
        file.write("27th is the date today\n")
        file.write("We have 3 holidays this month\n")
        file.write("PLP has 3000 students\n")


    with open("my_file.txt", "r") as file:
        
        print("Contents of my_file.txt:")
        print(file.read())

 
    with open("my_file.txt", "a") as file:
        
         file.write("Line 4: Appended line 4\n")
         file.write("Line 5: Appended line 5\n")
         file.write("Line 6: Appended line 6\n")


except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

except Exception as e:
    print("An error occurred:", e)

finally:
    print("File handling completed.")
