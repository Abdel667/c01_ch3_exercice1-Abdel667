#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	Puissance_dissipe= (voltage**2)/resistance
	print('La puissance dissipée est de ')
	# TODO: Calculer la puissance dissipée par la résistance.
	return Puissance_dissipe

def orthogonal(v1, v2):
	produit_scalaire = v1[0]*v2[0]+ v1[1]*v2[1]
	print('les vecteurs sont ils orthoghonaux?')
	if (produit_scalaire == 0):
		return True
	else:
		return False
	
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	 # Pour accéder au X
	 # Pour accéder au Y
	 

def average(values):
	
	somme=0# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	for v in values:
		somme += v
	moyenne= somme/len(values)	
	print('la moyenne est')
	return moyenne # La variable v contient une valeur de la liste.

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	if value != 0:
		if value >= 20:
			twenties= value // 20
			value= value - twenties*20
		if value >= 10:
			tens= value // 10
			value= value - tens*10
		if value >= 5:
			fives= value// 5
			value= value - fives*5
		if value >= 1:
			ones= value
	return (twenties, 'twenties', tens, 'tens', fives,'fives', ones, 'ones')

if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
