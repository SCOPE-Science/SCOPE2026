"""Independent direct finite-field enumeration of two-sided ideals of radical-square-zero quiver algebras.

Run: python check_ideal_census.py
Only prime fields are used for the exhaustive checks; the accompanying proof covers every field.
"""
from itertools import combinations, product
from math import prod

def gaussian(n, k, q):
    if k < 0 or k > n:
        return 0
    num = prod(q**(n-i)-1 for i in range(k))
    den = prod(q**(k-i)-1 for i in range(k))
    return num // den

def expected(v, edges, q):
    """Coefficient list indexed by ideal dimension, from vertex subsets and Grassmannians."""
    m = len(edges)
    out = [0]*(v+m+1)
    for mask in range(1<<v):
        internal = {}
        forced = 0
        for a,b in edges:
            if (mask>>a)&1 or (mask>>b)&1:
                forced += 1
            else:
                internal[(a,b)] = internal.get((a,b), 0)+1
        poly = [1]
        for mult in internal.values():
            x = [gaussian(mult,d,q) for d in range(mult+1)]
            old = poly
            poly = [0]*(len(old)+len(x)-1)
            for i,ai in enumerate(old):
                for j,bj in enumerate(x):
                    poly[i+j] += ai*bj
        shift = mask.bit_count()+forced
        for d,c in enumerate(poly):
            out[d+shift] += c
    return out

def rref_subspaces(n,q):
    for d in range(n+1):
        for piv in combinations(range(n),d):
            cells=[(i,j) for i,p in enumerate(piv) for j in range(p+1,n) if j not in piv]
            for vals in product(range(q), repeat=len(cells)):
                rows=[[0]*n for _ in range(d)]
                for i,p in enumerate(piv): rows[i][p]=1
                for (i,j),val in zip(cells, vals): rows[i][j]=val
                yield piv,rows

def is_in_span(vec,piv,rows,q):
    vec=vec[:]
    for p,row in zip(piv,rows):
        z=vec[p]
        if z:
            for j in range(p,len(vec)):
                vec[j]=(vec[j]-z*row[j])%q
    return all(x==0 for x in vec)

def direct_count(v, edges,q):
    n=v+len(edges)
    # Basis: vertex idempotents, then arrows. Each arrow a->b is e_a * arrow * e_b.
    tab=[[None]*n for _ in range(n)]
    for i in range(v): tab[i][i]=i
    for h,(a,b) in enumerate(edges,start=v):
        tab[a][h]=h
        tab[h][b]=h
    # Multiplication maps for each algebra basis element.
    actions=[]
    for x in range(n):
        for left in (True,False):
            act=[]
            for j in range(n):
                k=tab[x][j] if left else tab[j][x]
                act.append(k)
            actions.append(act)
    cnt=[0]*(n+1)
    num_subspaces=0
    for piv,rows in rref_subspaces(n,q):
        num_subspaces+=1
        okay=True
        for row in rows:
            for act in actions:
                out=[0]*n
                for j,c in enumerate(row):
                    k=act[j]
                    if k is not None:
                        out[k]=(out[k]+c)%q
                if not is_in_span(out,piv,rows,q):
                    okay=False
                    break
            if not okay: break
        if okay: cnt[len(rows)]+=1
    return cnt,num_subspaces

def main():
    cases=[(1,[(0,0),(0,0)],2),
           (2,[(0,1),(0,1)],2),(2,[(0,1),(0,1)],3),
           (2,[(0,1),(1,0)],2),(3,[(0,1),(1,2)],2),
           (3,[(0,1),(0,2)],2),(3,[(0,1),(1,2)],3),
           (3,[(0,1),(0,1),(1,2)],2), (2,[(0,0),(0,1)],2)]
    for v,e,q in cases:
        exp=expected(v,e,q)
        got,num=direct_count(v,e,q)
        print(f'v={v},edges={e},q={q},subspaces={num},counts={got},PASS={exp==got}')
        assert exp==got,(v,e,q,exp,got)
    print('RADICAL_SQUARE_ZERO_IDEAL_DIMENSION_CENSUS_DIRECT_CHECK_PASS')
if __name__=='__main__':main()

