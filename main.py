#sistema de gestão de despesas
from datetime import datetime
import json
def mostrar_lista(despesas):
   indice=1
   for despesa in despesas:
         print(f"DESPESA NUMERO {indice}:")
         for chave in despesa:
             if chave== "valor":
                   print(f"{apresentacao[chave]}:{despesa[chave]:.2f}")
             else:
                  print(f"{apresentacao[chave]}:{despesa[chave]}")
         indice=indice+1
         print(40*"-")
def calcular_estatisticas(despesas):
   #calcular o total das despesas
  total=0
  for despesa in despesas:
    total+=despesa["valor"]
  print(f"Total das despesas: $ {total:.2f}")

#calcular a média
  if len(despesas)==0:
    print("não há despesas para considerar")
  else:
     media=total/len(despesas)
     print(f"média das despesas:{media:.2f}")
#calcular a maior e menor despesa
  maior=despesas[0]["valor"]
  menor=despesas[0]["valor"]
  for despesa in despesas:
    if despesa["valor"]<menor:
     menor=despesa["valor"]
    if despesa["valor"]> maior:
         maior=despesa["valor"]
  print(f"a maior despesa foi no valor de:{maior:.2f}")
  print(f"a menor despesa foi no valor de:{menor:.2f}")

#categoria mais custosa e menos custosa
  total_despesas={}
  for despesa in despesas:
     if despesa["categoria"] in total_despesas:
          total_despesas[despesa["categoria"]]+=despesa["valor"]
     else:
          total_despesas[despesa["categoria"]]=despesa["valor"]
  maior_categoria=max(total_despesas,key=lambda categoria:total_despesas[categoria])
  menor_categoria=min(total_despesas,key=lambda categoria:total_despesas[categoria])
  print(f"a categoria mais custosa foi:{maior_categoria} com valor de {total_despesas[maior_categoria]}\n"
     f"a categoria menos custosa foi {menor_categoria} com valor de {total_despesas[menor_categoria]}")
   
try:
 with open("despesas.json","r") as ficheiro:
     despesas=json.load(ficheiro)
except FileNotFoundError:
     despesas=[]
except json.JSONDecodeError:
    print("o ficheiro json é invalido")
    raise
apresentacao={"categoria":"Categoria","valor":"Valor","data":"Data","estabelecimento":"Estabelecimento","descricao":"Descrição"}
while(True):
 print(40*'-')
 print(f"escolha uma opcao\n"
          f"1-adicionar despesa\n"
          f"2-consultar lista de despesas\n"
          f"3- consultar estatisticas\n"
          f"4-eliminar uma despesa\n"
          f"5-pesquisar uma categoria\n"
          f"6-alterar uma despesa\n"
          f"0-sair")
 opcao=input("insira a sua opcao:")
 print(40*'-')

    
 if (opcao=="1"):
    repetir="s"
    while(repetir.lower()=="s"):
     despesa={"categoria":None,"valor":None,"data":None,"estabelecimento":None,"descricao":None}
     despesa["categoria"]=input("insira a categoria da despesa:")
     valor_valido=False
     while(valor_valido==False):
        try:
                despesa["valor"]=float(input("insira o valor da despesa:"))
                if despesa["valor"]>0:
                 valor_valido=True
                else:
                     print("insira um valor válido:")
        except:
             print("insira um valor válido:")
     despesa["estabelecimento"]=input("insira o estabelecimento da despesa:")
     despesa["descricao"]=input("insira a descrição da despesa:")
     data=input("insira a data da despesa:")
     data_valida=False
     while(not data_valida):
         try:
              datetime.strptime(data,'%d/%m/%Y')
              data_valida=True
              despesa["data"]=data
         except:
              data=input("insira uma data válida:")   
     despesas.append(despesa)
     repetir=(input("quer adicionar uma nova despesa (s/n)?:"))
     while(repetir.lower()!="s"and repetir.lower()!="n" ):
        repetir=input("insira uma resposta válida(s/n)")
 elif (opcao=="2"):        
     mostrar_lista(despesas)
     print(40*'-')
 elif (opcao=="3"):
    calcular_estatisticas(despesas)

 elif(opcao=="4"):
    mostrar_lista(despesas)
    while(True):
     opcao=input("escolha o numero da dispesa a eliminar:")
     try :
       int(opcao)
       opcao=int(opcao)
       if (opcao-1)>=len(despesas) or (opcao-1)<0:
        print("insira uma opção válida:")
       else:
        break
     except:
        print("insira uma opção válida:")
    
    despesas.pop(opcao-1)
    print("despesa eliminada")
 elif(opcao=="5"):
    categoria=input("insira a categoria que pretende pesquisar:")
    nova_lista=[]
    for despesa in despesas:
       if categoria==despesa["categoria"]:
          nova_lista.append(despesa)
    if (len(nova_lista)==0):
       print("nenhuma categoria corresponde à pesquisa")
    else:
       mostrar_lista(nova_lista)

#ALTERAR DESPESAS
 elif(opcao=="6"):
    mostrar_lista(despesas)
    while(True):
     despesa=input("escolha o numero da despesa que quer alterar(escolha 0 pra retroceder)")
     try :
           opcao=int(despesa)
           if(opcao==0):
                break
           elif (opcao-1)>=len(despesas) or (opcao)<1:
            print("insira uma opção válida:")
           else:
            break
     except:
            print("insira uma opção válida:")
    if (opcao>0):
       while(True):
        campo=input("insira a categoria que quer alterar:")
        if campo in despesas[opcao-1]:
           while(True):
            novo_valor=input("insira o novo valor:")
            if campo=="valor":
              try:
               novo_valor=float(novo_valor)
               despesas[opcao-1][campo]=novo_valor
               break
              except:
                 print("insira um valor válido:")
            elif(campo=="data"):
               try:
                  datetime.strptime(novo_valor, "%d/%m/%Y")
                  despesas[opcao-1][campo]=novo_valor
                  break
               except ValueError:
                  print("Valor da data inválido")
            else:
               despesas[opcao-1][campo]=novo_valor
               break

           break
        else:
           print("insira um valor válido")
         
    
 
 
 elif(opcao=="0"):
#guardar as despesas em um arquivo json
  try:
     with open("despesas.json","w") as ficheiro:
      json.dump(despesas,ficheiro,indent=4)
     break
  except:
   print("erro a gravar")
  
 else:
    print("opçao inválida")