import pandas as pd

man = pd.read_csv("Data/man.csv")
kvinna = pd.read_csv("Data/kvinnor.csv")

man.rename(columns={"Antal Män 2020": "Antal 2020", "Antal Män 2019": "Antal 2019"}, inplace=True)
kvinna.rename(columns={"Antal kvinnor 2020": "Antal 2020", "Antal kvinnor 2019": "Antal 2019"}, inplace=True)
kvinna.rename(columns={"Förändring (%)": "Förändring"}, inplace=True)


df = pd.concat([man, kvinna], ignore_index=True)
df.set_index("Kommun", inplace=True)

