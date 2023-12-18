from gpt4all import GPT4All

# references
# https://docs.gpt4all.io/gpt4all_python.html#chatting-with-gpt4all


class GPT:
    SUPPORTED_MODELS = [
        'mistral-7b-openorca.Q4_0.gguf',  # best overall for open-ended questions
        'mistral-7b-instruct-v0.1.Q4_0.gguf',  # best for instructions
        'gpt4all-falcon-q4_0.gguf',  # fastest responses
        'orca-mini-3b-gguf2-q4_0.gguf'
    ]
    MODEL_PROMPTS = [
        'What do you want to know? \n',
        'What do you need me to do? \n',
        'How can I help you? \n',
        'How can I help you? \n'
    ]

    def __init__(self):
        self.idx = self.choose_model()
        self.model = GPT4All(model_name=self.SUPPORTED_MODELS[self.idx])
        self.system_prompt = ''
        self.prompt_template = ''

    def choose_model(self):
        for i, model in enumerate(self.SUPPORTED_MODELS):
            print(f'{i}: {model}')
        index = int(input('Choose a model: '))
        return index

    def generate(
        self,
        temp=0.7
    ):
        with self.model.chat_session(
            system_prompt=self.system_prompt,
            prompt_template=self.prompt_template
        ):
            text = input(self.MODEL_PROMPTS[self.idx])
            while text is not None and text != 'quit':
                response = self.model.generate(prompt=text, temp=temp)
                print(self.model.current_chat_session[-1]['content'])
                text = input(self.MODEL_PROMPTS[self.idx])


if __name__ == '__main__':
    gpt = GPT()
    gpt.generate()

# ARCHIVE
# works, but sometimes returns empty string
# response = model.generate(prompt=text, temp=0.7)
# time.sleep(2)
# print(response)
# print(response=='')
# print(type(response))
