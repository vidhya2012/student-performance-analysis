students = {
    "Arjun":{"marks":[80,87,92,99,83]},
    "Maran":{"marks":[86,89,97,99,89]},
    "jeet":{"marks":[45,50,40,56,47]},
    "veera":{"marks":[85,88,92,93,81]},
    "Yash":{"marks":[35,42,38,39,40]}    
}
def calculate_average(marks):
    total = 0
    for m in marks:
        total += m
    return total/len(marks)
def assign_grade(avg):
    if avg>= 80:
        return"A"
    elif avg>= 60:
        return"B"
    elif avg>=50:
        return"C"
    else:
        return"Fail"
pass_count = 0
fail_count = 0
highest_avg = 0
topper =""
print("Name\tAverage\tGrade")
print("-----------------------")
for name,data in students.items():
    avg = calculate_average(data["marks"])
    grade = assign_grade(avg)
    
    #Pass/Fail count
    if avg>=50:
        pass_count += 1
    else:
        fail_count +=1
    #Find Topper
    if avg>highest_avg:
        highest_avg=avg
        topper = name
    print(name,"\t",round(avg,2),"\t",grade)
print("\nPassed students:",pass_count)
print("Failed students:",fail_count)
print("Topper:",topper,"with average:",round(highest_avg,2))
