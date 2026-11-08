from main import validate,ValidateData

# def test_dict_keys():
#     data = {"date":"2022-01-01","category":"house","amount":150}

#     valide = ValidateData.dict_keys(data)
#     assert valide == (False, "missing keys:{'description'}"), f"Expected 'False' but got {valide}"


def test_validate():
    data = {"date":"2022-01-01","category":"house","amount":0,"description":"house needed"}
    is_valide = validate(data)
    assert is_valide == (False,["amount can not be 0"]), f"Expected '(True,[])' but got {validate(data)}"