import sys
def valid(c):
    if c == '0' or c == '1':
        return True
    else:
        return False

def read(f):
    row = []
    col = []
    with open(f) as fileObj:
        for line in fileObj:
            for c in line:
                if valid(c):
                    row.append(int(c))
            col.append(row)
            row = []
        return col

def main():
    col = read(sys.argv[1])
    print(col)

