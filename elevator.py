#! python3
# Sort given a list of revision numbers formated X.Y.Z, where
#   X = Major Revision
#   Y = Minor Revision
#   Z = Maintenance Revision
# each item in the list will have an X, but Y and Z are optional. If Z exists then Y exists.
# for items with identical number, give preference to the item with fewer elements.
#   IE: 1.2 will be before 1.2.0
# items are entered as strings
# Each revisions is turned into a list, with the major, minor, and maintenance number, as well as the full
# revisions number. Any blanks are turned into zeros
# Then add this to a new list, which is then sorted in the folloring order:
#   1) major
#   2) minor
#   3) maintenance
#   4) full
# this will sort by first numbers, then step 4 will sort the ones with and with out zeros in the minor and
# maintenance slots

from operator import attrgetter


class Revision:
    def __init__(self, full, major, minor, maintenance):
        self.full = full
        self.major = major
        self.minor = minor
        self.maintenance = maintenance

    def __repr__(self):
        return repr((self.full, self.major, self.minor, self.maintenance))


def answer(l):
    revisions = []
    for item in l:
        revisions.append(revision_split(item))
    revisions = sorted(revisions, key=attrgetter('major', 'minor', 'maintenance', 'full'))

    return new_list(revisions)

def revision_split(item):
    split_item = item.split('.')
    split_count = len(split_item)
    major = int(split_item[0])
    if split_count > 1:
        minor = int(split_item[1])
    else:
        minor = 0
    if split_count > 2:
        maintenance = int(split_item[2])
    else:
        maintenance = 0
    return Revision(item, major, minor, maintenance)

def new_list(l):
    n_l = []
    for items in l:
        n_l.append(items.full)
    return n_l

a = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
b = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]

print(answer(a))
print(answer(b))