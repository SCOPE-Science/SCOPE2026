"""Finite exhaustive checker for the stated Godel S5 structural facts."""
from itertools import product
V=list(product(range(4),repeat=2))
def imp(a,b): return 3 if a<=b else b
def closure(generators):
    seen=set(generators); todo=list(seen); i=0
    while i<len(todo):
        a=todo[i]
        for b in todo[:]:
            for f in (min,max,imp):
                for u,v in ((a,b),(b,a)):
                    w=tuple(f(s,t) for s,t in zip(u,v))
                    if w not in seen: seen.add(w);todo.append(w)
        i+=1
    return seen
zero=tuple(0 for _ in V);one=tuple(3 for _ in V)
x=tuple(a for a,b in V);y=tuple(b for a,b in V)
assert len(closure((zero,one,x,y)))==342
assert len(closure((tuple(0 for _ in range(4)),tuple(3 for _ in range(4)),tuple(range(4)))))==6
for x,y in V:
    lo=min(x,y);hi=max(x,y)
    q=min(imp(imp(x,lo),hi),imp(imp(hi,x),lo))
    assert q==y,(x,y,q)
for d in range(1,10):
    n=2*d+1; original=list(range(1,n+1)); values=original[:]
    for j in range(d):
        low=min(values)
        values=[max(z,n+2 if z<=low else low) for z in values]
    assert values==[n+2]*d+original[d:]
    assert min(values)==d+1
print('PASS: 6/342 term functions, 16 exchange pairs, 9 finite hierarchy witnesses')
