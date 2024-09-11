# -*- coding: utf-8 -*-
"""3A_VELINA_MP2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1x8ESkAMdft5F3MviZZ8vnYn-8YEq5Dct
"""

def and_(p, q):
    return p and q


def or_(p, q):
    return p or q

def not_(p):
    return not p

def implies_(p, q):
    return not p or q

p = True
q = False

print(f"AND: {and_(p, q)}")
print(f"OR: {or_(p, q)}")
print(f"NOT: {not_(p)}")
print(f"IMPLIES: {implies_(p, q)}")

def evaluate(statement, values):
    for proposition, truth_value in values.items():
        statement = statement.replace(proposition, str(truth_value))
    return eval(statement)

def evaluate(statement, values):

    for proposition, truth_value in values.items():

        statement = statement.replace(proposition, str(truth_value))


    statement = statement.replace("and", "&")
    statement = statement.replace("or", "|")
    statement = statement.replace("not", "~")

    return eval(statement)

def forall(predicate, domain):
    return all(predicate(x) for x in domain)

def exists(predicate, domain):
    return any(predicate(x) for x in domain)

domain = [1, 2, 3, 4]

predicate = lambda x: x > 0

print(f"For all x > 0: {forall(predicate, domain)}")
print(f"Exists x > 2: {exists(lambda x: x > 2, domain)}")

def ai_decision(environment_conditions):
    move = ""
    if and_(environment_conditions['is_safe'], environment_conditions['has_resources']):
        move = "Move Forward"
    elif not_(environment_conditions['is_safe']):
        move = "Stay"
    else:
        move = "Search for Resources"
    return move

environment_conditions = {
    'is_safe': True,
    'has_resources': False
}

print(f"AI Decision: {ai_decision(environment_conditions)}")
