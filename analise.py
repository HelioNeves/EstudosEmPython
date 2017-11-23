def converteRacaCor(racaCor):
  if racaCor == '1':
    return 'Branca'
  if racaCor == '2':
    return 'Preta'
  if racaCor == '3':
    return 'Amarela'
  if racaCor == '4':
    return 'Parda'
  if racaCor == '5':
    return 'Indigena'

def converteOrigemEncaminhamento(origemEncaminhamento):
  if origemEncaminhamento == '1':
    return 'SUS'
  if origemEncaminhamento == '2':
    return 'Nao SUS'
  if origemEncaminhamento == '3':
    return 'Conta propria'

def converteCustoTratamento(custoTratamento):
  if custoTratamento == '1':
    return 'SUS'
  if custoTratamento == '2':
    return 'Plano de Saude'
  if custoTratamento == '3':
    return 'Particular'

import csv
corOrigem = dict()
corCusto = dict()
with open('RHC-5-anos.XLS.csv') as arquivo:
  for row in csv.DictReader(arquivo):
    if row['RACACOR'] != '9' \
    and row['ORIGENCA'] != '8' and row['ORIGENCA'] != '9'\
    and row['CUSTRATAMTUMOR'] != '8' and row['CUSTRATAMTUMOR'] != '9' and row['CUSTRATAMTUMOR'] != '4':

      #ESTABELECE AS CHAVE NO DICIONÁRIO PARA CADA COR
      if not (converteRacaCor(row['RACACOR']) in corOrigem): 
        corOrigem[converteRacaCor(row['RACACOR'])] = dict()
      if not (converteRacaCor(row['RACACOR']) in corCusto):
        corCusto[converteRacaCor(row['RACACOR'])] = dict()

      #CONTABILIZA A ORIGEM DO ENCAMINHAMENTO PARA CADA COR
      if converteOrigemEncaminhamento(row['ORIGENCA']) in corOrigem[converteRacaCor(row['RACACOR'])]:
        corOrigem[converteRacaCor(row['RACACOR'])][converteOrigemEncaminhamento(row['ORIGENCA'])] += 1
      else:
        corOrigem[converteRacaCor(row['RACACOR'])][converteOrigemEncaminhamento(row['ORIGENCA'])] = 1

      #CONTABILIZA A ORIGEM DO CUSTO DO TRATAMENTO PARA CADA RAÇA
      if converteCustoTratamento(row['CUSTRATAMTUMOR']) in corCusto[converteRacaCor(row['RACACOR'])]:
        corCusto[converteRacaCor(row['RACACOR'])][converteCustoTratamento(row['CUSTRATAMTUMOR'])] += 1
      else:
        corCusto[converteRacaCor(row['RACACOR'])][converteCustoTratamento(row['CUSTRATAMTUMOR'])] = 1

print("Origem Encaminhamento")
print(corOrigem)
print("Custo")
print(corCusto)

import json
open("corOrigem.json", "w").write(json.dumps(corOrigem))
open("corCusto.json", "w").write(json.dumps(corCusto))
