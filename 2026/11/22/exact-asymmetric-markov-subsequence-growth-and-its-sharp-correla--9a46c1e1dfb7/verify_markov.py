"""Independent exact checks of the stationary binary Markov subsequence law.

Counts distinct *nonempty* subsequence words, not embeddings.
Requires only Python standard library. Optional symbolic audit with SymPy.
"""
from fractions import Fraction as F
from itertools import product


def distinct_count(word):
    subs = {''}
    for symbol in word:
        subs |= {s + symbol for s in list(subs)}
    return len(subs) - 1


def direct_expectation(n, p, q):
    pi0, pi1 = q / (p + q), p / (p + q)
    total = F(0)
    for w in product('01', repeat=n):
        pr = pi0 if w[0] == '0' else pi1
        for a, b in zip(w, w[1:]):
            if a == '0':
                pr *= p if b == '1' else 1-p
            else:
                pr *= q if b == '0' else 1-q
        total += pr * distinct_count(w)
    return total


def matrix_expectations(nmax, p, q):
    pi0, pi1 = q/(p+q), p/(p+q)
    # Vector order: E0,last=0 ; E1,last=0 ; E0,last=1 ; E1,last=1.
    v = [F(0)] * 4
    out = [F(0)]
    for n in range(1, nmax+1):
        w = [
            (1-p)*(v[0]+v[1]) + q*(v[2]+v[3]) + pi0,
            (1-p)*v[1] + q*v[3],
            p*v[0] + (1-q)*v[2],
            p*(v[0]+v[1]) + (1-q)*(v[2]+v[3]) + pi1,
        ]
        v = w
        out.append(sum(v))
    return out


def polynomial_values(nmax, p, q):
    # D(z) = (1-z)^2 (1-(1-S)z)^2 - P z^2.
    # N(z) = z (1-(1-S)z)
    #         [S+(S^2-2S+2P)z-S(S-1)z^2].
    # The series E(z)=N(z)/(S(1-z)D(z)).
    s, k = p+q, p*q
    def multiply(a, b):
        c = [F(0)]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b): c[i+j] += x*y
        return c
    l = [F(1), s-1]
    d = multiply(multiply([F(1),F(-1)], l), multiply([F(1),F(-1)],l))
    d[2] -= k
    den = [s*x for x in multiply([F(1),F(-1)],d)]
    numer = multiply([F(0),F(1)],multiply(l, [s,s*s-2*s+2*k,-s*(s-1)]))
    values = [F(0)]*(nmax+1)
    for n in range(0,nmax+1):
        values[n] = (numer[n] if n<len(numer) else F(0))
        values[n] -= sum(den[j]*values[n-j] for j in range(1,min(n,len(den)-1)+1))
        values[n] /= den[0]
    return values


def main():
    cases = [(F(i,7),F(j,9)) for i in range(1,8) for j in range(1,10)]
    cases += [(F(1),F(1)),(F(1),F(1,4)),(F(1,3),F(1)),(F(2,3),F(2,3))]
    comparisons = 0
    words = 0
    for p,q in cases:
        nmax=9
        matrix=matrix_expectations(nmax,p,q)
        rational=polynomial_values(nmax,p,q)
        assert matrix == rational, (p,q,matrix,rational)
        for n in range(1,nmax+1):
            brute=direct_expectation(n,p,q)
            assert matrix[n] == brute, (n,p,q,matrix[n],brute)
            comparisons += 1
            words += (1<<n)
    print('PASS exact independent host enumeration:',len(cases),'parameter pairs,',comparisons,'expectations,',words,'weighted host instances')
    print('PASS complete rational generating function vs direct 4-state expectation')
    # Exact symbolic characteristic polynomial and numerator factor, not numerical sampling.
    try:
        import sympy as sp
        p,q,L,z=sp.symbols('p q L z')
        s,k=p+q,p*q
        t=L-1
        M=sp.Matrix([[1-p,1-p,q,q],[0,1-p,0,q],[p,0,1-q,0],[p,p,1-q,1-q]])
        target=t*t*(t+s)**2-k*(t+1)**2
        assert sp.expand(M.charpoly(L).as_expr()-target)==0
        det=(1-z)**2*(1-(1-s)*z)**2-k*z**2
        assert sp.expand((sp.eye(4)-z*M).det()-det)==0
        stat=sp.Matrix([q/(p+q),0,0,p/(p+q)])
        numerator = (1-(1-s)*z)*(s+(s*s-2*s+2*k)*z-s*(s-1)*z*z)
        matrixGF=(sp.ones(1,4)*(sp.eye(4)-z*M).inv()*stat)[0]
        assert sp.cancel(matrixGF-numerator/(s*det))==0
        print('PASS exact symbolic characteristic factorization, determinant and generating-function numerator')
    except ImportError:
        print('SymPy unavailable; symbolic identity is established separately in the proof')

if __name__ == '__main__':
    main()
