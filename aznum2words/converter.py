class AzerbaijaniNumberConverter:
    def __init__(self):
        self.units = ["", "bir", "iki", "üç", "dörd", "beş", "altı", "yeddi", "səkkiz", "doqquz"]
        self.tens = ["", "on", "iyirmi", "otuz", "qırx", "əlli", "altmış", "yetmiş", "səksən", "doxsan"]
        self.hundreds = ["", "yüz", "iki yüz", "üç yüz", "dörd yüz", "beş yüz", "altı yüz", "yeddi yüz", "səkkiz yüz", "doqquz yüz"]
        self.thousands = ["", "min", "milyon", "milyard", "trilyon", "kvadrilyon", "kintilyon"]
        self.negword = "mənfi"
        self.pointword = "tam"

    def convert_integer(self, number):
        if number == 0:
            return "sıfır"
        
        parts = []
        group = 0

        while number > 0:
            n = number % 1000
            if n != 0:
                parts.append(self.convert_three_digits(n) + (f" {self.thousands[group]}" if group > 0 else ""))
            number //= 1000
            group += 1
        
        return " ".join(reversed(parts))

    def convert_three_digits(self, number):
        hundred = number // 100
        ten = (number % 100) // 10
        unit = number % 10

        parts = []
        if hundred > 0:
            parts.append(self.hundreds[hundred])
        if ten > 0:
            parts.append(self.tens[ten])
        if unit > 0:
            parts.append(self.units[unit])
        
        return " ".join(parts)

    def convert_fraction(self, number):
        fraction_units = ['', 'onda', 'yüzdə', 'mində', 'on mində', 'yüz mində', 'milyonda', 'on milyonda']
        fraction_str = str(number).split('.')[1]
        fractional_length = len(fraction_str)
        
        if fractional_length >= len(fraction_units):
            raise ValueError("Fractional part length exceeds supported precision.")

        fractional_value = int(fraction_str)
        return fraction_units[fractional_length] + ' ' + self.convert_integer(fractional_value)

    def convert(self, number):
        if isinstance(number, str):
            number = float(number)
        else:
            number = float(str(number))

        if number < 0:
            return self.negword + " " + self.convert(-number)
        
        integer_part = int(number)
        fractional_part = number - integer_part

        result = self.convert_integer(integer_part)
        if fractional_part > 0:
            # Round the fractional part to two decimal places
            fractional_part = round(fractional_part, 7)
            result += " " + self.pointword + " " + self.convert_fraction(fractional_part)
        
        return result