def direct_zero_product(v, edges, q):
    n=v+len(edges)
    tab=[[None]*n for _ in range(n)]
    for i in range(v): tab[i][i]=i
    for h,(a,b) in enumerate(edges,start=v):
        tab[a][h]=h
        tab[h][b]=h
    acts=[]
    for x in range(n):
        for left in (True,False):
            acts.append([tab[x][j] if left else tab[j][x] for j in range(n)])
    ideals=[]
    for piv,rows in rref_subspaces(n,q):
        good=True
        for row in rows:
            for act in acts:
                out=[0]*n
                for j,c in enumerate(row):
                    k=act[j]
                    if k is not None:
                        out[k]=(out[k]+c)%q
                if not is_in_span(out,piv,rows,q):
                    good=False
                    break
            if not good: break
        if good: ideals.append(rows)
    count={}
    for rows in ideals:
        for cols in ideals:
            good=True
            for u in rows:
                for w in cols:
                    out=[0]*n
                    for i,a in enumerate(u):
                        if a:
                            for j,b in enumerate(w):
                                k=tab[i][j]
                                if k is not None:
                                    out[k]=(out[k]+a*b)%q
                    if any(out):
                        good=False
                        break
                if not good: break
            if good:
                key=(len(rows),len(cols))
                count[key]=count.get(key,0)+1
    return count,len(ideals)

def predicted_zero_product(v,edges,q):
    mult={}
    for a,b in edges: mult[(a,b)]=mult.get((a,b),0)+1
    result={}
    for s in range(1<<v):
        for t in range(1<<v):
            if s & t: continue
            poly={(s.bit_count(),t.bit_count()):1}
            for (a,b),m in mult.items():
                u_full=bool((s>>a)&1 or (s>>b)&1)
                v_full=bool((t>>a)&1 or (t>>b)&1)
                u_zero=bool((t>>b)&1)
                v_zero=bool((s>>a)&1)
                if (u_full and u_zero) or (v_full and v_zero):
                    poly={}
                    break
                ua=[(m,1)] if u_full else ([(0,1)] if u_zero else [(d,gaussian(m,d,q)) for d in range(m+1)])
                va=[(m,1)] if v_full else ([(0,1)] if v_zero else [(d,gaussian(m,d,q)) for d in range(m+1)])
                new={}
                for (du,dv),c in poly.items():
                    for a1,ca in ua:
                        for b1,cb in va:
                            key=(du+a1,dv+b1)
                            new[key]=new.get(key,0)+c*ca*cb
                poly=new
            for k,c in poly.items(): result[k]=result.get(k,0)+c
    return result

def run_zero_tests():
    cases=[(1,[(0,0),(0,0)],2),
           (2,[(0,1),(0,1)],2),(2,[(0,1),(0,1)],3),
           (2,[(0,1),(1,0)],2),(2,[(0,1)],3),
           (3,[(0,1),(1,2)],2),(3,[(0,1),(0,2)],2),
           (3,[(0,1),(0,1),(1,2)],2)]
    for v,edges,q in cases:
        got,num=direct_zero_product(v,edges,q)
        pred=predicted_zero_product(v,edges,q)
        assert got==pred,(v,edges,q,got,pred)
        print(f'zero-product v={v},edges={edges},q={q},ideals={num},zero_pairs={sum(got.values())},PASS=True')
    print('RADICAL_SQUARE_ZERO_ORDERED_IDEAL_ANNIHILATION_DIRECT_CHECK_PASS')

if __name__=='__main__':run_zero_tests()

def spin_zero_product(v, edges, q):
    """Independent 3-state edge-weight evaluation for the full bivariate polynomial."""
    mm={}
    for a,b in edges:
        mm[(a,b)]=mm.get((a,b),0)+1
    def times(p,r):
        out={}
        for (a,b),u in p.items():
            for (c,d),w in r.items():
                out[(a+c,b+d)]=out.get((a+c,b+d),0)+u*w
        return out
    total={}
    for colors in product((0,1,2),repeat=v):
        initial={(sum(c==1 for c in colors),sum(c==2 for c in colors)):1}
        poly=initial
        for (a,b),m in mm.items():
            f=[gaussian(m,d,q) for d in range(m+1)]
            Fx={(d,0):z for d,z in enumerate(f)}
            Fy={(0,d):z for d,z in enumerate(f)}
            base={(0,0):1}
            Xm={(m,0):1}
            Ym={(0,m):1}
            weights=[
                [times(Fx,Fy),times(Xm,Fy),Ym],
                [Xm,Xm,{}],
                [times(Fx,Ym),times(Xm,Ym),Ym],
            ]
            poly=times(poly,weights[colors[a]][colors[b]])
        for key,coef in poly.items(): total[key]=total.get(key,0)+coef
    return total

def run_spin_tests():
    for v,edges,q in [(1,[(0,0),(0,0)],2),(2,[(0,1),(0,1)],3),
                      (2,[(0,1),(1,0)],2),(3,[(0,1),(0,2)],2),
                      (3,[(0,1),(0,1),(1,2)],2)]:
        old=predicted_zero_product(v,edges,q)
        new=spin_zero_product(v,edges,q)
        assert old==new,(v,edges,q)
        print(f'spin v={v},edges={edges},q={q},terms={len(new)},PASS=True')
    print('THREE_STATE_QUVER_EDGE_MODEL_CHECK_PASS')

if __name__=='__main__':run_spin_tests()
