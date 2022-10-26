# GETTING THE SOFTWARE DATA

import pandas as pd
import os


def software():
    user = os.getlogin()
    user_path = r"C:/Users/" + user
    export_path = os.path.join(user_path, 'Desktop/Licitatie Excel/export.xlsx')
    licitatii_path = os.path.join(user_path, 'Desktop/Licitatie Excel/licitatii.xlsx')

    data_export = pd.read_excel(export_path)
    licitatii_export = pd.read_excel(licitatii_path)

    data_export.columns = ['Autoritate contractanta', 'Nr anunt', 'Denumire contract', 'Tip contract', 'Tip anunt',
                           'Cod si denumire CPV', 'Data publicare', 'Data limita depunere oferta', 'Valoare estimata']
    licitatii_export.columns = ['Numar anunt', 'Data publicare', 'Erate', 'Denumire contract', 'Tip procedura',
                                'Tipul contractului',
                                'Stare procedura', 'Modalitate de desfasurare', 'Modalitatea de atribuire', 'Cod CPV',
                                'Autoritate contractanta', 'Data limita depunere', 'Valoare estimata']
    lista = ["48000000-8 - Pachete software si sisteme informatice (Rev.2)",
             "48300000-1 - Pachete software pentru creare de documente, pentru desen, imagistica, planificare si productivitate (Rev.2)",
             "48611000-4 - Pachete software pentru baze de date (Rev.2)",
             "48900000-7 - Diverse pachete software si sisteme informatice (Rev.2)",
             "48190000-6 - Pachete software educationale (Rev.2)"]

    data_to_export = data_export.loc[data_export['Cod si denumire CPV'].isin(lista)]
    data_to_licitatii = licitatii_export.loc[licitatii_export['Cod CPV'].isin(lista)]

    data_to_export.to_excel(user_path + '/Desktop/Licitatie Excel/adv/adv-soft.xlsx')
    data_to_licitatii.to_excel(user_path + '/Desktop/Licitatie Excel/scn/scn-soft.xlsx')


