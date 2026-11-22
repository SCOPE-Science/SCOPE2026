"""Independent finite-field enumeration for a degree-two prime-polynomial subgroup census.
Standard library only; finite checks do not replace the all-field proof.
"""
from collections import Counter, deque
from math import prod

FIELDS = ((2,1,(0,1)),(3,1,(0,1)),(5,1,(0,1)),
          (7,1,(0,1)),(2,2,(1,1,1)),(2,3,(1,1,0,1)),(3,2,(1,0,1)))

class GF:
    def __init__(self,p,r,irr):
        self.p,self.r,self.q,self.irr=p,r,p**r,irr
        self.vec=[tuple((x//p**i)%p for i in range(r)) for x in range(p**r)]
        self.to_i={v:i for i,v in enumerate(self.vec)}
        self.add=[[self.to_i[tuple((a+b)%p for a,b in zip(self.vec[x],self.vec[y]))] for y in range(self.q)] for x in range(self.q)]
        self.neg=[self.to_i[tuple((-a)%p for a in self.vec[x])] for x in range(self.q)]
        self.mul=[[0]*self.q for _ in range(self.q)]
        for x in range(self.q):
            for y in range(self.q):
                v=[0]*(2*r-1)
                for i,a in enumerate(self.vec[x]):
                    for j,b in enumerate(self.vec[y]):v[i+j]=(v[i+j]+a*b)%p
                for i in range(2*r-2,r-1,-1):
                    z=v[i]
                    for j in range(r):v[i-r+j]=(v[i-r+j]-z*irr[j])%p
                self.mul[x][y]=self.to_i[tuple(v[:r])]
        self.one=1
        assert all(self.mul[self.one][x]==x for x in range(self.q))
        assert all(self.mul[x][y]!=0 for x in range(1,self.q) for y in range(1,self.q))
    def roots(self,b,c):
        a,m,n=self.add,self.mul,self.neg
        return [x for x in range(self.q) if a[a[m[x][x]][m[b][x]]][c]==0]
    def units(self,b,c):
        a,m,n=self.add,self.mul,self.neg
        ans=[]
        for u in range(self.q):
            for v in range(self.q):
                det=a[m[u][a[u][n[m[v][b]]]]][m[m[v][v]][c]]
                if det:ans.append((u,v))
        return ans
    def ringmul(self,b,c,x,y):
        a,m,n=self.add,self.mul,self.neg
        u,v=x;w,z=y
        return (a[m[u][w]][n[m[m[v][z]][c]]],
                a[a[m[u][z]][m[v][w]]][n[m[m[v][z]][b]]])

def gaussian(r,j,p):
    num=den=1
    for i in range(j):num*=p**(r-i)-1;den*=p**(j-i)-1
    return num//den

def expected(g,kind):
    from math import gcd
    q=g.q;out=Counter()
    if kind=='irreducible':
        for d in range(1,q*q):
            if (q*q-1)%d==0 and gcd(d,q-1)==1:out[d]=1
    elif kind=='split':
        for d in range(1,q):
            if (q-1)%d==0:out[d]=d
    else:
        for j in range(g.r+1):out[g.p**j]=gaussian(g.r,j,g.p)
    return out

def subgroups(g,b,c):
    units=g.units(b,c);identity=(g.one,0)
    assert identity in units
    mul=lambda x,y:g.ringmul(b,c,x,y)
    orders={}
    for u in units:
        order=1;v=u
        while v!=identity:
            v=mul(v,u);order+=1
            assert order<=len(units)
        orders[u]=order
    groups={frozenset((identity,))};todo=deque(groups)
    while todo:
        H=todo.popleft()
        for u in units:
            if u in H:continue
            powers=[identity]
            for _ in range(1,orders[u]):powers.append(mul(powers[-1],u))
            K=frozenset(mul(h,v) for h in H for v in powers)
            assert len(K)%len(H)==0
            if K not in groups:
                groups.add(K);todo.append(K)
    good=Counter()
    for H in groups:
        if all((u,v)==identity or v!=0 for u,v in H):good[len(H)]+=1
    return good,len(groups)

def main():
    total=0
    for p,r,irr in FIELDS:
        g=GF(p,r,irr)
        fs=[(b,c) for b in range(g.q) for c in range(g.q)]
        if g.q>7:
            fs=[]
            for kind in ('irreducible','split','repeated'):
                for b in range(g.q):
                    for c in range(g.q):
                        k={0:'irreducible',1:'repeated',2:'split'}[len(g.roots(b,c))]
                        if k==kind:fs.append((b,c));break
                    else:continue
                    break
        for b,c in fs:
            roots=g.roots(b,c)
            kind={0:'irreducible',1:'repeated',2:'split'}[len(roots)]
            got,_=subgroups(g,b,c)
            want=expected(g,kind)
            assert got==want,(g.q,b,c,kind,got,want)
            total+=1
        print('q =',g.q,'polynomials checked =',len(fs),'all order profiles agree')
    print('PASS:',total,'polynomial cases; every subgroup independently enumerated')

if __name__=='__main__':main()
