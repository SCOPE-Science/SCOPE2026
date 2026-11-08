#!/usr/bin/env python3
"""Exact finite-state checker for ECA spatial-period lifting.
Only Python standard library; exact Boolean integer arithmetic.
"""
from collections import Counter, deque
import json
from pathlib import Path

RULES = range(256)
MULTIPLIERS = (1,2,3,4,5,6,7,8,9,10,11,12)


def make_rel(rule, bit):
    # matrix rows: predecessor pairs 00,01,10,11; successor 2nd bit + new bit
    ans = tuple(tuple(0 for _ in range(4)) for _ in range(4))
    mat = [list(row) for row in ans]
    for i in range(4):
        for c in range(2):
            j = 2 * (i & 1) + c
            bit_out = (rule >> (2*i+c)) & 1
            if bit_out == bit:
                mat[i][j] = 1
    return tuple(tuple(row) for row in mat)


def compose(a,b):
    return tuple(tuple(int(any(a[i][k] and b[k][j] for k in range(4)))
                       for j in range(4)) for i in range(4))

IDENTITY=tuple(tuple(int(i==j) for j in range(4)) for i in range(4))


def cycle_lengths(r):
    cur=r
    lens=[]
    for j in range(1,5):
        if any(cur[i][i] for i in range(4)):
            lens.append(j)
        cur=compose(cur,r)
    return tuple(lens)


def classify(rule):
    trans = make_rel(rule,0), make_rel(rule,1)
    found = {IDENTITY: ""}
    todo=deque([IDENTITY])
    while todo:
        x=todo.popleft()
        for b in range(2):
            y=compose(x,trans[b])
            if y not in found:
                found[y]=found[x]+str(b)
                todo.append(y)
    available={r:cycle_lengths(r) for r in found if cycle_lengths(r)}
    def period_lifts(relation, k):
        p=IDENTITY
        for _ in range(k):
            p=compose(p,relation)
        return any(p[i][i] for i in range(4))
    m=next(j for j in MULTIPLIERS if all(period_lifts(r,j) for r in available))
    return m,found,available


def literal_rule(rule, source):
    n=len(source)
    return tuple((rule >> (4*source[(i-1)%n]+2*source[i]+source[(i+1)%n]))&1 for i in range(n))


def raw_periods(rule,n):
    """Direct enumerator (independent of matrix multiplication) for n<=3."""
    maps=[]
    for k in range(1,5):
        N=k*n
        seen=set()
        for x in range(1<<N):
            src=tuple((x>>i)&1 for i in range(N))
            out=literal_rule(rule,src)
            if all(out[i]==out[i%n] for i in range(n,N)):
                seen.add(out[:n])
        maps.append(seen)
    return maps


def verify():
    counts=Counter()
    details={}
    for rule in RULES:
        m, found, available = classify(rule)
        counts[m]+=1
        assert m in (1,2,4,6),(rule,m)
        for relation in available:
            for k in (m,12):
                p=IDENTITY
                for _ in range(k):p=compose(p,relation)
                assert any(p[i][i] for i in range(4)),(rule,k)
        for n in (1,2,3):
            observed=raw_periods(rule,n)
            for y in __import__('itertools').product((0,1),repeat=n):
                mat=IDENTITY
                t=make_rel(rule,0),make_rel(rule,1)
                for b in y:
                    mat=compose(mat,t[b])
                allowed=bool(cycle_lengths(mat))
                assert allowed == any(y in s for s in observed),(rule,n,y)
                for k in range(1,5):
                    # Period k*n lift iff power k relation has diagonal
                    mk=IDENTITY
                    for _ in range(k):mk=compose(mk,mat)
                    exact=any(mk[i][i] for i in range(4))
                    assert exact == (y in observed[k-1]),(rule,n,k,y)
        details[str(rule)]={'least_multiplier':m,'reachable_relations':len(found),'periodic_relations':len(available)}
    assert counts == Counter({1:156,2:82,4:6,6:12}),counts
    assert [r for r in RULES if details[str(r)]['least_multiplier']==4]==[90,94,122,133,161,165]
    assert [r for r in RULES if details[str(r)]['least_multiplier']==6]==[22,30,86,104,106,120,135,149,151,169,225,233]
    for r, witnesses in ((90,['1']),(30,['1','011'])):
        _, found, available=classify(r)
        trans=make_rel(r,0),make_rel(r,1)
        for word in witnesses:
            rel=IDENTITY
            for bit in word: rel=compose(rel,trans[int(bit)])
            assert rel in available
            print('WITNESS',r,word,available[rel])
    return counts,details


if __name__=='__main__':
    counts,details=verify()
    out=Path(__file__).with_name('classification.json')
    out.write_text(json.dumps({'definition':'least common multiplier for all periodic outputs','counts':dict(sorted(counts.items())),'rules':details},indent=2)+'\n',encoding='utf-8')
    print('VERIFY_OK',dict(sorted(counts.items())),out.name)
