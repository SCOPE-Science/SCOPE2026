"""Independent brute-force / mod-3 verification of a quadratic-moment rank theorem.
Requires only Python's standard library and the accompanying kernel6.json.
"""
from itertools import permutations,combinations
from pathlib import Path
import json

def avoid231(p):
    n=len(p)
    return not any(p[b]>p[a]>p[c]
                   for a in range(n) for b in range(a+1,n)
                   for c in range(b+1,n))

def moment_keys(p):
    out = [('1',)]
    for i in range(len(p)): out.append((i,p[i]))
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            out.append((i,p[i],j,p[j]))
    return out

def rank_mod3(matrix):
    # Matrix is a sequence of sparse row dictionaries in a common column order.
    bases = {}
    for row in matrix:
        v=dict(row)
        while v:
            lead=min(v)
            if lead not in bases:
                mult=pow(v[lead],-1,3)
                bases[lead]={k:(a*mult)%3 for k,a in v.items() if (a*mult)%3}
                break
            s=v[lead]
            for k,w in bases[lead].items():
                z=(v.get(k,0)-s*w)%3
                if z: v[k]=z
                elif k in v: del v[k]
    return len(bases)

def check():
    for n, expected in [(1,1),(2,2),(3,5),(4,14),(5,42),(6,112)]:
        pp=[p for p in permutations(range(1,n+1)) if avoid231(p)]
        allkeys=sorted(set(k for p in pp for k in moment_keys(p)),key=repr)
        index={k:i for i,k in enumerate(allkeys)}
        rows=[{index[k]:1 for k in moment_keys(p)} for p in pp]
        actual=rank_mod3(rows)
        assert actual==expected,(n,actual)
        print('length',n,'Catalan_count',len(pp),'rank_mod_3',actual)
    pp=[p for p in permutations(range(1,7)) if avoid231(p)]
    names={''.join(map(str,p)):p for p in pp}
    cert=json.loads(Path(__file__).with_name('kernel6.json').read_text('utf-8'))
    for relation in cert:
        counts={}
        for name,sgn in relation:
            p=names[name]
            for k in moment_keys(p):counts[k]=counts.get(k,0)+sgn
        assert all(v==0 for v in counts.values())
    # Explicit globally valid signed three-cube trade, already at length six.
    for n in (6,7,8):
        words=[]
        for mask in range(8):
            q=list(range(1,n+1))
            for j in range(3):
                if mask & (1<<j): q[2*j],q[2*j+1] = q[2*j+1],q[2*j]
            assert avoid231(q)
            words.append((q,(-1)**mask.bit_count()))
        total={}
        for p,s in words:
            for k in moment_keys(p):total[k]=total.get(k,0)+s
        assert all(v==0 for v in total.values())
    print('PASS: independent brute-force enumeration, mod-3 ranks, signed moment certificates')
if __name__=='__main__': check()
