"""Exact finite-graph certificate and bounded direct checks for a cyclic binary automaton.
Run: python3 verify.py (Python standard library only).
"""
from collections import defaultdict

POTENTIAL = [
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    -1,0,0,-1,0,0,0,0,-2,0,0,-1,0,0,0,0,
    -1,0,0,-1,-2,0,0,-1,0,0,0,0,0,0,0,0,
    -1,0,0,-1,-2,0,0,-1,-2,0,0,-1,0,0,0,0,
]
assert len(POTENTIAL)==64
checks=0

def kbit(a,b,c,d):
    return b ^ (a & (1^c) & d)

def sbit(v,j):
    return (v>>j)&1

def K(v,n):
    def bit(i): return sbit(v,i%n)
    return sum(kbit(bit(i-1),bit(i),bit(i+1),bit(i+2))<<i for i in range(n))

def F(v,n):
    def bit(i): return sbit(v,i%n)
    return sum((bit(i+1)^bit(i+2)^
        (bit(i)&(1^bit(i+2))&bit(i+3))^
        (bit(i+1)&(1^bit(i+3))&bit(i+4)))<<i
        for i in range(n))

def D(v,n):
    return sum((sbit(v,i)^sbit(v,(i+1)%n))<<i for i in range(n))

def shift(v,n):
    return sum(sbit(v,(i+1)%n)<<i for i in range(n))

# All graph edges are enumerated without data files.
edges=[]
for u in range(64):
    a,b,c=((u>>2*j)&3 for j in range(3))
    for d in range(4):
        xs=[v&1 for v in (a,b,c,d)]
        zs=[v>>1 for v in (a,b,c,d)]
        if kbit(*xs) ^ kbit(*zs) != 1: continue
        v=b|(c<<2)|(d<<4)
        wt=(b&1)^(b>>1)
        edges.append((u,v,wt))
assert len(edges)==128
checks+=256

zero=defaultdict(list); one=[]
for u,v,w in edges:
    r=3*w-1+POTENTIAL[u]-POTENTIAL[v]
    assert r>=0,(u,v,w,r)
    if r==0:zero[u].append(v)
    if r==1:one.append((u,v))
    checks+=1
assert len(one)==16
for u,v in one:
    # No directed zero-cost path can return from v to u.
    seen={v}; todo=[v]
    for a in todo:
        for b in zero[a]:
            if b not in seen:
                seen.add(b);todo.append(b)
                checks+=1
    assert u not in seen, (u,v)
    checks+=1

# Patterns are symbols s=x+2z. No graph cycle can have smaller
# Hamming weight than the theorem, and these attain equality.
def pair_word(n):
    if n%3==0: return '302'*(n//3)
    if n%3==1: return '2' if n==1 else '3132'+'302'*(n//3-1)
    return '12'+'302'*(n//3)

def target(n):
    k,r=divmod(n,3)
    return k+(r==1)+2*(r==2)

def pair_valid(s):
    n=len(s)
    for i in range(n):
        a,b,c,d=[int(s[(i+j-1)%n]) for j in range(4)]
        x=[v&1 for v in (a,b,c,d)]
        z=[v>>1 for v in (a,b,c,d)]
        if kbit(*x)^kbit(*z) != 1:return False
    return True

for n in range(1,201):
    w=pair_word(n)
    assert len(w)==n and pair_valid(w)
    assert sum((int(s)&1)^(int(s)>>1) for s in w)==target(n)
    checks+=n+1

# The repetition argument is finite: for each family, after two
# repetitions every possible 4-symbol cyclic window has appeared.
for r in range(3):
    def windows(n):
        w=pair_word(n)
        return {''.join(w[(i+j)%n] for j in range(4)) for i in range(n)}
    base=set()
    for k in range(0,4):
        n=3*k+r
        if n>=1: base|=windows(n)
    for k in range(4,50):
        n=3*k+r
        assert windows(n)<=base
        checks+=1

# Directly compare rule and factor, involution, full fibers for short rings.
for n in range(1,13):
    fibers=defaultdict(list); mask=(1<<n)-1
    for x in range(1<<n):
        k=K(x,n)
        assert K(k,n)==x
        assert F(x,n)==D(shift(k,n),n)
        deck=K(mask^k,n)
        assert deck!=x and F(deck,n)==F(x,n)
        assert (x^deck).bit_count()>=target(n)
        fibers[F(x,n)].append(x)
        checks+=4
    assert len(fibers)==(1<<(n-1))
    assert all(len(a)==2 for a in fibers.values())
    checks+=len(fibers)+1
print(f'VERIFY_OK checks={checks} edges={len(edges)} ones={len(one)}')
