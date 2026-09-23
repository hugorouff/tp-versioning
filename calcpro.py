def moyenne_notes(notes):
    if notes is None:
        raise ValueError('notes ne peut pas etre None')
    if not notes:
        return 0
    return sum(notes) / len(notes)
