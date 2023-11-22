import os
import openai
import json
import panel as pn

# Replace this placeholder with your actual OpenAI API key
os.environ["OPENAI_API_KEY"] = "Enter your own API key - By Irfan"

# enable below syntax only when u have api as your enviormental
openai.api_key = os.getenv("OPENAI_API_KEY")

# If the environment variable is not set, you can also load it from a configuration file
if not openai.api_key:
    with open("config.json") as f:
        config = json.load(f)
        openai.api_key = config.get("openai_api_key", "")
#you create new file as config.json if that doesnt work for you - By Irfan

# Check if the API key is still not set
if not openai.api_key:
    raise ValueError("OpenAI API key is not set. Please provide a valid API key.")

# Now you can use the openai.api_key in your code

pn.extension()

# Placeholder for the fix_html_with_openai function
def fix_html_with_openai(html_code):
    # You need to implement this function using OpenAI API
    # For now, let's return the input HTML code as is
    return html_code

def on_fix_button_click(event):
    html_code = inp.value
    if html_code.strip():
        fixed_code = fix_html_with_openai(html_code)
        output_text.object = pn.pane.HTML(fixed_code) if fixed_code else "No errors"
    else:
        output_text.object = pn.pane.HTML("Please enter HTML code.")

inp = pn.widgets.TextAreaInput(
    value="",
    placeholder="Enter HTML code here",
    height=400,  # Increase the height of the input box
    sizing_mode="stretch_width"
)
button_conversation = pn.widgets.Button(name="Fix the code (By Irfan)")
button_conversation.on_click(on_fix_button_click)

output_text = pn.Row()

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    output_text
)

dashboard
