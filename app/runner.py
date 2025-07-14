from pydantic import BaseModel, ConfigDict

from .data import TextType, TargetStyle
from .reframer import BaseReframer
from .print import Printer

class ReframeRunner(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    to_reframe: BaseReframer
    printer: Printer


    def play(self):
        print("##################################")
        self.printer.print_info(TextType, TargetStyle)
        
        
        self.to_reframe.set_original_text()
        self.to_reframe.set_reframed_text()

        print("##################################")
        self.printer.print_original(self.to_reframe._original_text)
        print('\n')
        self.printer.print_reframed(self.to_reframe._reframed_text)


        

