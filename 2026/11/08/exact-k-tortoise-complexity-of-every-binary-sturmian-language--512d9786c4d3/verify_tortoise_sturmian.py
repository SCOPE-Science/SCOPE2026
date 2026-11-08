"""Reproducible checks of k-tortoise factor complexity for mechanical Sturmian words.

Requires only Python 3 standard library. Tests independent factor-generation methods:
(i) all rotation partition cells, (ii) long orbit prefixes, and compares
literal iterates of the binary tortoise operator against a proposed formula.
Finite checks support, but do not substitute for, the general proof.
"""
from decimal import Decimal, localcontext, ROUND_FLOOR
from collections import Counter


def tortoise_once(word):
    i = word.find('1')
    return word if i < 0 else word[:i] + word[i+1:] + '1'


def tortoise_k(word, k):
    for _ in range(k):
        word = tortoise_once(word)
    return word


def fractional(x):
    return x - x.to_integral_value(rounding=ROUND_FLOOR)


def rotation_factors(alpha, n):
    # A cut is at the beta with beta+j*alpha integral; one sample per cell.
    cuts = sorted(set([Decimal(0)] + [fractional(-j*alpha) for j in range(1,n+1)]))
    assert len(cuts) == n+1, ('cut collision', n)
    samples = [(cuts[i] + cuts[i+1])/2 for i in range(n)]
    samples.append((cuts[-1] + Decimal(1))/2)
    factors = set()
    for beta in samples:
        s = ''.join(str(int(beta+(i+1)*alpha)-int(beta+i*alpha)) for i in range(n))
        factors.add(s)
    assert len(factors)==n+1, ('factor count', n, len(factors))
    return factors


def orbit_factors(alpha, n, orbit_size=1500):
    # Different from the cut enumerator: follow a single irrational rotation.
    vals = [int(i*alpha) for i in range(orbit_size+n+1)]
    word=''.join(str(vals[i+1]-vals[i]) for i in range(orbit_size+n))
    return {word[i:i+n] for i in range(orbit_size+1)}


def main():
    cases=0; orbit_cases=0; cells=0
    with localcontext() as ctx:
        ctx.prec=64
        roots=(2,3,5,6,7,10,11,13)
        slopes=[]
        for rad in roots:
            root=Decimal(rad).sqrt()
            alpha=root-Decimal(int(root))
            slopes.append((str(rad),alpha))
        slopes += [('golden-small',(Decimal(3)-Decimal(5).sqrt())/2),
                   ('golden-large',(Decimal(5).sqrt()-1)/2)]
        for name,alpha in slopes:
            for n in range(1,71):
                fs=rotation_factors(alpha,n)
                cells+=len(fs)
                if n<=32:
                    os=orbit_factors(alpha,n)
                    assert os==fs,(name,n,'orbit vs partition',len(os),len(fs))
                    orbit_cases+=1
                for k in range(1,17):
                    images={tortoise_k(w,k) for w in fs}
                    q=int(Decimal(k)/alpha)
                    expected=2+max(0,n-1-q)
                    assert len(images)==expected,(name,n,k,len(images),expected)
                    cases+=1
    print(f'PASS: {cases} (slope,length,iteration) exact language checks')
    print(f'PASS: {orbit_cases} independent orbit-language comparisons; {cells} rotation cells')
    print('Limits: finitely many quadratic slopes/lengths/iterations; proof establishes infinite claim.')

if __name__=='__main__':
    main()
