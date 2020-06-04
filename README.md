# chat-analyzer
This application requires a whatsapp chat as input, with this it will output a chart with messages per hour by users.

How to use:

- Clone the repository.
- Make sure you have **matplotlib** on your machine.
- Go to your WhatsApp, choose a chat, go to settings, more, export chat **without** media, and send it to your email.
- Download the chat into your local machine in a path that fits better for you.
- Run the following command: **python -m chat-analyzer "Path_to_your_WhatsApp_file.txt"** (make sure to add the file extension).

This script basically do five things:

- Remove message content.
- Format the file in a csv way.
- Remove minutes from date and events like: number change, security code changed, etc...
- Store it as csv file.
- Generate the chart using the csv file.