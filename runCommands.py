from commands import *
import os

#
# Python script to run all the functions in commands.py.
#

img_dir = "src_img"
waldo = FindingWaldo(img_dir)

if not os.path.exists('info'):
    os.makedirs('info')
if not os.path.exists('data'):
    os.makedirs('data')

# Create samples for every positive images.
for i in range(0,len(waldo.pos_path)):
    waldo.createSamples(i)

# Run the rest of the function.
waldo.renameInfo()
waldo.joinInfo()
waldo.createVec()
