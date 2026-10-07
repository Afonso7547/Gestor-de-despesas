#sistema de gestão de despesas
from datetime import datetime
despesas=[]
apresentacao={"categoria":"Categoria","valor":"Valor","data":"Data","estabelecimento":"Estabelecimento","descricao":"Descrição"}
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
for despesa in despesas:
     for chave in despesa:
        if chave== "valor":
           print(f"{apresentacao[chave]}:{despesa[chave]:.2f}")
        else:
         print(f"{apresentacao[chave]}:{despesa[chave]}")

     print(40*'-')
#calcular o total das despesas
total=0
for despesa in despesas:
    total+=despesa["valor"]
print(f"Total das despesas: $ {total:.2f}")