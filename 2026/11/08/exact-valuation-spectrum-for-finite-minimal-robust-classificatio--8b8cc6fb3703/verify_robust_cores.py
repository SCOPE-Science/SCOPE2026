#!/usr/bin/env python3
"""Independent finite tests for exact robustness of finitely generated topologies."""
from itertools import product

def topologies(n):
    full=(1<<n)-1
    ans=[]
    for fam in range(1 << (1<<n)):
        if not (fam & 1 and fam & (1 << full)):
            continue
        elems=[s for s in range(1<<n) if fam >> s & 1]
        if all((fam >> (u|v) & 1) and (fam >> (u&v) & 1)
               for u in elems for v in elems):
            ans.append(frozenset(elems))
    return ans

def generated(n,rs):
    full=(1<<n)-1
    fam={0,full,*rs}
    while True:
        nxt=fam|{a|b for a in fam for b in fam}|{a&b for a in fam for b in fam}
        if len(nxt)==len(fam):return frozenset(fam)
        fam=nxt

def interior(topo,v):
    result=0
    for o in topo:
        if o&~v==0:result|=o
    return result

def signatures(n,rs,vs):
    full=(1<<n)-1
    out=[]
    for v in vs:
        core=0
        for x in range(n):
            u=full
            for r in rs:
                if r >> x & 1:u &= r
            if u & ~v == 0:core |= (1<<x)
        out.append(core)
    return tuple(out)

def valid_inputs(n,m):
    for state in product(range(3),repeat=n*m):
        vs=[];rs=[]
        for i in range(m):
            v=r=0
            for x in range(n):
                s=state[i*n+x]
                if s>=1:v|=1<<x
                if s==2:r|=1<<x
            vs.append(v);rs.append(r)
        yield tuple(vs),tuple(rs)

def main():
    cases=topotests=failures=forced=0
    for n in (1,2,3,4):
        tops=topologies(n)
        assert len(tops)==[0,1,4,29,355][n]
        count=0
        for vs,rs in valid_inputs(n,2):
            count+=1
            tg=generated(n,rs)
            f=tuple(interior(tg,v) for v in vs)
            assert f == signatures(n,rs,vs)
            tf=generated(n,f)
            assert tuple(interior(tf,v) for v in vs)==f
            assert tf.issubset(tg)
            can_exact=all(a==b for a,b in zip(rs,f))
            found_exact=False
            for t in tops:
                if not set(rs).issubset(t):continue
                topotests+=1
                interiors=tuple(interior(t,v) for v in vs)
                assert all((x&~y)==0 for x,y in zip(f,interiors))
                if interiors==rs:found_exact=True
            assert can_exact==found_exact
            if not found_exact: failures+=1
            forced+=sum((x & ~y).bit_count() for x,y in zip(f,rs))
        cases+=count
        print(f'n={n}, topologies={len(tops)}, label data={count}, all tests passed')
    print('COMPLETE:',cases,'datasets;',topotests,'admissible topology comparisons;',failures,'incompatible datasets;',forced,'forced extra labels')
    print('ALL_CHECKS_OK')
if __name__=='__main__':main()

def exact_count_formula(n, rs):
    """Compute maximal nonrobust signature blocks without calling topology code."""
    masks=[sum((1<<i) for i,r in enumerate(rs) if r>>x&1) for x in range(n)]
    counts=[]; extremal=[]
    for i,r in enumerate(rs):
        outside=[x for x in range(n) if not (r>>x&1)]
        distinct=set(masks[x] for x in outside)
        maximal={s for s in distinct if not any(s!=t and s&t==s for t in distinct)}
        sizes=[sum(masks[x]==s for x in outside) for s in maximal]
        e=2**(len(outside)-sum(sizes))
        for z in sizes:e*=2**z-1
        counts.append(e)
        extremal.append((len(maximal),__import__('math').prod(sizes)))
    return __import__('math').prod(counts),counts,extremal

def count_tests():
    checked=0
    for n in (1,2,3,4,5):
        full=(1<<n)-1
        for rs in product(range(1<<n),repeat=2):
            value=exact_count_formula(n,rs)[0]
            topo=generated(n,rs)
            observed=0
            for vs in product(range(1<<n),repeat=2):
                if not all((r&~v)==0 for r,v in zip(rs,vs)):continue
                if all(interior(topo,v)==r for r,v in zip(rs,vs)):
                    observed+=1
            assert observed==value,(n,rs,observed,value)
            checked+=1
        print(f'n={n} exact-completion-count formulas validated for {2**(2*n)} robust-region pairs')
    print('EXACT_COUNTS_OK:',checked,'robust-region pairs')

if __name__=='__main__':count_tests()
