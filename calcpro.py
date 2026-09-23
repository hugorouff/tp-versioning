def moyenne(notes):
	if not notes:
		return 0
	return sum(notes) / len(notes)


def mediane(notes):
	if not notes:
		return 0

	valeurs = sorted(notes)
	milieu = len(valeurs) // 2
	if len(valeurs) % 2:
		return valeurs[milieu]
	return (valeurs[milieu - 1] + valeurs[milieu]) / 2
