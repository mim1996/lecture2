year=int(input("please enter year\n"))
temp_year=year
while year<2018:
    year+=2
    print(year)

print("inside for loop")

year=int(input("please enter year\n"))
for x in range(temp_year,2018,1):
    print(x)
