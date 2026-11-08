"""Exact Hasse-Witt calculation for the degree-ten plane-filling curves over F_7.

Use: python3 verify_cartier.py. All calculations are integer arithmetic modulo 7.
The standard plane-curve Hasse-Witt formula is documented in RESULT.md.
"""
from collections import defaultdict
P = 7
D = 10
MONS = [(a, b, 7-a-b) for a in range(8) for b in range(8-a)]
assert len(MONS) == 36

def form(k):
    terms = defaultdict(int)
    for e, c in [((9,1,0),1),((3,7,0),-1),((0,9,1),1),
                 ((0,3,7),-1),((1,0,9),1),((7,0,3),-1),
                 ((3,0,7),k),((9,0,1),-k)]:
        terms[e] = (terms[e]+c)%P
    return {e:v for e,v in terms.items() if v}

def multiply(F,G):
    H = defaultdict(int)
    for a,ca in F.items():
        for b,cb in G.items():
            H[tuple(a[i]+b[i] for i in range(3))] += ca*cb
    return {e:v%P for e,v in H.items() if v%P}

def hasse(k):
    F = form(k)
    G = {(0,0,0):1}
    for _ in range(P-1):
        G = multiply(G,F)
    A = [[G.get(tuple(P*(a[i]+1)-(b[i]+1) for i in range(3)),0)
          for b in MONS] for a in MONS]
    return A, len(G)

def product(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(36))%P
             for j in range(36)] for i in range(36)]

def rank(M):
    A = [row[:] for row in M]
    r = 0
    pivots = []
    for j in range(len(A[0])):
        t = next((i for i in range(r,len(A)) if A[i][j]%P),None)
        if t is None: continue
        A[r],A[t] = A[t],A[r]
        inv = pow(A[r][j],-1,P)
        A[r] = [(v*inv)%P for v in A[r]]
        for i in range(r+1,len(A)):
            f = A[i][j]
            if f:
                A[i] = [(v-f*w)%P for v,w in zip(A[i],A[r])]
        pivots.append(j)
        r += 1
        if r == len(A): break
    return r, pivots

def determinant(M):
    A = [row[:] for row in M]
    n = len(A)
    det = 1
    for j in range(n):
        t = next((i for i in range(j,n) if A[i][j]%P),None)
        if t is None: return 0
        if t != j:
            A[j], A[t] = A[t], A[j]
            det = -det
        v = A[j][j]
        det = (det*v)%P
        inv = pow(v,-1,P)
        for i in range(j+1,n):
            m = A[i][j]*inv%P
            for col in range(j+1,n):
                A[i][col] = (A[i][col]-m*A[j][col])%P
            A[i][j]=0
    return det%P

def main():
    good = [k for k in range(7) if all((x**7+k*x**3-1)%7 for x in range(7))]
    assert good == [1,3]
    print('RATIONAL_SMOOTHNESS_PARAMETERS', good)
    for k in good:
        A, terms = hasse(k)
        r,pivots = rank(A)
        rr,_ = rank(product(A,A))
        assert (r,rr) == (35,35)
        assert len(pivots) == 35
        omitted = (34,35) if k==1 else (33,34)
        for label,M,expected in [('A',A,6),('A_squared',product(A,A),1 if k==1 else 6)]:
            assert determinant(M)==0
            rr0,cc0=omitted
            minor=[[M[i][j] for j in range(36) if j!=cc0]
                   for i in range(36) if i!=rr0]
            actual=determinant(minor)
            assert actual==expected
            print('NONZERO_MINOR_PASS',k,label,'deleted_row',rr0,
                  'deleted_column',cc0,'det',actual)
        print('HASSE_WITT_PASS', k, 'genus', 36, 'terms', terms,
              'cartier_rank',r,'square_rank',rr,'a_number',36-r,'p_rank',rr)
    print('ALMOST_ORDINARY_NEWTON_POLYGON_PASS')

if __name__=='__main__': main()
