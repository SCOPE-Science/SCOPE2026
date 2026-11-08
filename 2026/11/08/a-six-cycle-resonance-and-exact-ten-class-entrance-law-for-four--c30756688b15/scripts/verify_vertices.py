"""Separate direct labelled-vertex simulator for four-color CCA on bicliques."""
from collections import Counter
from itertools import product
from verify_supports import coeffs,predicted

def direct(m,n):
    N=m+n
    edges=[list(range(m,N)) for _ in range(m)]+[list(range(m)) for _ in range(n)]
    counts=Counter()
    for init in product(range(4),repeat=N):
        states={};q=init;time=0
        while q not in states:
            assert time<20,(m,n,init)
            states[q]=time
            nq=[]
            for i,v in enumerate(q):
                follow=(v+1)%4
                nq.append(follow if any(q[j]==follow for j in edges[i]) else v)
            q=tuple(nq)
            time+=1
        counts[(states[q],time-states[q])]+=1
    return counts

if __name__=='__main__':
    C,_,_=coeffs()
    total=0
    for m,n in [(1,1),(1,2),(1,3),(1,4),(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)]:
        got=direct(m,n);want=predicted(m,n,C)
        want={k:v for k,v in want.items() if v}
        assert dict(got)==want,(m,n,got,want)
        print('PASS',m,n,'labelled',4**(m+n),'classes',dict(sorted(got.items())))
        total+=4**(m+n)
    print('PASS all',total,'labelled states independently evolved')