def servicii():
    user = os.getlogin()
    user_path = r"C:/Users/" + user
    export_path = os.path.join(user_path, 'Desktop/Licitatie Excel/export.xlsx')
    licitatii_path = os.path.join(user_path, 'Desktop/Licitatie Excel/licitatii.xlsx')

    data_export = pd.read_excel(export_path)
    licitatii_export = pd.read_excel(licitatii_path)

    data_export.columns = ['Autoritate contractanta', 'Nr anunt', 'Denumire contract', 'Tip contract', 'Tip anunt',
                           'Cod si denumire CPV', 'Data publicare', 'Data limita depunere oferta', 'Valoare estimata']
    licitatii_export.columns = ['Numar anunt', 'Data publicare', 'Erate', 'Denumire contract', 'Tip procedura',
                                'Tipul contractului',
                                'Stare procedura', 'Modalitate de desfasurare', 'Modalitatea de atribuire', 'Cod CPV',
                                'Autoritate contractanta', 'Data limita depunere', 'Valoare estimata']
    lista2 = ["30211300-4 - Platforme informatice (Rev.2)", "30211400-5 - Configuratii informatice (Rev.2)",
              "71242000-6 - Pregatire de proiecte si proiectare, estimare a costurilor (Rev.2)",
              "71300000-1 - Servicii de inginerie (Rev.2)",
              "71317000-3 - Servicii de consultanta in protectia contra riscurilor si in controlul riscurilor (Rev.2)",
              "71356200-0 - Servicii de asistenta tehnica (Rev.2)", "71356300-1 - Servicii de suport tehnic (Rev.2)",
              "72000000-5 - Servicii IT: consultanta, dezvoltare de software, internet si asistenta (Rev.2)",
              "72212900-8 - Diverse servicii de dezvoltare de software si sisteme informatice (Rev.2)",
              "72224000-1 - Servicii de consultanta privind gestionarea proiectelor (Rev.2)",
              "72227000-2 - Servicii de consultanta privind integrarea software (Rev.2)",
              "72230000-6 - Servicii de dezvoltare de software personalizat (Rev.2)",
              "72267000-4 - Servicii de intretinere si reparatii de software (Rev.2)",
              "72268000-1 - Servicii de furnizare de software (Rev.2)", "72320000-4 - Servicii de baze de date (Rev.2)",
              "72413000-8 - Servicii de proiectare de site-uri WWW (World Wide Web) (Rev.2)",
              "72611000-6 - Servicii de asistenta tehnica informatica (Rev.2)",
              "73200000-4 - Servicii de consultanta in cercetare si in dezvoltare (Rev.2)",
              "79110000-8 - Servicii de consultanta si de reprezentare juridica (Rev.2)",
              "79311100-8 - Servicii de elaborare de studii (Rev.2)",
              "79311300-0 - Servicii de analiza a studiilor (Rev.2)",
              "79315000-5 - Servicii de cercetare sociala (Rev.2)",
              "79400000-8 - Consultanta in afaceri si in management si servicii conexe (Rev.2)",
              "79411000-8 - Servicii generale de consultanta in management (Rev.2)",
              "79419000-4 - Servicii de consultanta in domeniul evaluarii (Rev.2)",
              "80533100-0 - Servicii de formare in informatica (Rev.2)",
              "72224000-1 - Servicii de consultanta privind gestionarea proiectelor (Rev.2)",
              "72227000-2 - Servicii de consultanta privind integrarea software (Rev.2)",
              "72253200-5 - Servicii de asistenta pentru sisteme (Rev.2)", "72260000-5 - Servicii de software (Rev.2)",
              "72261000-2 - Servicii de asistenta pentru software (Rev.2)",
              "73110000-6 - Servicii de cercetare (Rev.2)",
              "73220000-0 - Servicii de consultanta in dezvoltare (Rev.2)"]

    data_e = data_export.loc[data_export['Cod si denumire CPV'].isin(lista2)]
    data_l = licitatii_export.loc[licitatii_export['Cod CPV'].isin(lista2)]

    data_e.to_excel(user_path + '/Desktop/Licitatie Excel/adv/adv-servicii.xlsx')
    data_l.to_excel(user_path + '/Desktop/Licitatie Excel/scn/scn-servicii.xlsx')


