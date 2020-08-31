from kivy.core.audio import SoundLoader
from kivy.app import App
sound = SoundLoader.load('recorded.mp3')


def main():

    if sound:
        print("Sound found at %s" % sound.source)
        print("Sound is %.3f seconds" % sound.length)
        sound.play()


if __name__ == "__main__":
    main()
