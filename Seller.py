class Seller:
    signature_seller: bool = False
    def __init__(self, name: str, employee_id: str):
        self.__name = name
        self.__employee_id = employee_id

    @property
    def name(self):
        return self.__name

    @property
    def employee_id(self):
        return self.__employee_id

    def sign_document(self) -> bool:
        self.signature_seller = True
        return self.signature_seller
