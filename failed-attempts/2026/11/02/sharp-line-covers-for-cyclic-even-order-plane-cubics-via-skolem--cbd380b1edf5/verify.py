"""Independent finite checks of a Skolem-based cubic-point line covering.
The general theorem uses the classical Skolem existence theorem and a symbolic proof.
"""

def skolem_pairs(sequence):
    m=len(sequence)//2
    assert len(sequence)==2*m
    pairs=[]
    for j in range(1,m+1):
        positions=[i+1 for i,v in enumerate(sequence) if v==j]
        assert len(positions)==2 and positions[1]-positions[0]==j
        pairs.append(tuple(positions))
    return pairs

def cover(m,seq):
    pairs=skolem_pairs(seq)
    triples=[(j,m+a,m+b) for j,(a,b) in enumerate(pairs,1)]
    assert sorted(v for triple in triples for v in triple)==list(range(1,3*m+1))
    N=6*m; h=3*m
    core=[t for t in triples if h in t]
    assert len(core)==1
    a,b=sorted(v for v in core[0] if v!=h)
    assert a+b==h
    lines=[]
    for u,v,w in triples:
        if w==h: continue
        assert u+v==w
        lines.extend([(u,v,(-w)%N),((-u)%N,(-v)%N,w)])
    lines.extend([(h,a,b),(h,(-a)%N,(-b)%N),(0,a,(-a)%N)])
    assert len(lines)==2*m+1
    assert all(len(set(t))==3 and sum(t)%N==0 for t in lines)
    assert set.union(*(set(t) for t in lines))==set(range(N))
    assert sum(range(N))%N==h
    return len(lines),len(set.union(*(set(t) for t in lines)))

if __name__=='__main__':
    for m,seq in [(1,[1,1]),(4,[4,2,3,2,4,3,1,1]),(5,[4,1,1,5,4,2,3,2,5,3])]:
        assert cover(m,seq)==(2*m+1,6*m)
    for p in [5,23,29,47,53,71]:
        if p%24 not in (5,23):continue
        residues={x*x%p for x in range(p)}
        count=1+sum((1 if (x*x*x+1)%p==0 else 2 if (x*x*x+1)%p in residues else 0) for x in range(p))
        assert count==p+1
    print('VERIFY_OK')
