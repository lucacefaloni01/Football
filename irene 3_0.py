
import pandas as pd
def import_seriea():
    import pandas as pd 
    

    import pandas as pd
    ###########SERIEA###########
    Sea = pd.read_html("https://fbref.com/it/comp/11/Serie-A-Seasons#results2022-2023111_home_away::1")
    for idx,table in enumerate(Sea):
        idx
        table
    SerieA = Sea[0]
    SerieA

    print('OK!!')
    #"#############ATALANTA#############"
    Ata = pd.read_html("https://fbref.com/it/squadre/922493f3/Statistiche-Atalanta#matchlogs_for")
    for idx,table in enumerate(Ata):
        idx
        table
    Atalanta = Ata[1]
    Atalanta = Atalanta[Atalanta['Rf'].notna()]
    Atalanta.to_csv('~/Desktop/irene3.0/Data/SerieA/Atalanta.csv')

    print('OK!!')
    #"############BOLOGNA####################"
    Bol = pd.read_html("https://fbref.com/it/squadre/1d8099f8/Statistiche-Bologna#matchlogs_for")
    for idx,table in enumerate(Bol):
        
        idx
        table
    Bologna = Bol[1]
    Bologna = Bologna[Bologna['Rf'].notna()]
    Bologna
    Bologna.to_csv('~/Desktop/irene3.0/Data/SerieA/Bologna.csv')
    print('OK!!')

    ##############CREMONESE##############
    Cre = pd.read_html("https://fbref.com/it/squadre/9aad3a77/Statistiche-Cremonese#matchlogs_for")
    for idx,table in enumerate(Cre):
        
        idx
        table
    Cremonese = Cre[1]
    Cremonese = Cremonese[Cremonese['Rf'].notna()]
    Cremonese
    Cremonese.to_csv('~/Desktop/irene3.0/Data/SerieA/Cremonese.csv')
    print('OK!!')
    #############EMPOLI################
    Emp = pd.read_html("https://fbref.com/it/squadre/a3d88bd8/Statistiche-Empoli#matchlogs_for")
    for idx,table in enumerate(Emp):
        
        idx
        table
    Empoli = Emp[1]
    Empoli = Empoli[Empoli['Rf'].notna()]
    Empoli
    Empoli.to_csv('~/Desktop/irene3.0/Data/SerieA/Empoli.csv')
    print('OK!!')
    ###########Fiorentina###############
    Fio = pd.read_html("https://fbref.com/it/squadre/421387cf/Statistiche-Fiorentina#matchlogs_for")
    for idx,table in enumerate(Fio):
        
        idx
        table
    Fiorentina = Fio[1]
    Fiorentina = Fiorentina[Fiorentina['Rf'].notna()]
    Fiorentina
    Fiorentina.to_csv('~/Desktop/irene3.0/Data/SerieA/Fiorentina.csv')
    print('OK!!')
    #Hellas Verona ################

    Hve = pd.read_html("https://fbref.com/it/squadre/0e72edf2/Statistiche-Hellas-Verona#stats_standard_11")
    for idx,table in enumerate(Hve):
        
        idx
        table
    HellasVerona = Hve[1]
    HellasVerona = HellasVerona[HellasVerona['Rf'].notna()]
    HellasVerona
    HellasVerona.to_csv('~/Desktop/irene3.0/Data/SerieA/HellasVerona.csv')
    print('OK!!')

    #########Inter############

    Int = pd.read_html("https://fbref.com/it/squadre/d609edc0/Statistiche-Internazionale#stats_standard_11")
    for idx,table in enumerate(Int):
        
        idx
        table
    Inter = Int[1]
    Inter = Inter[Inter['Rf'].notna()]
    Inter
    Inter.to_csv('~/Desktop/irene3.0/Data/SerieA/Inter.csv')
    print('OK!!')
    ########Juventus##########

    Juv = pd.read_html("https://fbref.com/it/squadre/e0652b02/Statistiche-Juventus#stats_standard_11")
    for idx,table in enumerate(Juv):
        
        idx
        table
    Juve = Juv[1]
    Juve = Juve[Juve['Rf'].notna()]
    Juve
    Juve.to_csv('~/Desktop/irene3.0/Data/SerieA/Juve.csv')
    print('OK!!')
    ###########Lazio############
    Laz = pd.read_html("https://fbref.com/it/squadre/7213da33/Statistiche-Lazio#matchlogs_for")
    for idx,table in enumerate(Laz):
        
        idx
        table
    Lazio = Laz[1]
    Lazio = Lazio[Lazio['Rf'].notna()]
    Lazio
    Lazio.to_csv('~/Desktop/irene3.0/Data/SerieA/Lazio.csv')
    print('OK!!')

    ##########Lecce#############
    Lec = pd.read_html("https://fbref.com/it/squadre/ffcbe334/Statistiche-Lecce#stats_standard_11")
    for idx,table in enumerate(Lec):
        idx
        table
    Lecce = Lec[1]
    Lecce = Lecce[Lecce['Rf'].notna()]
    Lecce
    Lecce.to_csv('~/Desktop/irene3.0/Data/SerieA/Lecce.csv')
    print('OK!!')
    ##########Milan#############
    Mil = pd.read_html("https://fbref.com/it/squadre/dc56fe14/Statistiche-Milan#matchlogs_for")
    for idx,table in enumerate(Mil):
        idx
        table
    Milan = Mil[1]
    Milan = Milan[Milan['Rf'].notna()]
    Milan
    Milan.to_csv('~/Desktop/irene3.0/Data/SerieA/Milan.csv')
    print('OK!!')
    ##########Monza#############
    Mon = pd.read_html("https://fbref.com/it/squadre/dc56fe14/Statistiche-Milan#matchlogs_for")
    for idx,table in enumerate(Mon):
        idx
        table
    Monza = Mon[1]
    Monza = Monza[Monza['Rf'].notna()]
    Monza
    Monza.to_csv('~/Desktop/irene3.0/Data/SerieA/Monza.csv')
    print('OK!!')
    #########Napoli################

    Nap = pd.read_html("https://fbref.com/it/squadre/d48ad4ff/Statistiche-Napoli#stats_standard_11")
    for idx,table in enumerate(Nap):
        
        idx
        table
    Napoli = Nap[1]
    Napoli = Napoli[Napoli['Rf'].notna()]
    Napoli
    Napoli.to_csv('~/Desktop/irene3.0/Data/SerieA/Napoli.csv')
    print('OK!!')
    ########Roma##################
    Rom = pd.read_html("https://fbref.com/it/squadre/cf74a709/Statistiche-Roma#matchlogs_for")
    for idx,table in enumerate(Rom):
        
        idx
        table
    Roma = Rom[1]
    Roma = Roma[Roma['Rf'].notna()]
    Roma
    Roma.to_csv('~/Desktop/irene3.0/Data/SerieA/Roma.csv')
    print('OK!!')
    #########Salernitana############
    Sal = pd.read_html("https://fbref.com/it/squadre/c5577084/Statistiche-Salernitana#stats_standard_11")
    for idx,table in enumerate(Sal):
        
        idx
        table
    Salernitana = Sal[1]
    Salernitana = Salernitana[Salernitana['Rf'].notna()]
    Salernitana
    Salernitana.to_csv('~/Desktop/irene3.0/Data/SerieA/Salernitana.csv')
    print('OK!!')
    ########Sampdoria############
    Sam = pd.read_html("https://fbref.com/it/squadre/8ff9e3b3/Statistiche-Sampdoria#matchlogs_for")
    for idx,table in enumerate(Sam):
        
        idx
        table
    Sampdoria = Sam[1]
    Sampdoria = Sampdoria[Sampdoria['Rf'].notna()]
    Sampdoria
    Sampdoria.to_csv('~/Desktop/irene3.0/Data/SerieA/Sampdoria.csv')
    print('OK!!')
    ###########Sassuolo###########
    Sas = pd.read_html("https://fbref.com/it/squadre/e2befd26/Statistiche-Sassuolo#stats_standard_11")
    for idx,table in enumerate(Sas):
        
        idx
        table
    Sassuolo = Sas[1]
    Sassuolo = Sassuolo[Sassuolo['Rf'].notna()]
    Sassuolo
    Sassuolo.to_csv('~/Desktop/irene3.0/Data/SerieA/Sassuolo.csv')
    print('OK!!')
    ######Spezia############

    Spe = pd.read_html("https://fbref.com/it/squadre/68449f6d/Statistiche-Spezia#stats_standard_11")
    for idx,table in enumerate(Spe):
        
        idx
        table
    Spezia = Spe[1]
    Spezia = Spezia[Spezia['Rf'].notna()]
    Spezia
    Spezia.to_csv('~/Desktop/irene3.0/Data/SerieA/Spezia.csv')
    print('OK!!')
    ########Torino#########
    Tor = pd.read_html("https://fbref.com/it/squadre/105360fe/Statistiche-Torino#stats_standard_11")
    for idx,table in enumerate(Tor):
        
        idx
        table
    Torino = Tor[1]
    Torino = Torino[Torino['Rf'].notna()]
    Torino
    Torino.to_csv('~/Desktop/irene3.0/Data/SerieA/Torino.csv')
    print('OK!!')

    #######Udinese##########
    Udi = pd.read_html("https://fbref.com/it/squadre/04eea015/Statistiche-Udinese#stats_standard_11")
    for idx,table in enumerate(Udi):
    
        idx
        table
    Udinese = Udi[1]
    Udinese = Udinese[Udinese['Rf'].notna()]
    Udinese
    Udinese.to_csv('~/Desktop/irene3.0/Data/SerieA/Udinese.csv')
    print('OK!!')
    return Atalanta ,Bologna, Cremonese, Empoli, Fiorentina, HellasVerona,Inter, Juve, Lazio, Lecce, Milan, Monza, Napoli, Roma, Salernitana, Sampdoria,Sassuolo,Spezia,Torino,Udinese
    from datetime import datetime
    print('Last Upload:  ', datetime.today())