def hardware():
    user = os.getlogin()
    user_path = r"C:/Users/" + user
    export_path = os.path.join(user_path, 'Desktop/Licitatie Excel/export.xlsx')
    licitatii_path = os.path.join(user_path, 'Desktop/Licitatie Excel/licitatii.xlsx')

    data_export = pd.read_excel(export_path)
    licitatii_export = pd.read_excel(licitatii_path)
    data_export.columns = ['Autoritate contractanta', 'Nr anunt', 'Denumire contract', 'Tip contract', 'Tip anunt',
                           'Cod si denumire CPV', 'Data publicare', 'Data limita depunere oferta', 'Valoare estimata']
    licitatii_export.columns = ['Numar anunt', 'Data publicare', 'Erate', 'Denumire contract', 'Tip procedura',
                                'Tipul contractului',
                                'Stare procedura', 'Modalitate de desfasurare', 'Modalitatea de atribuire', 'Cod CPV',
                                'Autoritate contractanta', 'Data limita depunere', 'Valoare estimata']
    lista3 = ["33195100-4 Monitoare (Rev.2)", "38652120-7 Videoproiectoare (Rev.2)",
              "30232110-8 Imprimante laser (Rev.2)",
              "30125100-2 Cartuse de toner (Rev.2)", "32250000-0 Telefoane mobile (Rev.2)",
              "30213100-6 Computere portabile (Rev.2)", "31531000-7 Becuri (Rev.2)",
              "31524000-5 Plafoniere sau aplice de perete (Rev.2)",
              "65400000-7 Alte surse de alimentare si de distributie a energiei electrice (Rev.2)",
              "31527200-8 Iluminat exterior (Rev.2)", "31527260-6 Sisteme de iluminat (Rev.2)",
              "31500000-1 Aparatura de iluminat si lampi electrice (Rev.2)",
              "34928530-2 Lampi de iluminat stradal (Rev.2)",
              "31521000-4 Lampi (Rev.2)",
              "38112100-4 Sisteme de navigare si de pozitionare globala (GPS sau echivalente) (Rev.2)",
              "37400000-2 Articole si echipament de sport (Rev.2)", "18522000-4 Ceasuri de mana (Rev.2)",
              "35125000-6 Sisteme de supraveghere (Rev.2)", "32420000-3 Echipament de retea (Rev.2)",
              "31712116-6 Microprocesoare (Rev.2)", "30125000-1 Piese si accesorii pentru fotocopiatoare (Rev.2)",
              "30237134-7 Acceleratoare grafice (Rev.2)", "30141200-1 Calculatoare de birou (Rev.2)",
              "38651000-3 Aparate de fotografiat (Rev.2)", "35125300-2 Camere video de securitate (Rev.2)",
              "30237460-1 Tastaturi pentru computer (Rev.2)", "30232150-0 Imprimante cu jet de cerneala (Rev.2)",
              "44423000-1 Diverse articole (Rev.2)", "32324000-0 Televizoare (Rev.2)",
              "30192113-6 Cartuse de cerneala (Rev.2)", "30237200-1 Accesorii pentru computere (Rev.2)",
              "32342100-3 Casti (Rev.2)", "30233132-5 Unitati de hard disk (Rev.2)",
              "30237000-9 Piese si accesorii pentru computere (Rev.2)", "31158000-8 - Incarcatoare (Rev.2)",
              "31154000-0 Surse de alimentare electrica continua (Rev.2)",
              "30237270-2 Genti pentru computere portabile (Rev.2)", "35121700-5 Sisteme de alarma (Rev.2)",
              "48000000-8 Pachete software si sisteme informatice (Rev.2)",
              "32000000-3 Echipament de radio, televiziune, comunicatii, telecomunicatii si articole conexe (Rev.2)",
              "30237240-3 Camera web (Rev.2)", "48900000-7 Diverse pachete software si sisteme informatice (Rev.2)",
              "39154100-7 Standuri de expozitie (Rev.2)", "33734000-4 Ochelari (Rev.2)",
              "30237140-2 Placi de baza (Rev.2)",
              "31430000-9 Acumulatori electrici (Rev.2)", "30234600-4 Memorie flash (Rev.2)",
              "38651100-4 Obiective pentru aparate de fotografiat (Rev.2)", "39711130-9 Frigidere (Rev.2)",
              "30233132-5 - Unitati de hard disk (Rev.2)", "44510000-8 Scule (Rev.2)",
              "44512940-3 Truse de scule (Rev.2)",
              "37414200-5 Lazi frigorifice (Rev.2)", "39713210-8 Masini de spalat si uscat rufe (Rev.2)",
              "32420000-3 - Echipament de retea (Rev.2)", "31111000-7 Adaptoare (Rev.2)",
              "39717200-3 Aparate de aer conditionat (Rev.2)", "39715210-2 Echipament de incalzire centrala (Rev.2)",
              "48761000-0 Pachete software antivirus (Rev.2)", "38520000-6 Scanere (Rev.2)",
              "31224810-3 Cabluri prelungitoare (Rev.2)", "35240000-8 Sirene (Rev.2)",
              "30233152-1 Dispozitiv de citire si/sau inscriptionare DVD-uri (Rev.2)",
              "30192113-6 - Cartuse de cerneala (Rev.2)", "32323500-8 Sistem video de supraveghere (Rev.2)",
              "39700000-9 Aparate de uz casnic (Rev.2)", "39112000-0 Scaune (Rev.2)",
              "32422000-7 Componente de retea (Rev.2)", "30213000-5 Computere personale (Rev.2)",
              "39713100-4 Masini de spalat vase (Rev.2)",
              "30200000-1 - Echipament si accesorii pentru computer (Rev.2)",
              "30237300-2 Accesorii informatice (Rev.2)", "31711310-9 Sistem de pontaj (Rev.2)",
              "33195100-4 - Monitoare (Rev.2)", "32552600-3 - Interfoane (Rev.2)",
              "39221000-7 Echipament de bucatarie (Rev.2)", "30237450-8 Tablete grafice (Rev.2)",
              "39721000-2 Aparate de uz casnic pentru gatit sau incalzit (Rev.2)",
              "39314000-6 Echipament de bucatarie industriala (Rev.2)",
              "39711330-1 Prajitoare de paine electrice (Rev.2)",
              "42923200-4 Cantare (Rev.2)", "39711361-7 Cuptoare electrice (Rev.2)", "39221110-1 Vesela (Rev.2)",
              "39711310-5 Filtre de cafea electrice (Rev.2)", "44511400-9 Topoare (Rev.2)",
              "42514200-4 Epuratoare electrostatice de aer si de gaz (Rev.2)",
              "39713510-1 Fiare de calcat cu aburi (Rev.2)", "31531000-7 - Becuri (Rev.2)",
              "32341000-5 Microfoane (Rev.2)",
              "39711362-4 Cuptoare cu microunde (Rev.2)",
              "39715240-1 Aparate electrice de incalzire ambientala (Rev.2)",
              "42113161-0 Deumidificatoare (Rev.2)", "39711210-4 Roboti de bucatarie (Rev.2)",
              "39711210-4 - Roboti de bucatarie (Rev.2)", "39130000-2 Mobilier de birou (Rev.2)",
              "39100000-3 Mobilier (Rev.2)", "18521000-7 Ceasuri (Rev.2)",
              "39141300-5 Dulapuri compartimentate (Rev.2)",
              "39711110-3 Frigidere cu congelator (Rev.2)", "39713430-6 Aspiratoare (Rev.2)",
              "33123100-9 Tensiometru (Rev.2)", "18522000-4 - Ceasuri de mana (Rev.2)",
              "33123100-9 Tensiometru (Rev.2)",
              "16320000-4 Masini de cosit (Rev.2)", "44511500-0 Ferastraie de mana (Rev.2)",
              "31625300-6 Sisteme de alarma antiefractie (Rev.2)", "30237410-6 - Mouse pentru computer (Rev.2)",
              "31440000-2 Baterii (Rev.2)", "30231200-9 Console (Rev.2)",
              "30233180-6 Dispozitive de stocare cu memorie flash (Rev.2)",
              "48760000-3 Pachete software de protectie antivirus (Rev.2)", "30237410-6 Mouse pentru computer (Rev.2)",
              "32342100-3 - Casti (Rev.2)",
              "42514000-2 Dispozitive si aparate de filtrare sau de purificare a gazelor (Rev.2)",
              "30237135-4 Placi de retea (Rev.2)", "39516000-2 Articole de mobilier (Rev.2)",
              "42662000-4 Echipament de sudare (Rev.2)",
              "42641300-4 Masini-unelte pentru prelucrarea betonului (Rev.2)",
              "31120000-3 Generatoare (Rev.2)", "38431200-7 - Detectoare de fum (Rev.2)",
              "16311000-8 Masini de tuns iarba (Rev.2)", "39831240-0 - Produse de curatenie (Rev.2)",
              "35125100-7 Senzori (Rev.2)", "39173000-5 Unitati de stocare (Rev.2)",
              "30234500-3 Suporturi de stocare cu memorie (Rev.2)", "32270000-6 Aparate de transmisie digitala (Rev.2)",
              "30237220-7 Suport pentru mouse (Rev.2)", "44321000-6 Cablu (Rev.2)",
              "30213300-8 Computer de birou (Rev.2)",
              "31681500-8 Aparate de reincarcare (Rev.2)", "42961100-1 Sisteme de control al accesului (Rev.2)",
              "30231100-8 Terminale informatice (Rev.2)", "32342412-3 Boxe (Rev.2)"]

    data_exp = data_export.loc[data_export['Cod si denumire CPV'].isin(lista3)]
    data_license = licitatii_export.loc[licitatii_export['Cod CPV'].isin(lista3)]

    data_exp.to_excel(user_path + '/Desktop/Licitatie Excel/adv/adv-hard.xlsx')
    data_license.to_excel(user_path + '/Desktop/Licitatie Excel/scn/scn-hard.xlsx')
