import sys

class File:
    
    def __init__(self, file_name):
        self.f = open(file_name, "w")
        
    def writer(self, text):
        #print("text : " + text)
        self.f.write( text )

    def close(self):
        self.f.close()

        
''' Main '''

f = File("newfile.txt")
f.writer( 'Test message' )
f.close()

        



