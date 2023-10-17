import csv
import random

def process_text_to_csv(input_text, output_filename):
    # Split the text into sentences
    sentences = [sentence.strip() for sentence in input_text.split('.') if sentence]
    
    # Define function to count nouns, their positions, and identify accusative nouns in a sentence
    def analyze_sentence(sentence):
        words = sentence.split()
        noun_endings = ["o", "oj", "on", "ojn"]
        noun_positions = [i+1 for i, word in enumerate(words) if any(word.endswith(ending) for ending in noun_endings)]
        accusative_nouns = [word for word in words if word.endswith("on") or word.endswith("ojn")]
        return len(noun_positions), noun_positions, len(words), accusative_nouns

    # Analyze sentences
    analyzed_data = [('"' + sentence + '"', *analyze_sentence(sentence)) for sentence in sentences]
    
    # Group by number of nouns and shuffle
    grouped_data = {}
    for data in analyzed_data:
        noun_count = data[1]
        if noun_count not in grouped_data:
            grouped_data[noun_count] = []
        grouped_data[noun_count].append(data)
    
    for noun_count in grouped_data:
        random.shuffle(grouped_data[noun_count])

    # Flatten shuffled data
    shuffled_data = [data for group in grouped_data.values() for data in group]
    
    # Write to CSV with UTF-8 encoding
    with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Sentence", "Number of Nouns", "Positions of Nouns", "Total Words", "Accusative Nouns"])
        for data in shuffled_data:
            noun_positions_str = str(data[2])
            writer.writerow([data[0], data[1], noun_positions_str, data[3], ', '.join(data[4])])



