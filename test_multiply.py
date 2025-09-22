from multiply import multiply

def test_first_one():
    assert multiply(1,1)==1

def test_second():
    assert multiply(2,2)==4  

def test_third():
    assert multiply(3,3) ==9    

def test_large_numbers():
    assert multiply(34,56)==34*56    