def calculate_grade(marks):
    "Calculate average and grade from 5 subject marks"
    if len(marks) != 5:
        raise ValueError ("Exactly 5 subject marks are required")
    
    average = sum(marks) / 5
    
    if average >= 90:
        grade = "A+"
    elif average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "Fail"
        
    return average, grade

if __name__ == "__main__":
    marks = []
    
    for i in range(5):
        mark = float(input(f"Emter marks for subject {i+1}: "))
        marks.append(mark)
        
    avg, grade = calculate_grade(marks)
    
    print("\nAverage Marks:", avg)
    print("Grade: ", grade)