if __name__ == "__main__":
    # Sample text for testing
    sample_text = """
    Mi vidas la hundon.
Ŝi manĝas la pomon.
Li legas la libron.
Ni amas la katojn.
Ili aŭskultas la muzikon.
Mi havas la bildon.
Ŝi kaptas la pilkon.
Li portas la sakon.
Ni ludas kun la infanojn.
Ili rigardas la filmojn.
La suno brilas.
Hundoj estas amikaj.
Ĉielo estas blua.
Ŝi estas bela.
Li estas studento.
Ili estas feliĉaj.
La maro estas profunda.
La herbo estas verda.
Nia domo estas granda.
Ŝia kanto estas belsona.
En la mateno, mi ĉiam trinkas mian kafojn.
Ŝi ŝatas promeni en la parko kun siaj hundojn.
Li ofte vojaĝas al fremdaj landoj pro sia laboron.
Malgraŭ la pluvo, ni decidis viziti la muzeon.
La infanoj ludis en la ĝardeno kun la novajn ludilojn.
Ŝi ĉiam sonĝis pri vojaĝado al tiu eksterlandon.
En la somero, multaj turistoj vizitas nian urbon.
Li skribas artikolon pri la influo de sociaj retojn.
Ni ofte aĉetas legomojn el la loka merkaton.
Ili planas festi sian unuan datrevenon en tiu restoracion.
La vetero estas tre varma en la somero.
Ŝi estas konata pro sia talenta voĉo.
Li estas la plej juna en la familio.
Ni vojaĝos al Francio venontan monaton.
La knabino kun la bluaj okuloj estas mia kuzino.
Ĉiu dimanĉo, ili vizitas sian avinon.
La domo kun la ruĝa tegmento apartenas al ŝi.
La lernejo estas fermita pro la ferioj.
Ŝia plej ŝatata koloro estas verda.
La montoj en tiu regiono estas tre altaj.
Mi aĉetas la panon.
Ŝi trinkas la lakton.
Li portas la ĉapelon.
Ni kolektas la florojn.
Ili kantas la kantojn.
Ŝi desegnas la bildojn.
Li serĉas la ŝlosilon.
Mi legas la gazeton.
Ni plantas la arbojn.
Ili prenas la fotojn.
La birdoj kantas.
La domo estas granda.
La luno brilas.
Li estas profesoro.
Ŝi estas muzikisto.
La steloj brilas.
Vintro estas malvarma.
La auto estas nova.
Printempo venas baldaŭ.
La libro estas interesa.
Post la leciono, mi volas manĝi grandan kukon.
Ŝi veturis tra la tuta lando por vidi tiun monumenton.
Li ofte aĉetas donacojn por siaj nevojn.
Ĉiu vintro, ni vizitas nian familian kabanon.
Malgraŭ sia timo, ŝi saltis de la altponton.
La knabo kun la grandaj okuloj kaptis la flugantan pilkon.
Ni planas organizi feston por niaj geamikojn.
Ŝi skribis longan leteron al sia kuzon.
Ili deziras spekti la novan filmon.
Ni spertos multajn novajn aventurojn dum nia vojaĝon.
La arboj en la arbaro estas tre malnovaj.
Ŝi ŝatas kanti kiam la suno leviĝas.
La knabo kun la ruĝa ĉapelo estas mia frato.
Li ĉiam sonĝas pri vojaĝado ĉirkaŭ la mondo.
La granda hotelo en la centro estas tre fama.
Ili volas studi ĉe la universitato en Parizo.
La ĉielo ĉiam ŝajnas pli blua post la pluvo.
Ŝiaj kantoj inspiras multajn homojn.
La knabino el Brazilo estas tre amika.
La kafejo apud la rivero estas mia preferata loko.
Mi sendis leteron al mia instruisto post la leciono.
Ŝi donis pomon al la knabo ĉe la pordo.
Li prenis libron de la breto kaj komencis legi.
Ni spektis filmojn kun niaj amikoj dum la ferioj.
Ili lernis Esperanton por komuniki kun homoj el aliaj landoj.
Ŝi desegnis bildon dum ŝi aŭskultis muzikon.
Li skribis rakonton kaj sendis ĝin al konkurso.
Ni ludis futbalon en la parko kun niaj kolegoj.
Ŝi trinkis teon kaj legas ĵurnalon en la mateno.
Ili vojaĝis tra multaj landoj kaj kolektis suvenirojn.
Mi preparis vespermanĝon por mia familio en la kuirejo.
Ni kaptis fiŝojn en la lago proksime de nia domo.
Li lernis kantadon kaj ludis gitaron.
Ŝi estis tre feliĉa kaj saltis sur la plaĝon.
Ni vizitis muzeojn kaj vidis pentraĵojn.
Ili aĉetis biletojn por la koncerto en la teatro.
Mi skribis leteron kaj sendis ĝin per poŝto.
Ŝi helpis homojn kaj donis monon.
Li promenis en la arbaro kaj kolektis fruktojn.
Ni kuiris kaj manĝis paston kune en la domo.
Kvankam mi laboris tutan tagon, mi ankoraŭ prenis mian libron kaj legis.
Antaŭ ol ŝi iris al la lernejo, ŝi donis panon al siaj fratoj.
Post kiam ni lernis la bazajn regulojn, ni komencis skribi poemojn.
Kiam li aŭdis la novaĵon, li tuj aĉetis bileton kaj flugis al Parizo.
Ĉar ŝi amas la muzikon, ŝi aŭskultis kantojn kaj lernis gitaron.
Dum ili promenis en la parko, ili vidis birdojn kaj kolektis florojn.
Kiam la suno subiris, ni sidis ĉe la fajro kaj rakontis historiojn.
Antaŭ ol ŝi ekdormis, ŝi skribis taglibron kaj memoris revojn.
Ĉar li ne havis tempon, li sendis leteron anstataŭ viziti sian avinon.
Kvankam ili estis okupitaj, ili trovis tempon kaj ludis kartojn.
Kiam la pluvo komencis, ni kuris kaj serĉis tegmenton.
Ĉar la knabo estis malsata, li manĝis panon kaj trinkis sukon.
Dum la leciono, ŝi skribis notojn kaj aŭskultis la instruiston.
Kvankam la filmo estis longa, ni ĝuis ĝin kaj diskutis scenojn.
Kiam ŝi estis juna, ŝi vizitis lokojn kaj kolektis bildojn.
Antaŭ ol la festo komenciĝis, ili aĉetis manĝaĵojn kaj trinkaĵojn.
Post kiam la suno leviĝis, li meditis kaj ekzercis sur la monton.
Kvankam la vojo estis malfacila, ni marŝis kaj atingis la pinton.
Dum li aŭskultis radion, li lernis novaĵojn kaj aŭdis muzikon.
Kiam la vespero alvenis, ŝi trankviliĝis kaj legis fabelon.
    """
    process_text_to_csv(sample_text, "C:\\Users\\Will\\Documents\\GitHub\\Akuzativludo\\output.csv")
    print("CSV file generated as 'output.csv'")
