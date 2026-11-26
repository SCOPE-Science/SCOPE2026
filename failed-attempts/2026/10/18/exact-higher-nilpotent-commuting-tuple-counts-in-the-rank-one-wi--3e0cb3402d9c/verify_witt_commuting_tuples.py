"""Independent finite-field enumeration of pairwise commuting nilpotent Witt derivations.
No external packages required. Run: python verify_witt_commuting_tuples.py
"""
from itertools import product
from collections import Counter

class Field:
    def __init__(self,p,e=1):
        self.p,self.e,self.q=p,e,p**e
        self.add=[[0]*self.q for _ in range(self.q)]
        self.mul=[[0]*self.q for _ in range(self.q)]
        for a in range(self.q):
            for b in range(self.q):
                if e==1:
                    self.add[a][b]=(a+b)%p
                    self.mul[a][b]=(a*b)%p
                elif e==2:
                    a0,a1=a%p,a//p; b0,b1=b%p,b//p
                    # u^2=-1 (irreducible for p=3)
                    self.add[a][b]=(a0+b0)%p+p*((a1+b1)%p)
                    self.mul[a][b]=(a0*b0-a1*b1)%p+p*((a0*b1+a1*b0)%p)
                else: raise ValueError('unsupported extension')
        self.neg=[next(b for b in range(self.q) if self.add[a][b]==0) for a in range(self.q)]
        self.inv=[0]*self.q
        for a in range(1,self.q):self.inv[a]=next(b for b in range(1,self.q) if self.mul[a][b]==1)

def deriv_matrix(f,F):
    p=F.p; M=[[0]*p for _ in range(p)]
    for j in range(1,p):
        for i in range(p-j+1):
            M[i+j-1][j]=F.mul[f[i]][j%p]
    return M

def mm(A,B,F):
    n=len(A);out=[[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k]:
                for j in range(n):
                    if B[k][j]:out[i][j]=F.add[out[i][j]][F.mul[A[i][k]][B[k][j]]]
    return out

def rank(A,F):
    A=[r[:] for r in A];n=len(A);row=0
    for j in range(n):
        piv=next((i for i in range(row,n) if A[i][j]),None)
        if piv is None:continue
        A[piv],A[row]=A[row],A[piv]
        t=F.inv[A[row][j]]
        for h in range(j,n):A[row][h]=F.mul[t][A[row][h]]
        for i in range(row+1,n):
            factor=A[i][j]
            if factor:
                for h in range(j,n):
                    A[i][h]=F.add[A[i][h]][F.neg[F.mul[factor][A[row][h]]]]
        row+=1
    return row

def nilpotent_profile(f,F):
    M=deriv_matrix(f,F);N=M;out=[]
    for j in range(1,F.p+1):
        r=rank(N,F);out.append(r)
        if r==0:return tuple(out)
        N=mm(N,M,F)
    return None

def commute(f,g,F):
    p=F.p
    # coefficient of t^d in f*g'-g*f'
    for d in range(p):
        z=0
        for i in range(d+1):
            j=d+1-i
            if j>=p:continue
            z=F.add[z][F.mul[f[i]][F.mul[j%p][g[j]]]]
            z=F.add[z][F.neg[F.mul[g[i]][F.mul[j%p][f[j]]]]]
        if z:return False
    return True

def rankcount_formula(p,q,r,s):
    def N(t):return 1 if t==0 else (q-1)*q**(t-1)
    if r<0 or s<0 or r>=p or s>=p:return 0
    if r==0 or s==0:return N(r)*N(s)
    if r+s<=p-1:return N(r)*N(s)
    if r==s:return (q-1)**2*q**(p-2)
    return 0

def total_formula(p,q,m):
    h=(p-1)//2
    return q**(p-2)*(q**m-1)+q**(m*h)+sum(q**(p-2*k)*(q**(m*k)-q**(m*(k-1))) for k in range(2,h+1))

def test(p,e):
    F=Field(p,e);q=F.q
    nil=[];profiles={}
    for f in product(range(q),repeat=p):
        prof=nilpotent_profile(f,F)
        if prof is not None:
            nil.append(f)
            r=prof[0]
            expected=tuple((p-j if f[0] else max(0,p-1-j*(p-r-1))) for j in range(1,len(prof)+1)) if r else (0,)
            # Explicit expected rank profile, with p-r=k when r<=p-2.
            if r:
                expected=tuple(p-j if f[0] else max(0,p-1-j*(p-r-1)) for j in range(1,len(prof)+1))
                assert prof==expected,(p,q,f,prof,expected)
            profiles[f]=r
    assert len(nil)==q**(p-1),('nilpotent count',p,q,len(nil))
    table=Counter();n=len(nil);adj=[0]*n
    for i,f in enumerate(nil):
        for j,g in enumerate(nil):
            if commute(f,g,F):
                adj[i]|=1<<j
                table[(profiles[f],profiles[g])]+=1
    for r in range(p):
        for s in range(p):
            assert table[(r,s)]==rankcount_formula(p,q,r,s),(p,q,r,s,table[(r,s)],rankcount_formula(p,q,r,s))
    paircount=sum(x.bit_count() for x in adj)
    assert paircount==total_formula(p,q,2),(p,q,'pairs',paircount,total_formula(p,q,2))
    counts={1:n,2:paircount}
    # Intersections enforce pairwise commutativity independently.
    for m in (3,4):
        total=0
        for i in range(n):
            neighbors=adj[i]
            jj=neighbors
            while jj:
                low=jj&-jj;j=low.bit_length()-1;jj-=low
                both=neighbors&adj[j]
                if m==3:total+=both.bit_count()
                else:
                    kk=both
                    while kk:
                        low2=kk&-kk;k=low2.bit_length()-1;kk-=low2
                        total+=(both&adj[k]).bit_count()
        counts[m]=total
        assert total==total_formula(p,q,m),(p,q,m,total,total_formula(p,q,m))
    print('OK',p,q,'nilpotents',n,'tuples',counts,'support',[x for x in sorted(table) if table[x]>0],flush=True)

if __name__=='__main__':
    for pp,ee in [(3,1),(3,2),(5,1)]:test(pp,ee)
    print('VERIFY_OK_WITT_ALL_ARITY_NILPOTENT_COMMUTING',flush=True)
