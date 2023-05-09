class DataType:
    def __init__(self):
        pass
    
    def get_info(self):
        pass


class PrimitiveType(DataType):
    def __init__(self):
        super().__init__()
        self.name = ""
    
    def get_info(self):
        pass


class NumberType(PrimitiveType):
    def __init__(self):
        super().__init__()
        self.min_value = 0
        self.max_value = 0
    
    def get_info(self):
        pass


class StringType(PrimitiveType):
    def __init__(self):
        super().__init__()
        self.length = 0
    
    def get_info(self):
        pass


class ContainerType(DataType):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.elements = []
    
    def add_element(self, element):
        pass
    
    def remove_element(self, element):
        pass
    
    def get_info(self):
        pass


class ListType(ContainerType):
    def __init__(self):
        super().__init__()
        self.length = 0
    
    def get_info(self):
        pass


class DictionaryType(ContainerType):
    def __init__(self):
        super().__init__()
        self.key_type = None
        self.value_type = None
    
    def get_info(self):
        pass
