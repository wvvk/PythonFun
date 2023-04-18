import pandas as pd

NATO_PHONETICS_FILE = "nato_phonetic_alphabet.csv"
phonetics_df = pd.read_csv(NATO_PHONETICS_FILE)

while True:
    name = input('Please input your name:')
    # for char in name:
    #     row =phonetics_df[phonetics_df.letter == char.upper()]
    #     print(row)
    #     code=row.iloc[0]['code']
    #     print(f"for {char} gives {code}")

    code_list = [phonetics_df[phonetics_df.letter == char.upper()].iloc[0]['code'] for char in name]
    print(code_list)
