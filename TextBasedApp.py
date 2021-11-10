import time
import os

while True:

    os.system("cls")
    print("Je word wakkergemaakt door een harde knal,")
    print("je kat heeft vast weer iets om ge gooit.")
    print("Je trekt je kleren aan een gaat kijken,\n")
    time.sleep(5)
    os.system("cls")
    print("Als je de kamer in loopt kan je niks vinden dat is omgevallen.")
    print("Je ziet ook dat je kat erg is geschrokken.\n")
    time.sleep(5)
    os.system("cls")
    print("Je gaat even op onderzoek uit om te kijken wat er is om gegooit.\n")
    time.sleep(4)
    os.system("cls")
    print("Je kijkt ook even bij je kinderen of die iets hebben omgegooid,")
    print("Ze liggen allebei nog te slapen.\n")
    time.sleep(5)
    os.system("cls")
    print("Als je even op onderzoek ben geef je op en denk je dat het in je slaap was,\n")
    time.sleep(3)
    os.system("cls")
    print("Als je net weer in bed ligt hoor je nog een knal,")
    print("Deze keer wordt ook je vrouw wakker.\n")
    time.sleep(5)
    os.system("cls")
    print("Je gaat weer uit je bed om te kijken wat er is gebeurd als je een berichtje krijgt op je telefoon,")
    print("Er vind zich een bom aanval plaats in het dorp naast je.\n")
    time.sleep(5)
    os.system("cls")
    print("Je maakt je vrouw en kinderen wakker.")
    time.sleep(3)
    os.system("cls")

    print ("Jullie mooeten vluchten, wat gaan jullie doen?\n\n")
    d1 = input ("Gaan jullie: \nA Spullen, eten en drinken verzamelen, daarna weg\nB Eten en drinken pakken, en dan weg \nC Niks pakken en zo snel mogelijk weg \nHier typen: " )
    if d1 == "A" or d1 == "a":
        os.system("cls")
        print ("Je hebt kleren, geld, telefoon en eten en drinken kunnen mee nemen,\nHet eten zal je ongeveer drie dagen doen met ze vieren.\nJe moet nu bedenken waar je heen wilt gaan.\nJe belt je neef op die in hetzelfde dorp woont en gaat daar langs,\nAls je aan komt zie je dat bijna je hele familie bij je neef is.\nJullie gaan samen een plan maken.")
        d2 = input ("Stel je voor om:\nA Een boot te nemen \nB Via Turkije\nC Via Libanon vluchten\nHier typen:")
        if d2 == "A" or d2 == "a":
            os.system("cls")
            print ("Je stelt voor om de boot te nemen naar Europa,")
            print ("Er is namelijk een Haven een paar honderd kilometer van je dorp vandaan.")
            print ("De rest vind het een goed idee,")
            print ("voordat jullie weg gaan moet iedereen controleren of ze een paspoort mee hebben,")
            print ("Je vrouw heeft de paspoorten van haarzelf en de kinderen in haar tas,")
            print ("Je kunt je eigen paspoort niet vinden.")
            print ("Je herinnerd dat je kleren hebt meegenomen,")
            print ("Je check je broeken en je jassen.")
            print ("Je voelt iets in een van de broekzakken, het is je portemonnee.")
            print ("Je paspoort zit erin, wat een geluk.")
            print ("Je gaat nu met iedereen in auto’s naar de haven.")
            print ("Jullie komen aan in de haven, er is nog maar een boot, het is een kleine boot,")
            print ("Er is genoeg ruimte voor tien mensen. Jullie zijn met veertien.")
            print ("Jullie zijn de enige familie met vier mensen.")
            d3 = input ("Ga je\nA Met je familie een andere manier zoeken om te vluchten\nB Zoeken naar een andere boot\nC Met andere mannen een manier zoeken\nHier typen: ")
            if d3 == "A" or d3 == "a":
                os.system("cls")
                print("Jullie krijgen een extra telefoon en wat geld omdat jullie een groot risico nemen")
                print("Maar jullie zijn nog niet klaar om op te geven.")
                print("Jullie gaan snel terug naar de auto,")
                print("Terwijl jullie naar de auto gaan moeten jullie een nieuw plan verzinnen.")  
                print("Je herinnert je ineens dat e r nog een vliegtuig naar Europa vliegt,") 
                print("Dit is jullie enige keuze, Er zijn drie wegen naar het vliegveld,")
                print("jullie hebben alleen niet zoveel tijd meer.")
                d4 = input ("Nemen jullie\nA De kortste route,\n    het is alleen door een gevaarlijk gebied, \n    waar de kans dat je geraakt wordt door een bom erg groot is \nB De langste route,\n     de kans dat je hier geraakt wordt door een bom is erg klein, \n     maar het gaat wel krap worden met de tijd voor het vliegtuig\nC De middellange route, \n    de kans dat je hier geraakt word is aanwezig maar het is een stuk kleiner\n    ook heb je genoeg tijd om het te maken bij het vliegveld als de reis goed verloopt\nHier typen:")
                if d4 == "A" or d4 == "a":
                    os.system("cls")
                    print ("Jullie nemen de kortste route")
                    print ("Dit was geen goed idee, tijdens de reis worden jullie geraakt door een bom,\njullie hebben het niet overleefd.")
                if d4 == "B" or d4 == "b":
                    os.system("cls")
                    print("B Jullie nemen de langste route, \nde reis gaat goed, jullie hebben geen een bom zien vallen, \njullie hebben ook goed doorgereden, \njullie hebben daarom nog genoeg tijd om een kaartje te kopen. \nJullie komen veilig aan in Europa met het vliegtuig.")
                if d4 == "C" or d4 == "c":
                    os.system("cls")
                    print("C Jullie nemen de middelste route, \nde reis gaat redelijk goed, \ner waren maar een paar bommen gezien. \nJullie hebben wel langzaam gereden, \nhierdoor moeten jullie haasten om kaartjes te kopen, \njullie hadden wel net genoeg tijd en hebben het vliegtuig gehaald")
            if d3 == "B"or d3 == "b":
                os.system("cls")
                print ("Je gaat met twee andere mannen zoeken naar een extra boot,\njullie moeten wel opschieten, \nje weet namelijk niet wanneer je gebombardeerd kan worden. \nEr zijn nog drie gebouwen waar een boot zou kunnen liggen, \nje kunt alleen nog maar één gebouw doorzoeken.")
                d10 = input ("Kies je\nA Gebouw 1\nB Gebouw 2\nC Gebouw 3")
                if d10 == "A"or d10 == "a":
                    os.system("cls")
                    print ("Je gaat snel het eerste gebouw in, \ner ligt een boot in dit gebouw, \nje haalt snel een paar andere mensen om jullie te helpen om de boot naar het water te krijgen, \nAls de boot in het water ligt gaan jullie met zijn alle naar Europa varen. \nNa een lange vaart komen jullie aan in Europa, \njullie zijn nu veilig")
                if d10 == "B" or d10 == "b":
                    os.system("cls")
                    print ("Jullie doorzoeken nog even snel het tweede gebouw, \ner ligt helaas geen extra boot, \nals jullie weer weg willen gaan krijgen jullie de deur niet meer open, \nna een paar minuten proberen krijgen jullie eindelijk de deur open. \nAls jullie bij de haven aankomen merken jullie dat iedereen al weg is. \nDit vinden jullie erg raar omdat jullie wel hadden verwacht dat ze zouden wachten, \njullie kijken even rond of jullie kunnen zien of er misschien iets is gebeurd. \nNa een paar minuten kijken zien jullie en erg fel licht. \nEr is een bom naast jullie ontploft, \njullie hebben het niet overleefd.")
                if d10 == "C" or d10 == "c":
                    os.system("cls")
                    print ("Jullie doorzoeken nog even snel het derde gebouw, \ner ligt helaas geen extra boot, \nals jullie weer weg willen gaan krijgen jullie de deur niet meer open, \nna een paar minuten proberen krijgen jullie eindelijk de deur open. \nAls jullie bij de haven aankomen merken jullie dat iedereen al weg is. \nDit vinden jullie erg raar omdat jullie wel hadden verwacht dat ze zouden wachten, \njullie kijken even rond of jullie kunnen zien of er misschien iets is gebeurd. \nNa een paar minuten kijken zien jullie en erg fel licht. \nEr is een bom naast jullie ontploft, \njullie hebben het niet overleefd.")
            if d3 == "C" or d3 == "c":
                os.system("cls")
                print("Je stelt het idee voor en de mannen vinden het goed, \njullie gaan snel naar de auto, \neen van de mannen zegt dan dat hij heeft gehoord dat er een vliegtuig vliegt. \nAls jullie optijd zijn zou dit jullie redding kunnen zijn. \nJullie overleggen het even en besluiten om naar het vliegveld te gaan.")
                d11 = input ("Nemen jullie:\nA De kortste route, \n    het is alleen door een gevaarlijk gebied \n     de kans dat je geraakt wordt door een bom is erg groot\nB De langste route, \n   de kans dat je hier geraakt wordt door een bom is erg klein, \n    maar het gaat wel krap worden met de tijd voor het vliegtuig\nC De middellange route, \n    de kans dat je hier geraakt word is aanwezig maar het is een stuk kleiner, \n    ook heb je genoeg tijd om het te maken bij het vliegveld als de reis goed verloopt\nHier typen:")
                if d11 == "A" or d11 == "a":
                    os.system("cls")
                    print ("Jullie nemen de kortste route, \nde reis begint goed,\nmaar als jullie even aan het rijden dan vallen er steeds meer bommen bij jullie in de buurt. \nNog een paar minuten worden jullie geraakt door een bom. \nJullie overleven het niet.")
                if d11 == "B" or d11 == "b":
                    os.system("cls")
                    print ("Jullie nemen de langste route, \nde reis gaat goed, jullie hebben geen een bom zien vallen, \njullie hebben ook goed doorgereden, \njullie hebben daarom nog genoeg tijd om een kaartje te kopen. \nJullie komen veilig aan in Europa met het vliegtuig.")
        if d2 == "B" or d2 == "b":
            os.system("cls")
            print ("Het plan is om naar Turkije te gaan, \nhet is een lange reis, \ngelukkig hebben jullie eten en drinken mee. \nHet was een lange en gevaarlijke reis, \nmaar jullie zijn aangekomen bij de grens. \nNu is alleen het gevaarlijkste gedeelte, \nDe Turkse grens over is namelijk erg moeilijk omdat, \nde Turkse overheid vluchtelingen niet zo leuk vindt.")
            d5 = input ("Gaan jullie:\nA Met de auto door de grenswacht\nB Nep paspoort regelen\nC schuilen in een ander voertuig\nHier typen:")
            if d5 == "A" or d5 == "a":
                os.system("cls")
                print ("Jullie besluiten om met de auto door de grenswacht te gaan, \ndit was een goede keuze, \nde grenswacht laat jullie namelijk gewoon door rijden. \nJullie hebben  het gevaarlijkste gedeelte nu gehad, \nhet enige wat jullie nu nog moeten doen is met de auto naar Europa")
            if d5 == "B"or d5 == "b":
                os.system("cls")
                print ("Jullie denken dat het beste is oom een nep paspoort te halen, \njullie zien iemand en vragen het aan hem, \nhij zegt dat hij dat voor jullie wilt doen, \nhij zegt dat hij zijn spullen moet halen en vraagt aan jullie om even te blijven. \nNa een paar minuten komt hij terug met de politie en jullie worden opgepakt en in de gevangenis gegooid.")
            if d5 == "C" or d5 == "c":
                os.system("cls")
                print("Jullie gaan opzoek naar een bus of een auto waar jullie mee kunnen gaan over de grens, \njullie vinden een bus die jullie mee wilt nemen, \nals jullie over de grens aan het gaan zijn worden jullie gestopt, \nde bus word doorgezocht. \nDe politie vind jullie in de bus, \njullie worden aangehouden en in de gevangenis gegooid.")
        if d2 == "C" or d2 == "c":
            print ("Jullie gaan naar Libanon, \nLibanon is een goede keuze omdat het dichtbij is en Libanon kan je veilig binnen. \nJullie komen aan in Libanon na een paar uur. \nJullie gaan opzoek naar een vliegveld om een vliegtuig te nemen naar Europa, \njullie weten namelijk dat je familie ook naar Europa gaat. \nGelukkig hebben jullie genoeg geld meegenomen om de tickets te betalen. \nDe vlucht is goed gegaan en jullie zijn nu veilig in Europa ")
    if d1 == "B" or d1 == "b":
        os.system("cls")
        print ("Je Hebt Geld, eten en drinken mee genomen, je bent je telefoon vergeten.")
        d16 = input ("Ga je:\nA Terug naar binnen om je telefoon te halen \nB Naar je neef\nC een plan verzinnen met je gezin\nHier typen:")
        if d16 == "A" or d16 == "a":
            os.system("cls")
            print ("\nJe gaat terug voor je telefoon, \nals je binnenkomt zie je een heel fel licht, \nje voelt ook een schok door je lichaam gaan, \ner is zojuist een bom naast je beland, \nje hebt het helaas niet overleefd" )
        if d16 == "B" or d16 == "b":
            os.system("cls")
            print ("Jullie besluiten om naar je neef te gaan, \nals jullie aankomen is iedereen al weg, \nje besluit je neef even te bellen om te vragen wat hij aan het doen is, \nhij verteld dat hij met de rest van jouw familie in de haven zijn en dat ze met een boot naar Europa gaan, \nje vraagt of jullie met hun mee kunnen, \nhij zegt dat er geen plek meer is voor jullie, \njullie zullen dus iets anders moeten verzinnen")
            d19 = input ("Wat gaan jullie doen\nA Alsnog naar de haven\nB Een vliegtuig nemen\nC Via Libanon vluchten\nHier typen:")
            if d19 == "A" or d19 == "a":
                os.system("cls")
                print ("Jullie gaan toch naar de haven \nook al heeft je neef gezegd dat er geen plaats is, \njullie hopen dat er nog een extra boot is, \nje vraagt aan je neef of ze nog voor een boot kunnen zoeken, \nze gaan nog even voor jullie kijken. \nAls jullie aankomen is iedereen druk aan het zoeken, \ner is nog geen boot gevonden. \nEr zijn nog drie gebouwen om te doorzoeken, \nmaar er is maar tijd om er één te doorzoeken, \n")
                d20 = input ("Welk gebouw kies je\nA Het eerste gebouw\nB het tweede gebouw\nC Het derde gebouw\nHier typen:")
                if d20 == "A" or d20 == "a":
                    os.system("cls")
                    print ("Jullie doorzoeken nog even snel het eerste gebouw, \ner ligt gelukkig een extra, \nje gaat snel hulp halen om de boot in het water te krijgen, \nmet de twee boten varen jullie allemaal gezamenlijk naar Europa, \njullie komen na een lange reis aan in Nederland.")
                if d20 == "B" or d20 == "b":
                    os.system("cls")
                    print("Jullie doorzoeken nog even snel het tweede gebouw, \ner ligt gelukkig een extra, \nje gaat snel hulp halen om de boot in het water te krijgen, \nmet de twee boten varen jullie allemaal gezamenlijk naar Europa, \njullie komen na een lange reis aan in Nederland.")
                if d20 == "C" or d20 == "c":
                    os.system("cls")
                    print("Jullie doorzoeken nog even snel het laatste gebouw, \ner ligt helaas geen extra boot, \nals jullie weer weg willen gaan krijgen jullie de deur niet meer open, \nna een paar minuten proberen krijgen jullie eindelijk de deur open. \nAls jullie bij de haven aankomen merken jullie dat iedereen al weg is. \nDit vinden jullie erg raar omdat jullie wel hadden verwacht dat ze zouden wachten, \njullie kijken even rond of jullie kunnen zien of er misschien iets is gebeurd. \nNa een paar minuten kijken zien jullie en erg fel licht. \nEr is een bom naast jullie ontploft, \njullie hebben het niet overleefd.")
            if d19 == "B"or d19 == "b":
                os.system("cls")
                print ("Jullie nemen het vliegtuig naar Europa, \nonderweg naar het vliegtuig hebben jullie een paar bommen gezien maar jullie hebben het overleefd, \njullie waren ook op tijd voor het vliegtuig. \nDe vlucht is goed gegaan en jullie zijn veilig in Europa aangekomen.")
            if d19 == "C" or d19 == "c":
                os.system("cls")
                print("Jullie zijn van plan om via Libanon naar Europa te gaan. \nDe reis naar Libanon is erg goed gegaan, \njullie zijn ook over de grens gelaten. \nJullie hebben in Libanon een vliegtuig genomen naar Europa.")
        if d16 == "C" or d16 == "c":
            os.system("cls")
            print ("Jullie gaan in de auto een plan verzinnen")
            d22 = input ("Gaan jullie\nA Naar Turkije\nB Naar het vliegveld\nC Naar Libanon\nHier typen:")
            if d22 == "A" or d22 == "a":
                os.system("cls")
                print ("Het plan is om naar Turkije te gaan, \nhet is een lange reis, \ngelukkig hebben jullie eten en drinken mee. \nHet was een lange en gevaarlijke reis, \nmaar jullie zijn aangekomen bij de grens. \nNu is alleen het gevaarlijkste gedeelte, \nDe Turkse grens over is namelijk erg moeilijk omdat de Turkse overheid vluchtelingen niet zo leuk vindt.")
                d23 = input ("Ga je\nA Met de auto\nB Nep paspoort regelen\nC Schuilen in een andere auto\nHier typen:")
                if d23 == "A" or d23 == "a":
                    os.system("cls")
                    print ("Jullie gaan met de auto door de grenswacht, \nterwijl jullie er doorheen rijden worden jullie aangehouden, \njullie auto wordt doorzocht, \nna de controle word er gevraagd wat jullie aan het doen zijn, \njullie leggen uit dat jullie aan het vluchten zijn. \nNadat jullie het verhaal hebben verteld worden jullie doorgelaten, \njullie zijn nu veilig.")
                if d23 == "B" or d23 == "b":
                    os.system("cls")
                    print ("Jullie denken dat het beste is oom een nep paspoort te halen, \njullie zien iemand en vragen het aan hem, \nhij zegt dat hij dat voor jullie wilt doen, \nhij zegt dat hij zijn spullen moet halen en vraagt aan jullie om even te blijven. \nNa een paar minuten komt hij terug met de politie en jullie worden opgepakt en in de gevangenis gegooid.")
                if d23 == "C" or d23 == "c":
                    os.system("cls")
                    print ("Jullie denken dat het het verstandigst is om te schuilen in een andere bus of auto, \njullie vinden een meneer in een bus die jullie wilt helpen, \njullie gaan achterin de bus zitten, \njullie komen zonder enige problemen over de grens, \njullie zijn veilig.")
            if d22 == "B" or d22 == "b":
                os.system("cls")
                print("Jullie gaan met het vliegtuig, \nJullie hebben geluk \ner is namelijk een vliegtuig dat jullie nog kunnen halen als jullie snel weg gaan\nJullie komen optijd aan bij het vliegveld\nJullie komen veilig aan in Europa")
            if d22 == "C" or d22 == "c":
                os.system("cls")
                print ("Jullie gaan naar Libanon\nJullie worden bij de grens aangehouden,\nGelukkig hebben jullie niks mee dus mogen jullie door rijden\nJullie zijn veilig")
    if d1 == "C" or d1 == "c":
        os.system("cls")
        print ("Je hebt alleen je Telefoon mee, \nje moet naar iemand de je kent, \nje herinnert dat je neef in hetzelfde dorp woont, \nje hebt geen andere keuze. \nAls je aankomt ben je net optijd, \niedereen was op het punt op weg te gaan, \nje ziet ook dat de rest van je familie er is. \nZe geven je wat extra oude kleren zodat je je kan omkleden als dat nodig is, \nook geven ze je wat geld.")
        print ("Jullie komen aan bij de haven, \ner zijn alleen niet genoeg plaatsen op de boot, \ner zijn vier plaatsen te weinig. \nJou familie is de enige met vier mensen dus er word voorgesteld om jullie achter te laten.")
        d30 = input ("Wat doe je \nA Je neemt het aanbot aan\nB Zoeken naar een andere boot\nC Met andere mannen een manier zoeken\nHier typen:")
        if d30 == "A" or d30 == "a":
            os.system("cls")
            print ("Jullie krijgen een extra telefoon en wat geld omdat jullie je hebben opgeofferd, \nmaar jullie zijn nog niet klaar om op te geven. \nJullie gaan snel terug naar de auto, \nterwijl jullie naar de auto gaan moeten jullie een nieuw plan verzinnen.")
            d31 = input ("Gaan jullie\nA Via de grens naar Turkije\nB 1Vliegtuig\nC Via Libanon\nHier typen: ")
            if d31 == "A" or d31 == "a":
                os.system("cls")
                print ("Jullie besluiten om via Turkije te vluchten, \nals jullie bij de grens komen worden jullie aangehouden, \nze doorzoeken jullie auto en alle spullen die jullie bij jullie hebben, \nze vragen daarna wat jullie van plan waren, \nje legt uit dat jullie aan het vluchten zijn, \njullie worden daarom opgepakt en in de gevangenis gestopt")
            if d31 == "B"or d31 == "b":
                os.system("cls")
                print ("Jullie gaan naar het vliegveld, \nonderweg hebben jullie al gekeken op de telefoon en er vliegt een vliegtuig. \nDoor het extra geld dat jullie hebben gekregen kunnen jullie tickets kopen. \nDe vlucht is goed gegaan en jullie zijn veilig in Europa")
            if d31 == "C" or d31 == "c":
                os.system("cls")
                print("Jullie gaan proberen om via Libanon te vluchten. \nDe reis naar Libanon ging goed, \njullie werden door de grens gelaten en konden met een vliegtuig naar Europa vliegen.")
        if d30 == "B" or d30 == "b":
            os.system("cls")
            print ("Jullie gaan opzoek naar een andere boot, \ner zijn erg veel gebouwen waar een boot zou kunnen liggen, \njullie moeten dus opschieten, \nje weet namelijk noot wanneer er een bom zou kunnen vallen. \nAls jullie een tijdje aan het zoeken zijn hebben jullie nog steeds geen boot gevonden, \ner zijn nog drie gebouwen over maar jullie hebben maar tijd om er één te doorzoeken.")
            d33 = input ("Welk gebouw doorzoeken jullie\nA Gebouw 1\nB Gebouw 2\nC Gebouw 3\nHier typen:")
            if d33 == "A" or d33 == "a":
                os.system("cls")
                print ("Jullie doorzoeken nog even snel het eerste gebouw, \ner ligt helaas geen extra boot, \nals jullie weer weg willen gaan krijgen jullie de deur niet meer open, \nna een paar minuten proberen krijgen jullie eindelijk de deur open. \nAls jullie bij de haven aankomen merken jullie dat iedereen al weg is. \nDit vinden jullie erg raar omdat jullie wel hadden verwacht dat ze zouden wachten, \njullie kijken even rond of jullie kunnen zien of er misschien iets is gebeurd. \nNa een paar minuten kijken zien jullie en erg fel licht. \nEr is een bom naast jullie ontploft, \njullie hebben het niet overleefd.")
            if d33 == "B"or d33 == "b":
                os.system("cls")
                print ("Jullie doorzoeken nog even snel het tweede gebouw, \ner ligt gelukkig een extra, \nje gaat snel hulp halen om de boot in het water te krijgen, \nmet de twee boten varen jullie allemaal gezamenlijk naar Europa, \njullie komen na een lange reis aan in Nederland.")
            if d33 == "C" or d33 == "c":
                os.system("cls")
                print("Jullie besluiten dat het te gevaarlijk is om nog een gebouw te doorzoeken,\nJullie gaan naar de auto, \nterwijl jullie in de auto stappen besluiten dat het het beste is om naar het vliegtuig te gaan. \nJullie hebben daarmee geluk want jullie kunnen het nog op tijd halen als jullie doorrijden. \nJullie komen aan bij het vliegveld, \nook zijn jullie nog op tijd voor het vliegtuig. \nJullie nemen het vliegtuig en komen veilig aan in Europa")
        if d30 == "C" or d30 == "c":
            os.system("cls")
            print ("Je stelt het idee voor, \nde mannen vinden het een goed idee, \njullie rennen snel naar de auto. \nIn de auto zegt een van de mannen dat hij had gezien dat er een vliegtuig vliegt naar Europa, \nen het vliegveld is redelijk dichtbij. \nHet vliegtuig vliegt alleen in een half uur. \nEr zijn drie wegen die je kunt nemen, \nde kortste is één kwartier, \nhet gaat alleen wel door het gebied waar de meeste bommen vallen. \nDe tweede weg is de langste, \ndeze weg duur vijfentwintig minuten, \nde kans dat je dan door een bom geraakt word is dan wel het kleinst, \nmaar jullie moeten ook nog kaartjes kopen. \nDe laatste weg duurt twintig minuten, \ndit zou genoeg moeten zijn om optijd bij het vliegveld te komen als er niks fout gaat. \nDe kans dat er een bom op je komt is via deze weg wel aanwezig, \nmaar het is een stuk kleiner als bij de eerste.")
            d36 = input ("Welke weg nemen jullie\nA De kortste\nB De langste\nC De middellange\nHier typen:")
            if d36 == "A" or d36 == "a":
                os.system("cls")
                print ("Jullie nemen de kortste weg\nAlles is goed gegaan en jullie zijn optijd bij het vliegveld gekomen\nJullie nemen het vliegtuig en jullie zijn veilig in Europa.")
            if d36 == "B" or d36 == "b":
                os.system("cls")
                print("Jullie nemen de langste weg,\nDe reis is goed gegaan en jullie zijn veilig en wel aangekomen\nEn omdat jullie goed hebben doorgereden zijn jullie nog optijd voor het vliegtuig.")
            if d36 == "C" or d36 == "c":
                os.system("cls")
                print ("Jullie nemen de middellange route\nHet begin van de reis gaat goed\nmaar als jullie op de helft van de reis zijn\nworden jullie geraakt door een bom\njullie overleven het niet")
    if (input("Wil je restarten?") == "Y"):
        os.system('cls')
        continue
    else:
     break

input()
                