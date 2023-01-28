from PIL import Image
import re
import glob
 
# Create the frames
frames = []

# sort by name so order is preserved 
# THIS METHOD DOES NOT WORK 
# imgs = sorted(glob.glob("*.png"))

imgs = sorted(glob.glob("*.png"))
imgs.pop(0)
imgs.sort(key=lambda f: int(re.sub('\D', '', f)))
print(imgs)
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)


 
# Save into a GIF file that loops forever
frames[0].save('created_gif_new.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=200, loop=0)