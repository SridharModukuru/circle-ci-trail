from main import add

def TestAdd():
    assert add(2,3) == 5
    print('add func works perfectly')


if __name__ == '__main__':
    TestAdd()