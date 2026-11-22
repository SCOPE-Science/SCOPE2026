#!/usr/bin/env python3
"""Exact exhaustive verification of finite undirected de Bruijn identifying-code counts.
Only Python standard library is required; no external data.
"""
from itertools import product,combinations,permutations
from collections import Counter
from pathlib import Path

def model(q):
    words=list(product(range(q),repeat=3))
    ix={w:i for i,w in enumerate(words)}
    balls=[]
    for w in words:
        neighbors={w}
        neighbors.update((a,)+w[:2] for a in range(q))
        neighbors.update(w[1:]+(a,) for a in range(q))
        balls.append(sum(1<<ix[v] for v in neighbors))
    return words,balls

def identifiable(mask,balls):
    seen=set()
    for ball in balls:
        s=mask&ball
        if s==0 or s in seen:
            return False
        seen.add(s)
    return True

def ordinary_counts(q,ks):
    words,balls=model(q)
    codes={}
    for k in ks:
        codes[k]=[]
        for comb in combinations(range(len(words)),k):
            mask=sum(1<<i for i in comb)
            if identifiable(mask,balls): codes[k].append(mask)
    return codes

def reversal_blocks(words):
    ix={w:i for i,w in enumerate(words)}
    seen=set();blocks=[]
    for i,w in enumerate(words):
        if i in seen:continue
        j=ix[w[::-1]]
        seen.update((i,j));blocks.append((1<<i)|(1<<j))
    return blocks

def reversal_counts(q):
    words,balls=model(q)
    blocks=reversal_blocks(words)
    result=Counter(); reps={}
    for sel in range(1<<len(blocks)):
        mask=0
        for i,b in enumerate(blocks):
            if sel>>i &1:mask|=b
        if identifiable(mask,balls):
            size=mask.bit_count();result[size]+=1;reps.setdefault(size,mask)
    return result,reps

def group_orbits(words,codes,q):
    ix={w:i for i,w in enumerate(words)}
    allmaps=[]
    for p in permutations(range(q)):
        for rev in (False,True):
            allmaps.append([ix[tuple(p[a] for a in (w[::-1] if rev else w))] for w in words])
    orbit_counts=Counter(); seen=set(); reps=[]
    code_set=set(codes)
    for m in sorted(codes):
        if m in seen:continue
        orbit=set()
        for perm in allmaps:
            mm=0
            for i in range(len(words)):
                if m>>i&1:mm |=1<<perm[i]
            orbit.add(mm)
        assert orbit<=code_set
        seen|=orbit
        orbit_counts[len(orbit)]+=1
        reps.append(min(orbit))
    assert seen==code_set
    return orbit_counts,reps

if __name__=='__main__':
    import time
    st=time.monotonic()
    a2=ordinary_counts(2,[3,4]);assert len(a2[3])==0 and len(a2[4])==4
    a3=ordinary_counts(3,[8,9]);assert len(a3[8])==0 and len(a3[9])==4366
    s2,r2=reversal_counts(2);assert min(s2)==5 and s2[5]==2
    s3,r3=reversal_counts(3);assert min(s3)==11 and s3[11]==117
    words,_=model(3)
    orbits,reps=group_orbits(words,a3[9],3)
    assert sum(k*v for k,v in orbits.items())==4366
    assert sum(orbits.values())==372
    # Every optimal 9-code is chiral under raw reversal.
    flip={w:i for i,w in enumerate(words)}
    for mask in a3[9]:
        rmask=sum(1<<flip[w[::-1]] for i,w in enumerate(words) if mask>>i&1)
        assert rmask!=mask
    print('binary minimum=4, count=4; reversal minimum=5, count=2')
    print('ternary minimum=9, count=4366; reversal minimum=11, count=117')
    print('natural-group orbits=',sum(orbits.values()),'orbit_sizes=',sorted(orbits.items()))
    sym_codes=[]
    blocks=reversal_blocks(words)
    _,balls=model(3)
    for selector in range(1<<len(blocks)):
        mask=0
        for i,b in enumerate(blocks):
            if selector>>i &1:mask|=b
        if mask.bit_count()==11 and identifiable(mask,balls):sym_codes.append(mask)
    sym_orbits,sym_reps=group_orbits(words,sym_codes,3)
    assert dict(orbits)=={4:1,6:15,12:356}
    assert dict(sym_orbits)=={3:5,6:17}
    assert len(sym_reps)==22
    def read_reps(name):
        lines=(Path(__file__).parent/name).read_text(encoding='utf-8').splitlines()
        assert lines[0]=='orbit_representative_codewords'
        wi={''.join(map(str,w)):i for i,w in enumerate(words)}
        ans=[]
        for line in lines[1:]:
            parts=line.split()
            assert len(parts)==len(set(parts))
            ans.append(sum(1<<wi[x] for x in parts))
        return ans
    assert read_reps('optimal_orbits.tsv')==reps
    assert read_reps('symmetric_orbits.tsv')==sym_reps
    assert 0x222c017 in a3[9]
    assert 0x128ada1 in sym_codes
    print('symmetric orbit sizes=',sorted(sym_orbits.items()))
    print('elapsed',round(time.monotonic()-st,2),'seconds; VERIFY_OK')
