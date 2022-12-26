def serieA():
    import pandas as pd
    #"#############ATALANTA#############"
    Ata = pd.read_html("https://fbref.com/it/squadre/922493f3/Statistiche-Atalanta#matchlogs_for")
    for idx,table in enumerate(Ata):
        idx
        table
    Atalanta = Ata[1]
    Atalanta = Atalanta[Atalanta['Rf'].notna()]
    Atalanta.to_csv('~/Desktop/irene3.0/Data/SerieA/Atalanta.csv') 
    return Atalanta



