import datetime
class Functions:
    def __init__(self):
        pass
    def displ(self, enteryourname):
        getName = str(enteryourname)
        statement = "Assalam-O-Alaikum "+getName+"."
        return statement

    def getInputFromUser(self, enterStatement='Hello'):
        dT = str(input(enterStatement))
        return dT

    def namazCalculator(self, birth_year):
    
        """
        This function calculates the namaz for you, according your age.
        You have to enter your birth year in order to correctly calculate it.
        Fajar: 2 Frz
        Zohar: 4 Frz
        Asr: 4 Frz
        Magrib: 3 Frz
        Isha: 4 Frz, 3 Watir
        """
        
        getBirthYear = int(birth_year)
        
        your_age = int((datetime.date.today().year - (getBirthYear + 7)))
        namaz = {
            'fajar_frz': float((((2 * 30) * 12) * your_age)), # Total namaz for Total Age
            'zohar_frz': float((((4 * 30) * 12) * your_age)), # Total namaz for Total Age
            'asr_frz': float((((4 * 30) * 12) * your_age)), # Total namaz for Total Age
            'magrib_frz': float((((3 * 30) * 12) * your_age)), # Total namaz for Total Age
            'isha_frz': float((((4 * 30) * 12) * your_age)), # Total namaz for Total Age
            'isha_watir': float((((3 * 30) * 12) * your_age)), # Total namaz for Total Age
        }
        done = {
            "fajar_frz": float((int(self.getInputFromUser("How many you have done namazs till now: ")) * int(self.getInputFromUser("Since how many days you are reciting pending namazs: ")))), # (4 * 7 )Done Reciting Namaz
            "zohar_frz": float((int(self.getInputFromUser("How many you have done namazs till now: ")) * int(self.getInputFromUser("Since how many days you are reciting pending namazs: ")))), # (8 * 1) Done Reciting Namaz
            "asr_frz": float((int(self.getInputFromUser("How many you have done namazs till now: ")) * int(self.getInputFromUser("Since how many days you are reciting pending namazs: ")))), # (8 * 1) Done Reciting Namaz
            "magrib_frz": float((int(self.getInputFromUser("How many you have done namazs till now: ")) * int(self.getInputFromUser("Since how many days you are reciting pending namazs: ")))), # (6 * 1) Done Reciting Namaz
            "isha_frz": float((int(self.getInputFromUser("How many you have done namazs till now: ")) * int(self.getInputFromUser("Since how many days you are reciting pending namazs: ")))), # (8 * 1) Done Reciting Namaz
            "isha_watir": float((int(self.getInputFromUser("How many you have done namazs till now: ")) * int(self.getInputFromUser("Since how many days you are reciting pending namazs: ")))), # (6 * 1) Done Reciting Namaz
        }
        for n in namaz:
            pending = float(namaz[n] - done[n]) # Remaining Namaz
            minimum = float((namaz[n] - done[n]) / your_age) # Per Year Rakaths
            total_month = float((minimum / 12)) # Per Month Rakaths
            total_daY = float((total_month / 30)) # Per Day Limit.
            
            # Calculations OutPut
            print(n, "=", round(namaz[n]) , "rakat namaz for the durtion of",round(your_age),"years.")
            print("Completed Now: ",round(done[n]), "rakat namaz.")
            print("Complete", round(pending) , "more rakat namaz.")
            print("Recite Minimum: ", round(minimum), " Namaz per year.")
            print("Total Per Month Namaz: ", round(total_month))
            print("Namaz Per Day: ", round(total_daY))
            print("\n")
            
    def costCalculator(self, total_price = 0.00, total_quantity = 0.00):
        get_total_price = float(total_price)
        get_total_quantity = float(total_quantity)
        price_per_item = float(get_total_price / get_total_quantity)
        return (price_per_item)

    def __del__(self):

        print("Goodbye")
        