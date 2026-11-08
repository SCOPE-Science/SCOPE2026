"""Exact-rational checks for two-leader inverse traces on quadrilateral books.

Run: python3 verify.py. Uses only the Python standard library.
The all-page-size theorem is proved in RESULT.md; finite checks are diagnostic.
"""
from fractions import Fraction as Q
from itertools import combinations


def laplacian(m):
    n = 2*m + 2
    a = [[0]*n for _ in range(n)]
    edges = [(0,1)]
    for p in range(m):
        i, j = 2+2*p, 3+2*p
        edges.extend([(0,i),(i,j),(j,1)])
    for u,v in edges:
        a[u][u] += 1
        a[v][v] += 1
        a[u][v] -= 1
        a[v][u] -= 1
    return a


def invert(matrix):
    n = len(matrix)
    A = [[Q(x) for x in matrix[i]] + [Q(int(i == j)) for j in range(n)]
         for i in range(n)]
    for c in range(n):
        p = next((r for r in range(c,n) if A[r][c]),None)
        assert p is not None, 'singular grounded Laplacian'
        A[c],A[p] = A[p],A[c]
        pivot = A[c][c]
        A[c] = [v/pivot for v in A[c]]
        for r in range(n):
            if r != c and A[r][c]:
                f = A[r][c]
                A[r] = [v-f*w for v,w in zip(A[r],A[c])]
    return [row[n:] for row in A]


def remove(mat, leaders):
    followers = [i for i in range(len(mat)) if i not in leaders]
    return [[mat[i][j] for j in followers] for i in followers]


def label(pair):
    u,v=pair
    if v < 2: return 'hubs'
    if u < 2:
        return 'hub-near' if (u == 0 and v%2==0) or (u == 1 and v%2==1) else 'hub-far'
    sideu,sidev=u%2,v%2
    if u//2 == v//2: return 'paired'
    if sideu == sidev: return 'same'
    return 'opposite'


def formula(m, case):
    return {
     'hubs':Q(4*m,3),
     'hub-near':Q(8*m*m+33*m-5,3*(2*m+7)),
     'hub-far':Q(8*m*m+45*m-17,6*(m+5)),
     'paired':Q(2*(7*m*m+21*m-10),3*(2*m+7)),
     'same':Q(12*m*m+25*m-29,6*(m+3)),
     'opposite':Q(2*(4*m*m+9*m-11),4*m+13),
    }[case]


def resistance_formulas(m):
    ruv=Q(3,m+3)
    e=Q(2*m+7,3*(m+3))
    f=Q(2*(m+5),3*(m+3))
    h=Q(4,3)
    g=Q(4*m+13,3*(m+3))
    return {(0,1):ruv,(0,2):e,(0,3):f,(2,3):e,(2,4):h,(2,5):g}


def verify():
    comparisons = 0
    classes = set()
    for m in range(2,10):
        L=laplacian(m)
        all_pairs=[]
        for leaders in combinations(range(len(L)),2):
            inverse=invert(remove(L,set(leaders)))
            actual=sum((inverse[i][i] for i in range(len(inverse))),Q(0))
            kind=label(leaders)
            assert actual==formula(m,kind),(m,leaders,kind,actual,formula(m,kind))
            classes.add(kind)
            all_pairs.append((actual,leaders,kind))
            comparisons+=1
        expected='opposite' if m==2 else ('hub-far' if m==3 else 'hubs')
        best=min(x[0] for x in all_pairs)
        optimal=[p for val,p,_ in all_pairs if val==best]
        assert all(k==expected for val,_,k in all_pairs if val==best)
        assert len(optimal)==(m*(m-1) if m==2 else (2*m if m==3 else 1))
        assert len({val for val,_,_ in all_pairs})==6 if m>=4 else True
        if m<=6:
            for (x,y),expected_R in resistance_formulas(m).items():
                C=invert(remove(L,{y}))
                nodes=[i for i in range(len(L)) if i!=y]
                observed_R=C[nodes.index(x)][nodes.index(x)]
                assert observed_R==expected_R,(m,x,y,observed_R,expected_R)
        print('m=%d  optimum=%s  count=%d  J=%s' %(m,expected,len(optimal),best))
    assert classes == {'hubs','hub-near','hub-far','paired','same','opposite'}
    # Positive differences used in the infinite proof. These are exact integer sign tests,
    # not substitutes for the factorizations derived in RESULT.md.
    for m in range(2,200):
        j={k:formula(m,k) for k in classes}
        assert j['hub-near']>j['hubs']
        assert j['paired']>j['hubs']
        assert j['same']>j['opposite']
        assert (j['hub-far']<j['hubs'])==(m<=3)
        assert (j['opposite']<j['hubs'])==(m==2)
        assert (j['opposite']<j['hub-far'])==(m==2)
    print('VERIFY_OK exact_grounded_pair_comparisons=%d; resistance_sample_checks=30; sign_samples=198'%comparisons)

if __name__=='__main__':
    verify()
