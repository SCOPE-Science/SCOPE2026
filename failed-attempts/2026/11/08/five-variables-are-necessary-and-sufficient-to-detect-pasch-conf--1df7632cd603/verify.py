"""Exact finite checks for variable-width logic of Steiner triple systems."""
from itertools import product, combinations
from collections import defaultdict


def projective_binary(d):
    n = (1 << d) - 1
    return list(range(1, n + 1)), lambda a, b, c: len({a,b,c}) == 3 and (a ^ b ^ c) == 0


def affine_ternary(d):
    points = list(product(range(3), repeat=d))
    def block(a,b,c):
        return len({a,b,c}) == 3 and all((a[i]+b[i]+c[i]) % 3 == 0 for i in range(d))
    return points,block


def check_steiner(points,block):
    x=list(points)
    for a,b in combinations(x,2):
        assert sum(block(a,b,c) for c in x) == 1
    return sum(block(*t) for t in combinations(x,3))


def profile(points,block):
    result=defaultdict(set)
    # Atomic type of (a,b,c) uses equality pattern and the block relation.
    for a,b,c in product(points,repeat=3):
        st=(a==b,a==c,b==c,block(a,b,c))
        responses=set()
        for v in points:
            # Every R relation on three distinct locations of four variables.
            responses.add((v==a,v==b,v==c,block(a,b,v),block(a,c,v),block(b,c,v)))
        result[st].add(frozenset(responses))
    return result


def pasch(points,block):
    for a,b,c,d,e in product(points,repeat=5):
        if len({a,b,c,d,e}) < 5 or not (block(a,b,c) and block(a,d,e)):
            continue
        for f in points:
            if block(f,b,d) and block(f,c,e):
                assert len({a,b,c,d,e,f}) == 6
                return (a,b,c,d,e,f)
    return None


def main():
    systems=[('Fano STS(7)',projective_binary(3)),('Affine STS(9)',affine_ternary(2)),
             ('Projective STS(15)',projective_binary(4)),('Affine STS(27)',affine_ternary(3))]
    last=None
    for name,(points,block) in systems:
        n=len(points)
        count=check_steiner(points,block)
        prof=profile(points,block)
        assert all(len(v)==1 for v in prof.values())
        canonical={k:next(iter(v)) for k,v in prof.items()}
        if last is not None: assert canonical==last
        last=canonical
        # The smallest two orders are used for sharp Pasch separation.
        witness=pasch(points,block) if n<=9 else 'not_checked'
        if n==7: assert witness is not None
        if n==9: assert witness is None
        print(f'{name}: {n} points, {count} blocks, {len(prof)} anchor atomic types, '+
              f'{sum(len(v) for v in canonical.values())} total completion categories; '+
              f'Pasch={"not checked" if witness == "not_checked" else "present" if witness is not None else "absent"}')
    print('FULL_STATIONARY_TRIPLE_EXTENSION_CATALOGUES_MATCH')
    print('FANO_AND_AFFINE9_SEPARATED_BY_FIVE_VARIABLE_PASCH_SENTENCE')
    print('VERIFICATION_OK')

if __name__ == '__main__': main()
