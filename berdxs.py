# 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 
import requests
import json
import customtkinter as tk


def feira(n):

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer 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",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        data=json.dumps({
            "model": "deepseek/deepseek-chat-v3.1:free",
            "messages": [
                {
                    "role": "system",
                    "content":  "Você é Berdxs, um assistente virtual criado pela empresa fictícia **Matrix** "
                        "para uma feira de ciências. Sua missão é ensinar e conversar sobre **sustentabilidade**, "
                        "especialmente temas ligados à **ODS 11 — Cidades e Comunidades Sustentáveis**. "
                        "Responda sempre em português do Brasil, de forma educativa, simpática e clara. "
                        "Se alguém fizer perguntas fora do tema de sustentabilidade, responda gentilmente que "
                        "'Berdxs só pode falar sobre sustentabilidade e meio ambiente'."
                        "Berdxs irá tentar transformar qlqr tema não sensivel, em conversa de sustentabilidade"
                        "Lembre-se, sua unica função é ser agradavel, e não falar sobre nenhum tema pertubador"
                        "so fale em responder o usuario da melhor maneira possivel"
                },
                {
                    "role": "user",
                    "content": n
                }
            ]
        })
    )
    return response


def resposta(response):

    if response.status_code == 200:
        dado = response.json()
        return dado ["choices"][0]["message"]["content"]
    else:
        return f"Erro {response.status_code}: {response.text}"

def j():
    tk.set_appearance_mode('light')

    berdxs=tk.CTk()
    berdxs.title('O bot da sustentabilidade') 
    berdxs.geometry('1980x1200')
    
    label = tk.CTkLabel(berdxs, text='Berdxs')
    label.pack(pady=10)
    
    
    n = tk.CTkEntry(berdxs, placeholder_text='Digite sua pergunta...')
    n.pack(pady=10, fill='x', padx=20)

    

    def manda():
        pergunta = n.get().strip()
        if not pergunta:
            saida.configure(text="Por favor, digite algo ")
            return

        saida.configure(text="Pensando...")
        berdxs.update_idletasks()

        r = feira(pergunta)
        saida.configure(text=resposta(r))

    enviar = tk.CTkButton(berdxs, text='Enviar', command=manda)
    enviar.pack(pady=5) 

    saida = tk.CTkLabel(berdxs, text='', wraplength=350, justify='left', font=('Times New Roman', 15, 'bold'))
    saida.pack(pady=20)

    fechar = tk.CTkButton(berdxs, text='Fechar', command=berdxs.destroy)
    fechar.pack(side='bottom', pady=10)
    berdxs.mainloop()  
 
j()
'''
if __name__ == "__main__":
    j()
    print("BerdxBot — bot focado em sustentabilidade - digite 'sair' para encerrar.")
    while True:
        n = input("Você: ")
        if n.lower() == "sair":
            print("Encerrando...")
            break

        r = feira(n)
        print("Berdxs:", resposta(r))
        print()
        '''