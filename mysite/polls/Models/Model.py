class Profile:
    def __init__(self, id, FirstName, LastName, Description, image):
        self.Id = id
        self.FirstName = FirstName
        self.LastName = LastName
        self.Description = Description
        self.image = image

    def FullName(self):
        return self.FirstName + " " + self.LastName