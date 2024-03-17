print('\033[1;37;41m{:|^40}\033[m'.format(' LOJAS AMERICANAS '))
valor = float(input('\033[32mDIGITE O VALOR TOTAL DE COMPRAS:\033[m R$ '))
print('''\033[33mNÓS TEMOS AS SEGUINTES OPÇÕES DE PAGAMENTO:\033[m
[1] DINHEIRO
[2] CARTÃO DE CRÉDITO À VISTA
[3] CARTÃO DE CRÉDITO 2x
[4] CARTÃO DE CŔEDITO 3x OU MAIS''')
escolha = int(input('\033[32mDIGITE A OPÇÃO DE PAGAMENTO ESCOLHIDA:\033[m '))
dinheiro = valor - (5*valor/100)
crédito = valor + (5*valor/100)
c2x = valor + (7.5*valor/100)
c3x = valor + (10*valor/100)
cx = valor + (12.5 * valor / 100)
if escolha == 1:
    print('VOCÊ ESCOLHEU A OPÇÃO DINHEIRO.')
    print('VOCÊ IRÁ PAGAR R$ {:.2f}, PAGANDO NO DINHEIRO VOCÊ POSSUI UM DESCONTO DE 5% DO VALOR TOTAL.'.format(dinheiro))
elif escolha == 2:
    print('VOCÊ ESCOLHEU A OPÇÃO CRÉDITO À VISTA.')
    print('VOCÊ IRÁ PAGAR R$ {:.2f}, PAGANDO NO CRÉDITO À VISTA, VOCÊ PAGARÁ O VALOR TOTAL COM UM JUROS DE 5%.'.format(crédito))
elif escolha == 3:
    print('VOCÊ ESCOLHEU A OPÇÃO CRÉDITO EM 2x.')
    print('VOCÊ IRÁ PAGAR R$ {:.2f}, EM 2x DE {:.2f} NO CARTÃO COM UM JUROS DE 7.5%'.format(c2x, c2x/2))
elif escolha == 4:
    print('VOCÊ ESCOLHEU A OPÇÃO CRÉDITO 3x OU MAIS.')
    parcelas = int(input('DIGITE O Nº DE PARCELAS: '))
    if parcelas == 3:
        print('VOCÊ IRÁ PAGAR R${:.2f}, EM 3x DE {:.2f} NO CARTÃO COM UM JUROS DE 10%.'.format(c3x, c3x/3))
    elif parcelas >= 4:
        print('VOCÊ IRÁ PAGAR R${:.2f}, EM {}x DE {:.2f} NO CARTÃO COM UM JUROS DE 12.5%.'.format(cx, parcelas, cx/parcelas))
