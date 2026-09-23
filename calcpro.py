def moyenne_notes(notes):
	if notes is None:
		return None
	if not notes:
		return 0
	if len(notes) == 1:
		return notes[0]
	return sum(notes) / len(notes)


def mediane(notes):
	if notes is None:
		return None
	if not notes:
		return 0

	valeurs = sorted(notes)
	milieu = len(valeurs) // 2
	if len(valeurs) % 2:
		return valeurs[milieu]
	return (valeurs[milieu - 1] + valeurs[milieu]) / 2


def export_resultat(resultat, chemin):
	texte = str(resultat)
	with open(chemin, "w", encoding="utf-8") as fichier:
		fichier.write(texte)
	return texte

def nouvelle_api_v3(): pass