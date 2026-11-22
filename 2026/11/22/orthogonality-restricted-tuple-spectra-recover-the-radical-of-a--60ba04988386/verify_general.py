"""Independent small-field enumeration of the totally orthogonal extension-type formula.
The program does not assume the Gaussian isotropic-subspace formula when tallying maps.
"""
from fractions import Fraction
from itertools import product


def gaussian(n, k, q):
    if k < 0 or k > n:
        return 0
    p = Fraction(1)
    for j in range(k):
        p *= Fraction(q ** (n - j) - 1, q ** (k - j) - 1)
    assert p.denominator == 1
    return int(p)


def iso_grass_sympl(m, t, q):
    if t < 0 or t > m:
        return 0
    p = Fraction(1)
    for i in range(t):
        p *= Fraction(q ** (2 * m - i) - q ** i, q ** t - q ** i)
    assert p.denominator == 1
    return int(p)


def iso_grass(d, rho, t, q):
    m = (d - rho) // 2
    return sum(gaussian(rho, j, q) *
               q ** ((t-j) * (rho-j)) * iso_grass_sympl(m, t-j, q)
               for j in range(max(0, t-m), min(t, rho)+1))


def sympl(u, v, d, rho, q):
    z = 0
    for i in range((d-rho)//2):
        z += u[2*i]*v[2*i+1] - u[2*i+1]*v[2*i]
    return z % q


def rank(columns, q):
    if not columns:
        return 0
    matrix = [list(row) for row in zip(*columns)]
    i = 0
    for j in range(len(columns)):
        pivot = next((k for k in range(i, len(matrix)) if matrix[k][j] % q), None)
        if pivot is None:
            continue
        matrix[i],matrix[pivot] = matrix[pivot],matrix[i]
        inv = pow(matrix[i][j], -1, q)
        matrix[i] = [(t*inv)%q for t in matrix[i]]
        for k in range(len(matrix)):
            if k != i:
                factor = matrix[k][j]
                matrix[k] = [(x-factor*y)%q for x,y in zip(matrix[k],matrix[i])]
        i += 1
        if i == len(matrix):
            break
    return i


def map_rank_counts(q, d, rho, h):
    vecs=list(product(range(q), repeat=d))
    tally=[0]*(min(d,h)+1)
    for cols in product(vecs, repeat=h):
        if all(sympl(cols[i], cols[j], d, rho, q) == 0
               for i in range(h) for j in range(i+1,h)):
            tally[rank(cols,q)] += 1
    return tally


def verify(q,d,rho,rmax):
    assert (d-rho)%2 == 0
    direct=[]
    for h in range(rmax+1):
        tally=map_rank_counts(q,d,rho,h)
        predicted=[]
        for t in range(min(d,h)+1):
            onto=1
            for i in range(t):
                onto *= q**h-q**i
            predicted.append(iso_grass(d,rho,t,q)*onto)
        assert tally==predicted, (q,d,rho,h,tally,predicted)
        direct.append(tally)
    for r in range(rmax+1):
        count_direct=sum(gaussian(r,h,q)*sum(n*q**((r-h)*(d-t))
                               for t,n in enumerate(direct[h])) for h in range(r+1))
        count_formula=sum(gaussian(r,h,q)*sum(
             iso_grass(d,rho,t,q)*
             __import__('math').prod(q**h-q**i for i in range(t))*
             q**((r-h)*(d-t))
             for t in range(min(d,h)+1)) for h in range(r+1))
        assert count_direct == count_formula
        if r==1:
            assert count_formula==2*q**d
        if r==2:
            Q=q**d
            pair=2*Q*Q-(Q-q**rho)*(Q-Q//q)+(q+1)*(Q+(Q-1)*(Q//q))
            assert count_formula == pair, (q,d,rho,count_formula,pair)
    print('GENERAL_MAP_CHECK_PASS',q,d,rho,'through_arity',rmax)

for args in [(2,1,1,4),(2,2,0,4),(2,2,2,4),(2,3,1,4),
             (2,3,3,4),(3,1,1,4),(3,2,0,4),(3,2,2,4)]:
    verify(*args)
print('GAUSSIAN_ISOTROPIC_SPECTRUM_PASS')
