from openai import OpenAI

# Initialize the OpenAI client with Qubrid base URL
client = OpenAI(
    base_url="https://platform.qubrid.com/v1",
    api_key="QUBRID_API_KEY",
)

response = client.chat.completions.create(
    model="Qwen/Qwen3.7-Max",
    messages=[
        {
            "role": "user",
            "content": "Summarize this support ticket into bullet-point next steps for the agent.",
        }
    ],
    max_tokens=500,
    temperature=0.7,
)

print(response.choices[0].message.content)
