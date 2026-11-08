#!/usr/bin/env python3
"""Finite checks of a four-variable neighborhood-XOR recognition criterion.
Uses only the Python standard library; no outside files are needed.
"""
from collections import Counter
from itertools import combinations


def symp(x, y, m):
    return sum(((x >> (2*i)) & 1) * ((y >> (2*i+1)) & 1) +
               ((x >> (2*i+1)) & 1) * ((y >> (2*i)) & 1)
               for i in range(m)) % 2


def symplectic_rows(m):
    v = list(range(1, 1 << (2*m)))
    return [sum(symp(x,y,m) << j for j,y in enumerate(v)) for x in v]


def xor_axiom(rows):
    n = len(rows)
    mask = (1 << n) - 1
    assert all(0 <= row <= mask for row in rows)
    assert all((row >> i) & 1 == 0 for i,row in enumerate(rows))
    assert all(((rows[i] >> j)&1) == ((rows[j] >> i)&1)
               for i in range(n) for j in range(n))
    if 0 in rows:
        return False, 'isolated'
    rowset=set(rows)
    for i in range(n):
        for j in range(i+1,n):
            if rows[i] ^ rows[j] not in rowset:
                return False, (i,j)
    return True, None


def rank2(rows):
    basis={}
    for row in rows:
        x=row
        while x:
            b=x.bit_length()-1
            if b in basis: x ^= basis[b]
            else:
                basis[b]=x
                break
    return len(basis)


def switch(rows, idx):
    n=len(rows)
    S=set(idx)
    out=rows[:]
    for j in range(n):
        if j in S: continue
        hits=sum((rows[j] >> i)&1 for i in S)
        assert hits in (0,2,4)
        if hits==2:
            for i in S:
                out[j] ^= 1<<i
                out[i] ^= 1<<j
    return out


def srg_stats(rows):
    n=len(rows)
    deg={row.bit_count() for row in rows}
    a=set(); z=set()
    for i in range(n):
        for j in range(i+1,n):
            c=(rows[i]&rows[j]).bit_count()
            if (rows[i]>>j)&1: a.add(c)
            else: z.add(c)
    return sorted(deg), sorted(a),sorted(z)


def two_pebble_extensions(rows):
    n=len(rows)
    # All four adjacency patterns to every distinct ordered pair occur
    # at a third vertex; this is sufficient for permanent 3-pebble equivalence.
    min_cells=[n]*4
    for x in range(n):
        for y in range(n):
            if x==y: continue
            counts=[0]*4
            for z in range(n):
                if z in (x,y): continue
                code=(((rows[z] >> x)&1)<<1)|((rows[z]>>y)&1)
                counts[code]+=1
            min_cells=[min(a,b) for a,b in zip(min_cells,counts)]
    return min_cells


def exhaustive_small():
    checked=0; satisfying={}
    for n in range(1,6):
        edges=list(combinations(range(n),2))
        found=0
        for bits in range(1 << len(edges)):
            rows=[0]*n
            for p,(i,j) in enumerate(edges):
                if (bits>>p)&1:
                    rows[i]|=1<<j
                    rows[j]|=1<<i
            ok,_=xor_axiom(rows)
            if ok: found+=1
            checked+=1
        satisfying[n]=found
    return checked,satisfying


def main():
    checked,counts=exhaustive_small()
    assert checked==1099 and counts=={1:0,2:0,3:1,4:0,5:0}
    for m in (1,2,3):
        rows=symplectic_rows(m)
        assert xor_axiom(rows)[0]
        assert rank2(rows)==2*m
        print('SYMPLECTIC',m,'vertices',len(rows),'two_rank',rank2(rows),'axiom',True)
    rows=symplectic_rows(3)
    # Four isotropic vertices from Abiad--Haemers, arXiv:1412.2945, section 2.
    vectors=[(1,0,1,0,1,0),(1,0,0,1,0,1),
             (0,1,1,0,0,1),(0,1,0,1,1,0)]
    def encode(t):return sum(b<<i for i,b in enumerate(t))
    S=[encode(t)-1 for t in vectors]
    assert len(set(S))==4
    assert [sum((rows[i]>>j)&1 for j in S) for i in S]==[0]*4
    switched=switch(rows,S)
    ok,witness=xor_axiom(switched)
    assert not ok and witness!='isolated'
    assert srg_stats(rows)==srg_stats(switched)==([32],[16],[16])
    assert rank2(switched)==8
    ext1=two_pebble_extensions(rows)
    ext2=two_pebble_extensions(switched)
    assert ext1==ext2==[13,15,15,16]
    print('SWITCHED', 'vertices',len(switched),'two_rank',rank2(switched),
          'axiom',ok,'failed_pair_indices',witness)
    print('SRG',srg_stats(switched),'two_fixed_min_extension_counts',ext2)
    print('EXHAUSTIVE',checked,'labelled_graphs_through_order_5',counts)
    print('VERIFICATION_OK')

if __name__=='__main__':main()
