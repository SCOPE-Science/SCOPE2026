#!/usr/bin/env python3
"""Exact finite certificate verifier for the full four-cube independence quotient.

Usage: python3 verify_q4_orbit.py q4_orbit_certificate.txt
Only the standard Python library is required.
"""
import sys
from collections import Counter
from itertools import permutations

def main(path):
    vertices=range(16)
    adj=[sum(1<<(v^(1<<i)) for i in range(4)) for v in vertices]
    independent=[m for m in range(1,1<<16) if all(not (adj[v]&m) for v in vertices if (m>>v)&1)]
    indep=set(independent)
    counts=Counter(m.bit_count() for m in independent)
    assert tuple(counts[k] for k in range(1,9)) == (16,88,208,228,128,56,16,2)
    # All graph automorphisms: translation followed by a four-coordinate permutation.
    perms=[]
    for p in permutations(range(4)):
        for t in range(16):
            image=tuple(t^sum(1<<p[i] for i in range(4) if x>>i&1) for x in vertices)
            perms.append(image)
    assert len(set(perms))==384
    for p in perms:
        assert set(p)==set(vertices)
        assert all(((p[v] ^ p[v^(1<<i)]).bit_count()==1) for v in vertices for i in range(4))
    mask_maps=[]
    for p in perms:
        bit=[1<<p[v] for v in vertices]
        tr={}
        for m in independent:
            x=m; out=0
            while x:
                b=x&-x; out|=bit[b.bit_length()-1];x^=b
            assert out in indep
            tr[m]=out
        mask_maps.append(tr)
    with open(path,'rt',encoding='utf-8') as f:
        lines=f.read().splitlines()
    assert lines[0]=='faces 742 visits 4399134 unique_flags 2199938 orbits 6721'
    cells=[]; steps=[]; entered_steps=False
    for line in lines[1:]:
        el=line.split()
        if el[0]=='CELL':
            assert not entered_steps
            ident=int(el[1]); k=int(el[2]); seq=tuple(int(s) for s in el[3:])
            assert ident==len(cells) and len(seq)==k and 1<=k<=8
            assert all(s in indep for s in seq)
            assert all((a & b)==a and a!=b for a,b in zip(seq,seq[1:]))
            cells.append(seq)
        else:
            assert el[0]=='COLLAPSE' and len(el)==3
            entered_steps=True
            steps.append((int(el[1]),int(el[2])))
    assert len(cells)==6721 and len(steps)==3360
    fvec=Counter(len(c) for c in cells)
    assert tuple(fvec[i] for i in range(1,9))==(20,133,501,1217,1895,1800,945,210)
    assert sum((-1)**(k-1)*v for k,v in fvec.items())==1
    # Encode flags without hashing Python tuples of long integers. Each face is 16 bits.
    def enc(seq):
        return sum(m<<(16*i) for i,m in enumerate(seq))
    orbit={}
    for cid,seq in enumerate(cells):
        for trans in mask_maps:
            key=enc(tuple(trans[m] for m in seq))
            existing=orbit.setdefault(key,cid)
            assert existing==cid,(cid,existing)
    # Number of flags in a simplicial complex from the ordered Bell numbers.
    bell=[0,1,3,13,75,541,4683,47293,545835]
    expected=sum(counts[k]*bell[k] for k in range(1,9))
    assert len(orbit)==expected,(len(orbit),expected)
    del mask_maps
    facets=[]
    cofaces=[[] for _ in cells]
    for c,seq in enumerate(cells):
        if len(seq)==1:
            facets.append([]); continue
        ff=[]
        for j in range(len(seq)):
            key=enc(seq[:j]+seq[j+1:]);f=orbit[key]
            assert len(cells[f])+1==len(seq)
            ff.append(f)
            cofaces[f].append(c)
        assert len(set(ff))==len(ff)
        facets.append(ff)
    del orbit
    active=[True]*len(cells)
    counts_now=[len(cc) for cc in cofaces]
    for idx,(f,c) in enumerate(steps):
        assert active[f] and active[c],(idx,f,c)
        assert len(cells[c])==len(cells[f])+1
        assert f in facets[c]
        assert counts_now[f]==1,(idx,f,c,counts_now[f])
        assert sum(active[d] for d in cofaces[f])==1
        active[f]=active[c]=False
        for d in facets[f]: counts_now[d]-=1
        for d in facets[c]:
            if d!=f:counts_now[d]-=1
    left=[i for i,a in enumerate(active) if a]
    assert len(left)==1 and len(cells[left[0]])==1,(len(left),left[:10])
    print('VERIFY_OK_Q4_INDEPENDENCE_FULL_ORBIT_COLLAPSIBLE faces=742 flags=%d group=384 cells=6721 collapses=3360 remaining_vertex=%d' %(expected,left[0]))
if __name__=='__main__':
    if len(sys.argv)!=2: sys.exit('Usage: python3 verify_q4_orbit.py q4_orbit_certificate.txt')
    main(sys.argv[1])
