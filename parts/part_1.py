from nicegui import ui

def text_to_hash(input_string):
    h = 0x9E3779B1
    for char in input_string:
        char_code = ord(char)
        h = h ^ char_code
        h = h * 0x517CC1C7
        h = h & 0xFFFFFFFF
    h = h ^ len(input_string)
    return h

def calculate_hash():
    """Calculates and displays the hash of the text in the input field."""
    input_text = text_input.value
    if input_text:
        hash_value = text_to_hash(input_text)
        result_label.set_text(f"Input: {input_text}\nHash: {hash_value}")
    else:
        result_label.set_text("Please enter some text.")

ui.label("Hash Generator").style('font-size: 1.5em; font-weight: bold')
ui.label("Enter text to generate a hash:")

text_input = ui.input(placeholder="Enter text here...").props('dense outlined')

ui.button("Generate Hash", on_click=calculate_hash)

result_label = ui.label("").style('white-space: pre-wrap; margin-top: 1em')

ui.run()
