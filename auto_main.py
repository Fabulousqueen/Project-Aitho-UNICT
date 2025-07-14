from app.reframer import AutoReframer
from app.print import VerboseTextPrinter
from app.runner import ReframeRunner

def main():
    
    runner = ReframeRunner(
        to_reframe=AutoReframer(model="gemma3:1b"),
        printer=VerboseTextPrinter(),
    )

    runner.play()

main()
