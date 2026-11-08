#!/usr/bin/env python3
"""Independent finite checks for the open-neighborhood complexes of matched clique pairs.
No external dependencies. Cases 4 <= m <= 8, 0 <= t <= m.
"""
from collections import defaultdict, Counter

def neighborhoods(m,t):
    ns=[]
    for i in range(m):
        ns.append((sum(1<<j for j in range(m) if i!=j) | ((1<<(m+i)) if i<t else 0)))
    for i in range(m):
        ns.append((sum(1<<(m+j) for j in range(m) if i!=j) | ((1<<i) if i<t else 0)))
    return ns

def faces(m,t):
    fs={0}
    for nbr in neighborhoods(m,t):
        sub=nbr
        while sub:
            fs.add(sub)
            sub=(sub-1)&nbr
    return fs

def expected_betti(m,t):
    out=Counter()
    if t==0:
        out[0]=1
    elif t<=2:
        out[1]=1
    elif t>=3:
        out[2]=t*t-3*t+1
    out[m-2]+=2
    return {k:v for k,v in sorted(out.items()) if v}

def betti_mod2(fs):
    levels=defaultdict(list)
    for f in fs:
        if f:
            levels[f.bit_count()-1].append(f)
    for d in levels:levels[d].sort()
    ranks={}
    for d in sorted(levels):
        if d==0:continue
        lower={f:i for i,f in enumerate(levels[d-1])}
        pivots={}
        for f in levels[d]:
            z=0;tmp=f
            while tmp:
                bit=tmp & -tmp;tmp^=bit
                face=f^bit
                z^=1<<lower[face]
            while z:
                p=z.bit_length()-1
                if p in pivots:z^=pivots[p]
                else:
                    pivots[p]=z;break
        ranks[d]=len(pivots)
    output={}
    for d in sorted(levels):
        dim=len(levels[d])-ranks.get(d,0)-ranks.get(d+1,0)
        if d==0:dim-=1
        if dim:output[d]=dim
    return output

for m in range(4,9):
    faces_by=[faces(m,t) for t in range(m+1)]
    assert all(faces_by[t]<=faces_by[t+1] for t in range(m))
    for t,fs in enumerate(faces_by):
        betti=betti_mod2(fs)
        assert betti==expected_betti(m,t),(m,t,betti,expected_betti(m,t))
    # persistence reduction with all boundary pairs
    all_faces=faces_by[-1]
    birth={f:next(t for t in range(m+1) if f in faces_by[t]) for f in all_faces if f}
    simplices=sorted(birth,key=lambda f:(birth[f],f.bit_count(),f))
    pos={f:i for i,f in enumerate(simplices)}
    reduced={}; created_nonzero=set(); bars=[]
    for i,f in enumerate(simplices):
        boundary=0;tmp=f
        while tmp:
            bit=tmp&-tmp;tmp^=bit
            face=f^bit
            if face:boundary^=1<<pos[face]
        while boundary:
            lead=boundary.bit_length()-1
            if lead in reduced: boundary^=reduced[lead]
            else:break
        if boundary:
            lead=boundary.bit_length()-1
            reduced[lead]=boundary
            created_nonzero.add(i)
            if birth[simplices[lead]]<birth[f]:
                bars.append((simplices[lead].bit_count()-1,birth[simplices[lead]],birth[f]-1))
    for i,f in enumerate(simplices):
        if i not in reduced and i not in created_nonzero:
            bars.append((f.bit_count()-1,birth[f],m))
    # for reduced homology, delete one eternal H0 bar
    essential_0=[x for x in bars if x[0]==0 and x[2]==m]
    assert len(essential_0)==1,(m,essential_0)
    bars.remove(essential_0[0]); actual=Counter(bars)
    wanted=Counter({(0,0,0):1,(1,1,2):1,(m-2,0,m):2})
    for t in range(3,m+1):
        wanted[(2,t,m)] += (1 if t==3 else 2*t-4)
    assert actual==wanted,(m,actual,wanted)
    print('m=%d count=%d all_stage_betti_and_persistence_pass'% (m,len(all_faces)-1))
print('ALL_MATCHED_CLIQUE_NEIGHBORHOOD_CHECKS_PASS')
