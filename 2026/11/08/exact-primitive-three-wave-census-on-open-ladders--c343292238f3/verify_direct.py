"""Independent direct dynamics and unnormalized color-pair transfer.
Run: python3 verify_direct.py (Python standard library only)."""
from itertools import product

C=list(product(range(3),repeat=2))

def advance(colors,n):
    new=list(colors)
    for row in range(2):
        for col in range(n):
            i=row*n+col
            c=colors[i]
            if c==1: new[i]=2
            elif c==2: new[i]=0
            else:
                neigh=[colors[(1-row)*n+col]]
                if col: neigh.append(colors[row*n+col-1])
                if col+1<n: neigh.append(colors[row*n+col+1])
                new[i]=int(1 in neigh)
    return tuple(new)

def direct(n):
    tally=0
    for state in product(range(3),repeat=2*n):
        z=state
        for _ in range(3): z=advance(z,n)
        if z==state and advance(state,n)!=state:
            tally+=1
    return tally

def ok(mid,left,right):
    for row in (0,1):
        wanted=(mid[row]+1)%3
        avail=[mid[1-row]]
        if left is not None: avail.append(left[row])
        if right is not None: avail.append(right[row])
        if wanted not in avail: return False
    return True

def dp(max_n):
    weights={(a,b):1 for a in C for b in C if ok(a,None,b)}
    counts={2:sum(w for (a,b),w in weights.items() if ok(b,a,None))}
    for n in range(3,max_n+1):
        nxt={}
        for (a,b),w in weights.items():
            for c in C:
                if ok(b,a,c): nxt[(b,c)]=nxt.get((b,c),0)+w
        weights=nxt
        counts[n]=sum(w for (a,b),w in weights.items() if ok(b,a,None))
    return counts

counts=dp(30)
assert [(n,counts[n]) for n in range(2,9)] == [
    (2,0),(3,6),(4,24),(5,90),(6,324),(7,1158),(8,4128)]
for n in range(5,31):
    assert counts[n]==4*counts[n-1]-counts[n-2]-2*counts[n-3]
state_total=0
for n in range(2,7):
    got=direct(n)
    state_total+=3**(2*n)
    assert got==counts[n],(n,got,counts[n])
    print('n=%d direct=%d transfer=%d'%(n,got,counts[n]))
print('DIRECT_OK configurations=%d lengths=2..6 unnormalized_transfer=2..30'%state_total)
