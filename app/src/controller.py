import random


def generate_branch():
    percent_sub_branch = 25
    max_level = 3
    max_branch_size = 5
    points = 30

    branch = []

    i = 0
    while i < points:
        # Generate the main branch
        if random.randint(0, 100) <= percent_sub_branch and i != 0:
            branch, i = sub_branch(branch, max_level, i,
                                   max_branch_size, percent_sub_branch, points)
        else:
            branch.append(i)
            i = i + 1

    return branch


# Generate sub branches, recursively
def sub_branch(branch, max_level, begin_branch, max_branch_size, percent_sub_branch, points):

    branch_size = random.randint(1, max_branch_size)

    # Avoid going above "points"
    if (branch_size + begin_branch) > points:
        branch_size = points - begin_branch

    new_branch = []

    j = begin_branch
    while j < (begin_branch + branch_size):

        if max_level > 0 and random.randint(0, 100) <= percent_sub_branch:
            new_branch, j = sub_branch(
                new_branch, max_level-1, j, max_branch_size, percent_sub_branch, points)
        else:
            new_branch.append(j)
            j = j + 1

    branch.append(new_branch)

    return branch, j
