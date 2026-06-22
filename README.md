# CATlude

```
 ,_     _              ,-.       _,---._ __  / \
 |\\_,-~/              /  )    .-'       `./ /   \
 / _  _ |    ,--.    (  (   ,'            `/    /|
(  @  @ )   / ,-'    \  `-"             \'\   / |
 \  _T_/-._( (        `.              ,  \ \ /  |
 /         `. \        /`.          ,'-`----Y   |
|         _  \ |      (            ;        |   '
 \ \ ,  /      |      |  ,-.    ,-'         |  /
  || |-_\__   /       |  | (   |        hjw | /
 ((_/`(____,-'        )  |  \  `.___________|/
                       `--'   `--'
     idle                   working
```

**Tiny coding cat agent**, like Claude Code, but with a cat.

Built following the [Build an AI Agent in Python](https://www.boot.dev/courses/build-ai-agents-python) course on [Boot.dev](https://www.boot.dev).

## Usage

```bash
python main.py "your prompt here"
python main.py "your prompt here" --verbose
```

Or, after `uv sync`:

```bash
catlude "your prompt here"
```

## Tools

| Tool | Description |
|---|---|
| `get_files_info` | List files and directories |
| `get_file_content` | Read file contents |
| `run_python_file` | Execute Python files |
| `write_file` | Write or overwrite files |

## Setup

```bash
uv sync
# create a .env file and add your key:
# GEMINI_API_KEY=your_key_here
```

## Project structure

```
CATlude/
├── main.py            # entry point
├── catlude/           # source package
│   ├── agent.py       # agent loop
│   ├── call_function.py
│   ├── cat_art.py     # the cats
│   ├── config.py
│   ├── prompts.py
│   └── functions/     # tool implementations
│       ├── get_file_content.py
│       ├── get_files_info.py
│       ├── run_python_file.py
│       └── write_file.py
├── tests/             # test scripts
└── calculator/        # sandbox working directory
```
