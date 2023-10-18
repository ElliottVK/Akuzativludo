import csv
import random

def process_text_to_csv(input_text, output_filename):
    # Split the text into sentences and filter out sentences with question marks
    sentences = [sentence.strip() for sentence in input_text.split('.') if sentence and '?' not in sentence]
    
    # Define function to count nouns, their positions, and identify accusative nouns in a sentence
    def analyze_sentence(sentence):
        words = sentence.split()
        noun_endings = ["o", "oj", "on", "ojn"]
        accusative_pronouns = ["lin", "min", "vin", "sin", "nin", "ĉiun", "iun", "tiun", "kiun"]
        
        # Including pronouns that end in "n" as nouns
        noun_positions = [i+1 for i, word in enumerate(words) if any(word.endswith(ending) for ending in noun_endings) or word in accusative_pronouns]
        
        # Identifying accusative nouns
        accusative_nouns = [word for word in words if word.endswith("on") or word.endswith("ojn") or word in accusative_pronouns]
        return len(noun_positions), noun_positions, len(words), accusative_nouns

    # Analyze sentences
    analyzed_data = [('"' + sentence + '"', *analyze_sentence(sentence)) for sentence in sentences]
    
    # Group by number of nouns and shuffle
    grouped_data = {}
    for data in analyzed_data:
        noun_count = data[1]
        if noun_count > 0:
            if noun_count not in grouped_data:
                grouped_data[noun_count] = []  # Initialize the key with an empty list
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
La knabo manĝis panon kun butero.
Ŝi aĉetis libron, plumon, kaj paperon.
La kato kaptis muson en la domo.
En la ĝardeno kreskas floroj, arboj, kaj herboj.
Mia amiko havas hundon, birdon, kaj fiŝon.
La instruisto montris bildon de monto kaj rivero.
En la skatolo estas pilko, ŝnurego, kaj ringo.
La doktoro donis al mi pilolojn, sirupon, kaj konsilojn.
En la muzeo, mi vidis pentraĵon, skulptaĵon, kaj fotografaĵon.
La kuracisto skribis sur paperon kun plumo kaj inko.
La aviadilo flugis super la urbo, rivero, kaj arbaro.
Mi trinkis teon kun sukero kaj lakto.
En la parko ludas infanoj kun pilkoj, ŝnuregoj, kaj ludoj.
La libro estas sur la tablo apud la lampo kaj horloĝo.
En la poŝo, ŝi havas monon, ŝlosilon, kaj spegulon.
Mia patrino kuiris supon kun legomoj, viando, kaj nudeloj.
En la zoologio, mi vidis elefanton, tigron, kaj papagajon.
La filmo montris dezerton, lageton, kaj piramidon.
En la botiko, li aĉetis ĉapelon, ŝuojn, kaj ĉemizon.
La poeto skribis pri la steloj, luno, kaj suno.
En la borsaĵo, ŝi havas poŝtelefono, monujon, kaj okulvitrojn.
La infano kolektis ŝtonojn, konkojn, kaj branĉojn sur la plaĝo.
La restoracio servas fiŝon, viandon, kaj legomojn.
La teamo ludis kun pilko sur la kampo kontraŭ la rivalo.
En la muzikvideo, oni vidas dancantojn, muzikistojn, kaj kantiston.
Sur la ĉielo brilas la suno, nuboj, kaj birdoj.
La reĝo havis kronon, septro, kaj mantelon.
La studento portas sakon kun libroj, kajeroj, kaj kalkulilo.
Ŝi fotis la kaskadon, monton, kaj valon dum sia vojaĝo.
La hotelo ofertas ĉambron kun televido, lito, kaj fenestro.
En la kastelo estas multaj ĉambroj, koridoroj, kaj turegoj.
La arboj donas ombrojn, fruktojn, kaj foliojn.
La artikolo diskutas politikon, ekonomion, kaj kulturon.
En la kafejo, oni povas aĉeti kafo, teo, kaj kuko.
La teatro prezentis dramon kun aktoroj, muziko, kaj dekoracioj.
La fiesta vespero enhavis kantojn, dancadojn, kaj ridojn.
En la haveno, oni vidas ŝipojn, boatojn, kaj maron.
La ĉefurbo havas palacojn, placojn, kaj statuojn.
La laboristo uzis martelon, najlojn, kaj tabulon.
En la aŭto, mi metis mian sakon, mapon, kaj poŝtelefono.
La hundo bojas.
La kato ronronas.
La libro fermiĝas.
La pomo falas.
La pluvo pluvas.
La suno brilas.
La luno lumas.
La birdo kantas.
La fiŝo naĝas.
La monto altas.
La horloĝo tikas.
La floro odoras.
La ĉielo bluas.
La vento blovas.
La stelo scintilas.
La lampo lumigas.
La arbusto kreskas.
La nubo moviĝas.
La ŝipo glitas.
La mono sonas.
La fenestro malfermiĝas.
La pordo fermiĝas.
La bildo pendis.
La arbo ombras.
La muziko sonas.
La ŝtrumpo ŝiriĝas.
La papero flugas.
La pilko saltas.
La inko sekas.
La krajono rompiĝas.
La panjo ridas.
La amiko venas.
La televido montras.
La telefono sonoris.
La letro rulas.
La radio ludas.
La teo varmiĝas.
La neĝo blankas.
La radio bruis.
La kuko dolĉas.
La hundo ĉasas la katon.
La knabo legas la libron.
La instruisto instruas la lernantojn.
La birdo flugas super la arbo.
La patro donas la pilkon al la filo.
La doktoro kuracas la pacienton.
La muzikisto ludas la violinon.
La fiŝo ĉasas la planktonon.
La artisto pentras la pejzaĝon.
La ĉevalo manĝas la herbon.
La ĝardenisto zorgas pri la floroj.
La bakisto faras la panon.
La aviadilo transportas la pasaĝerojn.
La kuiristo preparas la manĝon.
La vendedoro vendas la fruktojn.
La poeto skribas la poemon.
La aktoro rolas en la teatro.
La sportisto ludas la futbalon.
La maristo nagas en la maro.
La fotisto fotas la monton.
La profesoro enketas la historion.
La studento skribas la eseo.
La verkisto publikigas la romano.
La detektivo esploras la misteron.
La infano kolektas la ŝelojn.
La turisto vizitas la muzeon.
La mekaniko riparas la aŭton.
La piloto flugas la helikopteron.
La ĝurnalisto intervjuas la prezidenton.
La muzikisto ludas la gitaron.
La fermisto malsuprenigas la fenestron.
La botisto faras la ŝuojn.
La infano kaj la kuko estas sur la tablo.
La pianisto ludas la klavaron.
La dentisto kontrolas la dentojn.
La luno brilas super la lago.
La astronomo studas la stelojn.
La reĝo regas la landon.
La patrino kisas la infaneton.
La soldato portas la pafilon.
 Mi vidas hundon.
