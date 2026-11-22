"""Independent finite checks for the width-three random-minimizer Markov law.

Standard-library only.  Run: python3 verify.py
No finite computation is used as a substitute for the all-length proof.
"""
from fractions import Fraction
from itertools import permutations, product
from decimal import Decimal, localcontext


def legal_words(length):
    def extend(prefix):
        if len(prefix) == length:
            yield prefix
            return
        for symbol in (0, 1):
            if not prefix or prefix[-1] != 1 or symbol != 1:
                yield from extend(prefix + (symbol,))
    yield from extend(())


def charged_fraction(word, k):
    blocks = [word[i:i+k] for i in range(4)]
    distinct = tuple(dict.fromkeys(blocks))
    charged = 0
    total = 0
    for order in permutations(distinct):
        rank = {block: position for position, block in enumerate(order)}
        left = min(range(3), key=lambda i: (rank[blocks[i]], i))
        right = min(range(1, 4), key=lambda i: (rank[blocks[i]], i))
        charged += (left != right)
        total += 1
    return Fraction(charged, total)


def source_weight(word, p):
    q = 1 - p
    pi0 = 1 / (2 - p)
    w = pi0 if word[0] == 0 else q * pi0
    for a, b in zip(word, word[1:]):
        if a == 0 and b == 0:
            w *= p
        elif a == 0 and b == 1:
            w *= q
        elif a == 1 and b == 0:
            pass
        else:
            raise ValueError('forbidden source')
    return w


def claimed_density(k, p):
    if k == 1:
        return Fraction(1, 2) + p*p / (2 * (2-p))
    q = 1-p
    lam = p*q
    m, r = divmod(k, 3)
    if r == 0:
        periodic = q*(1+2*p)*lam**m/(2-p)
    elif r == 1:
        periodic = (3-p)*lam**(m+1)/(2-p)
    else:
        periodic = lam**(m+1)
    return Fraction(1, 2) + ((1+p+p*p)*p**k/(2-p) - periodic)/6


def exceptional_words(k):
    length = k+3
    found = set()
    for i in range(4):
        for j in range(i+1, 4):
            d = j-i
            for seed in product((0,1), repeat=d):
                periodic_segment = tuple(seed[t % d] for t in range(k+d))
                for before in product((0,1), repeat=i):
                    for after in product((0,1), repeat=length-i-k-d):
                        word = before + periodic_segment + after
                        if all(a+b <= 1 for a,b in zip(word,word[1:])):
                            found.add(word)
    return found


def verify():
    sources = [Fraction(1,4), Fraction(2,5), Fraction(1,2),
               Fraction(2,3), Fraction(4,5)]
    count = 0
    for k in range(1, 14):
        context_values = [(w, charged_fraction(w,k)) for w in legal_words(k+3)]
        count += len(context_values)
        for p in sources:
            direct = sum((source_weight(w,p)*v for w,v in context_values), Fraction(0))
            formula = claimed_density(k,p)
            assert direct == formula, (k,p,direct,formula)
    print('PASS direct enumeration (all',count,'admissible contexts, five rational source parameters)')
    for k in range(2, 81):
        special = exceptional_words(k)
        assert len(special) == 13, (k,len(special))
        observed = [charged_fraction(w,k) for w in special]
        assert sum(v != Fraction(1,2) for v in observed) == 10, k
        for p in sources:
            correction = sum((source_weight(w,p)*(charged_fraction(w,k)-Fraction(1,2))
                              for w in special),Fraction(0))
            assert correction + Fraction(1,2) == claimed_density(k,p), (k,p)
    print('PASS 13 exceptional contexts, 10 nonzero corrections, k=2..80')
    with localcontext() as ctx:
        ctx.prec = 70
        phi = (1+Decimal(5).sqrt())/2
        p = 1/phi
        c0 = (5-Decimal(5).sqrt())/20
        c1 = (4*Decimal(5).sqrt()-5)/30
        for k in range(2, 81):
            q=1-p; la=p*q; m,r=divmod(k,3)
            if r==0:
                per=q*(1+2*p)*la**m/(2-p)
            elif r==1:
                per=(3-p)*la**(m+1)/(2-p)
            else:
                per=la**(m+1)
            generic=Decimal('0.5')+((1+p+p*p)*p**k/(2-p)-per)/6
            closed=Decimal('0.5')+p**k*(c1 if r==1 else c0)
            assert abs(generic-closed)<Decimal('1e-60'),k
    print('PASS maximum-entropy golden-mean three-residue simplification, k=2..80')

if __name__ == '__main__':
    verify()
