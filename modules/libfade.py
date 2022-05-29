from pydub import AudioSegment
from pydub.playback import play

def crossfade(sound1, sound2, fade, output):
    print(f'Attempting`to crossfade {sound1} and {sound2} with a fade of {fade}ms')
    first = AudioSegment.from_wav(sound1)
    second = AudioSegment.from_wav(sound2)
    crossfaded = first.append(second, crossfade=fade)

    play(crossfaded)
    crossfaded.export(output, format="wav")