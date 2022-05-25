def tabelaVerdade(expr):
    expr_name = expr[0]
    x_y = [
        (True, True),
        (True, False),
        (False, True),
        (False, False),
    ]

    col_1 = 15
    col_2 = 15
    col_3 = 20
    
    print(f"╔{'═'*(col_1)}╦{'═'*(col_2)}╦{'═'*(col_3)}╗")
    print(f"║{'x':^{col_1}}║{'y':^{col_2}}║{'x '+expr_name+' y':^{col_3}}║")
    print(f"╠{'═'*(col_1)}╬{'═'*(col_2)}╬{'═'*(col_3)}╣")
    for x, y in x_y:
        print(f"║{str(x):^{col_1}}║{str(y):^{col_2}}║{str(expr[1](x,y)):^{col_3}}║")
    print(f"╚{'═'*(col_1)}╩{'═'*(col_2)}╩{'═'*(col_3)}╝")

f_and   = ['AND', (lambda x, y:     (x and y))]
f_nand  = ['NAND',(lambda x, y: not (x and y))]
f_or    = ['OR',  (lambda x, y:     (x or y))]
f_nor   = ['NOR', (lambda x, y: not (x or y))]
f_xor   = ['XOR', (lambda x, y:     ((x or y) and ((not x) or (not y))))]
f_xnor  = ['XNOR',(lambda x, y: not ((x or y) and ((not x) or (not y))))]

tabelaVerdade(f_and)
tabelaVerdade(f_nand)
tabelaVerdade(f_or)
tabelaVerdade(f_nor)
tabelaVerdade(f_xor)
tabelaVerdade(f_xnor)