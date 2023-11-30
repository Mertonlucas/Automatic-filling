from tkinter import Tk, Label, Entry, Button

def preencher_procuracao(dados):
    procuracao_preenchida = f"""
PROCURAÇÃO 

Outorgante:
Nome: {dados['nome_outorgante']} CPF: {dados['cpf_outorgante']}
Tel: {dados['tel_outorgante']} Estado Civil: {dados['estado_civil_outorgante']} Profissão: {dados['profissao_outorgante']}

Outorgante: FRANCISCO BERNARDO SILVA LOPES JUNIOR, brasileiro, solteiro, contador, inscrito na CRC-MA Nº 015310-O, e-mail bernardojuniorctb@gmail.com, com escritório na travessa Saraiva nº 190, Centro, Chapadinha-MA, local indicado para o recebimento das notificações, intimações e outros expedientes judiciais.

Poderes: Para representar o(a) outorgante e defender seus interesses, especialmente perante o Instituto Nacional de Seguro Social - INSS, para tratar de assuntos de seu interesse; gerar senha de acesso ao sistema MEU INSS e requerer benefícios previdenciários e suas revisões; realizar transformações de benefícios; obter vistas de procedimentos administrativos, assim como assinar quaisquer documentos, requerer benefícios, recadastrar, juntar e retirar documentos, fazer declarações e justificações, assinar livros e termos, dar recibos e quitações, endossar cheques recebidos para qualquer banco ou para Caixa Econômica Federal e estadual, descontá-los; praticar, enfim, todos os demais atos que forem necessários ao bom e fiel cumprimento deste mandato e que necessitem de sua presença, outorga ou assinatura.

______________________/{dados['estado']}, {dados['dia']} de {dados['mes']} de {dados['ano']}.

-Bernardo Junior-
"""

    with open("procuracao_preenchida.txt", "w") as file:
        file.write(procuracao_preenchida)

    print("Procuração preenchida e salva com sucesso!")

def obter_dados():
    dados = {
        "nome_outorgante": entrada_nome_outorgante.get(),
        "cpf_outorgante": entrada_cpf_outorgante.get(),
        "tel_outorgante": entrada_tel_outorgante.get(),
        "estado_civil_outorgante": entrada_estado_civil_outorgante.get(),
        "profissao_outorgante": entrada_profissao_outorgante.get(),
        "estado": entrada_estado.get(),
        "dia": entrada_dia.get(),
        "mes": entrada_mes.get(),
        "ano": entrada_ano.get(),
    }

    preencher_procuracao(dados)

# Criar janela principal
janela = Tk()
janela.title("FORMULÁRIO DE PREENCHIMENTO")

# Criar rótulos
rotulo_nome_outorgante = Label(janela, text="Nome Outorgante:")
rotulo_cpf_outorgante = Label(janela, text="CPF Outorgante:")
rotulo_tel_outorgante = Label(janela, text="Tel Outorgante:")
rotulo_estado_civil_outorgante = Label(janela, text="Estado Civil Outorgante:")
rotulo_profissao_outorgante = Label(janela, text="Profissão Outorgante:")
rotulo_estado = Label(janela, text="Estado:")
rotulo_dia = Label(janela, text="Dia:")
rotulo_mes = Label(janela, text="Mês:")
rotulo_ano = Label(janela, text="Ano:")

# Criar entradas
entrada_nome_outorgante = Entry(janela)
entrada_cpf_outorgante = Entry(janela)
entrada_tel_outorgante = Entry(janela)
entrada_estado_civil_outorgante = Entry(janela)
entrada_profissao_outorgante = Entry(janela)
entrada_estado = Entry(janela)
entrada_dia = Entry(janela)
entrada_mes = Entry(janela)
entrada_ano = Entry(janela)

# Botão para obter dados
botao_obter_dados = Button(janela, text="Obter Dados", command=obter_dados)

# Posicionar rótulos e entradas na janela
rotulo_nome_outorgante.grid(row=0, column=0)
entrada_nome_outorgante.grid(row=0, column=1)
rotulo_cpf_outorgante.grid(row=1, column=0)
entrada_cpf_outorgante.grid(row=1, column=1)
rotulo_tel_outorgante.grid(row=2, column=0)
entrada_tel_outorgante.grid(row=2, column=1)
rotulo_estado_civil_outorgante.grid(row=3, column=0)
entrada_estado_civil_outorgante.grid(row=3, column=1)
rotulo_profissao_outorgante.grid(row=4, column=0)
entrada_profissao_outorgante.grid(row=4, column=1)
rotulo_estado.grid(row=5, column=0)
entrada_estado.grid(row=5, column=1)
rotulo_dia.grid(row=6, column=0)
entrada_dia.grid(row=6, column=1)
rotulo_mes.grid(row=7, column=0)
entrada_mes.grid(row=7, column=1)
rotulo_ano.grid(row=8, column=0)
# Posicionar rótulos e entradas na janela (continuação)
entrada_ano.grid(row=8, column=1)

# Posicionar botão na janela
botao_obter_dados.grid(row=9, column=0, columnspan=2)

# Iniciar loop principal
janela.mainloop()