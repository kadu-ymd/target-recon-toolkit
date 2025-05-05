# Kit de ferramentas para reconhecimento de alvo

**Desenvolvedor**: Carlos Eduardo Porciuncula Yamada

---

O seguinte projeto possui ferramentas automatizadas para reconhecimento de um alvo a partir de seu endereco IP ou dominio, com o proposito de tornar o processo de escaneamento mais simples e pratico.

As seguintes ferramentas foram implementadas:

1. *DNS Lookup*

2. *Portscan*

3. *WAFW00F*

Para utilizar, e necessario ter os pacotes `nslookup` e `wafw00f` instalados (nativos no **Linux Kali**).

Se esses requisitos estiverem sendo cumpridos, o programa pode ser executado via CLI:

```bash
$ python main.py
```

## 1. DNS Lookup

Nessa ferramenta, as seguintes *flags* foram implementadas:

- `-type` (`ns`, `soa`, `any`, `ptr`)
- `-query` (`mx`)

Alem de outras funcionalidades como usar a ferramenta de forma inversa, utilizando o endereco IP como argumento e tambem utilizando o nameserver como segundo argumento.

## 2. Portscan

Essa ferramenta engloba todas as implementacoes feitas no projeto de [Portscan](https://github.com/kadu-ymd/portscan-python). A documentacao desse projeto engloba todas as implementacoes feitas nesse *toolkit*.

## 3. WAFW00F

Essa ferramenta foi implementada para verificar a existencia ou nao existencia de WAF em um ou mais dominios, de acordo com o padrao dito durante a execucao do CLI.

Todas as ferramentas geram um arquivo `.json` que armazenam o *output* da execucao da respectiva ferramenta.