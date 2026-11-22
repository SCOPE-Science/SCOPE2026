"""Independent state-by-state orbit, entry-time, and basin checks for GF(2) and GF(4).
The coefficient matrix has only 0/1 entries, so GF(4) coordinate addition is bitwise XOR.
Usage: python3 verify_orbits.py. Only standard Python is needed.
"""
from collections import Counter,defaultdict

def map_for(m,n,q):
    d=m+n
    neighbors=[[] for _ in range(d)]
    for i in range(m):
        for j in range(n):
            if i==0 and j==0:continue
            neighbors[i].append(m+j)
            neighbors[m+j].append(i)
    weights=[q**i for i in range(d)]
    def forward(state):
        a=[]
        for _ in range(d):a.append(state%q);state//=q
        b=[0]*d
        for i,neighbors_i in enumerate(neighbors):
            for j in neighbors_i:b[i]^=a[j]
        return sum(z*w for z,w in zip(b,weights))
    return forward

def prediction(m,n,q):
    N=m+n
    if m%2==n%2==0:
        depth={0:q**4,1:q**N-q**4}
        orbits={1:1,3:(q*q-1)//3,6:(q**4-q*q)//6}
        r=4
    elif m%2==n%2==1:
        depth={0:1,1:q**(N-4)-1,2:q**(N-2)-q**(N-4),3:q**N-q**(N-2)}
        orbits={1:1};r=0
    else:
        depth={0:q*q,1:q**(N-2)-q*q,2:q**(N-1)-q**(N-2),3:q**N-q**(N-1)}
        orbits={1:q,2:(q*q-q)//2};r=2
    return {k:v for k,v in depth.items() if v},orbits,r

def analyze(m,n,q):
    F=map_for(m,n,q)
    total=q**(m+n)
    nxt=[F(x) for x in range(total)]
    info=[None]*total
    attractor=Counter(); basin=Counter(); first=Counter()
    for x in range(total):
        seen={};cur=x;trace=[]
        while cur not in seen and info[cur] is None:
            seen[cur]=len(trace);trace.append(cur);cur=nxt[cur]
        if info[cur] is None:
            start=seen[cur];orb=tuple(sorted(trace[start:]));period=len(orb)
            for j in range(len(trace)-1,start-1,-1):
                info[trace[j]]=(orb,0)
            for j in range(start-1,-1,-1):
                info[trace[j]]=(orb,start-j)
        else:
            orb,d=info[cur]
            for z in reversed(trace):
                d+=1;info[z]=(orb,d)
        orb,d=info[x]
    for orb,d in info:
        basin[orb]+=1;first[d]+=1
    for orb in basin:attractor[len(orb)]+=1
    depths,wanted_orbits,r=prediction(m,n,q)
    assert first==Counter(depths),(m,n,q,'depth',first,depths)
    assert attractor==Counter(wanted_orbits),(m,n,q,'orbits',attractor,wanted_orbits)
    assert all(value==len(orb)*q**(m+n-r) for orb,value in basin.items()),(m,n,q,'basins')
    return total

def run():
    cases=[];states=0
    for m in range(2,5):
        for n in range(2,5):
            cases.append((m,n,2))
    for m,n in [(2,2),(2,3),(3,2),(3,3),(2,4),(4,2)]:
        cases.append((m,n,4))
    for m,n,q in cases:states+=analyze(m,n,q)
    print('INDEPENDENT_ORBIT_BASIN_CHECKS_PASSED',len(cases),'cases',states,'states')

if __name__=='__main__':run()
