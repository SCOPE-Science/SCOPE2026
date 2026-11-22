"""Independent automaton DP versus formal-series recurrence for hare image language."""
from math import comb
from collections import defaultdict

def formula(n):
    return sum(sum(comb(a,d)*comb(b,d) for d in range(min(a,b,c)+1))
               for a in range(n+1) for b in range(n-a+1) for c in [n-a-b])

def dynamic(n):
    # States = (phase,lastbit,unpaid #10 descents). Phase 0=before twos, 1=twos.
    dp={(0,-1,0):1}
    for k in range(n):
        nex=defaultdict(int)
        for (phase,last,debt),v in dp.items():
            if phase==0:
                for bit in (0,1):
                    nex[(0,bit,debt+int(last==1 and bit==0))]+=v
                nex[(1,-1,max(0,debt-1))]+=v
            else:
                nex[(1,-1,max(0,debt-1))]+=v
        dp=nex
    return sum(v for (phase,last,debt),v in dp.items() if debt==0)

# (1-t)(1-2t+t^2-t^3)=1-3t+3t^2-2t^3+t^4.
seq=[]
for n in range(40):
    r=dynamic(n); f=formula(n)
    assert r==f,(n,r,f)
    if n>=4:
        assert r==3*seq[n-1]-3*seq[n-2]+2*seq[n-3]-seq[n-4],(n,r)
    seq.append(r)
print('PASS two independent unbounded-length count methods n=0,...,39')
print('first terms:',seq[:15])
print('last term:',seq[-1])
