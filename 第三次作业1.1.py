chart1=['','    ##    ',' #######   ',' #######',' ######  ',' ####### ',' ####### ',' ###### ',' #      #',' ##### ','  ##### ',' #   #  ',' #      ',' #       # ',' ##     # ','   #####   ',' ######  ','  #####   ','  #####   ','  ####  ',' ####### ',' #      # ',' #     #  ',' #       # ',' ##   ## ',' #     # ',' #######']                                                        
chart2=['','  ##  ##  ',' #      #  ','#       ','#      # ',' #       ',' #       ','#       ',' #      #','   #   ','    #   ',' #  #   ',' #      ',' # #   # # ',' # #    # ','  #     #  ',' #     # ',' #     #  ',' #     #  ',' #      ','    #    ',' #      # ',' #     #  ',' #   #   # ','   # #   ','  #   #  ','      # ']                              
chart3=['',' ######## ',' ########  ','#       ','#      # ',' ######  ',' ######  ','#   ### ',' ########','   #   ','    #   ',' ##     ',' #      ',' #  # #  # ',' #  #   # ',' #       # ',' ######  ',' #   # #  ',' ######   ','  ####  ','    #    ',' #      # ','  #   #   ',' #   #   # ','    #    ','   # #   ','    #   ']
chart4=['',' #      # ',' #       # ','#       ','#      # ',' #       ',' #       ','#     # ',' #      #','   #   ','    #   ',' # #    ',' #      ',' #   #   # ',' #   #  # ',' #       # ',' #       ',' #   # #  ',' #    #   ','      # ','    #    ',' #      # ','  #   #   ','  # # # #  ','    #    ','    #    ','   #    ']                                                                                                                                                                                                                                                     
chart5=['',' #      # ',' #       # ','#       ','#     #  ',' #       ',' #       ','#     # ',' #      #','   #   ','#   #   ',' #  #   ',' #      ',' #       # ',' #    # # ','  #     #  ',' #       ',' #    #   ',' #     #  ','      # ','    #    ','  #    #  ','   # #    ','  # # # #  ','   # #   ','    #    ','  #     ']                           
chart6=['',' #      # ',' ########  ',' #######','######   ',' ####### ',' #       ',' ###### ',' #      #',' ##### ',' ###    ',' #   ## ',' ###### ',' #       # ',' #     ## ','   #####   ',' #       ','  #### #  ',' #      # ',' #####  ','    #    ','   ####   ','    #     ','   #   #   ',' ##   ## ','    #    ',' #######']
upsidedown=raw_input('do you want the character upsidedown(y/n)')
character=raw_input('enter the character:')
character_list=list(character.lower())
n=len(character_list)
if 'n' in upsidedown:
 if n==1:
  print chart1[ord(character_list[0])-96]
  print chart2[ord(character_list[0])-96]
  print chart3[ord(character_list[0])-96]
  print chart4[ord(character_list[0])-96]
  print chart5[ord(character_list[0])-96]
  print chart6[ord(character_list[0])-96]
 else:
  x=0
  while x<=n-2:
   print chart1[ord(character_list[x])-96],
   x+=1
  print chart1[ord(character_list[n-1])-96]
  y=0
  while y<=n-2:
   print chart2[ord(character_list[y])-96],
   y+=1           
  print chart2[ord(character_list[n-1])-96]             
  z=0
  while z<=n-2:
   print chart3[ord(character_list[z])-96],
   z+=1           
  print chart3[ord(character_list[n-1])-96]             
  a=0
  while a<=n-2:
   print chart4[ord(character_list[a])-96],
   a+=1           
  print chart4[ord(character_list[n-1])-96]             
  b=0
  while b<=n-2:
   print chart5[ord(character_list[b])-96],
   b+=1            
  print chart5[ord(character_list[n-1])-96]              
  c=0
  while c<=n-2:
   print chart6[ord(character_list[c])-96],
   c+=1
  print chart6[ord(character_list[n-1])-96]
else:
 if n==1:
  print chart6[ord(character_list[0])-96]
  print chart5[ord(character_list[0])-96]
  print chart4[ord(character_list[0])-96]
  print chart3[ord(character_list[0])-96]
  print chart2[ord(character_list[0])-96]
  print chart1[ord(character_list[0])-96]
 else:
  x=0
  while x<=n-2:
   print chart6[ord(character_list[x])-96],
   x+=1
  print chart6[ord(character_list[n-1])-96]
  y=0
  while y<=n-2:
   print chart5[ord(character_list[y])-96],
   y+=1           
  print chart5[ord(character_list[n-1])-96]             
  z=0
  while z<=n-2:
   print chart4[ord(character_list[z])-96],
   z+=1           
  print chart4[ord(character_list[n-1])-96]             
  a=0
  while a<=n-2:
   print chart3[ord(character_list[a])-96],
   a+=1           
  print chart3[ord(character_list[n-1])-96]             
  b=0
  while b<=n-2:
   print chart2[ord(character_list[b])-96],
   b+=1            
  print chart2[ord(character_list[n-1])-96]              
  c=0
  while c<=n-2:
   print chart1[ord(character_list[c])-96],
   c+=1
  print chart1[ord(character_list[n-1])-96]

