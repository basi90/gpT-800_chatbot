import openai

class OpenAIOperations:
    # Initializes the OpenAI GPT-3.5 integration and sets the API key from the specified file path
    def __init__(self, api_key_file_path):
        with open(api_key_file_path, "r") as file:
            self.api_key = file.read().strip()
            openai.api_key = self.api_key
    
    # Communicates with OpenAI GPT-3.5 and generates a response based on the given prompt
    def chat_with_gpt(self, prompt, system_content_file_path):
        with open(system_content_file_path, "r") as file:
            system_content = file.read().strip()
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": prompt}
            ],
            temperature=1,
            max_tokens=550,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        bot_response = response.choices[0].message.content.strip()
        return bot_response
