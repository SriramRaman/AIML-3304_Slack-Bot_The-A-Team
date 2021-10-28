import slack
import os
from pathlib import Path
clint = slack.WebClient(token='xoxb-2669722669409-2657230944979-LIhM2OeD5swk8BjcYIvxw6UH')
clint.chat_postMessage(channel='#general', text="Welcome to the Bot channel!!!")