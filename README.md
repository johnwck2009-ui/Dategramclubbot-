# Dategram Club Bot

A simple Telegram community bot for Dategram Club.

## Features

- Latest updates section
- Content section
- About section
- Button-based navigation
- Telegram bot token loaded securely from an environment variable

## Requirements

- Python 3.10+
- A Telegram bot created with BotFather
- `BOT_TOKEN` environment variable

## Run locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Set your bot token as an environment variable named `BOT_TOKEN`, then run:

```bash
python bot.py
```

## Render

Create a Python Web Service on Render using this repository.

Build command:

```bash
pip install -r requirements.txt
```

Start command:

```bash
python bot.py
```

Add this environment variable in Render:

`BOT_TOKEN` = your Telegram bot token

Never commit the real bot token to GitHub.
