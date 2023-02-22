from typing import Union
from bytesReader.bytesFormater import Formater

class DataArea:
    def __init__(self, byteArray:Union[list[bytes], tuple[bytes], set[bytes]]) -> None:
        self.byteArray = byteArray
        self.formater = Formater()
    