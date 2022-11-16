import sys
from scrapper import *
sys.path.append("../")


def test_titre():
    soup = get_page("iwG36P3_sYo")
    assert find_titre(soup) == "Jujutsu Kaisen: Gojo Satoru Hollow Purple Theme | EPIC VERSION (Besto Quality Remix)"


def test_nom_artiste():
    soup = get_page("iwG36P3_sYo")
    assert find_nom_artiste(soup) == "Samuel Kim Music"


def test_description():
    soup = get_page("iwG36P3_sYo")
    assert find_description(soup) == "Hollow Purple by Arisa Okehazama. Remix by Yours Truly🎧 Stream on Spotify, Apple Music & More! ►https://lnk.to/Gojo♫ Jujutsu Kaisen OST SPOTIFY PLAYLIST ► h..."
