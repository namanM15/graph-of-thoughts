import anthropic
from .abstract_language_model import AbstractLanguageModel

class Claude(AbstractLanguageModel):
    def __init__(self, config_path, model_name):
        super().__init__(config_path, model_name)
        # Narrow config to the Claude section
        self.config = self.config[model_name]
        self.client = anthropic.Anthropic(api_key=self.config["api_key"])
        self.model_id = self.config["model_id"]
        self.temperature = self.config.get("temperature", 0.7)
        self.max_tokens = self.config.get("max_tokens", 1024)

    def complete(self, prompt, stop=None):
        response = self.client.messages.create(
            model=self.model_id,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text

    def query(self, query: str, num_responses: int = 1):
        return self.complete(query)

    def get_response_texts(self, query_responses):
        return [query_responses]