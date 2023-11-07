## Site operation instructions:
## locate desired menu trees from embedded code (ex. http://github.captiveaire.com/Embedded/MUA/blob/develop/Src/MUA_board/assets/DoasMenu.smdsgn)
## download as text files, then run this program, then run index.html

import fnmatch
import os

for file in os.listdir("."):
    if fnmatch.fnmatch(file.upper(), '*.TXT'):
        with open(file, "r+") as f:
             old = f.read() # read everything in the file
             if old[0] == "{":
                 f.seek(0) # rewind
                 f.write(str(file)[0:-4] + " = " + old) #prepend the thing
