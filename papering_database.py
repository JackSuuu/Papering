

class PaperData:
    def __init__(self):
        self.year_base = 2000
        self.year_lis = []
        self.subject_lis = ["Mathematics",
                            "Further_Math",
                            "Computer Science(old)",
                            "Computer Science(new)",
                            "Physics",
                            "Sociology",
                            "Psychology",
                            "Economics",
                            "Business",
                            "Accounting",
                            "Biology",
                            "Geography",
                            "History(new)",
                            "History(old)"]

    def year(self):
        for i in range(22):
            self.year_base += 1
            self.year_lis.append(str(self.year_base))
        return self.year_lis

    def subject(self):
        return self.subject_lis




