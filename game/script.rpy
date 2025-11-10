# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define bibu = Character("Ibu")
define b1 = Character("Curly")
define b2 = Character("Chunky")
define b3 = Character("Pinky")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show 1 at left
    show 2 at right
    show 3 at right
    show 4 at right

    # These display lines of dialogue.

    bibu " Anak-anakku, sekarang kalian sudah dewasa, kalian harus berkelana sendirian, aku tidak bisa mendampingi kalian lagi."

    b1 "kau selalu menasehati! kami tahu apa yang harus dan tidak boleh dilakukan"

    b2 "iya! sekarang kami bukan anak manja yang harus mendengarkan nasehatmu"

    b3 "baiklah jika begitu, aku punya ide yang akan menolong kita semua"

    # This ends the game.

    return
