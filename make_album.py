def make_album(artist, title, tracks=''):
    """Return a dictionary of album and artist name"""
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album


rock_album = make_album("Meatloaf", "Bat out of Hell")
rap_album = make_album("Jay-Z", "Blue Album")
pop_album = make_album("Brittney Spears", "Candy")
metal_album = make_album("Metallica", "Black", "12")

print(rock_album)
print(rap_album)
print(pop_album)
print(metal_album)



