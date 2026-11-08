"""Independent direct multiplication checks for nilpotency-index distribution.
No formula is used to compute powers: multiplication uses the monomial relations.
"""
from itertools import product
from collections import Counter

BASE = [(i,j) for i in range(3) for j in range(3)]
IDX = {b:i for i,b in enumerate(BASE)}
RAD = [i for i,b in enumerate(BASE) if b!=(0,0)]

class Field:
    def __init__(self, q):
        self.q=q
        if q==4:
            self.add=[[i^j for j in range(q)] for i in range(q)]
            def rawmul(a,b):
                v=0
                for i in range(2):
                    for j in range(2):
                        if (a>>i)&1 and (b>>j)&1: v^=1<<(i+j)
                if v&8:v^=0b1100 # x^3=x^2+x
                if v&4:v^=0b111  # x^2=x+1
                return v
            self.mul=[[rawmul(i,j) for j in range(q)] for i in range(q)]
        else:
            self.add=[[(i+j)%q for j in range(q)] for i in range(q)]
            self.mul=[[(i*j)%q for j in range(q)] for i in range(q)]
    def pow(self,a,n):
        v=1
        for _ in range(n):v=self.mul[v][a]
        return v


def direct_hist(q,lam,prefix_only=False):
    F=Field(q)
    # Multiplication table of each pair of basis monomials.
    T=[]
    for i,j in BASE:
        row=[]
        for u,v in BASE:
            if i+u>=3 or j+v>=3: row.append(None)
            else: row.append((IDX[(i+u,j+v)],F.pow(lam,j*u)))
        T.append(row)
    add,mul=F.add,F.mul
    def multiply(X,Y):
        out=[0]*9
        for i,xi in enumerate(X):
            if not xi:continue
            for j,yj in enumerate(Y):
                if not yj or T[i][j] is None: continue
                k,t=T[i][j]
                out[k]=add[out[k]][mul[mul[xi][yj]][t]]
        return out
    hist=Counter()
    prefix=[IDX[x] for x in [(1,0),(0,1),(2,0),(1,1),(0,2)]]
    active=prefix if prefix_only else RAD
    scale=q**3 if prefix_only else 1
    for coords in product(range(q),repeat=len(active)):
        x=[0]*9
        for idx,v in zip(active,coords): x[idx]=v
        if not any(x):
            hist[1]+=1
            if prefix_only:hist[2]+=scale-1
            continue
        p=x
        for n in range(2,6):
            p=multiply(p,x)
            if not any(p):
                hist[n]+=scale;break
        else:raise AssertionError('J^5 nonzero')
    return tuple(hist.get(i,0) for i in range(1,6))


def theory(q,lam):
    F=Field(q);a,m=F.add,F.mul
    S=a[a[F.pow(lam,2)][lam]][1]
    T=a[a[F.pow(lam,2)][(q-lam)%q if q!=4 else lam]][1] # subtraction differs in char 2
    K=a[F.pow(lam,2)][1]
    if S==0:
        cube=q**8
    elif T==0:
        cube=(2*q-1)*q**6
    else:
        cube=q**5*(3*q-2)
    four=q**8 if S==0 or K==0 else (2*q-1)*q**6
    square=q**5
    return (1,square-1,cube-square,four-cube,q**8-four)


def main():
    cases=[(2,1),(3,1),(3,2),(4,1),(4,2),(4,3)]
    for q,lam in cases:
        seen=direct_hist(q,lam)
        pred=theory(q,lam)
        assert seen==pred,(q,lam,seen,pred)
        print(f'OK field={q} lambda={lam} distribution={seen}')
    # Powers through degree four, and the square-zero condition, depend only
    # on coefficients in radical degrees one and two. Check every 5-tuple
    # in larger prime fields using direct multiplication. A tuple represents
    # q^3 unrestricted higher-degree choices by the proved filtration bound.
    for q,lam in [(5,2),(5,4),(7,2),(7,3),(7,1)]:
        seen=direct_hist(q,lam,prefix_only=True)
        pred=theory(q,lam)
        assert seen==pred,(q,lam,seen,pred)
        print(f'OK_FILTERED field={q} lambda={lam} distribution={seen}')
    print('VERIFY_OK_QCI_NILPOTENCE')

if __name__=='__main__':main()
