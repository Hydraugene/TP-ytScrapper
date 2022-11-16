import re
import string
import requests
import sys
import json
from bs4 import BeautifulSoup
from dataclasses import dataclass


@dataclass
class video:
    id_video: string
    titre: string
    artiste: string
    pouces: int
    description: string
    liens: []
    comms: []

    def __init__(self):
        self.id_video=""
        self.titre=""
        self.artiste=""
        self.pouces=None
        self.description=""
        self.liens=[]
        self.comms=[]




def read_input_file_name():
    if sys.argv.__len__() >= 3:
        if sys.argv[1] == "--input":
            return sys.argv[2]
    return None


def read_output_file_name():
    if sys.argv.__len__() >= 5:
        if sys.argv[3] == "--output":
            return sys.argv[4]
    return None


def get_input():
    in_file = read_input_file_name()
    if in_file == None:
        return None
    else:
        with open(in_file, 'r') as i:
            return json.load(i)


def get_page(id_video):
    url = "https://www.youtube.com/watch?v="
    page = requests.get(url+id_video)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


def find_titre(soup):
    return soup.find("meta", {"itemprop": "name"})['content']


def find_nom_artiste(soup):
    return soup.find("link", {"itemprop": "name"})['content']


def find_likes(soup):
    # mon_regex = re.compile("/(\b+.)+clics/")
    # mon_regex = re.compile('[0-9]+.clics')
    mon_regex = re.compile(r'clics')
    like_brutes = soup.find_all("script")
    for script in like_brutes:
        print(re.match(mon_regex, str(script)))
    # print(like_brutes)


def find_description(soup):
    return soup.find("meta", {"name": "description"})['content']


def analyse_video(video_id):
    video_en_cours: video
    video_en_cours = video()
    soup = get_page(video_id)
    video_en_cours.id_video = video_id
    video_en_cours.titre = find_titre(soup)
    video_en_cours.artiste = find_nom_artiste(soup)
    # find_likes(soup)
    video_en_cours.description = find_description(soup)

    return video_en_cours


def export_resultats(resultats):
    results = [videos.__dict__ for videos in resultats]
    export_res = json.dumps({"results": results})

    outFile = read_output_file_name()
    if outFile!=None:
        with open(outFile, "w") as write_file:
            write_file.write(export_res)
    else:
        print('ERREUR, Fichier de sortie non valide')


def main():
    resultats = []
    ids_input = get_input()
    if ids_input != None:
        for id_video in get_input()['video_id']:
            resultats.append(analyse_video(id_video))
        export_resultats(resultats)
    else:
        print("ERREUR, Fichier d'entrée non valide")


def run():
    if sys.argv[0] == "scrapper.py":
        print("here we go")
        main()


run()



