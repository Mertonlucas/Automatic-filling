# Utilities/utility_functions.py
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

    with open("Generated Documents/procuracao_preenchida.txt", "w") as file:
        file.write(procuracao_preenchida)

    print("Procuração preenchida e salva com sucesso!")
