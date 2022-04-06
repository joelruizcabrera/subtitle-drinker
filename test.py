import json

text_file = open('test.txt', 'r')
text = text_file.read()

#cleaning
text = text.lower()
words = text.split()
""" words = [word.strip('.,!?";()[]:%') for word in words]
words = [word.replace("'s", '') for word in words] """

class movieWord:
    def __init__(self, word, count):
        self.word = word
        self.count = count

#finding unique
unique = []
count = []
for word in words:
    word = ''.join([i for i in word if i.isalpha()])
    if word not in unique:
        unique.append(word)
        count.append(movieWord(word, 1))
    else:
        for x in count:
            if x.word == word:
                x.count = x.count + 1

count.sort(key=lambda x: x.count, reverse=True)
newList = sorted(count, key=lambda x: x.count, reverse=True)

blackList = [
    "der",
    "die",
    "das",
    "sie",
    "er",
    "hast",
    "du",
    "uns",
    "dass",
    "wie",
    "mit",
    "auf",
    "an",
    "den",
    "was",
    "zu",
    "und",
    "ihr",
    "ihre",
    "ihren",
    "sein",
    "-->",
    "ich",
    "",
    " ",
    "wir",
    "nicht",
    "...",
    "..",
    "-",
    "#",
    "kannst",
    "oder",
    "nicht",
    "also",
    "ja",
    "gut",
    "diesen",
    "meinem",
    "%",
    "ist",
    "es",
    "ein",
    "von",
    "in",
    "für",
    "einen",
    "eine",
    "aber",
    "dem",
    "so",
    "war",
    "wenn",
    "sind",
    "mir",
    "euch",
    "noch",
    "um",
    "zum",
    "mich",
    "als",
    "einem",
    "ihn",
    "sich",
    "im",
    "mein",
    "dich",
    "dir",
    "habt",
    "hier",
    "bin",
    "des",
    "hat",
    "wo",
    "nur",
    "seid",
    "meine",
    "alle",
    "keine",
    "will",
    "mehr",
    "aus",
    "mann",
    "bist",
    "nach",
    "wird",
    "sehr",
    "kein",
    "kann",
    "auch",
    "haben",
    "wurdet",
    "eher",
    "reizend",
    "tun",
    "paar",
    "sorge",
    "wegen",
    "mieser",
    "bringt",
    "da",
    "tag",
    "nein",
    "diese",
    "jetzt",
    "hab",
    "doch",
    "lasst",
    "bei",
    "nun",
    "müssen",
    "bitte",
    "am",
    "einer",
    "nie",
    "dieser",
    "wäre",
    "muss",
    "dieses",
    "meinen",
    "weiß",
    "schon",
    "mal",
    "man",
    "schreit",
    "ihm",
    "bloß",
    "zur",
    "nichts",
    "gelächter",
    "klar",
    "können",
    "alles",
    "gibt",
    "habe",
    "eure",
    "zwei",
    "etwas",
    "euer",
    "komm",
    "weg",
    "dann",
    "werden",
    "zurück",
    "ho",
    "namen",
    "macht",
    "machen",
    "aye",
    "wahr",
    "seine",
    "los",
    "vor",
    "immer",
    "joho",
    "rasante",
    "guter",
    "ach",
    "jeder",
    "genau",
    "sagte",
    "geht",
    "na",
    "darf",
    "hätte",
    "kommt",
    "tür",
    "war",
    "wer",
    "letzte",
    "weit",
    "denn",
    "wohl",
    "wieder"
]
rank = 1
#print
for i, obj in enumerate(newList):
    if obj.count > 1:
        if obj.word not in blackList:
            if rank <= 15:
                print("{rank: " + str(rank) + ", word: '" + obj.word.title() + "', count: " + str(obj.count) + "},")
                rank+=1

