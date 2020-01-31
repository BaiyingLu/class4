def test_HDL_analysis_normal():
    from chol_analysis import HDL_anaysis
    answer = HDL_anaysis(80)
    expected = "Normal"
    assert answer == expected#look for  assertion error to see if it is correct
def test_HDL_analysis_bl():
    from chol_analysis import HDL_anaysis
    answer = HDL_anaysis(40)
    expected = "Borderline low"
    assert answer == expected
def test_LDL_anaysis():
    from chol_analysis import LDL_anaysis
    answer = LDL_anaysis(150)
    expected = "Borderline low"
    assert answer == expected
def test_fever_check():
    from chol_analysis import fever_check
    new_data = [96.0,100,105.1,97]
    answer = fever_check(new_data)
    exepcted = True
    assert answer == expected
