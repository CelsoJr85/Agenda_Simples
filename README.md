# Agenda de Contatos - Backend Simples

Este é um projeto simples de backend para gerenciar uma agenda de contatos, implementado em Python. 
Os contatos são armazenados em um arquivo CSV para garantir a persistência dos dados entre as execuções do programa.

## Funcionalidades

- **Incluir Contato**: Adicione novos contatos com nome e telefone.
- **Editar Contato**: Atualize as informações de um contato existente.
- **Excluir Contato**: Remova contatos da agenda.
- **Buscar por Nome**: Localize contatos pelo nome.
- **Listar Contatos**: Exiba todos os contatos cadastrados.

## Como Funciona

Este projeto atua como um backend simples e utiliza o arquivo `contatos.csv` para armazenar os dados. 
Ele pode ser integrado a uma interface frontend ou usado diretamente no terminal para aprendizado e testes.

## Pré-requisitos

- Python 3.x instalado.
- Biblioteca padrão do Python (não requer instalações adicionais).

## Como Usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/CelsoJr85/Agenda_Simples.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd Agenda_Simples
   ```
3. Execute o programa:
   ```bash
   python agenda.py
   ```

## Exemplo de Uso

Ao executar o programa, você verá o seguinte menu:
```
===================================
AGENDA DE CONTATOS
===================================
[1] - Incluir
[2] - Editar
[3] - Deletar
[4] - Localizar por nome
[5] - Listar contatos
[6] - Sair
===================================
Sua escolha: 
```

Siga as instruções no menu para gerenciar sua agenda de contatos.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias e novas funcionalidades.

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
