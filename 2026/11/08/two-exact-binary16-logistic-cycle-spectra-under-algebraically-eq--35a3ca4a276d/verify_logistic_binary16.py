"""Exact integer census for two IEEE binary16 logistic evaluations.
Run: python verify_logistic_binary16.py (Python standard library only).
Every graph vertex is one nonnegative binary16 encoding in [0,1].
"""
from bisect import bisect_right
from hashlib import sha256
import json

N=15361
U=1<<24

def scaled_value(bits):
    e=bits>>10; f=bits&1023
    return f if e==0 else (1024+f)<<(e-1)
V=[scaled_value(i) for i in range(N)]
assert V[0]==0 and V[-1]==U and all(V[i]<V[i+1] for i in range(N-1))

def rnd(n, exponent):
    """R(n/2**exponent), as a nonnegative binary16 encoding; ties to even."""
    assert 0<=n<=1<<exponent
    if exponent<=24:
        n<<=24-exponent; den=1
    else: den=1<<(exponent-24)
    i=bisect_right(V,n//den)
    if i==0: return 0
    if i==N: return N-1
    lo=i-1;hi=i
    dlo=n-V[lo]*den; dhi=V[hi]*den-n
    return lo if dlo<dhi or (dlo==dhi and lo%2==0) else hi

def single(x):
    return rnd(4*x*(U-x),48)

def square(x):
    z=2*x-U
    rz=V[rnd(abs(z),24)]
    zz=V[rnd(rz*rz,48)]
    return rnd(U-zz,24)

def census(succ):
    label=[-1]*N; dist=[-1]*N; cycles=[]
    for root in range(N):
        if label[root]>=0:continue
        path=[];loc={};p=root
        while label[p]<0 and p not in loc:
            loc[p]=len(path);path.append(p);p=succ[p]
        if p in loc:
            cyc=path[loc[p]:]; j=len(cycles);cycles.append(cyc)
            for y in cyc: label[y]=j;dist[y]=0
            tail=path[:loc[p]]
        else: tail=path
        for y in reversed(tail):label[y]=label[succ[y]];dist[y]=1+dist[succ[y]]
    assert all(x>=0 for x in label+dist)
    for v in range(N):
        assert (dist[v]==0)==(succ[v] in cycles[label[v]] and v in cycles[label[v]]) if dist[v]==0 else dist[v]==1+dist[succ[v]]
        assert label[v]==label[succ[v]]
    out=[]
    for j,cy in enumerate(cycles):
        v=min(cy); seq=[v]
        while succ[seq[-1]]!=v:seq.append(succ[seq[-1]])
        assert len(seq)==len(cy) and set(seq)==set(cy)
        out.append({'period':len(cy),'basin':label.count(j),'cycle_hex':[f'{q:04x}' for q in seq]})
    return sorted(out,key=lambda z:(z['period'],z['cycle_hex'][0])),max(dist)

def digest(succ):return sha256(b''.join(x.to_bytes(2,'little') for x in succ)).hexdigest()

def main():
    so=[single(v) for v in V];ss=[square(v) for v in V]
    a,ma=census(so);b,mb=census(ss)
    assert [(z['period'],z['basin']) for z in a]==[(1,15236),(1,8),(5,117)]
    assert [(z['period'],z['basin']) for z in b]==[(1,15048),(1,3),(8,310)]
    assert [z['cycle_hex'][0] for z in a]==['0000','3a00','2dbd']
    assert [z['cycle_hex'][0] for z in b]==['0000','3a00','2c30']
    assert (ma,mb)==(109,70)
    assert sum(s!=t for s,t in zip(so,ss))==12513
    report={'state_count':N,'semantics':'nonnegative IEEE 754 binary16, ties to even','single_round':{'cycles':a,'maximum_transient':ma,'successor_sha256':digest(so)},'completed_square':{'cycles':b,'maximum_transient':mb,'successor_sha256':digest(ss)},'different_edges':12513}
    print(json.dumps(report,indent=2,sort_keys=True))
    print('EXACT_BINARY16_LOGISTIC_CENSUS_OK')
    return report
if __name__=='__main__':main()
