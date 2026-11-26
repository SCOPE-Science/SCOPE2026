from itertools import product, combinations

class PrimeField:
    def __init__(self,p): self.q=p
    def add(self,a,b): return (a+b)%self.q
    def mul(self,a,b): return (a*b)%self.q
    def zero(self): return 0

class GF4:
    # 0,1,a,a+1 as 0,1,2,3; a^2=a+1
    q=4
    def add(self,a,b): return a^b
    def mul(self,a,b):
        if a==0 or b==0: return 0
        # exponent representation: 1=a^0, 2=a^1, 3=a^2, a^3=1
        exp={1:0,2:1,3:2}; val={0:1,1:2,2:3}
        return val[(exp[a]+exp[b])%3]
    def zero(self): return 0

def dot(F,x,y):
    s=0
    for a,b in zip(x,y): s=F.add(s,F.mul(a,b))
    return s

def scalar_multiple(F,x,y):
    # rank-one test without division: all 2x2 minors vanish
    n=len(x)
    return all(F.add(F.mul(x[i],y[j]), F.mul(x[j],y[i]))==0 if F.q==2 or F.q==4
               else (F.mul(x[i],y[j])-F.mul(x[j],y[i]))%F.q==0
               for i in range(n) for j in range(i+1,n))

def dependent(F,x,y):
    if F.q in (2,4):
        # subtraction=addition in characteristic 2
        return all(F.add(F.mul(x[i],y[j]),F.mul(x[j],y[i]))==0 for i in range(len(x)) for j in range(i+1,len(x)))
    return all((F.mul(x[i],y[j])-F.mul(x[j],y[i]))%F.q==0 for i in range(len(x)) for j in range(i+1,len(x)))

def verify(F,n):
    q=F.q
    V=[v for v in product(range(q), repeat=n) if any(v)]
    iso={v: dot(F,v,v)==0 for v in V}
    N={v:set() for v in V}
    for i,x in enumerate(V):
        for y in V[i+1:]:
            if dot(F,x,y)==0:
                N[x].add(y); N[y].add(x)
    hist={}
    types={}
    for i,x in enumerate(V):
        for y in V[i+1:]:
            if y not in N[x]: continue
            dep=dependent(F,x,y)
            r=1 if dep else 2
            expected=q**(n-r)-1-int(iso[x])-int(iso[y])
            actual=len(N[x]&N[y])
            assert actual==expected,(q,n,x,y,dep,iso[x],iso[y],actual,expected)
            key=('dep' if dep else 'ind',int(iso[x]),int(iso[y]))
            types.setdefault(key,set()).add(actual)
            hist[actual]=hist.get(actual,0)+1
    # Guaranteed witnesses in theorem: AA pair e1,e2 and some IA edge.
    e1=(1,)+(0,)*(n-1); e2=(0,1)+(0,)*(n-2)
    assert e2 in N[e1] and not iso[e1] and not iso[e2]
    aa=len(N[e1]&N[e2]); assert aa==q**(n-2)-1
    ia=None
    for x in V:
        if not iso[x]: continue
        for y in N[x]:
            if not iso[y] and not dependent(F,x,y):
                ia=(x,y,len(N[x]&N[y])); break
        if ia: break
    assert ia and ia[2]==q**(n-2)-2, (q,n,ia)
    assert aa!=ia[2]
    print(f'q={q} n={n} vertices={len(V)} edges={sum(map(len,N.values()))//2} common_hist={sorted(hist.items())} types={types}')

for F,n in [(PrimeField(2),3),(PrimeField(2),4),(PrimeField(3),3),(PrimeField(3),4),(GF4(),3),(PrimeField(5),3),(PrimeField(7),3)]:
    verify(F,n)
print('VERIFY_OK')


# Exact dimension-three edge-class and triangle formulas.
for F in [PrimeField(2),PrimeField(3),GF4(),PrimeField(5),PrimeField(7)]:
    q=F.q; n=3
    V=[v for v in product(range(q), repeat=n) if any(v)]
    iso={v: dot(F,v,v)==0 for v in V}
    N={v:set() for v in V}
    for i,x in enumerate(V):
        for y in V[i+1:]:
            if dot(F,x,y)==0:
                N[x].add(y); N[y].add(x)
    aa=ia=dep=0
    weighted=0
    for i,x in enumerate(V):
        for y in V[i+1:]:
            if y not in N[x]: continue
            c=len(N[x]&N[y]); weighted += c
            if dependent(F,x,y):
                assert iso[x] and iso[y]; dep += 1
            elif iso[x] != iso[y]: ia += 1
            else:
                assert not iso[x] and not iso[y]; aa += 1
    assert aa == q*(q-1)**2*(q*q-1)//2
    assert ia == q*(q-1)*(q*q-1)
    assert dep == (q*q-1)*(q-2)//2
    triangles=weighted//3
    assert weighted%3==0
    assert triangles == (q-1)*(q+1)*(q*q-3)*(q*q-2)//6
print('RANK3_COUNTS_OK')
