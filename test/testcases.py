import pytest
from src.student_grade_calculator import calculate_grade

def test_A_plus_grade():
    avg, grade = calculate_grade ([95, 92, 93, 94, 91])
    assert grade == "A+"
    
def test_A_grade():
    avg, grade = calculate_grade ([80, 78, 76, 75, 79])
    assert grade == "A"
    
def test_B_grade():
    avg, grade = calculate_grade ([65, 60, 62, 63, 64])
    assert grade == "B"
    
def test_C_grade():
    avg, grade = calculate_grade ([50, 52, 54, 51, 53])
    assert grade == "C"
    
def test_Fail_grade():
    avg, grade = calculate_grade ([40, 42, 45, 43, 41])
    assert grade == "Fail"
    
def test_invalid_number_of_subjects():
    with pytest.raises(ValueError):
        calculate_grade([90, 80, 70])