Ŝi aĉetis pomon.
Li manĝas kukon.
Ŝi amas ĉokoladon.
Mi legas libron.
Li kantas kanton.
Ŝi donis floron.
Mi ludas futbalon.
Ŝi trinkas vinon.
Li dormas sur tapiŝon.
Mi portas ĉapelon.
Ŝi rigardas bildon.
Li kuiras supon.
Mi metis la posxtelefonon.
Ŝi desegnas domon.
Li skribas leteron.
Mi forigis eraron.
Ŝi petis helpon.
Li falis sur plankon.
Mi uzas komputilon.
Ŝi pendigis veston.
Li ĵetas pilkon.
Mi prenas paperon.
Ŝi serĉas monujon.
Li vidis birdon.
Mi aŭdas muzikon.
Ŝi provis kukon.
Li tuŝis katon.
Mi mangxas glacion.
Ŝi malfermas pordon.
Li ĉirkaŭprenis amikon.
Mi lavis auto.
Ŝi paŝas sur vojon.
Li batis mian sur tablon.
Mi ĵetas ŝtonon.
Ŝi metis bieron.
Li portas valizon.
Mi aĉetis teon.
Ŝi vokas doktoron.
Li ĉasas leporon.
Mi amas ŝin.
Li vidas min.
Ĉu vi konas ilin?
Ŝi aŭskultas nin.
Mi kredas lin.
Ŝi renkontis nin.
Li komprenas vin.
Ĉu vi vidas ĝin?
Ŝi kisas min.
Mi invitis ilin.
Li timas ĝin.
Vi surprizis nin.
Mi salutis ŝin.
Li manĝis du.
Mi vidis tri el ili.
Vi devas elekti unu.
Ŝi portas ambaŭ.
Ni amas vin.
Li manĝis ok.
Ŝi prenis kvar.
Ĉu vi havas kvin?
Mi vidis ses.
Li manĝis sep.
Mi donis al ŝi dek.
Ni amegas ilin.
Vi ĉiam preferas tiun.
Mi elektis tiun ĉi.
Li serĉas tiun.
Vi bezonas tiujn.
Mi aĉetis tiujn ĉi.
Li volas tiun.
Ni adoras tiujn.
Vi elektos ambaŭ.
Ŝi invitos duonon.
Mi vidis neniun.
Ĉu vi vidos iun?
Li konas ĉiun.
Ni amas ĉiujn.
Ŝi aŭskultis multajn.
Vi aĉetos plurajn."""
    process_text_to_csv(sample_text, "C:\\Users\\Will\\Documents\\GitHub\\Akuzativludo\\output.csv")
    print("CSV file generated as 'output.csv'")
