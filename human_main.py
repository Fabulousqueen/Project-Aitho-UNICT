from app.reframer import HumanReframer
from app.print import HumanTextPrinter
from app.runner import ReframeRunner

def main():
    
    runner = ReframeRunner(
        to_reframe=HumanReframer(model="gemma3:1b"),
        printer=HumanTextPrinter(),
    )

    runner.play()

main()