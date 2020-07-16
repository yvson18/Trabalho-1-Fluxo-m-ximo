from leitura_dos_arquivos import processamento_dos_dados


def main():

    _N_M_S_T_, _i_j_c_m_ = processamento_dos_dados('problema4.txt')
    
    i_do_arco_m = [origem[0] for origem in _i_j_c_m_]
    j_do_arco_m = [fim[1] for fim in _i_j_c_m_]
    c_m_do_arco = [fluxos[2] for fluxos in _i_j_c_m_]

    print(i_do_arco_m)
    print(j_do_arco_m)
    print(c_m_do_arco)
    print(_N_M_S_T_)

    

        
    
if __name__ == "__main__":
    main()