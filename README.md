# term_split

[日本語版 README](README.ja.md)

A command-line tool to split iTerm2 windows and enable broadcast input to all panes.

## Overview

`term_split` is a macOS CLI tool that splits your current iTerm2 terminal into multiple panes and enables broadcast input, allowing you to type commands that are sent to all panes simultaneously. This is useful for tasks like running the same commands on multiple servers or testing identical operations in parallel.

## Features

- Split iTerm2 window into a specified number of panes
- Automatic directory synchronization across all panes
- Enable broadcast input to all panes in the current tab
- Support for both vertical and horizontal splitting
- Simple command to disable broadcast mode

## Requirements

- macOS
- iTerm2
- Python 3.6 or higher

## Installation

```bash
git clone https://github.com/furuya02/term-split.git
cd term-split
pip install -e .
```

## Usage

```bash
# Split into 10 panes (vertical)
term_split 10

# Split into 5 panes (vertical)
term_split 5

# Split into 10 panes (horizontal)
term_split 10 -H

# Disable broadcast input
term_split --off
```

## Options

| Option | Description |
|--------|-------------|
| `count` | Number of panes to create (2 or more) |
| `-H`, `--horizontal` | Split horizontally (default is vertical) |
| `--off` | Disable broadcast input |

## How it works

1. Run the command with the desired number of panes
2. The current iTerm2 tab is split into the specified number of panes
3. Each pane automatically navigates to the directory where the command was executed
4. Broadcast input is enabled, so all keystrokes are sent to every pane
5. Use `term_split --off` to disable broadcast mode when finished

## Notes

- You may need to grant Automation permissions to iTerm2 in macOS Security & Privacy settings
- Splitting into too many panes will result in very small pane sizes

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
