"""Independent finite-field reconstruction of Fermat cubic sixers (F2, F7)."""
from itertools import combinations

PAIRS = [((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
LABELS = [(f,a,b) for f in range(3) for a in range(3) for b in range(3)]


def check(q):
    if q == 2:
        # F4=F2[w]/(w*w+w+1): basis 1,w, w=2, w*w=3.
        def mul(a,b):
            x,y=a&1,a>>1
            u,v=b&1,b>>1
            return (x*u ^ y*v) | ((x*v ^ y*u ^ y*v)<<1)
        def sub(a,b): return a^b
        def inv(a):
            assert a
            return mul(a,a)
        roots=[1,2,3]
    elif q == 7:
        def mul(a,b): return a*b%7
        def sub(a,b): return (a-b)%7
        def inv(a): return pow(a,-1,7)
        roots=[1,2,4]
    else: raise ValueError
    rows=[]
    for f,a,b in LABELS:
        rr=[]
        for (i,j),e in zip(PAIRS[f],(a,b)):
            r=[0]*4;r[i]=1;r[j]=roots[e];rr.append(r)
        rows.append(rr)
    def rank(A):
        A=[r.copy() for r in A];n=0
        for j in range(4):
            k=next((r for r in range(n,4) if A[r][j]),None)
            if k is None: continue
            A[k],A[n]=A[n],A[k]
            u=inv(A[n][j]);A[n]=[mul(u,x) for x in A[n]]
            for r in range(4):
                if r!=n:
                    u=A[r][j]
                    A[r]=[sub(x,mul(u,y)) for x,y in zip(A[r],A[n])]
            n+=1
        return n
    meet=[[False]*27 for _ in LABELS]
    for i,j in combinations(range(27),2):
        meet[i][j]=meet[j][i]=(rank(rows[i]+rows[j])<4)
    assert sum(meet[i][j] for i,j in combinations(range(27),2))==135
    sixers=[s for s in combinations(range(27),6)
            if all(not meet[i][j] for i,j in combinations(s,2))]
    assert len(sixers)==72
    sixset=set(sixers)
    partner={}
    for s in sixers:
        t=tuple(i for i in range(27) if i not in s
                and sum(meet[i][j] for j in s)==5)
        assert t in sixset
        assert sorted(next(j for j in s if not meet[i][j]) for i in t)==list(s)
        partner[s]=t
    double={frozenset((s,partner[s])) for s in sixers}
    assert len(double)==36
    fmap={i:LABELS.index((f,(q*a)%3,(q*b)%3))
          for i,(f,a,b) in enumerate(LABELS)}
    f=lambda s:tuple(sorted(fmap[i] for i in s))
    fixed_s=[s for s in sixers if f(s)==s]
    fixed_d=[d for d in double if {f(s) for s in d}==set(d)]
    split=[d for d in fixed_d if all(f(s)==s for s in d)]
    if q==2:assert (len(fixed_s),len(fixed_d),len(split))==(2,4,1)
    else: assert (len(fixed_s),len(fixed_d),len(split))==(72,36,36)
    print('F'+str(q),'27 lines, 72 sixers, 36 double-sixes; fixed:',
          len(fixed_s),len(fixed_d),'split',len(split))

if __name__=='__main__':
    for q in (2,7):check(q)
    print('VERIFY_DOUBLE_SIX_FIELD_OK')
