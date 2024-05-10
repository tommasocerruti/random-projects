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

import re

def escape_single_quotes(text):
    if pd.isna(text) or isinstance(text, float):
        return text
    else:
        return re.sub(r"'", r"\'", str(text))

def main():
    file_csv_input = 'comuni_archivio.csv'
    file_csv_output = 'coppie_univoche.csv'
    coppie = estrai_coppie_univoche(file_csv_input)

    # Filter out entries where 'SIGLAPROVINCIA' is NaN
    coppie = coppie.dropna(subset=['SIGLAPROVINCIA'])

    # Apply escape_single_quotes function to both columns
    coppie['DENOMINAZIONE_IT'] = coppie['DENOMINAZIONE_IT'].apply(escape_single_quotes)
    coppie['SIGLAPROVINCIA'] = coppie['SIGLAPROVINCIA'].apply(escape_single_quotes)

    # Format the output string with single quotes
    coppie_formatted = []

    for index, row in coppie.iterrows():
        denominazione = row['DENOMINAZIONE_IT']
        sigla = row['SIGLAPROVINCIA']
        formatted_entry = f"'{denominazione} ({sigla})',"
        coppie_formatted.append(formatted_entry)

    # Write the formatted output to a CSV file
    with open(file_csv_output, 'w') as file:
        file.write("DENOMINAZIONE(SIGLAPROVINCIA)\n")
        for item in coppie_formatted:
            file.write("%s\n" % item)
    
    print(f"Coppie univoche salvate in '{file_csv_output}'.")




if __name__ == "__main__":
    main()
