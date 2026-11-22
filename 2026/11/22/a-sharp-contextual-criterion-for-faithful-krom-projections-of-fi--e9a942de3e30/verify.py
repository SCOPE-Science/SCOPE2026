"""Finite independent checks for context-preserving unary Horn projections."""
from itertools import combinations, product
from random import Random


def least_model(program, facts=frozenset()):
    current = set(facts)
    while True:
        new = current | {h for h, body in program if body <= current}
        if new == current:
            return frozenset(current)
        current = new


def context_criterion(program, contexts):
    models = [(facts, least_model(program, facts)) for facts in contexts]
    for h, body in program:
        if not body:
            continue
        candidates = set(body)
        for facts, model in models:
            if h not in model:
                candidates.difference_update(model)
        if not candidates:
            return False
    return True


def exact_projection_exists(program, contexts):
    facts = frozenset((h, body) for h, body in program if not body)
    nonfacts = [(h, body) for h, body in program if body]
    for choice in product(*[tuple(sorted(body)) for _, body in nonfacts]):
        projection = facts | frozenset((h, frozenset((b,))) for (h, body), b in zip(nonfacts, choice))
        if all(least_model(projection, S) == least_model(program, S) for S in contexts):
            return True
    return False


def chosen_projection(program, contexts):
    modelsets = [least_model(program, S) for S in contexts]
    rules = set((h, body) for h, body in program if not body)
    for h, body in program:
        if not body:
            continue
        admissible = set(body)
        for M in modelsets:
            if h not in M:
                admissible.difference_update(M)
        if not admissible:
            return None
        rules.add((h, frozenset({min(admissible)})))
    return frozenset(rules)


def construct_factors(program, contexts):
    """Build the clausewise factors from a semantics-faithful first factor."""
    first = chosen_projection(program, contexts)
    if first is None:
        return None
    facts = {(h, body) for h, body in program if not body}
    m = max([1] + [len(body) for h, body in program])
    factors = [set(facts) for _ in range(m)]
    modelsets = [least_model(program, S) for S in contexts]
    for h, body in sorted(program, key=lambda r: (r[0], len(r[1]), tuple(sorted(r[1])))):
        if not body:
            continue
        candidates = [b for b in sorted(body)
                      if all(h in M or b not in M for M in modelsets)]
        assert candidates
        selected = candidates[0]
        values = [selected] + [b for b in sorted(body) if b != selected]
        values += [selected] * (m - len(values))
        for i, b in enumerate(values):
            factors[i].add((h, frozenset((b,))))
    return [frozenset(factor) for factor in factors]


def body_union(factors):
    """All cross-factor unions for rules with a common head."""
    heads = {h for factor in factors for h, body in factor}
    joined = set()
    for h in heads:
        choices = [[body for k, body in factor if k == h] for factor in factors]
        for combination in product(*choices):
            joined.add((h, frozenset().union(*combination)))
    return frozenset(joined)


def check(program, contexts):
    criterion = context_criterion(program, contexts)
    searched = exact_projection_exists(program, contexts)
    assert criterion == searched, (program, contexts, criterion, searched)
    selected = chosen_projection(program, contexts)
    assert (selected is not None) == searched
    if selected is not None:
        assert all(least_model(selected, C) == least_model(program, C) for C in contexts)
        factors = construct_factors(program, contexts)
        assert factors is not None
        assert program <= body_union(factors)
        assert all(least_model(program, C) == set.intersection(
            *(set(least_model(K, C)) for K in factors)) for C in contexts)


def uniform_criterion(program, alphabet):
    return all(not body or any(h in least_model(program, frozenset({b})) for b in body)
               for h, body in program)

all_tests = 0
for n in (1,2):
    rules = [(h,frozenset(i for i in range(n) if mask >> i & 1))
             for h in range(n) for mask in range(1<<n)]
    contexts = [frozenset(i for i in range(n) if mask>>i&1) for mask in range(1<<n)]
    for pbits in range(1<<len(rules)):
        P = frozenset(rules[i] for i in range(len(rules)) if pbits>>i&1)
        for cbits in range(1<<len(contexts)):
            C = [contexts[i] for i in range(len(contexts)) if cbits>>i&1]
            check(P,C); all_tests += 1
        assert uniform_criterion(P, n) == context_criterion(P, contexts)

n = 3
rules = [(h,frozenset(i for i in range(n) if mask >> i & 1))
         for h in range(n) for mask in range(1<<n)]
contexts = [frozenset(i for i in range(n) if mask>>i&1) for mask in range(1<<n)]
for nr in range(3):
    for inds in combinations(range(len(rules)), nr):
        P = frozenset(rules[i] for i in inds)
        for cbits in range(1<<len(contexts)):
            C = [contexts[i] for i in range(len(contexts)) if cbits>>i&1]
            check(P,C);all_tests+=1
        assert uniform_criterion(P, n) == context_criterion(P, contexts)

rng = Random(31097)
n = 4
rules = [(h,frozenset(i for i in range(n) if mask >> i & 1))
         for h in range(n) for mask in range(1<<n)]
contexts = [frozenset(i for i in range(n) if mask>>i&1) for mask in range(1<<n)]
for it in range(3000):
    P = frozenset(rng.sample(rules, rng.randrange(0,6)))
    C = rng.sample(contexts, rng.randrange(0,8))
    check(P,C);all_tests+=1
    assert uniform_criterion(P,n) == context_criterion(P, contexts)

for t in range(2,7):
    head=t
    body=frozenset(range(t))
    P=frozenset({(head,body)})
    contexts=[frozenset({i}) for i in range(t)]
    assert not context_criterion(P,contexts)
    for j in range(t):
        assert context_criterion(P,contexts[:j]+contexts[j+1:])

print('VERIFY_OK',all_tests,'program/context-family comparisons; sharp examples t=2..6')
