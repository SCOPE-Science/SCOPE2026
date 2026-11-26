"""Exact rational checks of the weighted two-layer quantum-walk mixing formula.

Run: python3 verify.py. Uses only Python's standard library. Finite tests
corroborate the separately supplied unrestricted algebraic proof.
"""
from fractions import Fraction as Q
from itertools import combinations

def zero(n,m): return [[Q(0) for _ in range(m)] for _ in range(n)]
def ident(n): return [[Q(int(i==j)) for j in range(n)] for i in range(n)]
def add(a,b): return [[v+w for v,w in zip(row,srow)] for row,srow in zip(a,b)]
def sub(a,b): return [[v-w for v,w in zip(row,srow)] for row,srow in zip(a,b)]
def scale(a,x): return [[x*v for v in row] for row in a]
def multiply(a,b): return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def had(a,b): return [[v*w for v,w in zip(row,srow)] for row,srow in zip(a,b)]
def kron(a,b):
    return [[a[i][j]*b[k][l] for j in range(len(a[0])) for l in range(len(b[0]))]
            for i in range(len(a)) for k in range(len(b))]
def rank(a):
    a=[row[:] for row in a]
    m,n=len(a),len(a[0]); r=0
    for c in range(n):
        k=next((i for i in range(r,m) if a[i][c]),None)
        if k is None: continue
        a[k],a[r]=a[r],a[k]
        p=a[r][c]; a[r]=[v/p for v in a[r]]
        for i in range(m):
            if i!=r and a[i][c]:
                p=a[i][c]; a[i]=[x-p*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==m: break
    return r

def polyprojector(A,lamb,distinct):
    n=len(A); P=ident(n)
    for mu in distinct:
        if lamb!=mu:
            P=multiply(P,scale(sub(A,scale(ident(n),mu)),Q(1,lamb-mu)))
    return P

def adjoin(names):
    n=len(names); A=zero(n,n)
    for i,j in combinations(range(n),2):
        if names[i]==names[j]: continue
        A[i][j]=A[j][i]=Q(1)
    return A

def complete(n): return adjoin(list(range(n)))
def cycle(n):
    A=zero(n,n)
    for i in range(n): A[i][(i+1)%n]=A[(i+1)%n][i]=Q(1)
    return A

def mixed_integer_spectrum(levels):
    n=len(levels)
    O=sub(ident(n),scale([[Q(1) for _ in range(n)] for _ in range(n)],Q(2,n)))
    D=zero(n,n)
    for i,l in enumerate(levels): D[i][i]=Q(l)
    return multiply(multiply(O,D),O)

def check(A, spectrum, t):
    n=len(A)
    E={l:polyprojector(A,l,spectrum) for l in spectrum}
    assert sum_matrices([E[l] for l in spectrum])==ident(n)
    for l in spectrum:
        assert multiply(E[l],E[l])==E[l]
    M=sum_matrices([had(E[l],E[l]) for l in spectrum])
    Fplus=[[Q(1,2),Q(1,2)],[Q(1,2),Q(1,2)]]
    Fminus=[[Q(1,2),Q(-1,2)],[Q(-1,2),Q(1,2)]]
    I2=ident(2)
    if t==0:
        direct=kron(M,I2)
        assert rank(direct)==2*rank(M)
        return n,rank(M),rank(direct),0
    blocks={}
    for l in spectrum:
        for energy,F in ((l+t,Fplus),(l-t,Fminus)):
            P=kron(E[l],F)
            blocks[energy]=add(blocks.get(energy,zero(2*n,2*n)),P)
    direct=sum_matrices([had(P,P) for P in blocks.values()])
    B=sum_matrices([had(E[l],E[l+2*t]) for l in spectrum if l+2*t in E],n=n)
    formula=add(kron(M,Fplus),kron(B,Fminus))
    assert direct==formula, ('identity fails',n,t)
    assert rank(direct)==rank(M)+rank(B),('rank fails',n,t)
    return n,rank(M),rank(direct),rank(B)

def sum_matrices(mats,n=None):
    if not mats:
        assert n is not None
        return zero(n,n)
    result=zero(len(mats[0]),len(mats[0][0]))
    for A in mats: result=add(result,A)
    return result

if __name__=='__main__':
    cases=[('K2',complete(2),[-1,1]),('K3',complete(3),[-1,2]),
           ('C4',cycle(4),[-2,0,2]),('C6',cycle(6),[-2,-1,1,2]),
           ('weighted3',mixed_integer_spectrum([0,1,3]),[0,1,3]),
           ('weighted4',mixed_integer_spectrum([-3,0,2,5]),[-3,0,2,5])]
    vals=[Q(0),Q(1,4),Q(1,2),Q(1),Q(3,2),Q(2),Q(5,2)]
    count=0; resonant=0; entries=0
    for name,A,spec in cases:
        for t in vals:
            n,rb,rp,extra=check(A,spec,t)
            count+=1; entries+=(2*n)**2
            if extra>0: resonant+=1
            print(f'{name} t={t} base_rank={rb} doubled_rank={rp} gap_rank={extra}')
    print('VERIFY_OK exact_profiles=',count,'resonant_profiles=',resonant,'matrix_entries=',entries)
