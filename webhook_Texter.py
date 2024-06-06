import tkinter as tk
import requests
from tkinter import *

def webhook():
    global webhook_url
    webhook_url = webhook_entry.get()

def send_message():
    message = message_entry.get()
    requests.post(webhook_url, json={"content": message})
    # message_entry.delete(0, tk.END)

def main():
    global message_entry
    global webhook_entry
    window = tk.Tk()
    window.title("Webhook Messenger")
    window.geometry("300x400")

    placeholder_label1 = tk.Label(window, text="")
    placeholder_label1.pack(pady=5)

    webhook_label = tk.Label(window, text="Enter webhook link")
    webhook_label.pack()
    webhook_entry = tk.Entry(window, width=40, borderwidth=3)
    webhook_entry.pack(pady=10)
    send_webhook = tk.Button(window, text="Send webhook", command=webhook)
    send_webhook.pack(pady=10)

    placeholder_label = tk.Label(window, text="")
    placeholder_label.pack(pady=40)

    message_label = tk.Label(window, text="Enter your message")
    message_label.pack()
    message_entry = tk.Entry(window, width=30, borderwidth=3)
    message_entry.pack(pady=10)

    send_button = tk.Button(window, text="Send", command=send_message)
    send_button.pack(pady=10)


    window.mainloop()

if __name__ == "__main__":
    main()