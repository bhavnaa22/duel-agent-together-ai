import together

# You must have your Together AI API key in an environment variable or config
together.api_key = "YOUR_TOGETHER_API_KEY"

def complete(prompt, stop=None):
    response = together.Complete.create(
        prompt=prompt,
        model="meta-llama/Llama-3-8B-Instruct",
        max_tokens=100,
        temperature=0.7,
        stop=stop or ["\n"]
    )
    return response['output']['choices'][0]['text'].strip()

def simulate_duel(agent1, agent2, turns):
    log = ""
    last_response = f"{agent1}: Hello {agent2}, shall we begin?\n"
    log += last_response
    for i in range(turns):
        speaker = agent2 if i % 2 else agent1
        prompt = log + f"{speaker}:"
        reply = complete(prompt)
        entry = f"{speaker}: {reply}\n"
        log += entry
    return log