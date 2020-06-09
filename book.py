class Book():
    def __init__(self, name = None, authorName = None, memberLegajo = None):
        self._name = name
        self._authorName = authorName
        self._memberLegajo = memberLegajo

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name.upper()

    @property
    def authorName(self):
        return self._authorName
    
    @authorName.setter
    def authorName(self, authorNam):
        self._authorName = authorName.upper()

    @property
    def memberLegajo(self):
        return self._memberLegajo
    
    @memberLegajo.setter
    def memberLegajo(self, value):
        self._memberLegajo = value

    def __str__(self):
        string = '('
        string += str(self.name)
        string += ', '
        string += str(self.authorName)
        string += ', '
        string += str(self.memberLegajo)
        string += ')'
        return string