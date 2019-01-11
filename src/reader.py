import os
import sys
class Reader:
    
    def __init__(self, f):
        self.fileObj = self.open_file(f)
        self.maze = self.read(self.fileObj)
        #print(self.maze)

    def valid(self, c):
        ''' Return true if character is valid '''
        if c == '0' or c == '1':
            return True
        else:
            return False

    def open_file(self, f):
        ''' Return open file object '''
        if os.path.isfile(f): 
            fObj = open(f, "r")
            return fObj
        else:
            print('Could not open maze file ' + f)
            sys.exit(1)

    def read(self, fObj):
        row = []
        col = []
        for line in fObj:
            for c in line:
                if self.valid(c):
                    row.append(int(c))
            col.append(row)
            row = []
        fObj.close()
        return col
