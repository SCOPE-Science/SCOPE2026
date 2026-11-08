"""Independent finite-prime checks for endpoint norms of odd-field Veronese cones.

Run: python check_veronese.py
Requires only the Python standard library. Large-field formulas apply to prime powers;
direct exhaustive checks here use prime fields.
"""
import cmath
import itertools
import math


def symmetric_matrix(m, entries):
    matrix = [[0]*m for _ in range(m)]
    it = iter(entries)
    for i in range(m):
        for j in range(i, m):
            matrix[i][j] = matrix[j][i] = next(it)
    return matrix


def rank_mod(matrix, p):
    a = [row[:] for row in matrix]
    n = len(a)
    pivot_row = 0
    for col in range(n):
        pivot = next((i for i in range(pivot_row, n) if a[i][col] % p), None)
        if pivot is None:
            continue
        a[pivot], a[pivot_row] = a[pivot_row], a[pivot]
        inv = pow(a[pivot_row][col], -1, p)
        a[pivot_row] = [(v * inv) % p for v in a[pivot_row]]
        for i in range(pivot_row+1, n):
            fac = a[i][col]
            a[i] = [(x-fac*y) % p for x, y in zip(a[i], a[pivot_row])]
        pivot_row += 1
    return pivot_row


def rank_count(q, m, r):
    # Formula from symmetric-form orbit enumeration, integer by construction.
    h = r // 2
    num, den = 1, 1
    for i in range(1, h+1):
        num *= q**(2*i)
        den *= q**(2*i)-1
    for i in range(r):
        num *= q**(m-i)-1
    assert num % den == 0
    return num//den


def predicted(q, m):
    N = q**(m*(m+1)//2)
    counts = [rank_count(q,m,r) for r in range(m+1)]
    assert sum(counts) == N
    value=0.0
    for r,nr in enumerate(counts):
        T=q**(m-r/2)
        if r%2 == 0:
            term=T+q**(-r/2)
        else:
            term=T if q%4==1 else math.sqrt(1+T*T)
        value += nr*term
    return value/(2*N), counts


def brute(q,m):
    N=q**(m*(m+1)//2)
    sq={}
    for v in itertools.product(range(q),repeat=m):
        key=tuple((v[i]*v[j])%q for i in range(m) for j in range(i,m))
        sq[key]=1
    assert len(sq)==1+(q**m-1)//2
    roots=[cmath.exp(2j*math.pi*k/q) for k in range(q)]
    byrank=[0]*(m+1)
    sumabs=0.0
    residual=0.0
    for entries in itertools.product(range(q),repeat=m*(m+1)//2):
        a=symmetric_matrix(m,entries)
        r=rank_mod(a,q)
        byrank[r]+=1
        total=0j
        for b in sq:
            # trace(A B) = sum diag + twice the off-diagonal products.
            s=0
            z=0
            for i in range(m):
                for j in range(i,m):
                    s+= (1 if i==j else 2)*entries[z]*b[z]
                    z+=1
            total+=roots[s%q]
        sumabs+=abs(total)
        # Independent verification of quadratic-Gauss modulus:
        G=2*total-1
        residual=max(residual,abs(abs(G)-q**(m-r/2)))
    exact=sumabs/N
    formula, counts=predicted(q,m)
    assert counts==byrank, (q,m,counts,byrank)
    assert abs(exact-formula)<1e-9, (q,m,exact,formula)
    assert residual<1e-8,(q,m,residual)
    print(f'EXHAUSTIVE q={q} m={m} ambient={N} cone={len(sq)} norm={exact:.12f} counts={counts}')


def limiting(q):
    Q=1/q
    c=1.
    for j in range(1,151,2):
        c *= (1-Q**j)
    pk=[];D=1.
    for k in range(24):
        if k: D*=1-Q**k
        pk.append(c*Q**(k*(k+1)/2)/D)
    t=math.sqrt(q)
    S=sum(pk[k]*t**k for k in range(24))
    d=q/((t+1)*(q+1))
    C=[]
    for parity in (0,1):
        A=sum(pk[k]*t**k for k in range(24) if k%2==parity)
        B=sum(pk[k]*t**k for k in range(24) if k%2!=parity)
        J=sum(pk[k]*t**(-k) for k in range(24) if k%2!=parity)
        C.append((1-d)*A-d*Q*B+(J/2 if q%4==3 else 0))
    assert all(v>0 for v in C)
    for m in range(4,17):
        L,_=predicted(q,m)
        H=2*q**(-m/2)*L
        approx=S+C[m%2]*q**(-m)
        error=abs(H-approx)
        # Numerically check the second-order tail with a generous coefficient.
        assert error<100*q**(-2*m)+1e-12,(q,m,error)
    print(f'ASYMPTOTIC q={q} S={S:.12f} C_even={C[0]:.12f} C_odd={C[1]:.12f} pass')

if __name__=='__main__':
    for q,m in ((3,1),(3,2),(3,3),(5,1),(5,2),(5,3),(7,2),(11,1)):
        brute(q,m)
    for q in (3,5,7,9,11,13,19):
        limiting(q)
    print('ODD_VERONESE_ENDPOINT_AND_PARITY_CHECKS_PASS')
