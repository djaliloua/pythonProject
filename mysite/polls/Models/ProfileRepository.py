from Model import Profile


class Repository:
    def __init__(self):
        self.GetAll = [
            Profile(0, "ali", "fouseni", "my..", "/profiles/1.png"),
            Profile(1, "alessio", "abdou", "Some example text some example text. John Doe is an architect and engineer", "/profiles/1.png"),
            Profile(2, "gianluca", "djalilou", "my..", "/profiles/1.png"),
            Profile(3, "razak", "baraka", "my..", "/profiles/1.png"),
            Profile(4, "fadil", "awawou", "my..", "/profiles/1.png"),
            Profile(5, "rahaman", "shafatou", "my..", "/profiles/1.png"),
            Profile(6, "youssouf", "papa", "my..", "/profiles/1.png"),
            Profile(7, "abass", "moussa", "my..", "/profiles/1.png"),
        ]

    def getbyid(self, id):
        for p in self.GetAll:
            if id == p.Id:
                return p


if __name__ == "__main__":
    repository = Repository()
    profile = repository.getbyid(2)
    print(profile.Id, profile.FullName())
