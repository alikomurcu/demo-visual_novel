# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Şaban", color = "#354E9F")
define r = Character("Ramazan", color = "35A09F")

# The game starts here.

label start:
    play music "audio/hababam.mp3" fadein 1.0
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene pl robert with zoomin: 
        xsize 1280
        ysize 720

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    # These display lines of dialogue.
    show saban happy at truecenter with fade

    s "Kim olmak istersin ey yolcu..."
    s "Ramazan mı, Kel Mahmut mu (aman duymasın)?"
    menu:
        "Ramazan":
            show saban happy with pixellate:
                xpos 0.75
                ypos 0.4
            s "Ramazan bitti niye ramazanı seçiyorsun yahu?"
            jump the_end
        "Kel Mahmut":
            show saban happy with pixellate:
                xpos 0.75
                ypos 0.4
            jump mahmut

label mahmut:

        s "Demo sürüme hoşgeldiniz Mahmut Hocam!"

        scene pl odtu with Dissolve(0.7):
            xsize 1280
            ysize 720
            
        show saban happy with fade:
            xpos 0.15
            ypos 0.4

#        show saban happy at truecenter with Dissolve(.05) 

        s "Bizler Dünya'yı değiştirebiliriz, değil mi Mahmut Hocam?"
        menu:

            "Kesinlikle!":
                show saban happy with moveinright:
                    xpos 0.75
                    ypos 0.4
                s "Anlat bakalım hocam emekliliğe ne kaldı?"
                menu:
                    "Ne anlatayım be evladım, emekli olsak bile kafamız rahat olmicak.":
                        show saban happy with moveoutright:
                            xpos 0.75
                            ypos 0.4
                        s "Niye hocam bizden mi bıktın yoksa?"
                        menu:
                            "Sizden bıkmadım ama beni yıprattınız be evladım.":
                                jump choice1_yes
                            "Bıktım tabi lan bıkmaz mıyım, illallah dedirttiniz.":
                                jump choice1_no
                    "5 yıl kaldı, merak etme sen mezun olmadan ben emekli olacağım.":
                        jump choice1_no
            "Anca uzaktan değiştirirsiniz.":
                jump choice1_no

label choice1_yes:
    play music "audio/opeyim.mp3"
    queue music "audio/hababam.mp3"
    show saban kissing with pixellate:
        xpos 0.3
        ypos 0.4
    s "Ge seni bi öpiyim Mahmut hocam."
    menu:
        "Gel ben de seni öpeyim.":
            $openFlag = True
            jump saban_if
        "Şaban evladım biraz ders çalışsan keşke.":
            $openFlag = False
            jump saban_if

label choice1_no:
    show saban yanbakan with moveinleft:
        xpos 0.2
        ypos 0.4
    s "Ayıp ettin ulen kel Mahmut."
    jump the_end


label saban_if:
    if not openFlag:
        s "Ayıp ettin ulen kel Mahmut."
        jump the_end
    else:
        s "En büyük Mahmut bizim Mahmut."
        jump the_end
        # This ends the game.
label the_end:
    scene pl robert with zoomout:
        xsize 1280
        ysize 720
    show mahmut at truecenter with pixellate
    s "SON"
return
