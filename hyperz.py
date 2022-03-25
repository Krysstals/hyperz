import sys
from os import system
from PIL import Image
from math import trunc
from pystyle import Colorate, Colors, Center, Write, Anime
system("mode 140, 40")
system("title Hyperz")
banner = '''
LSD                  H
                     |
               H  H  C--H
                `.|,'|
                  C  H  H
                  |     |
             O    N  H  C
             \\\\ ,' `.|,'|`.
               C     C  H  H
               |     |
            H--C     H
             ,' `.
      H  H--C  H--C--H
      |     ||    |
H     C     C     N  H  H
 `. ,' `. ,' `. ,' `.|,'
   C  _  C  H  C     C
   | (_) |   `.|     |
   C     C     C     H
 ,' `. ,' `. ,' `.
H     C     C     H
      |    ||
      N-----C
      |     |
      H     H

      
      [enter]
'''
imageW = """
              _-o#&&*''''?d:>b\_
          _o/\"`''  '',, dMF9MMMMMHo_
       .o&#'        `\"MbHMMMMMMMMMMMHo.
     .o\"\" '         vodM*$&&HMMMMMMMMMM?.
    ,'              $M&ood,~'`(&##MMMMMMH\\
   /               ,MMMMMMM#b?#bobMMMMHMMML
  &              ?MMMMMMMMMMMMMMMMM7MMM$R*Hk
 ?$.            :MMMMMMMMMMMMMMMMMMM/HMMM|`*L
|               |MMMMMMMMMMMMMMMMMMMMbMH'   T,
$H#:            `*MMMMMMMMMMMMMMMMMMMMb#}'  `?
]MMH#             \"\"*\"\"\"\"*#MMMMMMMMMMMMM'    -
MMMMMb_                   |MMMMMMMMMMMP'     :
HMMMMMMMHo                 `MMMMMMMMMT       .
?MMMMMMMMP                  9MMMMMMMM}       -
-?MMMMMMM                  |MMMMMMMMM?,d-    '
 :|MMMMMM-                 `MMMMMMMT .M|.   :
  .9MMM[                    &MMMMM*' `'    .
   :9MMk                    `MMM#\"        -
     &M}     Hyperz |        `          .-
      `&.    github.com/Krysstals     .
        `~,   .                     ./
            . _                  .-
              '`--._,dd###pp=\"\"'
\n\n
"""
Anime.Fade(Center.Center(banner), Colors.green_to_blue,
           Colorate.Horizontal, enter=True)
def hyperz():
  system("cls")
  print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(imageW)))
  try:
      image_path = sys.argv[1]
  except:
      image_path = Write.Input('  [>] Drag Image: ', Colors.blue_to_cyan, interval= 0.005)
  try:
    scale = int(Write.Input('  [>] Image Scale: ', Colors.blue_to_cyan, interval= 0.005))
  except:
    Write.Input(' Please enter a number.', Colors.red, interval=0)
  try:
    img = Image.open(image_path)
  except:
    Write.Input(' This file was not found.', Colors.red, interval=0)
    return
  width, height = img.size
  new_width = trunc(width/scale)
  new_height = trunc(height/scale)
  img = img.resize((new_width, new_height))
  img = img.convert('L')

  pixels = img.getdata()
  chars = ["B","S","#","&","@","$","%","*","!",":","."]
  new_pixels = [chars[pixel//25] for pixel in pixels]
  new_pixels = ''.join(new_pixels)

  new_pixels_count = len(new_pixels)
  ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
  ascii_image = "\n".join(ascii_image)
  with open("converted\converted.txt", "w") as f:
      f.write(ascii_image)
  Write.Input('\n Done! Press enter to open the file.', Colors.green_to_blue, interval= 0)
  system("notepad converted/converted.txt")

while True: hyperz()
