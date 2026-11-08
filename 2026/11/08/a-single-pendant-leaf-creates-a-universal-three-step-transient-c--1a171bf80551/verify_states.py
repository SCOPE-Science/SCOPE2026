"""Independent labeled-state graph simulation over GF(2) for small pendant cubes."""
from collections import Counter

def vertex_neighborhoods(n):
    V=1<<n
    nbr=[]
    for v in range(V):
        m=0
        for j in range(n):m |= 1<<(v^(1<<j))
        if v==0:m |= 1<<V
        nbr.append(m)
    nbr.append(1)
    return nbr

def update(state, masks):
    value=0
    active=state
    while active:
        low=active & -active
        value ^= masks[low.bit_length()-1]
        active ^= low
    return value

def dimensions(n):
    V=1<<n
    if n%2:return V-2,(V-2)//2,[0,1,2,3]
    return 2,1,[0,V//2-1,V-2,V-1]

def predicted(n):
    R,F,k=dimensions(n)
    hs=[1]+[2**k[t]-2**k[t-1] for t in range(1,4)]
    return {(t,p):z for t,h in enumerate(hs) for p,z in [(1,(2**F)*h),(2,(2**R-2**F)*h)] if z}

def run():
    total=0
    for n in range(1,5):
        masks=vertex_neighborhoods(n)
        N=len(masks)
        counts=Counter()
        for x in range(1<<N):
            sequence=[x]
            for k in range(5):sequence.append(update(sequence[-1], masks))
            assert sequence[3]==sequence[5]
            result=None
            for t in range(4):
                if sequence[t]==sequence[t+1]:result=(t,1);break
                if sequence[t]==sequence[t+2]:result=(t,2);break
            assert result is not None
            counts[result]+=1
        assert dict(counts)==predicted(n), (n, dict(counts), predicted(n))
        total += 1<<N
        print(f'n={n}, total={1<<N}, entrance_period_classes={dict(sorted(counts.items()))}: PASS')
    print(f'PASS: {total} complete labeled GF(2) trajectories, n=1..4, independent implementation')

if __name__=='__main__':run()
