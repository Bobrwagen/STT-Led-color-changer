import openai as AI

class AI_Wrapper:
    def __init__(self,key=None):
        self.key = key
        try:
            if key is None:
                self.client = AI.OpenAI()
            else:
                self.client = AI.OpenAI(key)
        except:
            print("Failed to instantiate OpenAI instance, check your environment variables or the provided key")

    def get_color_from_ai(self,message):
        msg = ""
        try:
            response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages = [{"role":"system","content":"""Your task is to receive text and try to think of colors
         by using the visual apperance of the text or any other logical connections to generate me the result in the form of a python list.
         Here is an example: My text input is Russia, your answer would be: [white,blue,red]. You are restricted to have only the color list as answer and you cannot provide any other
         kind of responses apart from that"""},
         {"role":"user","content":message}]
        )
            msg = response.choices[0].message.content
        except:
            print(response)
        finally:
            return msg
        

wrap = AI_Wrapper()
res = wrap.get_color_from_ai("The ocean while the sun is rising")

print(res)








