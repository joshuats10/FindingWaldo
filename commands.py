import glob
import subprocess
import os
import shutil

class FindingWaldo:
    def __init__(self, img_dir):
        
        # Finding the path of the source images (both positives and negatives).
        self.pos_path = glob.glob(img_dir+"/pos/*")
        self.neg_path = glob.glob(img_dir+"/neg/*")
        
        # Allowed angle that can be changed to create samples in respective axis.
        self.max_xangle = 0.5
        self.max_yangle = 0.5
        self.max_zangle = 0.5
        
        # w -> width; h -> height
        self.w = 25
        self.h = 25

        # Formula for determining number of samples needed to be made for every positives images.
        self.num1 = int(len(self.neg_path)*2/len(self.pos_path))
        self.num2 = self.num1 + (len(self.neg_path)*2 - self.num1*len(self.pos_path))

    def createSamples(self, current_iter):

        # Deterimining number of samples needed to be made for every positive images.
        if current_iter == 0:
            num = self.num2
        else:
            num = self.num1

        os.makedirs("info/info" + str(current_iter))

        # command to create samples for one positive image.
        com = "opencv_createsamples -img src_img/pos/waldo" + str(current_iter) + ".png -bg bg.txt -info info/info"+ str(current_iter) +"/info" + str(current_iter) + \
        ".lst -pngoutput info -maxxangle " + str(self.max_xangle) + " -maxyangle " +str(self.max_yangle) + " -maxzangle " + str(self.max_zangle) + \
            " -num " + str(num)
        subprocess.call(com, shell=True)

    def renameInfo(self):
        """
            Renaming each file in every info{0} directory and info{0}.lst files, 
            as it is possible that there are same file name in different directory. 
        """
        print("Now renaming files...")

        # Updating the current number after info0 directory.
        current_num = self.num2 + 1
        current_num1 = current_num  

        for i in range(1,len(self.pos_path)):
            path = "info/info"+str(i)
            for file in sorted(os.listdir(path)):
                if file.endswith(".jpg"): # Renaming every .jpg file.
                    f_name, f_ext = os.path.splitext(file)
                    new_f_name = str(0)*(4-len(str(current_num))) + str(current_num) + f_name[4:]
                    newFileName = new_f_name+f_ext
                    os.rename(os.path.join(path,file), os.path.join(path,newFileName))
                    current_num += 1
                elif file.endswith(".lst"): # Renaming the filename inside .lst file.
                    store = []
                    info = open(os.path.join(path,file),'r')
                    for k in info.readlines():
                        new_line = str(0)*(4-len(str(current_num1))) + str(current_num1) + k[4:]
                        store = store + [new_line]
                        current_num1 += 1
                    info.close()

                    info_new = open(os.path.join(path,file),'w+')
                    for line in store:
                        info_new.write(line)
        print("Finished renaming files.")

    def joinInfo(self):
        """
            Joining/Merging every files in info{0} directory into one directory.
        """
        print("Now joining files...")
        path = 'info'
        fol = os.listdir(path)

        merged_fol = 'info_merged'
        os.makedirs(merged_fol)

        for i in fol:
            p1 = os.path.join(path,i)
            if os.path.isdir(p1) == True:
                p3 = 'cp -r ' + p1 + '/* ' + merged_fol
                subprocess.call(p3, shell=True)

        shutil.rmtree(path)
        os.rename(merged_fol,'info')
        print("Finished joining files.")

    def createVec(self):
        """
            Creating vector file
        """
        print("Now creating Vector file...")

        # Merging every info{0}.lst file into one info.lst file.
        infoLists = []
        for i in range(0,len(self.pos_path)):
            infoLists = infoLists + ['info/info'+str(i)+'.lst']

        store = []
        for j in infoLists:
            infoList = open(j,'r')
            for k in infoList.readlines():
                store = store + [k]
            infoList.close()

        final_info = open('info/info.lst', 'w+')
        for i in store:
            final_info.write(i)

        for j in infoLists:
            os.remove(j)

        # command for creating the vector file
        com2 = "opencv_createsamples -info info/info.lst -num " + str(len(self.neg_path)*2) + " -w " + str(self.w) + " -h " + str(self.h) + " -vec positives.vec"
        subprocess.call(com2, shell=2)