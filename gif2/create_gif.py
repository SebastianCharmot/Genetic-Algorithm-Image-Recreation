from PIL import Image
import glob
 
# Create the frames
frames = []

# sort by name so order is preserved 
imgs = sorted(glob.glob("gif2/*.png"))
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)
 
# Save into a GIF file that loops forever
frames[0].save('gif2/created_gif.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=300, loop=0)