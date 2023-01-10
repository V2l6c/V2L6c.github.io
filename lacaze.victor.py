#exercice 1

#"float désigne les nombres à virgules tandis que int désigne les entiers"

#"pour faire une fonction qui prend un nombres x et qui renvoie un nombre entier"
#"on va mettre un return int"
def arrondi_decime(x:float) -> float :
	return int((x*10)+1)/10

assert arrondi_decime(1.23)==1.3

#pour ce qui est d'arrondir on va prendre une inconnue X la multiplier par 1O ce qui va décaler la virgule d'un cran vers la droite, ajouter 1 ce qui signifie qu'on va passer à la décimale supérieur. Puis diviser le tout par 10 pour revenir  au résultat initiale sauf que l'on aura arrondi à la décimale supérieure



#exercie 2

#"le calcul qui permet de déterminer le prix d'un trajet de TER s'écrit de tel sorte A+d(x)*B"

#"comme A et B varie en fonction de d(x) on va faire comme pour le programme qui permet d'afficher un message en fonction de la moyenne"
def prixkm(x:float)->int :
	if x>=1 and x<=16
		return arrondi_decime(0.7781+(x*0.1944))
	elif x>=17 and x<=32 :
		return arrondi_decime(0.2503+(x*0.2165))
	elif x>=33 and x<=64 :
		return arrondi_decime(2.0707+(x*0.1597))

#"pour chaque intervalle on poser une condition grace à des boucles if ou elif"

	elif x>=65 and x<=109 :
		return arrondi_decime(2.8891+(x*0.1489))
	elif x>=110 and x<=149 :
		return arrondi_decime(4.0864+(x*0.1425))
	elif x>=150 and x<=199 :
		return arrondi_decime(8.0871+(x*0.1193))
	elif x>=200 and x<=300 :
		return arrondi_decime(7.7677+(x*0.1209))
	elif x>=301 and x<=499 :
		return arrondi_decime(13.6514+(x*0.1030))
	elif x>=500 and x<=799 :
		return arrondi_decime(18.4449+(x*0.0921))
	elif x>=800 :
		return arrondi_decime(32.2041+(x*0.0755))

#"cela permettra de passer à la boucle suivante jusqu'a ce que x soit compris dans l'intervalle"

assert prixkm(90)==16.3 


#exercie 3

def prixkm1ere(x:float)->int :

#multiplier le prix des billets de seconde classe par 1.5 pour obtenir le prix des billets de 1ere revient a faire 1.5*(A+d*B)

	if x>=1 and x<=16
		return arrondi_decime(1.50*(0.7781+(x*0.1944))

#pour éviter de fausser les calculs on va rajouter des parenthèses

	elif x>=17 and x<=32 :
		return arrondi_decime(1.50*(0.2503+(x*0.2165))
	elif x>=33 and x<=64 :
		return arrondi_decime(1.50*(2.0707+(x*0.1597))
	elif x>=65 and x<=109 :
		return arrondi_decime(1.50*(2.8891+(x*0.1489))
	elif x>=110 and x<=149 :
		return arrondi_decime(1.50*(4.0864+(x*0.1425))
	elif x>=150 and x<=199 :
		return arrondi_decime(1.50*(8.0871+(x*0.1193))
	elif x>=200 and x<=300 :
		return arrondi_decime(1.50*(7.7677+(x*0.1209))
	elif x>=301 and x<=499 :
		return arrondi_decime(1.50*(13.6514+(x*0.1030))
	elif x>=500 and x<=799 :
		return arrondi_decime(1.50*(18.4449+(x*0.0921))
	elif x>=800 :
		return arrondi_decime(1.50*(32.2041+(x*0.0755))

assert prixkm1ere(876)==147.6


#exercice 4

#"comme pour la 1ere classe sauf qu'ici on va multiplier par 2.1 au lieu de 1.5"


def prix_speciale_max(x:float)->int :
	if x>=1 and x<=16
		return arrondi_decime(0.7781+(x*0.1944))
	elif x>=17 and x<=32 :
		return arrondi_decime(0.2503+(x*0.2165))
	elif x>=33 and x<=64 :
		return arrondi_decime(2.0707+(x*0.1597))
	elif x>=65 and x<=109 :
		return arrondi_decime(2.8891+(x*0.1489))
	elif x>=110 and x<=149 :
		return arrondi_decime(4.0864+(x*0.1425))
	elif x>=150 and x<=199 :
		return arrondi_decime(8.0871+(x*0.1193))
	elif x>=200 and x<=300 :
		return arrondi_decime(7.7677+(x*0.1209))
	elif x>=301 and x<=499 :
		return arrondi_decime(13.6514+(x*0.1030))
	elif x>=500 and x<=799 :
		return arrondi_decime(18.4449+(x*0.0921))
	elif x>=800 :
		return arrondi_decime(32.2041+(x*0.0755))

assert prix_speciale_max(777)==189.1

#exercie 5

#comme les distance entre les gares sont en mètre il est nécéssaire de faire plusieur correction pour ne pas fausser le prix qui lui est basé en kilomètre

def prixm(x:float)->int :
	if x>=1000 and x<=16000
		return arrondi_decime(0.7781+(x*0.0001944))

#on va donc multiplier par 1000 les intervalles de distance et diviser par 1000 le prix du kilomètre

#1km=1000m

	elif x>=17000 and x<=32000 :
		return arrondi_decime(0.2503+(x*0.0002165))
	elif x>=33000 and x<=64000 :
		return arrondi_decime(2.0707+(x*0.0001597))
	elif x>=65000 and x<=109000 :
		return arrondi_decime(2.8891+(x*0.0001489))
	elif x>=110000 and x<=149000 :
		return arrondi_decime(4.0864+(x*0.0001425))
	elif x>=150000 and x<=199000 :
		return arrondi_decime(8.0871+(x*0.0001193))
	elif x>=200000 and x<=300000 :
		return arrondi_decime(7.7677+(x*0.0001209))
	elif x>=301000 and x<=499000 :
		return arrondi_decime(13.6514+(x*0.0001030))
	elif x>=500000 and x<=799000 :
		return arrondi_decime(18.4449+(x*0.0000921))
	elif x>=800000 :
		return arrondi_decime(32.2041+(x*0.0000755))

assert prixm(825000)==94.5