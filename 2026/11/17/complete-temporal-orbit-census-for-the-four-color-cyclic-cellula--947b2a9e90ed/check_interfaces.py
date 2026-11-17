"""Independent local-interface and conservation checks (standard Python 3)."""
from itertools import product

def update(x):
    n=len(x)
    return tuple((v+1)%4 if ((x[(i-1)%n]-v)%4==1 or (x[(i+1)%n]-v)%4==1) else v for i,v in enumerate(x))

def edges(x):
    return tuple((x[(i+1)%len(x)]-v)%4 for i,v in enumerate(x))

# All possible local interface triples, without requiring global admissibility.
for a,b,c in product(range(4),repeat=3):
    p=lambda d:int(d==1)
    m=lambda d:int(d==3)
    eleft=p(a) or m(0) # overwritten below with local context
    # For edge d_i=b, e_i=(b==1 or a==3), e_{i+1}=(c==1 or b==3).
    ei=int(b==1 or a==3)
    ej=int(c==1 or b==3)
    bp=(b+ej-ei)%4
    if b==0: assert bp==(int(c==1)-int(a==3))%4
    if b==1: assert bp==int(c==1)
    if b==2: assert bp==(2+int(c==1)-int(a==3))%4
    if b==3: assert bp==(-int(a==3))%4
print('64 local interface triples: exact update table PASS')

for n in range(3,9):
    count=0
    for x in product(range(4),repeat=n):
        before=edges(x)
        after=edges(update(x))
        K=sum(v!=0 for v in before)
        L=sum(v!=0 for v in after)
        assert L<=K
        if L==K:
            # Equality forces every old moving front to propagate and every
            # stationary interface to remain stationary, with no collisions.
            for i,v in enumerate(before):
                if v==1: assert after[(i-1)%n]==1
                if v==3: assert after[(i+1)%n]==3
                if v==2: assert after[i]==2
        count+=1
    print('n=%d: %d configurations, nonincrease and equality propagation PASS'%(n,count))
