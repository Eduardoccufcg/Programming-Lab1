# coding: utf-8
# Aluno: Eduardo Pereira
# Matricula: 117210342
# Atividade: Mais Velhos entre duas pessoas

nome1 = raw_input()
dia1 = int(raw_input())
mes1 = int(raw_input())
ano1 = int(raw_input())
nome2 = raw_input()
dia2 = int(raw_input())
mes2 = int(raw_input())
ano2 = int(raw_input())

if ano1 < ano2:
	print nome1
elif ano2 < ano1:
	print nome2
else:
	if mes1 < mes2:
		print nome1
	elif mes2 < mes1:
		print nome2
	else:
		if dia1 < dia2:
			print nome1
		elif dia2 < dia1:
			print nome2
		else:
			print'nenhuma'
	
