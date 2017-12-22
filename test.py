class Revision:
    def __init__(self, major, minor, maintenance):
        self.major = major
        self.minor = minor
        self.maintenance = maintenance

    def __repr__(self):
        return repr((self.major, self.minor, self.maintenance))

student_objects = [
    Revision('john', 'A', 15),
    Revision('jane', 'B', 12),
    Revision('dave', 'B', 10),
]
print(sorted(student_objects, key=lambda student: student.maintenance))  # sort by maintenance
