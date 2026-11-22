"""Independent binary-cut encoding and exact rational-series checks."""
from itertools import product,combinations
from fractions import Fraction

def bit_to_comp(bits):
    c=[];v=1
    for i,b in enumerate(bits):
        if b==1:c.append(v);v=1
        else:v+=1
    assert v==1
    return tuple(c)

def comp_to_bits(c):
    return tuple(bit for a in c for bit in ((0,)*(a-1)+(1,)))

def admissible_binary_decks(bits):
    out=set()
    assert bits[-1]==1
    for i,b in enumerate(bits):
        permitted = (b==0 or i==0 or (b==1 and (bits[i-1]==1 or (i+1<len(bits) and bits[i+1]==1))))
        if permitted:
            z=bits[:i]+bits[i+1:]
            if not z or z[-1]==1:out.add(z)
    return out

def formula(n):
    # rational GFs via recurrence: A(z)=num(z)/den(z).
    def coef(num,den,N):
        a=[0]*(N+1)
        for j in range(N+1):
            a[j]= (num.get(j,0)-sum(den.get(t,0)*a[j-t] for t in den if t>0 and t<=j))//den[0]
        return a[N]
    # C(z)=(1-z)(1+z²)/[(1-z)^2-z³(1+z²)]
    comp=coef({0:1,1:-1,2:1,3:-1},{0:1,1:-2,2:1,3:-1,5:-1},n)
    # I(z)=(1-z)(1+z²-z³)/[(1-z)^2-z³(1+z²-z³)]
    isolated=coef({0:1,1:-1,2:1,3:-2,4:1},{0:1,1:-2,2:1,3:-1,5:-1,6:1},n)
    return comp,isolated

for n in range(1,12):
    bits=[w+(1,) for w in product((0,1),repeat=n-1)]
    comp={b:bit_to_comp(b) for b in bits}
    assert len(set(comp.values()))==len(bits)
    deck={b:admissible_binary_decks(b) for b in bits}
    for b in bits:
        c=comp[b];direct=set()
        for j,p in enumerate(c):
            if p==1:direct.add(c[:j]+c[j+1:])
            else:direct.add(c[:j]+(p-1,)+c[j+1:])
        assert {bit_to_comp(v) for v in deck[b]}==direct,(n,c,'invalid binary deck')
    adj={b:set() for b in bits}
    for i,u in enumerate(bits):
        for v in bits[:i]:
            if len(deck[u]&deck[v])>=2:adj[u].add(v);adj[v].add(u)
    ed=sum(map(len,adj.values()))//2
    if n>=3:
        assert ed==(n-1)*2**(n-4) if n>=4 else ed==1
    iso=sum(not a for a in adj.values())
    visited=set();cc=0
    for b in bits:
        if b in visited:continue
        cc+=1;seen={b};todo=[b]
        for u in todo:
            for v in adj[u]:
                if v not in seen:seen.add(v);todo.append(v)
        visited.update(seen)
    fcc,fiso=formula(n)
    assert (cc,iso)==(fcc,fiso),(n,cc,iso,fcc,fiso)
    print('n=%d bitwords=%d edges=%d components=%d isolated=%d PASS'%(n,len(bits),ed,cc,iso))
print('All independent bit/deck/generating-function checks PASS.')
