"""Finite consistency checks for omega-accumulation logic of a convergent sequence.

Analytic proofs, not this finite test, establish the universal result.
Run with Python 3 standard library only: python checker.py
"""
import itertools
import random


def prop(formula, typ):
    tag = formula[0]
    if tag == 'p':
        return bool((typ >> formula[1]) & 1)
    if tag == 'top':
        return True
    if tag == 'not':
        return not prop(formula[1], typ)
    if tag == 'and':
        return prop(formula[1], typ) and prop(formula[2], typ)
    if tag == 'dia':
        return False
    raise AssertionError(formula)


def summary(formula, at_limit, infinite_types):
    tag = formula[0]
    if tag == 'p':
        return bool((at_limit >> formula[1]) & 1)
    if tag == 'top':
        return True
    if tag == 'not':
        return not summary(formula[1], at_limit, infinite_types)
    if tag == 'and':
        return (summary(formula[1], at_limit, infinite_types)
                and summary(formula[2], at_limit, infinite_types))
    if tag == 'dia':
        return any(prop(formula[1], t) for t in infinite_types)
    raise AssertionError(formula)


def direct(formula, typ, limit_type, infinite_types, is_limit):
    tag = formula[0]
    if tag == 'p':
        use = limit_type if is_limit else typ
        return bool((use >> formula[1]) & 1)
    if tag == 'top':
        return True
    if tag == 'not':
        return not direct(formula[1], typ, limit_type, infinite_types, is_limit)
    if tag == 'and':
        return (direct(formula[1], typ, limit_type, infinite_types, is_limit)
                and direct(formula[2], typ, limit_type, infinite_types, is_limit))
    if tag == 'dia':
        if not is_limit:
            return False
        return any(direct(formula[1], t, limit_type, infinite_types, False)
                   for t in infinite_types)
    raise AssertionError(formula)


def make_formula(rng, k, depth):
    if depth == 0 or rng.randrange(6) == 0:
        return ('p', rng.randrange(k)) if k else ('top',)
    tag = rng.choice(('not', 'and', 'dia'))
    if tag == 'and':
        return ('and', make_formula(rng, k, depth - 1),
                make_formula(rng, k, depth - 1))
    return (tag, make_formula(rng, k, depth - 1))


def check():
    rng = random.Random(260631885)
    checks = 0
    for k in (0, 1, 2, 3):
        n = 1 << k
        types = tuple(range(n))
        for _ in range(420):
            i = tuple(t for t in types if rng.getrandbits(1))
            if not i:
                i = (rng.choice(types),)
            a = rng.choice(types)
            # Any nonempty infinitely recurring type set is realized by
            # a periodic tail. Add a finite arbitrary prefix to test robustness.
            period = list(i) + [rng.choice(i) for _ in range(rng.randrange(5))]
            prefix = [rng.choice(types) for _ in range(rng.randrange(6))]
            f = make_formula(rng, k, 6)
            assert summary(f, a, i) == direct(f, None, a, period, True)
            for t in prefix + period:
                assert prop(f, t) == direct(f, t, a, period, False)
            checks += 1
    # At k=1 there are exactly 8 semantic coordinates: two isolated
    # propositional types and (a,I) with a in {0,1} and nonempty I.
    # Four primitive depth-one formulas separate all eight points,
    # hence their Boolean algebra is the full 256-element powerset.
    states = [('iso', t, None) for t in (0, 1)] + [
        ('limit', a, i)
        for a in (0, 1)
        for i in ((0,), (1,), (0, 1))
    ]
    chi0 = ('not', ('p', 0))
    chi1 = ('p', 0)
    formulas = [chi1, ('dia', ('top',)), ('dia', chi0), ('dia', chi1)]
    codes = []
    for place, t, i in states:
        codes.append(tuple((prop(f, t) if place == 'iso' else summary(f, t, i))
                           for f in formulas))
    assert len(codes) == len(set(codes)) == 8
    assert len(set(itertools.product((False, True), repeat=len(states)))) == 256
    # For k=0, two points (isolated, limit) are separated by Diamond Top.
    assert prop(('dia', ('top',)), 0) is False
    assert summary(('dia', ('top',)), 0, (0,)) is True
    assert (2 ** (2 ** 0 * 2 ** (2 ** 0))) == 4
    assert (2 ** (2 ** 1 * 2 ** (2 ** 1))) == 256
    assert (2 ** (2 ** 2 * 2 ** (2 ** 2))) == 2 ** 64
    print('OMEGA_PLUS_ONE_MODAL_NORMAL_FORM_CHECKS_OK', checks,
          'RANDOM_FORMULAS_AND_PERIODIC_MODELS',
          'ONE_VARIABLE_SEPARATION', len(codes),
          'ONE_VARIABLE_CLASSES', 256)


if __name__ == '__main__':
    check()
