chart1=['','    ##    ',' #######   ',' #######',' ######  ',' ####### ',' ####### ',' ###### ',' #      #',' ##### ','  ##### ',' #   #  ',' #      ',' #       # ',' ##     # ','   #####   ',' ######  ','  #####   ','  #####   ','  ####  ',' ####### ',' #      # ',' #     #  ',' #       # ',' ##   ## ',' #     # ',' #######']                                                        
chart2=['','  ##  ##  ',' #      #  ','#       ','#      # ',' #       ',' #       ','#       ',' #      #','   #   ','    #   ',' #  #   ',' #      ',' # #   # # ',' # #    # ','  #     #  ',' #     # ',' #     #  ',' #     #  ',' #      ','    #    ',' #      # ',' #     #  ',' #   #   # ','   # #   ','  #   #  ','      # ']                              
chart3=['',' ######## ',' ########  ','#       ','#      # ',' ######  ',' ######  ','#   ### ',' ########','   #   ','    #   ',' ##     ',' #      ',' #  # #  # ',' #  #   # ',' #       # ',' ######  ',' #   # #  ',' ######   ','  ####  ','    #    ',' #      # ','  #   #   ',' #   #   # ','    #    ','   # #   ','    #   ']
chart4=['',' #      # ',' #       # ','#       ','#      # ',' #       ',' #       ','#     # ',' #      #','   #   ','    #   ',' # #    ',' #      ',' #   #   # ',' #   #  # ',' #       # ',' #       ',' #   # #  ',' #    #   ','      # ','    #    ',' #      # ','  #   #   ','  # # # #  ','    #    ','    #    ','   #    ']                                                                                                                                                                                                                                                     
chart5=['',' #      # ',' #       # ','#       ','#     #  ',' #       ',' #       ','#     # ',' #      #','   #   ','#   #   ',' #  #   ',' #      ',' #       # ',' #    # # ','  #     #  ',' #       ',' #    #   ',' #     #  ','      # ','    #    ','  #    #  ','   # #    ','  # # # #  ','   # #   ','    #    ','  #     ']                           
chart6=['',' #      # ',' ########  ',' #######','######   ',' ####### ',' #       ',' ###### ',' #      #',' ##### ',' ###    ',' #   ## ',' ###### ',' #       # ',' #     ## ','   #####   ',' #       ','  #### #  ',' #      # ',' #####  ','    #    ','   ####   ','    #     ','   #   #   ',' ##   ## ','    #    ',' #######']
upsidedown=raw_input('do you want the character upsidedown(y/n)')
character1=raw_input('the first character:')
character2=raw_input('the second character:')
character3=raw_input('the third character:')
character4=raw_input('the forth character:')
if not character1.strip():
  character1_number=96
else:
  character1_number=ord(character1)
if not character2.strip():
  character2_number=96
else:
  character2_number=ord(character2)
if not character3.strip():
  character3_number=96
else:
  character3_number=ord(character3)
if not character4.strip():
  character4_number=96
else:
  character4_number=ord(character4)
if 'n' in upsidedown:
  print chart1[character1_number-96] + chart1[character2_number-96] + chart1[character3_number-96] + chart1[character4_number-96]
  print chart2[character1_number-96] + chart2[character2_number-96] + chart2[character3_number-96] + chart2[character4_number-96]
  print chart3[character1_number-96] + chart3[character2_number-96] + chart3[character3_number-96] + chart3[character4_number-96]
  print chart4[character1_number-96] + chart4[character2_number-96] + chart4[character3_number-96] + chart4[character4_number-96]
  print chart5[character1_number-96] + chart5[character2_number-96] + chart5[character3_number-96] + chart5[character4_number-96]
  print chart6[character1_number-96] + chart6[character2_number-96] + chart6[character3_number-96] + chart6[character4_number-96]
else:
  print chart6[character1_number-96] + chart6[character2_number-96] + chart6[character3_number-96] + chart6[character4_number-96]
  print chart5[character1_number-96] + chart5[character2_number-96] + chart5[character3_number-96] + chart5[character4_number-96]
  print chart4[character1_number-96] + chart4[character2_number-96] + chart4[character3_number-96] + chart4[character4_number-96]
  print chart3[character1_number-96] + chart3[character2_number-96] + chart3[character3_number-96] + chart3[character4_number-96]
  print chart2[character1_number-96] + chart2[character2_number-96] + chart2[character3_number-96] + chart2[character4_number-96]
  print chart1[character1_number-96] + chart1[character2_number-96] + chart1[character3_number-96] + chart1[character4_number-96]
