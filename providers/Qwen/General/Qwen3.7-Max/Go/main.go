package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

func main() {
	url := "https://platform.qubrid.com/v1/chat/completions"

	data := map[string]interface{}{
		"model": "Qwen/Qwen3.7-Max",
		"messages": []map[string]string{
			{
				"role":    "user",
				"content": "Summarize this support ticket into bullet-point next steps for the agent.",
			},
		},
		"temperature": 0.7,
		"max_tokens":  500,
	}
	jsonData, err := json.Marshal(data)
	if err != nil {
		panic(err)
	}

	req, err := http.NewRequest("POST", url, bytes.NewBuffer(jsonData))
	if err != nil {
		panic(err)
	}
	req.Header.Set("Authorization", "Bearer QUBRID_API_KEY")
	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	res, err := client.Do(req)
	if err != nil {
		panic(err)
	}
	defer res.Body.Close()

	body, _ := io.ReadAll(res.Body)
	fmt.Println(string(body))
}
