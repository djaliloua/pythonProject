from models import Profile

data = Profile.objects.create(
    firstname="Ali",
    lastname="Abdou-Djalilou",
    description="hello, i am Engineer",
    photo="C:\\Users\\djali\\PycharmProjects\\pythonProject\\mysite\\static\\profiles\\1.jpg",
)

if __name__ == "__main__":
    data.save()
