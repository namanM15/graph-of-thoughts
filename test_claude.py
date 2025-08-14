from graph_of_thoughts.language_models import Claude

# Update your actual Claude API key here
claude_config_path = "config.json"
model_name = "claude-3.5-sonnet"

# Init Claude
lm = Claude(config_path=claude_config_path, model_name=model_name)

# Define a simple prompt
prompt = "What is the derivative of sin(x)? Explain step by step."

# Call Claude
response = lm.complete(prompt)
print("\nClaude's Response:\n")
print(response)