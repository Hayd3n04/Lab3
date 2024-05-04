import bmi

def test_bmi_normal_weight():
    assert(bmi.calculate_bmi(169, 58)==0) 
def test_bmi_over_weight():
    assert(bmi.calculate_bmi(169,58 )==1) 
def test_bmi_under_weight():
    assert(bmi.calculate_bmi(169,58 )==-1) 