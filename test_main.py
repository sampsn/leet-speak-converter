from main import convert


def test_converter():
    assert convert("Gabriel Sampson") == "G@8r!31 5@mp50n"
    assert convert("Mike Jacks") == "M!k3 J@ck5"
