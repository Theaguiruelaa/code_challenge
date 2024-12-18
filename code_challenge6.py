name = input("Enter your name: ")

prelim = eval(input("Enter your Prelim grade: "))

midterm = eval(input("Enter your Midterm grade: "))

semifinal = eval(input("Enter your Semifinals grade: "))

quiz = eval(input("Enter your Quiz grade: "))

finals = eval(input("Enter your Finals grade: "))

project = eval(input("Enter your Project grade: "))

if (prelim >= 65 and prelim <=100) and (midterm >= 65 and midterm <=100) and (semifinal >=65 and semifinal <=100) and (quiz >= 65 and quiz <=100) and (finals >= 65 and finals <=100) and (project >= 65 and project <=100):
	FG = (prelim * 0.15) + (midterm * 0.15) + (semifinal *0.15) + (finals * 0.15) + (quiz *0.25) + (project *0.15)
		
	if FG >= 75:
		print(f"Result: " , FG )
		print(f"Congratulation {name}! You passed your first year of college.")
	else:
		print(f"Result: " , FG )
		print(f"I'm sorry {name} You didn't pass your first year of college.")

else:
	print("Invalid Input")

