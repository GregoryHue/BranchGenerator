import random


def generate_branch():
    branch = []
    branch.append([])
    for i in range(0, 5):
        branch = generate_sub_branch(branch)


    return branch

def generate_sub_branch(branch):
    for x in branch:
        x.append([])
    return branch