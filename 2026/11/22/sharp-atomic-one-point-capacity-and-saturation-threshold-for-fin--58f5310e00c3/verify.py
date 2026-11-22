"""Reproducible finite checks for marked atomic one-type capacity in multiorders.
No external dependencies; run: python verify.py
"""
from itertools import product, combinations, permutations
from math import comb

def type_of(x, pars, orders, successor_indices):
    if x in pars:
        return ('=', pars.index(x))
    coords=[]
    for j, order in enumerate(orders):
        pos={v:i for i,v in enumerate(order)}
        gap=sum(pos[p]<pos[x] for p in pars)
        if j in successor_indices:
            left=next((i for i,p in enumerate(pars) if pos[p]+1==pos[x]), None)
            right=next((i for i,p in enumerate(pars) if pos[p]-1==pos[x]), None)
            coords.append((gap,left,right))
        else:
            coords.append((gap,))
    return ('u',tuple(coords))

def make_extremizer(m,q,successor_indices,perms=None):
    assert q>=1
    pars=tuple('a'+str(i) for i in range(m))
    generic={p:('g'+''.join(map(str,p))) for p in product(range(m+1),repeat=q)}
    special={(j,i,side):f's{j}_{i}_{side}' for j in successor_indices for i in range(m) for side in ['L','R']}
    if perms is None:
        perms=[pars for j in range(q)]
    orders=[]
    for j in range(q):
        seq=[]
        for g in range(m+1):
            seq.extend(generic[p] for p in generic if p[j]==g)
            if g==0:
                seq.extend(special[key] for key in sorted(special) if key[0]!=j)
            if g<m:
                p=perms[j][g]
                i=pars.index(p)
                if j in successor_indices:
                    seq.extend([special[j,i,'L'],p,special[j,i,'R']])
                else:
                    seq.append(p)
        orders.append(seq)
    expected=m+(m+1)**q+2*m*len(successor_indices)
    assert len(orders[0])==expected and all(len(set(v))==expected for v in orders)
    assert all(set(v)==set(orders[0]) for v in orders)
    return pars,orders,expected

def test_construct():
    cases=0
    for m in range(0,5):
        for q in range(1,4):
            for mask in range(1<<q):
                ss={j for j in range(q) if mask>>j&1}
                pp=[tuple(reversed(['a'+str(i) for i in range(m)])) if j%2 else tuple('a'+str(i) for i in range(m)) for j in range(q)]
                pars,orders,want=make_extremizer(m,q,ss,pp)
                seen={type_of(x,pars,orders,ss) for x in orders[0]}
                assert len(seen)==want,(m,q,ss,want,len(seen))
                cases+=1
    return cases

def exhaustive_small():
    checks=0
    for m,q,ss,Nmax in [(1,1,{0},9),(2,1,{0},9),(1,2,{0},7),(1,2,{0,1},7),(2,2,{0},6)]:
        expected=m+(m+1)**q+2*m*len(ss)
        for n in range(max(1,m),Nmax+1):
            base=tuple(range(n))
            pars=base[:m]
            for second in (permutations(base) if q==2 else [base]):
                orders=[base,second] if q==2 else [base]
                typ={type_of(v,pars,orders,ss) for v in base}
                assert len(typ)<=min(n,expected)
                checks+=1
    return checks

def test_random_saturation():
    cases=0
    for m in range(1,5):
        for n in range(m,21):
            if comb(n,m)>20000: continue
            actual=0
            for P in combinations(range(n),m):
                types={type_of(i,P,[tuple(range(n))],{0}) for i in range(n)}
                actual+=(len(types)==4*m+1)
            predicted=comb(n-3*m-1,m) if n-3*m-1>=m else 0
            assert actual==predicted,(m,n,actual,predicted)
            cases+=1
    return cases

if __name__=='__main__':
    a=test_construct();b=exhaustive_small();c=test_random_saturation()
    print(f'VERIFY_OK constructions={a} small_order_checks={b} random_saturation_cases={c}')
