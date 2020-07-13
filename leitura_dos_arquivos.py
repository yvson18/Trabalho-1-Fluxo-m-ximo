import re

def processamento_dos_dados(path_file):

    with open(path_file,'r') as manipulador:
        lista_de_dados = manipulador.readlines()

    _N_M_S_T_string = lista_de_dados[:4]

    _i_j_c_m_string = lista_de_dados[4:]

    _N_M_S_T_ = []
    
    for _N_M_S_T_indice  in _N_M_S_T_string:
        _N_M_S_T_.append(int(re.sub(r'\n','',_N_M_S_T_indice)))
    
    _i_j_c_m_ = []

    for indice_i_j_c_m_ in _i_j_c_m_string:
        _i_j_c_m_.append([int(s) for s in indice_i_j_c_m_.split() if s.isdigit()])
    
    return (_N_M_S_T_ , _i_j_c_m_)

def main():
    _N_M_S_T_ ,_i_j_c_m_ =   processamento_dos_dados('problema.txt')

    print(_N_M_S_T_)
    print(_i_j_c_m_)

if __name__ == "__main__":
    main()