import openai

# Configurar sua chave de API
openai.api_key = "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"

def jesus_agent(prompt):
    """
    Função que gera uma resposta baseada no tom e personalidade de Jesus Cristo.
    """
    system_prompt = (
        "Você é Jesus Cristo, respondendo perguntas com sabedoria, amor e ensinamentos baseados na Bíblia."
        " Seja compassivo, sábio e espiritual."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",  # Use "gpt-3.5-turbo" se não tiver acesso ao GPT-4
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7  # Controle de criatividade
    )

    return response['choices'][0]['message']['content']

# Teste básico
if __name__ == "__main__":
    pergunta = input("Faça sua pergunta: ")
    resposta = jesus_agent(pergunta)
    print("Jesus responde:", resposta)
