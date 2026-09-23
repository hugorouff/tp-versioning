from pathlib import Path
from tempfile import TemporaryDirectory

from calcpro import export_resultat, mediane, moyenne_notes
assert moyenne_notes([10, 20]) == 15 
assert moyenne_notes([1.5, 2.5]) == 2.0
assert moyenne_notes([17]) == 17
assert moyenne_notes([]) == 0 
assert moyenne_notes(None) is None
assert mediane([3, 1, 2]) == 2
assert mediane([4, 1, 3, 2]) == 2.5
assert mediane([]) == 0
assert mediane(None) is None
with TemporaryDirectory() as dossier:
	chemin = Path(dossier) / 'resultat.txt'
	assert export_resultat('Moyenne : 15', chemin) == 'Moyenne : 15'
	assert chemin.read_text(encoding='utf-8') == 'Moyenne : 15'
print('tests OK') 