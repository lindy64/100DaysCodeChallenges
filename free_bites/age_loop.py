MIN_DRIVING_AGE = 18

def allowed_driving(name, age):
    if age >= MIN_DRIVING_AGE:
        print(f"{name} is allowed to drive")
    else:
        print(f"{name} is not allowed to drive")


def test_not_allowed_to_drive(capfd):
    allowed_driving('tim', 17)
    output = capfd.readouterr()[0].strip()
    assert output == 'tim is not allowed to drive'


def test_allowed_to_drive(capfd):
    allowed_driving('bob', 18)
    output = capfd.readouterr()[0].strip()
    assert output == 'bob is allowed to drive'

    allowed_driving('julian', 19)
    output = capfd.readouterr()[0].strip()
    assert output == 'julian is allowed to drive'