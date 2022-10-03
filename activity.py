"""
	Activity:
	1. Create an activity folder and an activity.py file inside of it.
	2. Create 5 variables and output them in the command prompt in the following format:
	- "I am < name (string)> , and I am < age (integer)> years old, I work as a < occupation (string)> , and my rating for < movie (string)> is < rating (decimal)> %"
	3. Create 3 variables, num1, num2, and num3
	- Get the product of num1 and num2
	- Check if num1 is less than num3
	- Add the value of num3 to num2
	4. Create a git repository named s01.
	5. Initialize a git repository, stage the files in preparation for a commit, create a commit with the message Add Activity Code and push the changes to the remote repository.
	6. Add the link in Boodle
"""

name = "Jose"
age = 38
occupation = "writer"
movie = "one more chance"
rating = 99.6

print(f"I am {str(name)}, and I am {int(age)} years old, I work as a {str(occupation)}, and my rating for {str(movie)} is {float(rating)}%")

num1, num2, num3 = 3, 50, 150

print(num1 * num2)
print(num1 < num3)

