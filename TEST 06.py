print('TESTE DE GEOGRAFIA 101')

estado={
'Acre': 'Rio Branco',
'Alagoas': 'Maceió',
'Amapá': 'Macapá',
'Amazonas': 'Manaus',
'Bahia': 'Salvador',
'Ceará': 'Fortaleza',
'Distrito Federal': 'Brasília',
'Espírito Santo': 'Vitória',
'Goiás': 'Goiânia',
'Maranhão': 'São Luís',
'Mato Grosso': 'Cuiabá',
'Mato Grosso do Sul': 'Campo Grande',
'Minas Gerais': 'Belo Horizonte',
'Pará': 'Belém',
'Paraíba': 'João Pessoa',
'Paraná': 'Curitiba',
'Pernambuco': 'Recife',
'Piauí': 'Teresina',
'Rio de Janeiro': 'Rio de Janeiro',
'Rio Grande do Norte': 'Natal',
'Rio Grande do Sul': 'Porto Alegre',
'Rondônia': 'Porto Velho',
'Roraima': 'Boa Vista',
'Santa Catarina': 'Florianópolis',
'São Paulo': 'São Paulo',
'Sergipe': 'Aracaju',
'Tocantins': 'Palmas'
}
acertos = 0
rodadas = 0

for estado, capital in estado.items():
    print(f'Qual a capital do estado {estado}?')
    rodadas += 1
    resposta = input('Resposta: ')
    if resposta.lower() == capital.lower():
        print('Resposta correta!')
        acertos += 1
    else:
        print(f'Resposta errada! A capital do estado {estado} é {capital}')
    while True:
        opcao = input('Deseja continuar? (S/N) ').lower()
        if opcao == 's':
            break
        elif opcao == 'n':
            porcentagem = (acertos / rodadas) * 100
            print(f'Fim do teste! Você acertou {acertos} de {rodadas} questões. Porcentagem de acertos: {porcentagem:.2f}%')
            exit()
        else:
            print('Opção inválida! Digite S ou N.')            
