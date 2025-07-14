# Project-Aitho-UNICT

This repository contains the implementation of the **Track 2:*"AI agent for creative rewriting and reframing"***, proposed as the final assignment for the *"Intelligent Agents and Machine Learning"* seminar, held by the **Aitho** group at the Department of Mathematics and Computer Science of University of Catania.

For more details about the assignment, the PDF file `slide_esami.pdf` is included in the repository (Italian only).

# HOW TO MAKE IT WORK:

### ollama (Local LLM Server)

This project requires `ollama`, a local LLM (Language Model) server. 
Download `ollama` from the official site:

https://ollama.com/download/windows

Then pull the model needed to run the examples (Gemma3) with:

```sh
ollama pull gemma3:1b
```

### uv (Dependency Manager)

You need to install `uv`. You can find all the information about its installation here: 
https://docs.astral.sh/uv/#installation

### Create Python virtual environment

Clone the repository, access the folder via terminal, then execute:

```sh
uv venv
```

This command creates a `Python virtual environment` in the current directory using `uv`.

### Install the Ollama Python Package

Finally, install the ollama package for Python by running:

```sh
uv pip install ollama
``` 

# EXECUTE THE PROGRAM:

There are two versions of the program:

- `auto_main`: the *program automatically chooses* the text type, its content, and the style in which it should be rewritten. It is executed with the command:

```sh
uv run auto_main
``` 

- `human_main`: the *user manually inputs* the text to be rewritten, specifies its type, and chooses the desired style for reframing. It is executed with the command:

```sh
uv run human_main
```

