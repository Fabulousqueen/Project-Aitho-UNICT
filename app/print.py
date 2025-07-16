from typing import Protocol, runtime_checkable
from pydantic import BaseModel
from .data import OriginalText, ReframedText

@runtime_checkable
class Printer(Protocol):
    def print_info(self, types_text, target_styles):
        pass
    def print_original(self, original_text):
        pass
    def print_reframed(self, reframed_text):
        pass

class VerboseTextPrinter(BaseModel):

    def print_info(self, types_text, target_styles):
        print("## Reframing Process")
        print("This program takes a text (like an email, tweet, or essay) and rewrites it in a different tone or style.")
        print("The system will reframe your text and explain why the transformation makes sense.")
        print("The goal is to explore how changing the style can affect the perception and impact of a message.\n")
       
        print("Available text types:")
        for type_text in types_text:
            print(f"- {type_text}")

        print("\nAvailable target styles:")
        for style in target_styles:
            print(f"- {style}")

        print("\nThe original text and the style will be randomly chosen by the system to demonstrate the reframing capabilities.")
        

    def print_original(self, original_text: OriginalText):
        print("## Original Text")
        print(original_text)

    def print_reframed(self, reframed_text: ReframedText):
        print("## Reframed Text")
        print(reframed_text)
        print("\n## Justification")
        print(reframed_text.justification)

class HumanTextPrinter(BaseModel):
    
    def print_info(self, types_text, target_styles):
        print("## Reframing Process")
        print("This program takes a text (like an email, tweet, or essay) and rewrites it in a different tone or style.")
        print("The system will reframe your text and explain why the transformation makes sense.")
        print("The goal is to explore how changing the style can affect the perception and impact of a message.\n")
       
        print("Available text types:")
        for type_text in types_text:
            print(f"- {type_text}")

        print("\nAvailable target styles:")
        for style in target_styles:
            print(f"- {style}")

        print("\nPlease provide the original text and select a target style when prompted.")
        

    def print_original(self, original_text: OriginalText):
        print("\n##Original Text")
        print(original_text)

    def print_reframed(self, reframed_text: ReframedText):
        print("## Reframed Text")
        print(f"{reframed_text}\n")
        print("\n## Justification")
        print(f"{reframed_text.justification}\n")

