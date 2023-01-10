def autoFusion(liste:list[int]) -> list[int]:

debut=O
milieu=len(liste)//2
while debut<milieu and milieu<len(liste): 
	if liste[debut]<liste[milieu]:
		debut=debut+1
	else
		tmp=liste[debut]
		liste[debut]=liste[milieu]
		liste[milieu]=tmp
		debut=debut+1
	if debut==milieu:
		milieu=milieu+1
	return liste


def calcul_occurence(liste:list[int],element:int)->list[int]:

	N=len(liste)
	compteur=0
	for i in range (0,N)
		if liste[i]=element :
			compteur=compteur+1
	return compteur






