class Solution:

    def encode(self, strs: List[str]) -> str:
        # create empty string
        # Iterate through each word and add it to the string
        # Somehow place a marker in between each word so that they remain separated
        encoded_string = ""
        for s in strs:
            for char in s:
                encoded_string += ''.join(char)
            encoded_string += ''.join(chr(128))
        #just memorize that ascii characters range from hex values 0 to 127
        return encoded_string

    def decode(self, s: str) -> List[str]:
        #Take in that long string and each marker you know you have a word
        # create list of words
        decoded_strs = []
        current_str = ""
        for char in s:
            if char.isascii():
                current_str += ''.join(char)
            if not char.isascii():
                decoded_strs.append(current_str)
                current_str = ""
        return decoded_strs