def PermierLigue():
    import pandas as pd
    #######Arsenal##########
    Ars = pd.read_html("https://fbref.com/it/squadre/18bb7c10/Statistiche-Arsenal#stats_standard_9")
    for idx,table in enumerate(Ars):
        print('********')
        idx
        table
    Arsenal = Ars[1]
    Arsenal = Arsenal[Arsenal['Rf'].notna()]
    Arsenal

    ######AstonVilla##########
    Asv = pd.read_html("https://fbref.com/it/squadre/8602292d/Statistiche-Aston-Villa#stats_standard_9")
    for idx,table in enumerate(Asv):
        print('********')
        idx
        table
    AstonVilla = Asv[1]
    AstonVilla = AstonVilla[AstonVilla['Rf'].notna()]
    AstonVilla

    ############Bournemouth##########
    Bou = pd.read_html("https://fbref.com/it/squadre/4ba7cbea/Statistiche-Bournemouth#stats_standard_9")
    for idx,table in enumerate(Bou):
        print('********')
        idx
        table
    Bournemouth = Bou[1]
    Bournemouth = Bournemouth[Bournemouth['Rf'].notna()]


    #########Brentford##################
    Bre = pd.read_html("https://fbref.com/it/squadre/cd051869/Statistiche-Brentford#stats_standard_9")
    for idx,table in enumerate(Bre):
        print('********')
        idx
        table
    Brentford = Bre[1]
    Brentford = Brentford[Brentford['Rf'].notna()]


    #############Brighton#################
    Bri = pd.read_html("https://fbref.com/it/squadre/d07537b9/Statistiche-Brighton-and-Hove-Albion#stats_standard_9")
    for idx,table in enumerate(Bre):
        print('********')
        idx
        table
    Brighton = Bri[1]
    Brighton = Brighton[Brighton['Rf'].notna()]




    ##########Chelsea#############
    Che = pd.read_html("https://fbref.com/it/squadre/cff3d9bb/Statistiche-Chelsea#stats_standard_9")
    for idx,table in enumerate(Che):
        print('********')
        idx
        table
    Chelsea = Che[1]
    Chelsea = Chelsea[Chelsea['Rf'].notna()]


    ##########Crystal Palace############
    Crp = pd.read_html("https://fbref.com/it/squadre/47c64c55/Statistiche-Crystal-Palace#stats_standard_9")
    for idx,table in enumerate(Crp):
        print('********')
        idx
        table
    CrystalPalace = Crp[1]
    CrystalPalace = CrystalPalace[CrystalPalace['Rf'].notna()]


    ##Everton#########
    Eve = pd.read_html("https://fbref.com/it/squadre/d3fd31cc/Statistiche-Everton#stats_standard_9")
    for idx,table in enumerate(Eve):
        print('********')
        idx
        table
    Everton = Eve[1]
    Everton = Everton[Everton['Rf'].notna()]




    #############Fulham##########
    Ful = pd.read_html("https://fbref.com/it/squadre/fd962109/Statistiche-Fulham#stats_standard_9")
    for idx,table in enumerate(Ful):
        print('********')
        idx
        table
    Fulham = Ful[1]
    Fulham = Fulham[Fulham['Rf'].notna()]



    ############LeedsUnited#########
    Leu = pd.read_html("https://fbref.com/it/squadre/5bfb9659/Statistiche-Leeds-United#stats_standard_9")
    for idx,table in enumerate(Leu):
        print('********')
        idx
        table
    LeedsUnited = Leu[1]
    LeedsUnited = LeedsUnited[LeedsUnited['Rf'].notna()]




    ########Leicester City###########
    Lec = pd.read_html("https://fbref.com/it/squadre/a2d435b3/Statistiche-Leicester-City#stats_standard_9")
    for idx,table in enumerate(Lec):
        print('********')
        idx
        table
    LeicesterCity = Lec[1]
    LeicesterCity = LeicesterCity[LeicesterCity['Rf'].notna()]


    ##############Liverpool
    Liv = pd.read_html("https://fbref.com/it/squadre/fd962109/Statistiche-Fulham#stats_standard_9")
    for idx,table in enumerate(Liv):
        print('********')
        idx
        table
    Liverpool = Liv[1]
    Liverpool = Liverpool[Liverpool['Rf'].notna()]




    ###########ManchesterCity
    Mac = pd.read_html("https://fbref.com/it/squadre/fd962109/Statistiche-Fulham#stats_standard_9")
    for idx,table in enumerate(Mac):
        print('********')
        idx
        table
    ManchesterCity = Mac[1]
    ManchesterCity = ManchesterCity[ManchesterCity['Rf'].notna()]


    #Manchester Utd
    Mau = pd.read_html("https://fbref.com/it/squadre/fd962109/Statistiche-Fulham#stats_standard_9")
    for idx,table in enumerate(Mau):
        print('********')
        idx
        table
    ManchesterUtd = Mau[1]
    ManchesterUtd = ManchesterUtd[ManchesterUtd['Rf'].notna()]


    #Newcastle Utd
    Neu = pd.read_html("https://fbref.com/it/squadre/fd962109/Statistiche-Fulham#stats_standard_9")
    for idx,table in enumerate(Neu):
        print('********')
        idx
        table
    NewcastleUtd = Neu[1]
    NewcastleUtd = NewcastleUtd[NewcastleUtd['Rf'].notna()]


    #Nott'hamForest
    Nof = pd.read_html("https://fbref.com/it/squadre/fd962109/Statistiche-Fulham#stats_standard_9")
    for idx,table in enumerate(Nof):
        print('********')
        idx
        table
    NotthamForest = Nof[1]
    NotthamForest = NotthamForest[NotthamForest['Rf'].notna()]


    #Southampton
    Sou = pd.read_html("https://fbref.com/it/squadre/fd962109/Statistiche-Fulham#stats_standard_9")
    for idx,table in enumerate(Sou):
        print('********')
        idx
        table
    Southampton = Sou[1]
    Southampton = Southampton[Southampton['Rf'].notna()]


    #Tottenham
    Tot = pd.read_html("https://fbref.com/it/squadre/fd962109/Statistiche-Fulham#stats_standard_9")
    for idx,table in enumerate(Tot):
        print('********')
        idx
        table
    Tottenham = Sou[1]
    Tottenham = Tottenham[Tottenham['Rf'].notna()]

    #WestHam
    Weh = pd.read_html("https://fbref.com/it/squadre/fd962109/Statistiche-Fulham#stats_standard_9")
    for idx,table in enumerate(Weh):
        print('********')
        idx
        table
    WestHam = Weh[1]
    WestHam = WestHam[WestHam['Rf'].notna()]

    #Wolves
    Wel = pd.read_html("https://fbref.com/it/squadre/fd962109/Statistiche-Fulham#stats_standard_9")
    for idx,table in enumerate(Wel):
        print('********')
        idx
        table
    Wolves = Wel[1]
    Wolves = Wolves[Wolves['Rf'].notna()]
