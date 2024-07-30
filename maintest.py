from main import add

def TestAdd():
    assert add(2,3) == 5
    print('add func works perfectly')


if __name__ == '__main__':
    TestAdd()# Import the Add function, and assert that it works correctly.
from main import Add

def TestAdd():
        assert Add(2,3) == 5
        print("Add Function works correctly")

if __name__ == '__main__':
        TestAdd()