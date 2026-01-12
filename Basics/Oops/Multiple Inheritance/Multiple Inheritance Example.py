class Father:
    def skills(self):
        print("Father's skills are : Badminton Player")
class Mother:
    def mother_skills(self):
        print("Mother's skills are : Artist")
class Child(Father,Mother):
    def skills(self):
        super().skills()
        print("Child skills are : Singer")
child1=Child()
child1.skills()# imp:In this inheritance, if method with same name exist in same classes either of one is executed and other would be discarded
child1.mother_skills()
