import customtkinter as ctk
from threading import Thread
from gemini_chatbot import ask_bot

# ---------- APP ----------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

FONT_MAIN = ("JetBrains Mono", 20)

app = ctk.CTk()
app.geometry("700x820")
app.title("Gemini Pro Chat UI")

# ---------- CHAT FRAME ----------
chat_frame = ctk.CTkScrollableFrame(app)
chat_frame.pack(fill="both", expand=True, padx=10, pady=10)

# ---------- STATUS ----------
status = ctk.StringVar(value="Status: Online")
status_label = ctk.CTkLabel(app, textvariable=status, anchor="w", font=FONT_MAIN)
status_label.pack(fill="x", padx=10)

# ---------- INPUT ----------
input_frame = ctk.CTkFrame(app)
input_frame.pack(fill="x", padx=10, pady=10)

entry = ctk.CTkTextbox(input_frame, height=90, font=FONT_MAIN)
entry.pack(side="left", fill="x", expand=True, padx=(0,10))

# ---------- HELPERS ----------

def create_copy_button(parent, text):
    def copy():
        app.clipboard_clear()
        app.clipboard_append(text)

    btn = ctk.CTkButton(parent, text="Copy", width=80, height=34,
                        font=FONT_MAIN, command=copy)
    btn.pack(anchor="e", pady=(4,0))


def create_message(sender, message):

    bubble = ctk.CTkFrame(chat_frame, corner_radius=16)
    bubble.pack(fill="x", pady=8, padx=8, anchor="e" if sender=="You" else "w")

    if sender == "You":
        bubble.configure(fg_color="#14532d")
        text_color = "white"
    else:
        bubble.configure(fg_color="#1e293b")
        text_color = "#22c55e"

    parts = message.split("```")

    for i, part in enumerate(parts):

        # CODE BLOCK
        if i % 2 == 1:
            code_box = ctk.CTkTextbox(
                bubble,
                height=160,
                font=FONT_MAIN
            )
            code_box.insert("1.0", part.strip())
            code_box.configure(state="disabled")
            code_box.pack(fill="x", padx=14, pady=(6,2))

            create_copy_button(bubble, part.strip())

        # NORMAL TEXT
        else:
            if part.strip():
                label = ctk.CTkLabel(
                    bubble,
                    text=part.strip(),
                    justify="left",
                    wraplength=540,
                    font=FONT_MAIN,
                    text_color=text_color
                )
                label.pack(anchor="w", padx=14, pady=10)

    chat_frame._parent_canvas.yview_moveto(1.0)


def bot_thread(user_msg):
    try:
        status.set("Status: Typing...")
        reply = ask_bot(user_msg)

        if not reply:
            reply = "No response."

        app.after(0, lambda: create_message("Bot", reply))
        status.set("Status: Online")

    except:
        app.after(0, lambda: create_message("Bot","Offline / quota limit reached"))
        status.set("Status: Offline")

    entry.configure(state="normal")


def send_message(event=None):

    # Shift+Enter → newline
    if event and (event.state & 0x0001):
        return

    msg = entry.get("1.0","end-1c").strip()
    if not msg:
        return "break"

    create_message("You", msg)
    entry.delete("1.0","end")
    entry.configure(state="disabled")

    Thread(target=bot_thread,args=(msg,),daemon=True).start()

    return "break"

# ---------- SEND BUTTON ----------
send_btn = ctk.CTkButton(input_frame, text="Send", width=100,
                         font=FONT_MAIN, command=send_message)
send_btn.pack(side="right")

entry.bind("<Return>", send_message)

app.mainloop()

