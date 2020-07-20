from __future__ import print_function
from leitura_dos_arquivos import processamento_dos_dados
from ortools.linear_solver import pywraplp

def Trabalho1_main():

    solver = pywraplp.Solver('Trabalho1_main', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING) #Definindo o solver como variável

    _N_M_S_T_, _i_j_c_m_ = processamento_dos_dados('problema.txt') #Lendo o arquivo desejado (.txt)
    
    i_do_arco_m = [origem[0] for origem in _i_j_c_m_] #Array i
    j_do_arco_m = [fim[1] for fim in _i_j_c_m_] #Array j
    c_m_do_arco = [fluxos[2] for fluxos in _i_j_c_m_] #Array custo


    numero_de_nos = _N_M_S_T_[0]
    numero_de_arcos = _N_M_S_T_[1]

    varSolver = [] #Array dos arcos como variáveis
    restricoes = [] #Array das constraints

    
    #Criando as variáveis de cada arco para o solver
    cont = 0
    while(cont < numero_de_arcos):
        varSolver.append(solver.NumVar(0, c_m_do_arco[cont], str(cont+1)))
        cont+=1

    #Criação do arco que liga o nó escoadouro até o nó de entrada
    varSolver.append(solver.NumVar(0, solver.infinity(), 'X'))
    
    #Definindo as restrições
    cont = 2
    cont_aux = 0
    while(cont <= numero_de_nos):
        cont_aux = 0
        constraint = solver.Constraint(0, 0)
        while(cont_aux < len(i_do_arco_m)):
            if(cont == i_do_arco_m[cont_aux]):
                constraint.SetCoefficient(varSolver[cont_aux], 1)
            cont_aux+=1
        cont_aux=0
        while(cont_aux < len(j_do_arco_m)):
            if(cont == j_do_arco_m[cont_aux]):
                constraint.SetCoefficient(varSolver[cont_aux], -1)
            cont_aux+=1
        cont_aux=0
        if(cont==numero_de_nos):
            constraint.SetCoefficient(varSolver[len(varSolver)-1], 1)
            restricoes.append(constraint)
            cont+=1
        else:
            cont+=1
            restricoes.append(constraint)
            del constraint   

    #Definindo a função objetivo
    objective = solver.Objective()
    objective.SetCoefficient(varSolver[len(varSolver)-1], -1) #Definindo Z = -X
    objective.SetMinimization() #Definindo min Z

    solver.Solve() #Acionando o solver
    opt_solution = varSolver[len(varSolver)-1].solution_value() #Solução ótima
    print('Número de arcos =', solver.NumVariables())
    print('Número de restrições =', solver.NumConstraints())
    print('Solução (Arcos enumerados):')
    cont=0
    while(cont < len(varSolver)):
        if(varSolver[cont].solution_value()!=0):
            print(varSolver[cont].name(), ' : ', varSolver[cont].solution_value(), '/', varSolver[cont].ub())
        cont+=1
    print('Valor objetivo ótimo =', opt_solution)
        
Trabalho1_main()