def LaLiga():
    import pandas as pd
    ##Almería
    Alm = pd.read_html("https://fbref.com/it/squadre/78ecf4bb/Statistiche-Almeria#stats_standard_12")
    for idx,table in enumerate(Alm):
        print('********')
        idx
        table
    Almeria = Alm[1]
    Almeria = Almeria[Almeria['Rf'].notna()]


    #Athletic Club
    Ath = pd.read_html("https://fbref.com/it/squadre/2b390eca/Statistiche-Athletic-Club#stats_standard_12")
    for idx,table in enumerate(Ath):
        print('********')
        idx
        table
    AthleticClub = Ath[1]
    AthleticClub = AthleticClub[AthleticClub['Rf'].notna()]

    #Atlético Madrid
    Atl = pd.read_html("https://fbref.com/it/squadre/db3b9613/Statistiche-Atletico-Madrid#stats_standard_12")
    for idx,table in enumerate(Atl):
        print('********')
        idx
        table
    AtleticoMadrid = Atl[1]
    AtleticoMadrid = AtleticoMadrid[AtleticoMadrid['Rf'].notna()]

    #Barcelona
    Bar = pd.read_html("https://fbref.com/it/squadre/206d90db/Statistiche-Barcelona#stats_standard_12")
    for idx,table in enumerate(Bar):
        print('********')
        idx
        table
    Barcelona = Bar[1]
    Barcelona = Barcelona[Barcelona['Rf'].notna()]

    #Betis
    Bet = pd.read_html("https://fbref.com/it/squadre/fc536746/Statistiche-Real-Betis#stats_standard_12")
    for idx,table in enumerate(Bet):
        print('********')
        idx
        table
    Betis = Bet[1]
    Betis = Betis[Betis['Rf'].notna()]



    #Cádiz
    Cad = pd.read_html('https://fbref.com/it/squadre/ee7c297c/Statistiche-Cadiz#stats_standard_12')
    for idx,table in enumerate(Cad):
        print('********')
        idx
        table
    Cadiz = Cad[1]
    Cadiz = Cadiz[Cadiz['Rf'].notna()]

    #Celta Vigo
    Cel = pd.read_html('https://fbref.com/it/squadre/f25da7fb/Statistiche-Celta-Vigo#stats_standard_12')
    for idx,table in enumerate(Cel):
        print('********')
        idx
        table
    CeltaVigo = Cel[1]
    CeltaVigo = CeltaVigo[CeltaVigo['Rf'].notna()]


    #Elche
    Elc = pd.read_html('https://fbref.com/it/squadre/6c8b07df/Statistiche-Elche#stats_standard_12')
    for idx,table in enumerate(Elc):
        print('********')
        idx
        table
    Elche = Elc[1]
    Elche = Elche[Elche['Rf'].notna()]


    #Espanyol
    Esp = pd.read_html('https://fbref.com/it/squadre/a8661628/Statistiche-Espanyol#stats_standard_12')
    for idx,table in enumerate(Esp):
        print('********')
        idx
        table
    Espanyol = Esp[1]
    Espanyol = Espanyol[Espanyol['Rf'].notna()]


    #Getafe
    Get = pd.read_html('https://fbref.com/it/squadre/7848bd64/Statistiche-Getafe#stats_standard_12')
    for idx,table in enumerate(Get):
        print('********')
        idx
        table
    Getafe = Get[1]
    Getafe = Getafe[Getafe['Rf'].notna()]

    #Girona
    Gir = pd.read_html('https://fbref.com/it/squadre/9024a00a/Statistiche-Girona#stats_standard_12')
    for idx,table in enumerate(Gir):
        print('********')
        idx
        table
    Girona = Gir[1]
    Girona = Girona[Girona['Rf'].notna()]


    #Mallorca
    Mal = pd.read_html('https://fbref.com/it/squadre/2aa12281/Statistiche-Mallorca#stats_standard_12')
    for idx,table in enumerate(Mal):
        print('********')
        idx
        table
    Mallorca = Mal[1]
    Mallorca = Mallorca[Mallorca['Rf'].notna()]

    #Osasuna
    Osa = pd.read_html('https://fbref.com/it/squadre/03c57e2b/Statistiche-Osasuna#stats_standard_12')
    for idx,table in enumerate(Osa):
        print('********')
        idx
        table
    Osasuna = Osa[1]
    Osasuna = Osasuna[Osasuna['Rf'].notna()]

    #Rayo Vallecano
    Ray = pd.read_html('https://fbref.com/it/squadre/98e8af82/Statistiche-Rayo-Vallecano#stats_standard_12')
    for idx,table in enumerate(Ray):
        print('********')
        idx
        table
    RayoVallecano = Ray[1]
    RayoVallecano = RayoVallecano[RayoVallecano['Rf'].notna()]


    #Real Madrid
    Rea = pd.read_html('https://fbref.com/it/squadre/53a2f082/Statistiche-Real-Madrid#stats_standard_12')
    for idx,table in enumerate(Rea):
        print('********')
        idx
        table
    RealMadrid = Rea[1]
    RealMadrid = RealMadrid[RealMadrid['Rf'].notna()]

    #Real Sociedad
    Res = pd.read_html('https://fbref.com/it/squadre/e31d1cd9/Statistiche-Real-Sociedad#stats_standard_12')
    for idx,table in enumerate(Res):
        print('********')
        idx
        table
    RealSociedad = Res[1]
    RealSociedad = RealSociedad[RealSociedad['Rf'].notna()]

    #Sevilla
    Sev = pd.read_html('https://fbref.com/it/squadre/ad2be733/Statistiche-Sevilla#stats_standard_12')
    for idx,table in enumerate(Sev):
        print('********')
        idx
        table
    Sevilla = Sev[1]
    Sevilla = Sevilla[Sevilla['Rf'].notna()]

    #Valencia
    Val = pd.read_html('https://fbref.com/it/squadre/dcc91a7b/Statistiche-Valencia#stats_standard_12')
    for idx,table in enumerate(Val):
        print('********')
        idx
        table
    Valencia = Val[1]
    Valencia = Valencia[Valencia['Rf'].notna()]

    #Valladolid
    Vad = pd.read_html('https://fbref.com/it/squadre/17859612/Statistiche-Valladolid#stats_standard_12')
    for idx,table in enumerate(Vad):
        print('********')
        idx
        table
    Valladolid = Vad[1]
    Valladolid = Valladolid[Valladolid['Rf'].notna()]

    #Villarreal
    Vil = pd.read_html('https://fbref.com/it/squadre/2a8183b3/Statistiche-Villarreal#stats_standard_12')
    for idx,table in enumerate(Vil):
        print('********')
        idx
        table
    Villarreal = Vil[1]
    Villarreal = Villarreal[Villarreal['Rf'].notna()]


