import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://platform.qubrid.com/v1",
  apiKey: "QUBRID_API_KEY",
});

const response = await client.chat.completions.create({
  model: "Qwen/Qwen3.7-Max",
  messages: [
    {
      role: "user",
      content:
        "Summarize this support ticket into bullet-point next steps for the agent.",
    },
  ],
  max_tokens: 500,
  temperature: 0.7,
});

console.log(response.choices[0].message.content);
