# THIS FILE MUST BE IN POINTNET GITHUB FOLDER

import os
nums = [1, 3, 6, 8, 10, 15, 20, 25] # number of items from each category
categories = ["airplane","bathtub","bed","bench","bookshelf","bottle","bowl","car","chair","cone","cup","curtain","desk","door","dresser","flower_pot","glass_box","guitar","keyboard","lamp","laptop","mantel","monitor","night_stand","person","piano","plant","radio","range_hood","sink","sofa","stairs","stool","table","tent","toilet","tv_stand","vase","wardrobe","xbox"]
for n in nums:
    os.system(f"touch data/modelnet40_normal_resampled/train_size{n}.txt")
    for c in categories:
        cmd = f"ls data/modelnet40_normal_resampled/{c}/ | head -{n} | sed -e 's/\.txt$//' >> data/modelnet40_normal_resampled/train_size{n}.txt"
        print(cmd)
        os.system(cmd) 