#Librerie
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson 
from statistics import median
from matplotlib import pyplot

#Funzioni 
#For calcolate median and calcolate a diff. Home/Away
def unopuntozero(data1,data2):
    from statistics import median
    print("Mediana Casa")
    i_fatti = median(data1["Rf"])
    i_subiti = median(data1["Rs"])
    print("Fatti Casa: ",i_fatti)
    print("Subiti Casa: ",i_subiti)
    from statistics import median
    print("Mediana Ospiti")
    y_fatti = median(data2["Rf"])
    y_subiti = median(data2["Rs"])
    print("Fatti Ospiti",y_fatti)
    print("Subiti Ospiti",y_subiti)
    casa_dif = i_fatti - y_subiti 
    ospiti_dif = y_fatti - i_subiti 
    import numpy as np
    print('Diferenza tra fatti e subiti')
    risultato = np.array([[casa_dif, ospiti_dif]])
    print(risultato)
#Use poassion for calcolate probability 
def irene2(data1, data2):
    from scipy.stats import poisson 
    from statistics import median
    i_fatti = median(data1["Rf"])
    i_subiti = median(data1["Rs"])
    y_fatti = median(data2["Rf"])
    y_subiti = median(data2["Rs"])
    # goals_scored * goals_conceded
    lamb_home = i_fatti * y_subiti
    lamb_away = y_fatti * i_subiti
    prob_home, prob_away, prob_draw = 0, 0, 0
    for x in range(0,5): #number of goals home team
        for y in range(0, 5): #number of goals away team
            p = poisson.pmf(x, lamb_home) * poisson.pmf(y, lamb_away)
            if x == y:
                prob_draw += p
            elif x > y:
                prob_home += p
            else:
                prob_away += p

    points_home = 3 * prob_home + prob_draw
    points_away = 3 * prob_away + prob_draw
    return (points_home, points_away)
