import GPT_interface
import Microphone
import STT_interface
import subprocess
class Client():
        def __init__(self):
                self.mic = Microphone.Mic()
                self.gpt = GPT_interface.AI_Wrapper()
                self.stt = STT_interface.STT()
        
        def make_colors(self):

                subprocess.run(["rm","-rf","/home/davidlauer/Desktop/developer/STT-Led-color-changer/record.flac"])
                subprocess.run(["rm","-rf","/home/davidlauer/Desktop/developer/STT-Led-color-changer/record.wav"])
                self.mic.record()
                text = self.stt.transcribe_file("record.flac")
                colors = self.gpt.get_color_from_ai(text)
                return colors

