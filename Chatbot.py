import nltk
import random
import string  # za uklanjanje interpunkcija
from nltk.chat.util import Chat, reflections

# Pravila za odgovaranje (možeš dodati svoja pravila)
parovi = [
    [r"zdravo|ćao|pozdrav", ["Ćao! Kako mogu pomoći?", "Zdravo! Šta te zanima?", "Pozdrav! Kako si?"]],
    [r"kako si", ["Dobro sam, hvala na pitanju!", "Super, a ti?", "Odlično, hvala!"]],
    [r"(.*) tvoje ime", ["Ja sam chatbot! Kako mogu pomoći?", "Možeš me zvati ChatGPT."]],
    [r"(.*) vreme", ["Nažalost, ne mogu proveriti vreme. Ali ti možeš pogledati na internetu!"]],
    [r"(.*) (hvala|hvala ti)", ["Nema na čemu!", "Uvek sam tu da pomognem!", "Nema problema!"]],
    [r"(.*) (zbogom|ćao|doviđenja)", ["Ćao! Vidimo se sledeći put!", "Pozdrav!", "Doviđenja!"]],
    [r"ko je tvoj tvorac", ["Ja sam kreiran od strane programera poput tebe!", "Razvili su me vešti programeri."]],
    [r"šta možeš da radiš", ["Mogu da pričam sa tobom, odgovaram na pitanja i učim nove stvari!"]],
    [r"reci mi vic", ["Zašto je programer prešao ulicu? Da bi rešio bug na drugoj strani!", "Kako programeri broje? 0, 1, 2, 3..."]],
    [r"šta je Python", ["Python je moćan i popularan programski jezik koji se koristi za mnoge stvari, uključujući i pravljenje mene!"]],
    [r"šta je mašinsko učenje", ["Mašinsko učenje je grana AI koja omogućava računarima da uče iz podataka."]],
    [r"šta je neuralna mreža", ["Neuralne mreže su algoritmi inspirisani ljudskim mozgom."]],
    [r"šta je big data", ["Big Data označava ogromne količine podataka koje AI može analizirati."]],
    [r"kako napraviti mobilnu aplikaciju", ["Koristi Flutter, React Native ili Kotlin za razvoj mobilnih aplikacija."]],
    [r"šta je frontend", ["Frontend je deo aplikacije koji korisnici vide i koriste."]],
    [r"šta je backend", ["Backend je deo aplikacije koji upravlja podacima i logikom."]],
    [r"šta je cloud computing", ["Cloud computing omogućava skladištenje i obradu podataka na internetu."]],
    [r"šta je IoT", ["Internet of Things omogućava povezivanje uređaja na internet."]],
    [r"šta je cyber security", ["Cyber security se bavi zaštitom podataka i sistema od napada."]],
    [r"šta je enkripcija", ["Enkripcija štiti podatke tako što ih kodira."]],
    [r"šta je VPN", ["VPN je alat koji šifrira tvoju internet vezu radi sigurnosti."]],
    [r"šta je SQL", ["SQL je jezik za upravljanje bazama podataka."]],
    [r"šta je API", ["API omogućava različitim aplikacijama da komuniciraju međusobno."]],
    [r"šta je JSON", ["JSON je format za skladištenje i prenos podataka."]],
    [r"šta je Git", ["Git je sistem za verzionisanje koda."]],
    [r"šta je GitHub", ["GitHub je platforma za skladištenje i upravljanje kodom."]],
    [r"šta je Docker", ["Docker omogućava kreiranje kontejnera za aplikacije."]],
    [r"šta je Kubernetes", ["Kubernetes upravlja kontejnerizovanim aplikacijama."]],
    [r"šta je DevOps", ["DevOps spaja razvoj i operacije radi brže isporuke softvera."]],
    [r"šta je Agile", ["Agile je metodologija razvoja softvera bazirana na iterativnom pristupu."]],
    [r"šta je Scrum", ["Scrum je framework za Agile razvoj softvera."]],
    [r"šta je UML", ["UML je jezik za modelovanje softverskih sistema."]],
    [r"šta je VR", ["VR omogućava uranjanje u digitalne svetove."]],
    [r"šta je AR", ["AR dodaje digitalne elemente u stvarni svet."]],
    [r"šta je Metaverse", ["Metaverse je digitalni univerzum u kojem korisnici mogu komunicirati."]],
    [r"šta je robotika", ["Robotika se bavi dizajnom i razvojem robota."]]
]

# Kreiranje chatbota
chatbot = Chat(parovi, reflections)

def pokreni_chat():
    print("Zdravo! Ja sam chatbot. Pitaj me nešto ili napiši 'ćao' za izlaz.")
    while True:
        korisnikov_unos = input(">> ")
        if korisnikov_unos.lower() in ["ćao", "zbogom", "doviđenja"]:
            print("Ćao! Vidimo se sledeći put!")
            break
        odgovor = chatbot.respond(korisnikov_unos)
        print(odgovor)

# Pokretanje chata
if __name__ == "__main__":
    pokreni_chat()
