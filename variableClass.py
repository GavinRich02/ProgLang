class variable:
    def __init__(s,name,value):
        s.name=name
        s.value=value
    def getName(s):
        return s.name
    def getValue(s):
        return s.value
    def setValue(s,newVal):
        s.value=newVal
