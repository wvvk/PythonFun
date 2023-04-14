import os


class LetterAutomator:
    def __init__(self):
        self.invited_guests = []

    def read_inivited(self, file_name):
        try:
            with open(file_name) as file:
                self.invited_guests = file.readlines()
                self.invited_guests = [guest.strip('\n') for guest in self.invited_guests]
                print(self.invited_guests)
        except:
            print("Error: missing invited names file ")

    def create_send_folder(self):
        os.makedirs(INVITATION_FOLDER, exist_ok=True)

    def read_template(self):
        try:
            with open(TEMPLATE_LETTER) as file:
                self.template_letter = file.read()
        except:
            print("missing starting letter")

    def create_letters(self):
        for name in self.invited_guests:
            self.create_letter(name, self.template_letter)

    def create_letter(self, name, template_letter):
        try:
            with open(f"{INVITATION_FOLDER}/{name}_invite.txt", "w") as file:
                file.write(template_letter.replace(PLACEHODER, name))
        except:
            print("error opening file to write letters")

PLACEHODER = "[name]"
path = "."
GUESTLIST_FOLDER = "Input/Names"
TEMPLATE_LETTER_FOLDER = "Input/Letters"
GUESTLIST = os.path.join(path, GUESTLIST_FOLDER,"invited_names.txt")
INVITATION_FOLDER = os.path.join(path, "ReadyToSend")
TEMPLATE_LETTER = os.path.join(path,TEMPLATE_LETTER_FOLDER, "starting_letter.txt")

my_letter_robot = LetterAutomator()
my_letter_robot.read_inivited(GUESTLIST)
my_letter_robot.create_send_folder()
my_letter_robot.read_template()
my_letter_robot.create_letters()
