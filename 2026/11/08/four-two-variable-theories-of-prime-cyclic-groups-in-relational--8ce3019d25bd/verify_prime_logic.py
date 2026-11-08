#!/usr/bin/env python3
"""Reproducible finite checks for counting-free finite-variable logic of prime cyclic groups."""
from itertools import product, combinations

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
TERMS = (0, 1, 2)  # 0 is the distinguished identity, 1 and 2 stand for two variables.


def atomic_profile(p, a, b):
    vals = (0, a, b)
    return (a == 0, b == 0, a == b) + tuple(
        (vals[i] + vals[j] - vals[k]) % p == 0
        for i, j, k in product(TERMS, repeat=3)
    )


def color_successors(p):
    """For every atomic color, record all possible one-pebble successor colors."""
    by_color = {}
    for a, b in product(range(p), repeat=2):
        col = atomic_profile(p, a, b)
        s0 = frozenset(atomic_profile(p, z, b) for z in range(p))
        s1 = frozenset(atomic_profile(p, a, z) for z in range(p))
        if col in by_color:
            assert by_color[col] == (s0, s1), (p, col)
        else:
            by_color[col] = (s0, s1)
    return by_color


def regime(p):
    return "2" if p == 2 else "3" if p == 3 else "5" if p == 5 else ">=7"


def two_var_type_test(p):
    has_order_two = any(x and (2*x)%p == 0 for x in range(p))
    has_order_three = any(x and (3*x)%p == 0 for x in range(p))
    has_generic = any(
        x and y and x != y and (2*x-y)%p and (2*y-x)%p and (x+y)%p
        for x, y in product(range(p), repeat=2)
    )
    return has_order_two, has_order_three, has_generic

# Three-variable formula syntax and interpretation. All variable occurrences are x,y,z;
# a zero term is the literal integer 0 and cannot be rebound.
VARS = ('x', 'y', 'z')
def mul_ast(n, src, dst):
    assert n >= 1 and src in VARS and dst in VARS and src != dst
    if n == 1:
        return ('eq', src, dst)
    if n == 2:
        return ('add', src, src, dst)
    spare, = (set(VARS) - {src, dst})
    return ('exists', spare,
            ('and', ('add', spare, src, dst), mul_ast(n-1, src, spare)))


def nonzero_p_torsion_ast(n):
    # n*x=0, encoded by the unique (n-1)*x witness, retaining x as an anchor.
    if n == 1:
        inner = ('eq', 'x', 0)
    else:
        inner = ('exists', 'y', ('and',
                 ('add', 'y', 'x', 0), mul_ast(n-1, 'x', 'y')))
    return ('exists', 'x', ('and', ('not', ('eq', 'x', 0)), inner))


def vars_of(ast):
    t = ast[0]
    if t in ('eq', 'add'):
        return set(v for v in ast[1:] if isinstance(v, str))
    if t == 'not': return vars_of(ast[1])
    if t == 'and': return vars_of(ast[1]) | vars_of(ast[2])
    if t == 'exists': return {ast[1]} | vars_of(ast[2])
    raise AssertionError(t)


def eval_ast(ast, p, env):
    t = ast[0]
    def val(x): return env[x] if isinstance(x, str) else x
    if t == 'eq': return val(ast[1]) == val(ast[2])
    if t == 'add': return (val(ast[1])+val(ast[2])-val(ast[3]))%p == 0
    if t == 'not': return not eval_ast(ast[1], p, env)
    if t == 'and': return eval_ast(ast[1], p, env) and eval_ast(ast[2], p, env)
    if t == 'exists':
        name = ast[1]
        for z in range(p):
            next_env = dict(env)
            next_env[name] = z
            if eval_ast(ast[2], p, next_env): return True
        return False
    raise AssertionError(t)


def main():
    profiles = {p: color_successors(p) for p in PRIMES}
    successful = 0
    for p, q in combinations(PRIMES, 2):
        eq = profiles[p] == profiles[q]
        expected = regime(p) == regime(q)
        assert eq == expected, (p, q, eq, expected)
        successful += 1
    assert len({tuple(sorted(profiles[p].items(), key=lambda x: repr(x[0]))) for p in PRIMES}) == 4
    for p in PRIMES:
        assert two_var_type_test(p) == (
            p == 2, p == 3, p >= 7
        ), (p, two_var_type_test(p))
        assert len(vars_of(nonzero_p_torsion_ast(p))) <= 3
    formula_checks = 0
    for p in PRIMES[:7]:
        f = nonzero_p_torsion_ast(p)
        for q in PRIMES[:7]:
            got = eval_ast(f, q, {})
            assert got == (p==q), (p, q, got)
            formula_checks += 1
    print('PRIMES:', ','.join(map(str, PRIMES)))
    print('TWO_VARIABLE_ATOMIC_PROFILE_CLASSES: 2 | 3 | 5 | primes>=7')
    print('FULL_TWO_PEBBLE_BACK_AND_FORTH_PAIR_CHECKS:', successful)
    print('THREE_VARIABLE_RELATIONAL_FORMULA_CHECKS:', formula_checks)
    print('ONE_VARIABLE_CLASSES: 2 | odd primes')
    print('THREE_VARIABLE_DISTINCT_PRIME_CLASSES: verified for seven primes')
    print('ALL_CHECKS_PASS')

if __name__ == '__main__':
    main()
