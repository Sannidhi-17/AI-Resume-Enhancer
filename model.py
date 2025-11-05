from ollama import Client

class LLMModel:
    def __init__(self, model_name="gemma3:4b"):
        self.model_name = model_name
        self.client = Client()

    def generate(self, prompt: str) -> str:
        try:
            response = self.client.generate(
                model=self.model_name,
                prompt=prompt
            )
            # ✅ Ensure plain text output
            if isinstance(response, dict) and "response" in response:
                return response["response"].strip()
            elif isinstance(response, dict) and "message" in response:
                return response["message"].get("content", "").strip()
            elif isinstance(response, str):
                return response.strip()
            else:
                return str(response).strip()
        except Exception as e:
            print("Error generating text:", e)
            return "Error generating response."
