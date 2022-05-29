import os
import shutil
from modules import libfade
from modules import libwav

os.chdir(os.path.dirname(os.path.realpath(__file__)))

consonants = [x.split('.')[0] for x in os.listdir("./consonants")]
vowels = [x.split('.')[0] for x in os.listdir("./vowels")]

print(f"Consonants: {consonants}\n\nVowels: {vowels}")

for consonant in consonants:
    conslength = libwav.getlength(f"./consonants/{consonant}.wav")
    for vowel in vowels:
        vowlength = libwav.getlength(f"./vowels/{vowel}.wav")

        fade = min([conslength, vowlength]) / 2

        libfade.crossfade(f"./consonants/{consonant}.wav", f"./vowels/{vowel}.wav", fade, f"./result/{consonant}{vowel}.wav")

for vowel in vowels:
    shutil.copy(f"./vowels/{vowel}.wav", "./result")