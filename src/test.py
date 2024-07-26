import GPT_interface as GPT
import STT_interface as STT

gpt = GPT.AI_Wrapper()

res = gpt.get_color_from_ai("blue")
assert res == "[blue]"

stt = STT.STT()
assert "hi there this is your text 34s" == stt.transcribe_file("test.mp3")

