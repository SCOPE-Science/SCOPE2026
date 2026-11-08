#!/usr/bin/env python3
"""Finite computational tests of reflection-fixed higher path-independence complexes.

No mathematical conclusions beyond tested cases are inferred from this program.
"""
from itertools import combinations


def faces_from_original(n, r):
    m=n//2
    odd=n%2
    k=m+odd
    orbits=[(i,n-1-i) for i in range(m)]
    if odd: orbits.append((m,))
    result=set()
    for mask in range(1<<k):
        selected=[0]*n
        for j,O in enumerate(orbits):
            if mask>>j&1:
                for v in O: selected[v]=1
        run=0
        ok=True
        for v in selected:
            run=(run+1) if v else 0
            if run>r:
                ok=False;break
        if ok:result.add(mask)
    return result


def runs_ok(mask,m,r,s):
    run=0
    for i in range(m):
        run=run+1 if mask>>i&1 else 0
        if run>r:return False
    return run<=s


def faces_model(n,r):
    m=n//2; odd=n%2
    if not odd:
        return {v for v in range(1<<m) if runs_ok(v,m,r,r//2)}
    t=(r-1)//2
    return {v for v in range(1<<(m+1)) if runs_ok(v&((1<<m)-1),m,r,t if (v>>m)&1 else r)}


def matching_on_model(m,r,odd):
    n=2*m+int(odd)
    faces=faces_model(n,r)
    s=(r-1)//2 if odd else r//2
    pairs=[]
    if m>=r+2:
        matched=set()
        for f in sorted(faces):
            if not f&1 and f|1 in faces:
                pairs.append((f,f|1));matched.add(f);matched.add(f|1)
        rest=faces-matched
        block=((1<<r)-1)<<1
        assert all(not f&1 and f&block==block and not f>>(r+1)&1 for f in rest)
        t=m-r-2
        tail=set()
        for f in rest:
            tailmask=(f>>(r+2))&((1<<t)-1)
            if odd and f>>m&1:tailmask|=1<<t
            tail.add(tailmask)
        predicted_tail=faces_model(2*t+int(odd),r)
        assert tail==predicted_tail, (m,r,odd,tail,predicted_tail)
        subpairs,subcrit=matching_on_model(t,r,odd)
        def lift(f):
            return block| ((f&((1<<t)-1))<<(r+2)) | (((f>>t)&1)<<m if odd else 0)
        pairs += [(lift(a),lift(b)) for a,b in subpairs]
        critical={lift(c) for c in subcrit}
    elif not odd:
        if m==0:critical={0}
        elif m==s+1:
            pairs=[(f,f|1) for f in faces if not f&1 and f|1 in faces]
            critical={((1<<m)-1)&~1}
        else:
            j=0
            pairs=[(f,f|(1<<j)) for f in faces if not f&(1<<j)]
            assert all((f|(1<<j)) in faces for f in faces if not f&(1<<j))
            critical=set()
    elif m==s+1:
        pairs=[(f,f|1) for f in faces if not f&1 and f|1 in faces]
        critical={((1<<(m+1))-1)&~1}
    elif m==r+1:
        c=1<<m;j=1
        pairs += [(f,f|j) for f in faces if f&c and not f&j]
        assert all(f|j in faces for f in faces if f&c and not f&j)
        base={f for f in faces if not f&c}
        pairs += [(f,f|1) for f in base if not f&1 and f|1 in base]
        critical={((1<<m)-1)&~1}
    elif m==0:
        pairs=[(0,1)];critical=set()
    elif m<=s:
        c=1<<m
        pairs=[(f,f|c) for f in faces if not f&c]
        critical=set()
    else:
        c=1<<m;j=1
        pairs += [(f,f|j) for f in faces if f&c and not f&j]
        assert all(f|j in faces for f in faces if f&c and not f&j)
        base={f for f in faces if not f&c}
        pairs += [(f,f|1) for f in base if not f&1]
        assert all(f|1 in base for f in base if not f&1)
        critical=set()
    used=[]
    for a,b in pairs:
        assert a in faces and b in faces and (a & b)==a and (b.bit_count()-a.bit_count())==1
        used.extend((a,b))
    assert len(used)==len(set(used))
    assert critical==faces-set(used), (m,r,odd,critical,faces-set(used))
    return pairs,critical


def predicted(m,r,odd):
    q,b=divmod(m,r+2)
    s=(r-1)//2 if odd else r//2
    if odd:
        if b==s+1: return q*r+s
        if b==r+1: return q*r+r-1
        return None
    if b==0:return q*r-1
    if b==s+1:return q*r+s-1
    return None


def acyclic(faces,pairs,k):
    match=set(pairs)
    nodes=sorted(faces)
    indeg={f:0 for f in nodes};out={f:[] for f in nodes}
    for f in nodes:
        for j in range(k):
            if f>>j&1:continue
            g=f|1<<j
            if g not in faces:continue
            if (f,g) in match: a,b=f,g
            else:a,b=g,f
            out[a].append(b);indeg[b]+=1
    stack=[f for f,v in indeg.items() if v==0];seen=0
    while stack:
        f=stack.pop();seen+=1
        for g in out[f]:
            indeg[g]-=1
            if indeg[g]==0:stack.append(g)
    return seen==len(nodes)


def main():
    checked=0;edges=0;max_faces=0
    for n in range(2,23):
        m=n//2
        for r in range(1,10):
            F=faces_from_original(n,r)
            assert F==faces_model(n,r),(n,r)
            pairs,crit=matching_on_model(m,r,n%2)
            k=m+n%2
            assert acyclic(F,pairs,k), (n,r)
            want=predicted(m,r,n%2)
            if want is None:
                assert not crit,(n,r,crit)
            else:
                assert len(crit)==1 and next(iter(crit)).bit_count()-1==want,(n,r,crit,want)
            checked+=1;max_faces=max(max_faces,len(F));edges+=sum(f.bit_count() for f in F)
    print('REFLECTION_PATH_EXACT_ORBITS_AND_ACYCLIC_MATCHINGS_OK')
    print('cases=',checked,'direct_original_face_sets=1','max_face_count=',max_faces,'cover_relations_examined=',edges)

if __name__=='__main__':main()
