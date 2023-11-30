# Automatic-filling
 Preenche documentos apenas com Informações específicas


**Mapa mental para criação de software para gerar procurações**

**Pasta raiz**

* **código**
    * **app.py** (código principal do software)
    * **modelos** (modelos de documentos)
    * **utilitários** (funções e classes auxiliares)
* **dados**
    * **procurações** (arquivos PDF das procurações geradas)
* **outros**
    * **licença** (arquivo de licença do software)
    * **readme.md** (arquivo de documentação do software)

**Nomes adequados**

* **app.py** (nome do arquivo principal do software)
* **modelos** (nome da pasta que contém os modelos de documentos)
* **utilitários** (nome da pasta que contém funções e classes auxiliares)
* **procurações** (nome da pasta que contém os arquivos PDF das procurações geradas)
* **licença** (nome do arquivo de licença do software)
* **readme.md** (nome do arquivo de documentação do software)

**Passos para criação do software**

1. **Crie a pasta raiz**

```
mkdir software-para-gerar-procurações
```

2. **Crie as pastas necessárias**

```
mkdir software-para-gerar-procurações/código
mkdir software-para-gerar-procurações/dados
mkdir software-para-gerar-procurações/outros
```

3. **Copie os arquivos necessários**

* **código/app.py**
* **modelos/modelo-de-procuração.txt**
* **readme.md**

4. **Edite o arquivo app.py**

* Importe as bibliotecas necessárias
* Defina o modelo de documento
* Colete as informações do usuário
* Substitua as informações do modelo
* Imprima o documento

5. **Execute o software**

```
python app.py
```

**Exemplo de modelo de procuração**


Eu, [nome do outorgante], [cpf do outorgante], [rg do outorgante], residente e domiciliado na [endereço do outorgante], nomeio e constituo como meu(minha) procurador(a) o(a) senhor(a) [nome do procurador], [cpf do procurador], [rg do procurador], residente e domiciliado na [endereço do procurador], para o fim específico de [poderes].

[data]
[assinatura do outorgante]


**Exemplo de código do arquivo app.py**

```python
import os
import re

def main():
    # Coletar as informações do usuário
    NOME_OUTORGANTE = input("Informe o nome do outorgante: ")
    CPF_OUTORGANTE = input("Informe o CPF do outorgante: ")
    RG_OUTORGANTE = input("Informe o RG do outorgante: ")
    ENDERECO_OUTORGANTE = input("Informe o endereço do outorgante: ")
    NOME_PROCURADOR = input("Informe o nome do procurador: ")
    CPF_PROCURADOR = input("Informe o CPF do procurador: ")
    RG_PROCURADOR = input("Informe o RG do procurador: ")
    ENDERECO_PROCURADOR = input("Informe o endereço do procurador: ")
    PODERES = input("Informe os poderes: ")

    # Substituir as informações do modelo
    MODELO_PROCURACAO = re.sub(r"[nome do outorgante]", NOME_OUTORGANTE, MODELO_PROCURACAO)
    MODELO_PROCURACAO = re.sub(r"[cpf do outorgante]", CPF_OUTORGANTE, MODELO_PROCURACAO)
    ...

    # Imprimir o documento
    print(MODELO_PROCURACAO)

if __name__ == "__main__":
    main()
```

Este mapa mental fornece um plano geral para a criação de um software para gerar procurações. Os nomes adequados para as pastas e arquivos são fornecidos, bem como os passos necessários para a criação do software.