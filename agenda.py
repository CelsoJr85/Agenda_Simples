import csv

# Nome do arquivo CSV
ARQUIVO_CONTATOS = "contatos.csv"


def carregar_contatos():
    """Carrega os contatos do arquivo CSV."""
    contatos = []
    try:
        with open(ARQUIVO_CONTATOS, mode='r', newline='', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            contatos = list(leitor)
    except FileNotFoundError:
        pass
    return contatos


def salvar_contatos(contatos):
    """Salva os contatos no arquivo CSV."""
    with open(ARQUIVO_CONTATOS, mode='w', newline='', encoding='utf-8') as arquivo:
        campos = ['nome', 'fone']
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(contatos)


def menu():

    print('\n' * 1)
    print("=" * 50)
    print('AGENDA DE CONTATOS'.center(50))
    print("=" * 50)
    print('[1] - Incluir')
    print('[2] - Editar')
    print('[3] - Deletar')
    print('[4] - Localizar por nome')
    print('[5] - Listar contatos')
    print('[6] - Sair')
    print("=" * 50)
    try:
        return int(input('Sua escolha: '))
    except ValueError:
        return 0


def cria_contato():
    """Cria um novo contato."""
    nome = input('Digite o nome: ').strip()
    fone = input('Digite o telefone: ').strip()
    return {'nome': nome, 'fone': fone}


def buscar_indice_por_nome(contatos, nome):
    """Busca o índice de um contato pelo nome."""
    for i, contato in enumerate(contatos):
        if contato['nome'].lower() == nome.lower():
            return i
    return -1


def incluir(contatos):
    """Inclui um novo contato."""
    while True:
        contato = cria_contato()
        if buscar_indice_por_nome(contatos, contato['nome']) != -1:
            print('Contato já existe!')
        else:
            contatos.append(contato)
            salvar_contatos(contatos)
            print('Contato incluído com sucesso!')
        continuar = input('Deseja incluir outro contato? [s/n]: ').strip().lower()
        if continuar != 's':
            break


def editar(contatos):
    """Edita um contato existente."""
    nome = input('Digite o nome do contato a ser editado: ').strip()
    indice = buscar_indice_por_nome(contatos, nome)
    if indice != -1:
        print(f'Contato atual: Nome: {contatos[indice]["nome"]}, Telefone: {contatos[indice]["fone"]}')
        contato = cria_contato()
        contatos[indice] = contato
        salvar_contatos(contatos)
        print('Contato atualizado com sucesso!')
    else:
        print('Contato não encontrado!')


def excluir(contatos):
    """Exclui um contato."""
    nome = input('Digite o nome do contato a ser excluído: ').strip()
    indice = buscar_indice_por_nome(contatos, nome)
    if indice != -1:
        print(f'Removendo contato: Nome: {contatos[indice]["nome"]}, Telefone: {contatos[indice]["fone"]}')
        contatos.pop(indice)
        salvar_contatos(contatos)
        print('Contato excluído com sucesso!')
    else:
        print('Contato não encontrado!')


def buscar_por_nome(contatos):
    """Busca e exibe um contato pelo nome."""
    nome = input('Digite o nome do contato: ').strip()
    indice = buscar_indice_por_nome(contatos, nome)
    if indice != -1:
        print(f'Contato encontrado: Nome: {contatos[indice]["nome"]}, Telefone: {contatos[indice]["fone"]}')
    else:
        print('Contato não encontrado!')


def listar_contatos(contatos):
    """Lista todos os contatos."""
    if not contatos:
        print('Não há contatos cadastrados.')
    else:
        print('Lista de Contatos:')
        print("=" * 50)
        for contato in contatos:
            print(f'Nome: {contato["nome"]} | Telefone: {contato["fone"]}')
        print("=" * 50)


def main():
    contatos = carregar_contatos()
    while True:
        opcao = menu()
        if opcao == 1:
            incluir(contatos)
        elif opcao == 2:
            editar(contatos)
        elif opcao == 3:
            excluir(contatos)
        elif opcao == 4:
            buscar_por_nome(contatos)
        elif opcao == 5:
            listar_contatos(contatos)
        elif opcao == 6:
            print('Obrigado por usar a Agenda!')
            break
        else:
            print('Opção inválida!')


if __name__ == "__main__":
    main()