#Grafici
#Grafico per reti fatte e subite 
def graph_diff(data1,data2):    
    from matplotlib import pyplot

    x = data1['Rf']
    y = data2['Rf']

    pyplot.hist(x, alpha=0.5, label='Casa')
    pyplot.hist(y, alpha=0.5, label='Trasferta')
    pyplot.legend(loc='upper right')
    pyplot.title("Reti Fatte")
    pyplot.show()

    z = data1['Rs']
    i = data2['Rs']

    pyplot.hist(z, alpha=0.5, label='Casa')
    pyplot.hist(i, alpha=0.5, label='Trasferta')
    pyplot.legend(loc='upper right')
    pyplot.title("Reti Subite")
    pyplot.show()
#Torta per frequenza esito incontri 
def freq(data1, data2):
    from matplotlib import pyplot
    freq_tabli = pd.crosstab(data1['Risultato'], 'n di esiti')
    op = ['N','P','V']
    plt.pie(freq_tabli['n di esiti'], labels=op , autopct='%1.1f%%')
    plt.title("Esiti Casa")
    plt.show()
    
    from matplotlib import pyplot
    freq_table = pd.crosstab(data2['Risultato'], 'n di esiti')
    op = ['N','P','V']
    plt.pie(freq_table['n di esiti'], labels=op , autopct='%1.1f%%')
    plt.title("Esiti Ospiti")
    plt.show()

