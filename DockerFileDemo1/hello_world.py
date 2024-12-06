import pandas as pd

print("this is my first image")

def print_hi(name):
    print(f'Hi,{name}')
    data = {'Name' : ['John','Alice','Bob'],
            'Age' : [28,24,22],
            'City' : ['New York', 'San Francisco', 'Los Angles']
            }

    df = pd.DataFrame(data)
    print(df)

if __name__ == '__main__':
    print_hi('PyCharm')