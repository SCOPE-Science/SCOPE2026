"""Independent recurrence and random tests, no graph NOR implementation needed.
Run: python3 verify_transport.py
"""
import random

def successor(a,b,J):
    m=len(a)
    return ([1 if j in J else a[(j-1)%m] for j in range(m)],
            [1 if (j+1)%m in J else b[(j+1)%m] for j in range(m)])

def gaps(m,J):
    js=sorted(J)
    return [((js[(i+1)%len(js)]-j-1)%m)+1 for i,j in enumerate(js)]

def test():
    rng=random.Random(7513791)
    cases=0
    for m in range(2,61):
        patterns=[{0},{m//2},set(range(m)),set(range(0,m,2))]
        patterns += [{j for j in range(m) if rng.randrange(5)==0} for _ in range(80)]
        for J in patterns:
            if not J:continue
            gs=gaps(m,J);L=max(gs)
            q=lambda t:sum(max(v-t,0) for v in gs)
            # Which coordinate original bits survive after t shifts?
            for t in sorted(set([0,1,L//2,max(0,L-1),L])):
                pa=list(range(m));pb=list(range(m))
                for _ in range(t):
                    pa,pb=([None if j in J else pa[(j-1)%m] for j in range(m)],
                           [None if (j+1)%m in J else pb[(j+1)%m] for j in range(m)])
                assert sum(x is not None for x in pa)==q(t)
                assert sum(x is not None for x in pb)==q(t)
                assert len(set(x for x in pa if x is not None))==q(t)
                assert len(set(x for x in pb if x is not None))==q(t)
            # Recover convergence of both bit streams without shortcut formulas
            for _ in range(5):
                a=[rng.randrange(2) for _ in range(m)]; b=[rng.randrange(2) for _ in range(m)]
                a0,b0=a[:],b[:]
                for t in range(L+1):
                    if t==L:assert all(a) and all(b),(m,J,a0,b0)
                    else:a,b=successor(a,b,J)
            cases+=1
    print('PASS:',cases,'fault layouts, m=2..60; direct transport and source-tracking identities.')
if __name__=='__main__':test()
