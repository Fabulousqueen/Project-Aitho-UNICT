from enum import StrEnum

from pydantic import BaseModel 

class TextType(StrEnum):
    email = "email"
    tweet = "tweet"
    essay = "essay"
    review = "review"
    message = "message"

class TargetStyle(StrEnum):
    ironic = "ironic"
    professional = "professional"
    poetic = "poetic"
    empathetic = "empathetic"
    sarcastic = "sarcastic"
    enthusiastic = "enthusiastic"
    bureaucratic = "bureaucratic"
    direct = "direct"

class Text(BaseModel):
    type_text:TextType
    content: str

    def __str__(self):
        pass

class OriginalText(Text):

    def __str__(self):
        return f"## The original {self.type_text} is:\n{self.content}"
    
class ReframedText(Text):
    target_style:TargetStyle
    justification:str

    def __str__(self):
        return f"## Here is the reframed {self.type_text} in an {self.target_style} style:\n {self.content} "
    
