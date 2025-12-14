# Link Bypass Telegram Bot

This is a Telegram bot that bypasses various link shorteners and file hosting services using external APIs.

## Commands

The bot supports the following commands to bypass links:

*   `/cdn <url>` - Bypass HubCDN links
*   `/eflix <url>` - Bypass ExtraFlix links
*   `/elink <url>` - Bypass ExtraLink links
*   `/gd <url>` - Bypass DriveLeech links
*   `/gdr <url>` - Bypass GdRex links
*   `/ged <url>` - Bypass GdFlix links
*   `/hb <url>` - Bypass HBLinks
*   `/hub <url>` - Bypass HubCloud links
*   `/lux <url>` - Bypass LuxDrive links
*   `/neo <url>` - Bypass Neo links
*   `/nex <url>` - Bypass NexDrive links
*   `/pcdn <url>` - Bypass PixelCDN links
*   `/seed <url>` - Bypass HubDrive links
*   `/vcl <url>` - Bypass VCloud links
*   `/vega <url>` - Bypass Vega links

## Usage

1.  Start the bot with `/start`.
2.  Send a command followed by the URL you want to bypass.
    Example: `/hub https://hubcloud.link/example`

## Deployment

### Prerequisites

*   Python 3.9+
*   Telegram Bot Token

### Installation

1.  Clone the repository.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the bot:
    ```bash
    python bot.py
    ```
