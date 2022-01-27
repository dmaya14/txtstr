# PingüiMaya. Open SourceCode
# https://bit.ly/pinguimaya


class txtstr:
    def __init__(self):
        pass

    def write(self,text,name):
        name = str(name)
        name = name + ".txt"
        file = open(name, "w")
        file.write(text)
        file.close()

    def read(self,rute):
        with open(rute, "r") as archive:
            for line in archive:
                print(line)

    def transcript(self,rute,new_name):
        with open(rute, "r") as archive:
            name = str(new_name)
            name = name + ".txt"
            file = open(name, "w")

            for line in archive:
                file.write(line)

            file.close()




