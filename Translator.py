# engloding-python/translator.py

import openai

openai.api_key = "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"

def translate_engloding_to_python(engloding_text):
    prompt = f"Translate this into Python code:\n\n'{engloding_text}'\n\nPython code:"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful Python coding assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    code = response['choices'][0]['message']['content']
    return code


# Example usage:
if __name__ == "__main__":
    user_input = input("Engloding phrase: ")
    output_code = translate_engloding_to_python(user_input)
    print("\n--- Translated Python Code ---\n")
    print(output_code)
