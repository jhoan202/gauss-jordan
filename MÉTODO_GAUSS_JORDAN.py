#ORDEN 1(2) 1(3) 2(3) 3(2) 3(1) 2(1)
print("MÉTODO GAUSS JORDAN MATRIZ 3X3")

class matriz_3x3():
	def __init__(self):
		print("BY: JHOAN BARRRERA")
		self.x1=int(input("VALOR PARA LA 'X' EN LA FILA 1: "))
		self.y1=int(input("VALOR PARA LA 'Y' EN LA FILA 1: "))
		self.z1=int(input("VALOR PARA LA 'Z' EN LA FILA 1: "))
		self.resultado1=int(input("VALOR PARA EL RESULTADO EN LA FILA 1: "))

		self.x2=int(input("VALOR PARA LA 'X' EN LA FILA 2: "))
		self.y2=int(input("VALOR PARA LA 'Y' EN LA FILA 2: "))
		self.z2=int(input("VALOR PARA LA 'Z' EN LA FILA 2: "))

		self.resultado2=int(input("VALOR PARA EL RESULTADO EN LA FILA 2: "))

		self.x3=int(input("VALOR PARA LA 'X' EN LA FILA 3: "))
		self.y3=int(input("VALOR PARA LA 'Y' EN LA FILA 3: "))
		self.z3=int(input("VALOR PARA LA 'Z' EN LA FILA 3: "))
		self.resultado3=int(input("VALOR PARA EL RESULTADO EN LA FILA 3: "))
		
		print("==========ORDEN A SEGUIR")
		print("ORDEN 1(2) 1(3) 2(3) 3(2) 3(1) 2(1)")
		print("======================================")
		print("EJERCICIO DE MATRIZ A REALIZAR")
		self.imprimir_matriz_principal_original()
		print()
		print("=======================")	
		print()
		self.primera_fila_con_segunda()
		self.primera_fila_con_tercera()
		print("======================MATRIZ SEGUNDO PASO: PRIMERA FILA MULTIPLICADA CON LA SEGUNDA Y PRIMERA FILA MULTIPLICADA CON LA TERCERA")
		self.nueva_matriz_segundo_paso()
		print("=====================================")
		self.segunda_fila_con_tercera()
		print("========MATRIZ TERCER PASO: SEGUNDA FILA MULTIPLICADA CON LA TERCERA")
		self.nueva_matriz_tercer_paso()
		print("=======================")

		print("======MATRIZ CUARTO PASO: TERCERA FILA MULTIPLICADA CON LA SEGUNDA")
		self.tercera_fila_con_segunda()
		self.nueva_matriz_cuarto_paso()
		print("===============")
		print("============MATRIZ QUINTO PASO: TERCERA FILA MULTIPLICADA CON LA PRIMERA")
		self.tercera_fila_con_prinmera()
		self.nueva_matriz_quinto_paso()
		print("========================")
		print("===MATRIZ RESULTANTE PASO: SEGUNDA FILA MULTIPLICADA CON LA PRIMERA")
		self.segunda_fila_con_primera()
		self.nueva_matriz_sexto_paso()
		print("NO SE TE OLVIDE SIMPLIFICAR")
		print("SALUDOS TE MANDA JHOAN BARRERA")

	

	def imprimir_matriz_principal_original(self):
		print("=======================================")
		print("MATRIZ ORIGINAL")
		print("=======================================")
		print(f"  {self.x1} ", end=" ")
		print(f"  {self.y1} ", end=" ")
		print(f"  {self.z1} ", end=" ")
		print(" | ", end=" ")
		print(f" {self.resultado1} ",end=" ")


		print()

		print(f"  {self.x2} ", end=" ")
		print(f"  {self.y2} ", end=" ")
		print(f"  {self.z2} ", end=" ")
		print(" | ", end=" ")
		print(f" {self.resultado2} ",end=" ")

		print()

		print(f" {self.x3} ", end=" ")
		print(f"  {self.y3} ", end=" ")
		print(f"  {self.z3} ", end=" ")
		print(" | ", end=" ")
		print(f" {self.resultado3} ",end=" ")

	def primera_fila_con_segunda(self):
		multiplicador_fila1=self.x2
		multiplicador_fila2=self.x1*-1

		self.lista_primera_fila_con_segunda=[]

		resultado_fila1_multilicando_arriba_1=multiplicador_fila1*self.x1
		resultado_fila1_multilicando_arriba_2=multiplicador_fila1*self.y1
		resultado_fila1_multilicando_arriba_3=multiplicador_fila1*self.z1
		resultado_fila1_multilicando_arriba_4=multiplicador_fila1*self.resultado1

		resultado_fila2_multilicando_arriba_1=multiplicador_fila2*self.x2
		resultado_fila2_multilicando_arriba_2=multiplicador_fila2*self.y2
		resultado_fila2_multilicando_arriba_3=multiplicador_fila2*self.z2
		resultado_fila2_multilicando_arriba_4=multiplicador_fila2*self.resultado2

		resultado_final_fila1_fila2_1=resultado_fila1_multilicando_arriba_1+resultado_fila2_multilicando_arriba_1
		resultado_final_fila1_fila2_2=resultado_fila1_multilicando_arriba_2+resultado_fila2_multilicando_arriba_2
		resultado_final_fila1_fila2_3=resultado_fila1_multilicando_arriba_3+resultado_fila2_multilicando_arriba_3
		resultado_final_fila1_fila2_4=resultado_fila1_multilicando_arriba_4+resultado_fila2_multilicando_arriba_4

		self.lista_primera_fila_con_segunda.append(resultado_final_fila1_fila2_1)
		self.lista_primera_fila_con_segunda.append(resultado_final_fila1_fila2_2)
		self.lista_primera_fila_con_segunda.append(resultado_final_fila1_fila2_3)
		self.lista_primera_fila_con_segunda.append(resultado_final_fila1_fila2_4)

		return self.lista_primera_fila_con_segunda


	def primera_fila_con_tercera(self):
		multiplicador_fila1=self.x3*-1
		multiplicador_fila3=self.x1

		self.lista_primera_fila_con_tercera=[]

		resultado_fila1_multilicando_arriba_1=multiplicador_fila1*self.x1
		resultado_fila1_multilicando_arriba_2=multiplicador_fila1*self.y1
		resultado_fila1_multilicando_arriba_3=multiplicador_fila1*self.z1
		resultado_fila1_multilicando_arriba_4=multiplicador_fila1*self.resultado1


		resultado_fila3_multilicando_arriba_1=multiplicador_fila3*self.x3
		resultado_fila3_multilicando_arriba_2=multiplicador_fila3*self.y3
		resultado_fila3_multilicando_arriba_3=multiplicador_fila3*self.z3
		resultado_fila3_multilicando_arriba_4=multiplicador_fila3*self.resultado3


		resultado_final_fila1_fila3_1=resultado_fila1_multilicando_arriba_1+resultado_fila3_multilicando_arriba_1
		resultado_final_fila1_fila3_2=resultado_fila1_multilicando_arriba_2+resultado_fila3_multilicando_arriba_2
		resultado_final_fila1_fila3_3=resultado_fila1_multilicando_arriba_3+resultado_fila3_multilicando_arriba_3
		resultado_final_fila1_fila3_4=resultado_fila1_multilicando_arriba_4+resultado_fila3_multilicando_arriba_4

		self.lista_primera_fila_con_tercera.append(resultado_final_fila1_fila3_1)
		self.lista_primera_fila_con_tercera.append(resultado_final_fila1_fila3_2)
		self.lista_primera_fila_con_tercera.append(resultado_final_fila1_fila3_3)
		self.lista_primera_fila_con_tercera.append(resultado_final_fila1_fila3_4)

		return self.lista_primera_fila_con_tercera


	def nueva_matriz_segundo_paso(self):

		self.lista_primera_fila=[]
		self.lista_primera_fila.append(self.x1)
		self.lista_primera_fila.append(self.y1)
		self.lista_primera_fila.append(self.z1)
		self.lista_primera_fila.append(self.resultado1)
		print(self.lista_primera_fila)
		print(self.lista_primera_fila_con_segunda)
		print(self.lista_primera_fila_con_tercera)

	def segunda_fila_con_tercera(self):
		multiplicador_fila2=self.lista_primera_fila_con_tercera[1]*-1
		multiplicador_fila3=self.lista_primera_fila_con_segunda[1]
		self.lista_segunda_fila_con_tercera=[]

		resultado_fila2_multilicando_arriba_1=multiplicador_fila2*self.lista_primera_fila_con_segunda[0]
		resultado_fila2_multilicando_arriba_2=multiplicador_fila2*self.lista_primera_fila_con_segunda[1]
		resultado_fila2_multilicando_arriba_3=multiplicador_fila2*self.lista_primera_fila_con_segunda[2]
		resultado_fila2_multilicando_arriba_4=multiplicador_fila2*self.lista_primera_fila_con_segunda[3]


		resultado_fila3_multilicando_arriba_1=multiplicador_fila3*self.lista_primera_fila_con_tercera[0]
		resultado_fila3_multilicando_arriba_2=multiplicador_fila3*self.lista_primera_fila_con_tercera[1]
		resultado_fila3_multilicando_arriba_3=multiplicador_fila3*self.lista_primera_fila_con_tercera[2]
		resultado_fila3_multilicando_arriba_4=multiplicador_fila3*self.lista_primera_fila_con_tercera[3]


		resultado_final_fila1_fila3_1=resultado_fila2_multilicando_arriba_1+resultado_fila3_multilicando_arriba_1
		resultado_final_fila1_fila3_2=resultado_fila2_multilicando_arriba_2+resultado_fila3_multilicando_arriba_2
		resultado_final_fila1_fila3_3=resultado_fila2_multilicando_arriba_3+resultado_fila3_multilicando_arriba_3
		resultado_final_fila1_fila3_4=resultado_fila2_multilicando_arriba_4+resultado_fila3_multilicando_arriba_4

		self.lista_segunda_fila_con_tercera.append(resultado_final_fila1_fila3_1)
		self.lista_segunda_fila_con_tercera.append(resultado_final_fila1_fila3_2)
		self.lista_segunda_fila_con_tercera.append(resultado_final_fila1_fila3_3)
		self.lista_segunda_fila_con_tercera.append(resultado_final_fila1_fila3_4)

		return self.lista_segunda_fila_con_tercera

	def nueva_matriz_tercer_paso(self):

		print(self.lista_primera_fila)
		print(self.lista_primera_fila_con_segunda)
		print(self.lista_segunda_fila_con_tercera)

	def tercera_fila_con_segunda(self):
		multiplicador_fila2=self.lista_segunda_fila_con_tercera[2]*-1
		multiplicador_fila3=self.lista_primera_fila_con_segunda[2]


		self.lista_tercera_fila_con_segunda=[]

		resultado_fila2_multilicando_arriba_1=multiplicador_fila2*self.lista_primera_fila_con_segunda[0]
		resultado_fila2_multilicando_arriba_2=multiplicador_fila2*self.lista_primera_fila_con_segunda[1]
		resultado_fila2_multilicando_arriba_3=multiplicador_fila2*self.lista_primera_fila_con_segunda[2]
		resultado_fila2_multilicando_arriba_4=multiplicador_fila2*self.lista_primera_fila_con_segunda[3]
	

		resultado_fila3_multilicando_arriba_1=multiplicador_fila3*self.lista_segunda_fila_con_tercera[0]
		resultado_fila3_multilicando_arriba_2=multiplicador_fila3*self.lista_segunda_fila_con_tercera[1]
		resultado_fila3_multilicando_arriba_3=multiplicador_fila3*self.lista_segunda_fila_con_tercera[2]
		resultado_fila3_multilicando_arriba_4=multiplicador_fila3*self.lista_segunda_fila_con_tercera[3]


		resultado_final_fila1_fila3_1=resultado_fila2_multilicando_arriba_1+resultado_fila3_multilicando_arriba_1
		resultado_final_fila1_fila3_2=resultado_fila2_multilicando_arriba_2+resultado_fila3_multilicando_arriba_2
		resultado_final_fila1_fila3_3=resultado_fila2_multilicando_arriba_3+resultado_fila3_multilicando_arriba_3
		resultado_final_fila1_fila3_4=resultado_fila2_multilicando_arriba_4+resultado_fila3_multilicando_arriba_4

		self.lista_tercera_fila_con_segunda.append(resultado_final_fila1_fila3_1)
		self.lista_tercera_fila_con_segunda.append(resultado_final_fila1_fila3_2)
		self.lista_tercera_fila_con_segunda.append(resultado_final_fila1_fila3_3)
		self.lista_tercera_fila_con_segunda.append(resultado_final_fila1_fila3_4)

		return self.lista_tercera_fila_con_segunda

	def nueva_matriz_cuarto_paso(self):
		print(self.lista_primera_fila)
		print(self.lista_tercera_fila_con_segunda)
		print(self.lista_segunda_fila_con_tercera)
		
	def tercera_fila_con_prinmera(self):
		multiplicador_fila1=self.lista_segunda_fila_con_tercera[2]*-1
		multiplicador_fila3=self.lista_primera_fila[2]

		self.lista_tercera_fila_con_primera=[]

		resultado_fila2_multilicando_arriba_1=multiplicador_fila1*self.lista_primera_fila[0]
		resultado_fila2_multilicando_arriba_2=multiplicador_fila1*self.lista_primera_fila[1]
		resultado_fila2_multilicando_arriba_3=multiplicador_fila1*self.lista_primera_fila[2]
		resultado_fila2_multilicando_arriba_4=multiplicador_fila1*self.lista_primera_fila[3]
	

		resultado_fila3_multilicando_arriba_1=multiplicador_fila3*self.lista_segunda_fila_con_tercera[0]
		resultado_fila3_multilicando_arriba_2=multiplicador_fila3*self.lista_segunda_fila_con_tercera[1]
		resultado_fila3_multilicando_arriba_3=multiplicador_fila3*self.lista_segunda_fila_con_tercera[2]
		resultado_fila3_multilicando_arriba_4=multiplicador_fila3*self.lista_segunda_fila_con_tercera[3]
		

		resultado_final_fila1_fila3_1=resultado_fila2_multilicando_arriba_1+resultado_fila3_multilicando_arriba_1
		resultado_final_fila1_fila3_2=resultado_fila2_multilicando_arriba_2+resultado_fila3_multilicando_arriba_2
		resultado_final_fila1_fila3_3=resultado_fila2_multilicando_arriba_3+resultado_fila3_multilicando_arriba_3
		resultado_final_fila1_fila3_4=resultado_fila2_multilicando_arriba_4+resultado_fila3_multilicando_arriba_4

		self.lista_tercera_fila_con_primera.append(resultado_final_fila1_fila3_1)
		self.lista_tercera_fila_con_primera.append(resultado_final_fila1_fila3_2)
		self.lista_tercera_fila_con_primera.append(resultado_final_fila1_fila3_3)
		self.lista_tercera_fila_con_primera.append(resultado_final_fila1_fila3_4)

		return self.lista_tercera_fila_con_primera

	def nueva_matriz_quinto_paso(self):
		print(self.lista_tercera_fila_con_primera)
		print(self.lista_tercera_fila_con_segunda)
		print(self.lista_segunda_fila_con_tercera)

	def segunda_fila_con_primera(self):
		multiplicador_fila1=self.lista_tercera_fila_con_segunda[1]*-1
		multiplicador_fila2=self.lista_tercera_fila_con_primera[1]

		self.lista_segunda_fila_con_primera=[]

		resultado_fila2_multilicando_arriba_1=multiplicador_fila1*self.lista_tercera_fila_con_primera[0]
		resultado_fila2_multilicando_arriba_2=multiplicador_fila1*self.lista_tercera_fila_con_primera[1]
		resultado_fila2_multilicando_arriba_3=multiplicador_fila1*self.lista_tercera_fila_con_primera[2]
		resultado_fila2_multilicando_arriba_4=multiplicador_fila1*self.lista_tercera_fila_con_primera[3]
	

		resultado_fila3_multilicando_arriba_1=multiplicador_fila2*self.lista_tercera_fila_con_segunda[0]
		resultado_fila3_multilicando_arriba_2=multiplicador_fila2*self.lista_tercera_fila_con_segunda[1]
		resultado_fila3_multilicando_arriba_3=multiplicador_fila2*self.lista_tercera_fila_con_segunda[2]
		resultado_fila3_multilicando_arriba_4=multiplicador_fila2*self.lista_tercera_fila_con_segunda[3]
		

		resultado_final_fila1_fila3_1=resultado_fila2_multilicando_arriba_1+resultado_fila3_multilicando_arriba_1
		resultado_final_fila1_fila3_2=resultado_fila2_multilicando_arriba_2+resultado_fila3_multilicando_arriba_2
		resultado_final_fila1_fila3_3=resultado_fila2_multilicando_arriba_3+resultado_fila3_multilicando_arriba_3
		resultado_final_fila1_fila3_4=resultado_fila2_multilicando_arriba_4+resultado_fila3_multilicando_arriba_4

		self.lista_segunda_fila_con_primera.append(resultado_final_fila1_fila3_1)
		self.lista_segunda_fila_con_primera.append(resultado_final_fila1_fila3_2)
		self.lista_segunda_fila_con_primera.append(resultado_final_fila1_fila3_3)
		self.lista_segunda_fila_con_primera.append(resultado_final_fila1_fila3_4)

		return self.lista_segunda_fila_con_primera

	def nueva_matriz_sexto_paso(self):
		print(self.lista_segunda_fila_con_primera)
		print(self.lista_tercera_fila_con_segunda)
		print(self.lista_segunda_fila_con_tercera)

def main():
	App=matriz_3x3()

if __name__ == '__main__':
	main()