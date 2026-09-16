import itertools
from flipsearch import strand_of_facets
def cycle_edges(n,off):
    return [(off+i,off+(i+1)%n) for i in range(n)]
def join_complex(E1,E2):
    return [frozenset((a,b,c,d)) for (a,b) in E1 for (c,d) in E2]
m=6; n_=6
E1=cycle_edges(m,0); E2=cycle_edges(n_,m)
J=join_complex(E1,E2)
N=12
nbr=[0]*N
for F in J:
    for a,b in itertools.combinations(sorted(F),2):
        nbr[a]|=(1<<b); nbr[b]|=(1<<a)
ne=sum(bin(x).count('1') for x in nbr)//2
print('f1=',ne)
from collections import Counter
prof=Counter()
tot=Counter()
for mask in range(1,1<<N):
    W=[v for v in range(N) if (mask>>v)&1]
    s=len(W)
    rem=mask; comp=0
    while rem:
        comp+=1
        v=(rem&(-rem)).bit_length()-1
        stack=(1<<v); seen=0
        while stack:
            u=(stack&(-stack)).bit_length()-1
            stack^=(1<<u)
            if (seen>>u)&1: continue
            seen|=(1<<u)
            stack|= (nbr[u]&mask&~seen)
        rem&=~seen
    if comp>1:
        col=tuple(sorted((v%2 if v<6 else 2+((v-6)%2)) for v in W))
        prof[(s,col)]+=(comp-1)
        tot[s]+=(comp-1)
print('tot by size:',dict(tot))
for k in sorted(prof): print(k,prof[k])
