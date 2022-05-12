#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import base64

### Leitura, criacao da lista e fechamento do arquivo

arq=open("msg.txt", "r")
lista_linhas=arq.readlines()
arq.close()

### Remover espacos em branco e quebras de linha

regex=(r".*[^\s]")

linhas_limpas=[]

for linha in lista_linhas:
    limpa=re.findall(regex, linha)
    linhas_limpas.append(*limpa)

### Ordenando Lista anterior

linhas_ordenadas=sorted(linhas_limpas, key=int)

### Criando Dicionario Ja ordenado e ja quantificando as repeticoes das suas chaves

dic={}

for linha in linhas_ordenadas:
    if linha in dic:
        dic[linha]=dic[linha]+1
    else:
        dic[linha]=1

### Criando lista com os caracteres decodificados (ASCII)

lista_convertidos=[]

for key, value in dic.items():
    lista_convertidos.append(chr(int(value)))

### Printando String com o codigo Base64 gerado

cod_gerado=(''.join(lista_convertidos))
    
### Usando exercicio do simulado para ja decodificar o base64

codigo_ascii=cod_gerado.encode("ascii")

base64_ascii=base64.b64decode(codigo_ascii)
codigo_traduzido=base64_ascii.decode("ascii")

print()
print(f"Texto convertido: {codigo_traduzido}")
