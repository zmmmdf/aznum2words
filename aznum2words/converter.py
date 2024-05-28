class AzerbaijaniNumberConverter:
    def __init__(self):
        self.units = ['', 'bir', 'iki', 'üç', 'dörd', 'beş', 'altı', 'yeddi', 'səkkiz', 'doqquz']
        self.tens = ['', 'on', 'iyirmi', 'otuz', 'qırx', 'əlli', 'altmış', 'yetmiş', 'səksən', 'doxsan']
        self.hundreds = ['', 'yüz', 'iki yüz', 'üç yüz', 'dörd yüz', 'beş yüz', 'altı yüz', 'yeddi yüz', 'səkkiz yüz', 'doqquz yüz']
        self.thousands = ['', 'min', 'milyon', 'milyard', 'trilyon', 'kvadrilyon', 'kintilyon', 'sekstilyon', 'septilyon', 'oktilyon', 'nonilyon']  
        self.large_number_groups = ['deqad', 'yüzqatı', 'mingqatı', 'milyonqatı', 'milyardqatı', 'trilyonqatı', 'kvadrilyonqatı', 'kintilyonqatı', 'sekstilyonqatı', 'septilyonqatı', 'oktilyonqatı', 'nonilyonqatı']

    def convert(self, number):
        if number == 0:
            return "sıfır"
        
        result = ''
        
        if number < 0:
            result = "mənfi "
            number = abs(number)
        
        chunk_count = 0
        while number > 0:
            chunk = number % 1000
            if chunk != 0:
                chunk_str = self.convert_chunk(chunk)
                if chunk_count > 0:
                    chunk_str = chunk_str + ' ' + self.thousands[chunk_count]
                result = chunk_str + ' ' + result
            number //= 1000
            chunk_count += 1

        return result.strip()

    def convert_chunk(self, number):
        # Convert a chunk of maximum 3 digits into Azerbaijani words
        result = ''
        
        # Handle hundreds
        if number >= 100:
            result += self.hundreds[number // 100] + ' '
            number %= 100

        # Handle tens and ones
        if number >= 10:
            if number < 20:
                # Handle special cases from 10 to 19
                result += self.units[number % 10] + ' on'
                return result.strip()
            else:
                result += self.tens[number // 10] + ' '
                number %= 10

        if number > 0:
            result += self.units[number]

        return result.strip()
