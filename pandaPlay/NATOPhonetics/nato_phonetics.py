import pandas as pd


class NATOPhonetics:
    def __init__(self, filename):
        self.phonetics_df = pd.read_csv(filename)

    def name_to_code(self, name):
        return [self.phonetics_df[self.phonetics_df.letter == char.upper()].iloc[0]['code'] for char in name]


if __name__ == '__main__':
    NATO_PHONETICS_FILE = "nato_phonetic_alphabet.csv"
    nato_phonetics = NATOPhonetics(NATO_PHONETICS_FILE)

    while True:
        name = input('Please input your name:')
        code_list = nato_phonetics.name_to_code(name)
        print(code_list)
