"""Independent cyclic-word transfer for maximal-extinction counts, standard library only."""
from itertools import product

def terminal(q,n):
    # Collapsed alphabet: 0, 1, q-1, and all other colours (multiplicity q-3).
    weights=(1,1,1,q-3)
    words=list(product(range(4),repeat=4))
    ids={w:i for i,w in enumerate(words)}
    transitions=[]
    for w in words:
        arr=[]
        for c in range(4):
            v=w+(c,)
            p=(v[0]==1 and v[1]==0 and v[2] in (0,2) and v[3]==0 and v[4]==1)
            r=(v[2]==1 and v[3]==0 and v[4]==1)
            arr.append((ids[v[1:]], weights[c], p, r))
        transitions.append(arr)
    avoidP=0;at_most_one_R=0
    for start in range(4**4):
        # count P avoidance, and separately counts with 0 or 1 occurrence of 101.
        dpP={start:1};dpR0={start:1};dpR1={}
        for _ in range(n):
            np={};nr0={};nr1={}
            for s,v in dpP.items():
                for t,w,p,r in transitions[s]:
                    if not p:np[t]=np.get(t,0)+v*w
            for s,v in dpR0.items():
                for t,w,p,r in transitions[s]:
                    d=nr1 if r else nr0
                    d[t]=d.get(t,0)+v*w
            for s,v in dpR1.items():
                for t,w,p,r in transitions[s]:
                    if not r:nr1[t]=nr1.get(t,0)+v*w
            dpP,dpR0,dpR1=np,nr0,nr1
        avoidP+=dpP.get(start,0)
        at_most_one_R+=dpR0.get(start,0)+dpR1.get(start,0)
    a=q**n-avoidP
    b=q**n-at_most_one_R
    return a,b,a+b

if __name__=='__main__':
    expected={(4,3):(0,0,0),(4,4):(8,2,10),(4,5):(10,5,15),(4,6):(48,23,71),(4,7):(0,0,0)}
    for q,n in [(4,3),(4,4),(4,5),(4,6),(4,7),(4,8),(5,4),(5,5),(5,6),(5,7),(6,4),(6,5),(6,6),(7,4),(7,5),(7,6)]:
        a,b,c=terminal(q,n)
        if (q,n) in expected and n<=6:assert (a,b,c)==expected[q,n],(q,n,a,b,c)
        print(f'q={q} n={n} A={a} B={b} E={c}')
    print('TRANSFER_OK')
