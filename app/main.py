class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict[str, str | int]]) -> list[Person]:
    person_list = []

    # Перший цикл: створення екземплярів
    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        person = Person(name, age)
        person_list.append(person)

    # Другий цикл: встановлення wife і husband
    for person_dict in people:
        person = Person.people[person_dict["name"]]
        if wife_name := person_dict.get("wife"):
            wife = Person.people.get(wife_name)
            person.wife = wife
            if wife:
                wife.husband = person
        if husband_name := person_dict.get("husband"):
            husband = Person.people.get(husband_name)
            person.husband = husband
            if husband:
                husband.wife = person

    return person_list
