import sys

functions    = {}
function     = ''
args         = []

def init():
    global functions, function, args

    functions  = {
        '-alt'    : (func_alt,      'Alterar e gravar o mesmo arquivo. Parâmetros: arquivo, [de, para]*N', 1),
        '-altto'  : (func_alt,      'Alterar e gravar no arquivo de saída especificado. Parâmetros: arquivo, arquivosaida, [de, para]*N', 2),
        '-h'      : (func_showhelp, 'Apresentar esta tela de ajuda', 0),
        '--help'  : (func_showhelp, 'Apresentar esta tela de ajuda', 0)
    }

    if len(sys.argv) < 2 or sys.argv[1] not in functions:
        func_showhelp()

    function = sys.argv[1].lower()

    if (len(sys.argv) - 2) < functions[function][2]:
        func_showhelp()

    args = sys.argv[2:]
    
    return

def main():
    global function, functions

    init()
    functions[function][0]()
    return

def func_alt():
    global args, function

    init = 1
    arqent = args[0]
    arqsai = args[0]

    if function == '-altto':
        init = 2
        arqsai = args[1]

    texto = open(args[0], 'r').read()

    i = init

    while i < (len(args) - 1):
        texto = texto.replace(args[i], args[i+1])
        i = i + 2

    fsai = open(arqsai, 'w')
    fsai.write(texto)
    fsai.close()

    print('Arquivo gravado:', arqsai)
    return

def func_showhelp():
    print('Opções e argumentos de utilização:')

    for k, v in functions.items():
        print(k.ljust(12,' '), ':', v[1])
    exit(0)

main()
