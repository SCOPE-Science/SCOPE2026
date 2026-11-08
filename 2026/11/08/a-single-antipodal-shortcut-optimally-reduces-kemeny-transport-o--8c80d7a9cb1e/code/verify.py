"""Exact, independent small-order check for the single-chord cycle Kemeny law.

Requires only Python 3 standard library. Uses rational grounded-Laplacian
inversion and the electrical resistance formula, not the rank-one proof.
"""
from fractions import Fraction as Q


def inverse(a):
    n=len(a)
    m=[[Q(x) for x in row]+[Q(int(i==j)) for j in range(n)] for i,row in enumerate(a)]
    for k in range(n):
        pivot=next((i for i in range(k,n) if m[i][k]),None)
        assert pivot is not None
        m[k],m[pivot]=m[pivot],m[k]
        factor=m[k][k]
        m[k]=[x/factor for x in m[k]]
        for i in range(n):
            if i!=k:
                factor=m[i][k]
                if factor:
                    m[i]=[a-factor*b for a,b in zip(m[i],m[k])]
    return [row[n:] for row in m]


def electrical_kemeny(n,d):
    edges={(min(i,(i+1)%n),max(i,(i+1)%n)) for i in range(n)}
    edges.add((0,d))
    degree=[0]*n
    lap=[[0]*n for _ in range(n)]
    for i,j in edges:
        degree[i]+=1;degree[j]+=1
        lap[i][i]+=1;lap[j][j]+=1
        lap[i][j]-=1;lap[j][i]-=1
    B=inverse([row[1:] for row in lap[1:]])
    def r(i,j):
        if i==j:return Q(0)
        if i==0:return B[j-1][j-1]
        if j==0:return B[i-1][i-1]
        return B[i-1][i-1]+B[j-1][j-1]-2*B[i-1][j-1]
    return sum(degree[i]*degree[j]*r(i,j) for i in range(n)
               for j in range(i+1,n))/Q(2*len(edges))


def formula_delta(n,d):
    r=d*(n-d)
    return Q(n**3-n+n*r*(n-2)-(n+4)*r*r,
             6*(n+1)*(n+r))


def run():
    trials=0
    for n in range(4,23):
        prior=Q(n*n-1,6)
        last=Q(0)
        for d in range(2,n//2+1):
            got=electrical_kemeny(n,d)-prior
            want=formula_delta(n,d)
            assert got==want,(n,d,got,want)
            assert got<0,(n,d,got)
            assert got<last,(n,d,got,last)
            last=got
            trials+=1
    for n in range(23,301):
        deltas=[formula_delta(n,d) for d in range(2,n//2+1)]
        assert all(x<0 for x in deltas)
        assert all(a>b for a,b in zip(deltas,deltas[1:]))
        assert deltas[-1]==min(deltas)
    print('EXACT_INDEPENDENT_LAPLACIAN_OK', trials, 'chords n=4..22')
    print('FORMULA_ALL_CHORDS_OK n=23..300')


if __name__=='__main__':run()
