month = int(input("Enter the name:"))
year = int(input())
if month=="feb":
	print("Number of days is 28/29")
elif month in("april","june","sep","nov"):
	print("Number of days is 30")
elif month in("jan","march","may","july","aug","oct","dec"):
	print("Number of days is 31")
else:
	print("wrong month name")
