from main import leet_converter


def test_converter():
    assert leet_converter("Gabriel Sampson") == "G@8r!31 5@mp50n"
    assert leet_converter("Mike Jacks") == "M!k3 J@ck5"