def analisi(data1, data2):
    print("""                                                   
   (            (        (            (            
   )\      (    )\ )     )\           )\ )     (   
 (((_)    ))\  (()/(   (((_)    (    (()/(    ))\  
 )\___   /((_)  /(_))  )\___    )\    ((_))  /((_) 
((/ __| (_))   (_) _| ((/ __|  ((_)   _| |  (_))   
 | (__  / -_)   |  _|  | (__  / _ \ / _` |  / -_)  
  \___| \___|   |_|     \___| \___/ \__,_|  \___|  
    """)
    print("""

/$$      /$$           /$$                                            
| $$  /$ | $$          | $$                                            
| $$ /$$$| $$  /$$$$$$ | $$  /$$$$$$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$ 
| $$/$$ $$ $$ /$$__  $$| $$ /$$_____/ /$$__  $$| $$_  $$_  $$ /$$__  $$
| $$$$_  $$$$| $$$$$$$$| $$| $$      | $$  \ $$| $$ \ $$ \ $$| $$$$$$$$
| $$$/ \  $$$| $$_____/| $$| $$      | $$  | $$| $$ | $$ | $$| $$_____/
| $$/   \  $$|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$ | $$ | $$|  $$$$$$$
|__/     \__/ \_______/|__/ \_______/ \______/ |__/ |__/ |__/ \_______/


.___________. ______   
|           |/  __  \  
`---|  |----|  |  |  | 
    |  |    |  |  |  | 
    |  |    |  `--'  | 
    |__|     \______/  



 __  .______      _______ .__   __.  _______ ____          ___   
|  | |   _  \    |   ____||  \ |  | |   ____|___ \        / _ \  
|  | |  |_)  |   |  |__   |   \|  | |  |__    __) |      | | | | 
|  | |      /    |   __|  |  . `  | |   __|  |__ <       | | | | 
|  | |  |\  \----|  |____ |  |\   | |  |____ ___) |      | |_| | 
|__| | _| `._____|_______||__| \__| |_______|____/ ______ \___/  
                                                  |______|     
               

    """)

    print('*GRAFICI*')
    graph_diff(data1, data2)
    freq(data1, data2)
    print('*Differenza della mediana statistica tra reti fatte e reti subite')
    unopuntozero(data1, data2)
    print('*Probabilità del numero di gol *')
    print(irene2(data1, data2))

from time import sleep
from tqdm import tqdm

print("data update:!")
Sq_casa = input("Squadra in casa: ")
Sq_away = input("Squadra furoicasa: ")
analisi(Sq_casa, Sq_away)
