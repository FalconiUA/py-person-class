class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        person = Person(name, age)
        person_list.append(person)

    for person_dict in people:
        person = Person.people[person_dict["name"]]  # Отримуємо відповідний екземпляр
        if "wife" in person_dict and person_dict["wife"]:
            wife = Person.people.get(
                person_dict["wife"]
            )
            person.wife = wife
            if wife:
                wife.husband = person
        if "husband" in person_dict and person_dict["husband"]:
            husband = Person.people.get(
                person_dict["husband"]
            )
            person.husband = husband
            if husband:
                husband.wife = person

    return person_list
