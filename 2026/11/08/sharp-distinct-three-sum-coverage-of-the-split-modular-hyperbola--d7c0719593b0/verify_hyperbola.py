"""Independent finite-field checks for restricted threefold sums of (u,u^-1)."""
import itertools
from collections import defaultdict

class FiniteField:
    def __init__(self, p, d=1, nonsquare=None):
        assert p >= 5 and d in (1,2)
        self.p, self.d, self.q = p,d,p**d
        if d == 2:
            assert nonsquare is not None and pow(nonsquare, (p-1)//2, p)==p-1
            self.eta = nonsquare
        self.add_table = [[self.add(x,y) for y in range(self.q)] for x in range(self.q)]
        self.mul_table = [[self.mul(x,y) for y in range(self.q)] for x in range(self.q)]
        self.one=1
        self.inv={x:self.power(x,self.q-2) for x in range(1,self.q)}
        self.squares={self.mul(x,x) for x in range(1,self.q)}

    def const(self,n):return n%self.p
    def add(self,a,b):
        if self.d==1:return (a+b)%self.p
        p=self.p;return (a%p+b%p)%p+p*((a//p+b//p)%p)
    def neg(self,a):
        if self.d==1:return (-a)%self.p
        p=self.p;return (-a%p)+p*((-(a//p))%p) # for a//p in [0,p)
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):
        p=self.p
        if self.d==1:return a*b%p
        a0,a1=a%p,a//p;b0,b1=b%p,b//p
        return (a0*b0+self.eta*a1*b1)%p+p*((a0*b1+a1*b0)%p)
    def power(self,a,e):
        ans=1
        while e:
            if e&1:ans=self.mul(ans,a)
            a=self.mul(a,a);e//=2
        return ans
    def chi(self,a):return 0 if a==0 else 1 if a in self.squares else -1


def check(p,d=1,eta=None):
    f=FiniteField(p,d,eta);q=f.q
    add=f.add_table;mul=f.mul_table;sub=f.sub;inv=f.inv
    four=f.const(4);nine=f.const(9);three=f.const(3)
    minus3=f.const(-3)
    cnt=defaultdict(int)
    for x,y,z in itertools.combinations(range(1,q),3):
        a=add[x][add[y][z]]
        b=add[inv[x]][add[inv[y]][inv[z]]]
        cnt[(a,b)]+=6
    for s in range(q):
        for t in range(q):
            c=mul[s][t]
            if s==0 and t==0:
                pred=2*(q-1) if (q-1)%3==0 else 0
            elif c==1:
                pred=3*(q-3)
            elif c==0 or c==nine:
                pred=q-6-f.chi(minus3)
            else:
                delta=mul[sub(c,1)][sub(c,nine)]
                r=1+f.chi(delta)
                summ=0
                for x in range(q):
                    h=sub(mul[t][x],1)
                    j=sub(s,x)
                    D=mul[mul[h][j]][sub(mul[h][j],mul[four][x])]
                    summ+=f.chi(D)
                pred=q+summ-4-3*r
            got=cnt[(s,t)]
            if got != pred:
                raise AssertionError(f'q={q}, target=({s},{t}), predicted {pred}, direct {got}')
    holes=q*q-sum(v>0 for v in cnt.values())
    expected_holes=int((q%3)==2) if q>=23 else None
    if q>=23: assert holes==expected_holes, (q,holes,expected_holes)
    print(f'PASS q={q} targets={q*q} ordered_distinct_triples={(q-1)*(q-2)*(q-3)} missing={holes}')
    return q*q

if __name__=='__main__':
    totals=[]
    for p in [5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67]:
        totals.append(check(p))
    for p,eta in [(5,3),(7,6),(11,10)]:totals.append(check(p,2,eta))
    print(f'VERIFY_OK levels={len(totals)} target_fibers={sum(totals)}')
