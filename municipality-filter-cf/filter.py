import pandas as pd

def estrai_coppie_univoche(file_csv):
    # Carica il CSV in un DataFrame
    df = pd.read_csv(file_csv)

    # Filtra i dati in base ai criteri specificati (comuni che non esistevano quando il CF è nato)
    filtro = (df['DATACESSAZIONE'] > '1973-12-31') & (df['DATACESSAZIONE'].notnull())
    df_filtrato = df[filtro]

    # Estrae le coppie univoche di DENOMINAZIONE_IT e SIGLAPROVINCIA
    coppie_univoche = df_filtrato[['DENOMINAZIONE_IT', 'SIGLAPROVINCIA']].drop_duplicates()

    return coppie_univoche

def scrivi_su_csv(df, nome_file):
    # Scrive il DataFrame su un nuovo file CSV
    df.to_csv(nome_file, index=False)

def main():
    file_csv_input = 'comuni_archivio.csv'  # Inserisci il percorso del tuo file CSV
    file_csv_output = 'coppie_univoche.csv'  # Specifica il nome del file di output
    coppie = estrai_coppie_univoche(file_csv_input)
    scrivi_su_csv(coppie, file_csv_output)
    print(f"Coppie univoche salvate in '{file_csv_output}'.")

if __name__ == "__main__":
    main()
