#!/usr/bin/env python3
"""Exact, standalone finite-field and quotient checks for the stated F_11 family."""
from collections import Counter, defaultdict
import csv
from pathlib import Path
P = 11
SQUARES = {x*x % P for x in range(1,P)}

def chi(v):
    v %= P
    return 0 if v == 0 else (1 if v in SQUARES else -1)

def smooth(M,N):
    return ((N+2*M+2)*(N-2*M+2)*(M*M-4*N+8)) % P != 0

def ell_counts(M,N):
    f1 = lambda x: (x**4 + M*x**3 + N*x*x + M*x + 1)%P
    f2 = lambda x: (x**4 + (M-4)*x*x + N-2*M+2)%P
    f3 = lambda x: (x**4 + (M+4)*x*x + N+2*M+2)%P
    return tuple(2 + sum(1+chi(f(x)) for x in range(P)) for f in (f1,f2,f3))

def direct_fp(M,N):
    return 2+sum(1+chi(x**8+M*x**6+N*x**4+M*x*x+1) for x in range(P))

def field(d):
    assert d not in SQUARES and d%P
    F = [(a,b) for a in range(P) for b in range(P)]
    def add(u,v):return ((u[0]+v[0])%P,(u[1]+v[1])%P)
    def mul(u,v):return ((u[0]*v[0]+d*u[1]*v[1])%P,(u[0]*v[1]+u[1]*v[0])%P)
    sq = {mul(v,v) for v in F}
    def count(M,N):
        total=2
        for x in F:
            x2=mul(x,x); x4=mul(x2,x2); x6=mul(x4,x2); x8=mul(x4,x4)
            z=add(add(add(x8,mul((M,0),x6)),mul((N,0),x4)),add(mul((M,0),x2),(1,0)))
            total += 1 if z==(0,0) else (2 if z in sq else 0)
        return total
    return count

def main():
    traces = defaultdict(list)
    by_number=Counter()
    by_rank=Counter()
    for M in range(P):
        for N in range(P):
            if not smooth(M,N): continue
            counts=ell_counts(M,N)
            t=tuple(P+1-x for x in counts)
            assert direct_fp(M,N)==P+1-sum(t), (M,N,t)
            key=tuple(sorted(t))
            traces[key].append((M,N))
            by_number[P+1-sum(t)]+=1
            by_rank[sum(ti%P!=0 for ti in t)]+=1
    assert len(traces)==28 and sum(map(len,traces.values()))==91
    assert by_rank == {1:18,2:45,3:28},by_rank
    assert by_number == {4:10,8:15,12:26,16:23,20:12,24:5},by_number
    squares = {v*v%P for v in range(1,P)}
    split_types=set()
    nonsplit_types=set()
    parameter_rows=[]
    for triple,pairs in sorted(traces.items()):
        for M,N in sorted(pairs):
            delta=(M*M-4*N+8)%P
            split=delta in squares
            (split_types if split else nonsplit_types).add(triple)
            parameter_rows.append((M,N,delta,'split' if split else 'nonsplit',*triple,P+1-sum(triple)))
    assert (len(split_types),len(nonsplit_types),len(split_types & nonsplit_types))==(8,23,3)
    assert sum(x[3]=='split' for x in parameter_rows)==36
    assert sum(x[3]=='nonsplit' for x in parameter_rows)==55
    summary=[]
    for triple,pairs in sorted(traces.items()):
        s=sum(1 for M,N in pairs if (M*M-4*N+8)%P in squares)
        summary.append((*triple,s,len(pairs)-s,len(pairs)))
    root=Path(__file__).parent
    with (root/'spectrum_28.csv').open(newline='',encoding='utf-8') as fin:
        rows=list(csv.reader(fin))
        assert rows[0]==['t1','t2','t3','split','nonsplit','total']
        assert [tuple(int(z) for z in row) for row in rows[1:]]==summary
    with (root/'parameters_91.csv').open(newline='',encoding='utf-8') as fin:
        rows=list(csv.reader(fin))
        assert rows[0]==['M','N','delta','factorization','t1','t2','t3','n1']
        assert sorted((int(a),int(b),int(d),status,int(t1),int(t2),int(t3),int(n)) for a,b,d,status,t1,t2,t3,n in rows[1:]) == sorted(parameter_rows)
    max_pairs=sorted(pair for triple,pairs in traces.items() if P+1-sum(triple)==24 for pair in pairs)
    assert max_pairs == [(1,10),(2,10),(5,4),(6,2),(8,5)],max_pairs
    for d in (2,6):
        f=count=field(d)
        for triple,pairs in traces.items():
            t2=sum(z*z-2*P for z in triple)
            n2=P*P+1-t2
            for M,N in pairs:
                assert f(M,N)==n2,(d,M,N,triple,n2,f(M,N))
    print('HOWE_F11_SPLIT_NONSPLIT_WEIL_VERIFIED smooth=91 spectra=28 split=36 nonsplit=55 nonsplit_only_types=20 ranks=18,45,28 point_max=24 attained=5 fp2_models=2')
    print('spectrum count/traces:')
    for triple,pairs in sorted(traces.items()):print(*triple,len(pairs))
    print('point-count frequencies:',sorted(by_number.items()))
    print('maximizers:',max_pairs)
if __name__=='__main__':main()
