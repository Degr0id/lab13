class Stud:
    def __init__(self, fields, widths=None):
        if widths is None:
            widths = [0, 0, 0, 0]
        self.name = fields[0].strip()
        self.year = fields[1].strip()
        self.res = fields[2].strip()
        self.passed = fields[3].strip()
        self.wname = widths[0]
        self.wyear = widths[1]
        self.wres = widths[2]
        self.wpassed = widths[3]

    def __str__(self):
        return f"{self.name.center(self.wname)}|{self.year.center(self.wyear)}|" \
               f"{self.res.center(self.wres)}|{self.passed.center(self.wpassed)}\n"

    def check_fields(self):
        part_name = self.name.split()
        if len(part_name) == 2:
            if not (part_name[0].isalpha() and part_name[0][0].isupper() and
                    len(part_name[1]) == 2 and part_name[1][0].isalpha() and
                    part_name[1][0].isupper() and part_name[1][1] == "."):
                return False
        else:
            return False
        if not (self.year.isdigit() and 1850 <= int(self.year) <= 2022):
            return False
        if not (self.res.isdigit() and 0 <= int(self.res) <= 100):
            return False
        if not (self.passed == "Да" or self.passed == "Нет"):
            return False
        return True
