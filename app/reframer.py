from ollama import chat
from abc import ABC, abstractmethod
from pydantic import BaseModel
import random
from .data import OriginalText, ReframedText, TextType, TargetStyle  

class BaseReframer(BaseModel, ABC):
    model: str
    _original_text: OriginalText | None = None
    _reframed_text: ReframedText | None = None
    
    @abstractmethod
    def set_original_text(self):
        pass

    @abstractmethod
    def set_reframed_text(self):
        pass

    def send_request(self, prompt, output_model: type[BaseModel]) -> dict:
    
        messages = [{"role": "user", "content": prompt}]

        while True:
            try:
                response = chat(
                    model = self.model,
                    messages = messages,
                    format = output_model.model_json_schema(),
                    options = {"temperature": 0.8},
                )
                return output_model.model_validate_json(response.message.content)
            except Exception as e:
                print(f"Exception while making a request: {e}, retrying...")


    def reframe_text(self, original_text: OriginalText, target_style: TargetStyle) -> ReframedText:
        prompt = load_prompt(
            "general_system",
            text_type=original_text.type_text,
            target_style=target_style,
            input_text=original_text.content,
        )
        response = self.send_request(prompt, ReframedText)
        return response

        
def load_prompt(prompt: str, **kwargs):
    return open(f"prompts/{prompt}.md", "r").read().format(**kwargs)



class AutoReframer(BaseReframer):

    def set_original_text(self):
        type_text= random.choice(list(TextType))
        content = open(f"inputs/{str(type_text)}.txt", 'r').read() 
        self._original_text = OriginalText(type_text=type_text, content=content)

    def set_reframed_text(self):
        target_style = random.choice(list(TargetStyle))
        self._reframed_text = self.reframe_text(self._original_text, target_style)

class HumanReframer(BaseReframer):

    def _get_input(self, prompt: str) -> str:
        return input(prompt).strip()
    

    def _get_type_text(self) -> TextType:
        while True:
            user_input = self._get_input(
                f"Insert the type of text ({', '.join([t.value for t in TextType])}): "
            )
            try:
                return TextType(user_input)
            except ValueError:
                print("Invalid text type. Try again.\n")
                
    
    def _get_content(self) -> str:
        content = self._get_input("Type your original text: ")
        return content
    
    def _get_target_style(self) -> TargetStyle:
        while True:
            user_input = self._get_input(
                f"Type the wanted reframe style ({', '.join([t.value for t in TargetStyle])}): "
            )
            try:
                return TargetStyle(user_input)
            except ValueError:
                print("Invalid text type. Try again.\n")

    def set_original_text(self, text_type: None = None): 
        text_type = self._get_type_text()
        content = self._get_content()
        self._original_text = OriginalText(type_text = text_type, content = content)     
    
    def set_reframed_text(self):
        target_style = self._get_target_style()
        self._reframed_text = self.reframe_text(self._original_text, target_style)

