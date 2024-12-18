from flask import Flask, request, jsonify
import openai

# Configuração da API da OpenAI
openai.api_key = "SUA_API_KEY"

# Configurar o Flask
app = Flask(__name__)

def jesus_agent(prompt):
    """
    Gera uma resposta baseada no tom e personalidade de Jesus Cristo.
    """
    system_prompt = (
        "Você é Jesus Cristo, respondendo perguntas com sabedoria, amor e ensinamentos baseados na Bíblia."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.7
    )

    return response.choices[0].message.content.strip()

@app.route("/perguntar", methods=["POST"])
def perguntar():
    data = request.get_json()
    pergunta = data.get("pergunta", "")
    if not pergunta:
        return jsonify({"erro": "A pergunta é necessária."}), 400

    resposta = jesus_agent(pergunta)
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(debug=True)
