"""Independent literal zero-forcing checks and cyclic-window transfer enumeration.
Usage: python verify.py
"""
from collections import Counter
from itertools import combinations

def literal_forces(n,k,blue):
    adj=[]
    for v in range(n):
        adj.append(set((v+d)%n for d in range(-k,k+1) if d))
    b=set(blue)
    while len(b)<n:
        moves=[next(iter(w)) for i in tuple(b) if len(w:=adj[i]-b)==1]
        if not moves: return False
        b.add(moves[0])
    return True

def local_trigger(n,k,blue):
    b=set(blue)
    if len(b)==n:return True
    return any(v in b and sum((v+d)%n not in b for d in range(-k,k+1) if d)<=1 for v in range(n))

def trace_nontriggers(n,k):
    p=2*k; states=range(1<<p)
    arcs=[]
    for old in states:
        o=[(old>>(p-1-j))&1 for j in range(p)]
        rr=[]
        for bit in (0,1):
            w=o+[bit]
            center=w[k]
            is_trigger=center==1 and (w.count(0)<=1)
            if not is_trigger:
                nxt=((old<<1)&((1<<p)-1))|bit
                rr.append((nxt,bit))
        arcs.append(rr)
    out=Counter()
    for s in states:
        d={(s,0):1}
        for _ in range(n):
            nxt={}
            for (a,wt),num in d.items():
                for b,v in arcs[a]:
                    nxt[b,wt+v]=nxt.get((b,wt+v),0)+num
            d=nxt
        for (a,wt),num in d.items():
            if a==s:out[wt]+=num
    return out

def main():
    total=0; profiles=[]
    for k in (1,2,3):
        for n in range(2*k+1,17 if k<3 else 16):
            z=Counter()
            for mask in range(1<<n):
                blue={v for v in range(n) if mask&(1<<v)}
                observed=literal_forces(n,k,blue)
                trigger=local_trigger(n,k,blue)
                assert observed==trigger,(n,k,mask,observed,trigger)
                if observed:z[len(blue)]+=1
                total+=1
            bad=trace_nontriggers(n,k)
            for j in range(n+1):
                assert z[j]+bad[j]==__import__('math').comb(n,j),(n,k,j,z[j],bad[j])
            assert min(z)==2*k,(n,k,z)
            if n>=4*k+2:
                assert z[2*k]==(2*k-1)*n,(n,k,z[2*k])
            profiles.append((k,n,z[2*k],sum(z.values())))
    from itertools import combinations
    for k in range(1,6):
        for n in range(2*k+1,2*k+7):
            count=sum(local_trigger(n,k,blue) for blue in combinations(range(n),2*k))
            expected=(n if n==2*k+1 else k*n if n==2*k+2 else (2*k-1)*n)
            assert count==expected,(n,k,count,expected)
    print('VERIFY_OK profiles',len(profiles),'all_subsets_checked',total,'literal_dynamics=PASS','cyclic_transfer_polynomial=PASS','minimum_multiplicity=PASS','minimum_boundary_profiles=30')
    print('boundary_profiles',profiles[:10])
    print('large_profiles',profiles[-8:])

if __name__=='__main__':main()
