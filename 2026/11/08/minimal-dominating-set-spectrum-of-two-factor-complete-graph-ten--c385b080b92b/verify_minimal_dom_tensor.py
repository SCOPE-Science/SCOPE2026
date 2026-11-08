"""Self-contained finite checks for minimal domination in two-factor complete-graph tensor products.

Run: python verify_minimal_dom_tensor.py
No external dependencies. All-set search and predicted family construction are independent.
"""
from itertools import combinations, permutations
from collections import Counter
from math import comb


def graph(m,n):
    coords = [(i,j) for i in range(m) for j in range(n)]
    neighborhoods = []
    for i,j in coords:
        neighborhoods.append(sum(1<<k for k,(a,b) in enumerate(coords) if (i,j)==(a,b) or (i!=a and j!=b)))
    return coords, neighborhoods


def raw_family(m,n):
    coords, closed = graph(m,n)
    order=len(coords)
    all_bits=(1<<order)-1
    def dominates(mask):
        cover=0; s=mask
        while s:
            bit=s&-s; k=bit.bit_length()-1
            cover |= closed[k]; s-=bit
            if cover==all_bits:return True
        return cover==all_bits
    minimal=set(); tested=0; dominating=0
    for mask in range(1,1<<order):
        tested+=1
        if dominates(mask):
            dominating+=1
            if all(not dominates(mask^(1<<k)) for k in range(order) if (mask>>k)&1):
                minimal.add(mask)
    return minimal,tested,dominating


def predicted_family(m,n):
    family=set()
    def add(points):
        family.add(sum(1<<(i*n+j) for i,j in points))
    for i in range(m):add([(i,j) for j in range(n)])
    for j in range(n):add([(i,j) for i in range(m)])
    if m>=3 and n>=3:
        for rows in combinations(range(m),2):
            for cols in combinations(range(n),2):
                for omitted in range(4):
                    positions=[(i,j) for i in rows for j in cols]
                    add([p for k,p in enumerate(positions) if k!=omitted])
    for rows in combinations(range(m),3):
        for cols in combinations(range(n),3):
            for perm in permutations(cols):add(list(zip(rows,perm)))
    for rows in combinations(range(m),2):
        for cols in combinations(range(n),4):
            for leftcols in combinations(cols,2):
                rest=[j for j in cols if j not in leftcols]
                add([(rows[0],j) for j in leftcols]+[(rows[1],j) for j in rest])
    for cols in combinations(range(n),2):
        for rows in combinations(range(m),4):
            for top_rows in combinations(rows,2):
                rest=[i for i in rows if i not in top_rows]
                add([(i,cols[0]) for i in top_rows]+[(i,cols[1]) for i in rest])
    return family


def theoretical_coeff(m,n):
    C=lambda a,b:comb(a,b) if a>=b else 0
    out=Counter()
    out[m]+=n; out[n]+=m
    if m>=3 and n>=3:out[3]+=4*C(m,2)*C(n,2)
    out[3]+=6*C(m,3)*C(n,3)
    out[4]+=6*(C(m,2)*C(n,4)+C(n,2)*C(m,4))
    return Counter({k:v for k,v in out.items() if v})


def main():
    cases=[(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(3,6),(4,4),(4,5)]
    subsets=dominating=mins=0
    for m,n in cases:
        raw,tested,dom=raw_family(m,n)
        prediction=predicted_family(m,n)
        assert raw==prediction,(m,n,len(raw),len(prediction),raw^prediction)
        counts=Counter(mask.bit_count() for mask in raw)
        assert counts==theoretical_coeff(m,n),(m,n,counts,theoretical_coeff(m,n))
        subsets+=tested;dominating+=dom;mins+=len(raw)
    extra=[(3,8),(3,11),(4,7),(5,6),(6,8)]
    for m,n in extra:
        pred=predicted_family(m,n)
        assert Counter(mask.bit_count() for mask in pred)==theoretical_coeff(m,n)
        _,closed=graph(m,n);full=(1<<(m*n))-1
        def dom(s):
            mask=0
            while s:
                bit=s&-s;mask|=closed[bit.bit_length()-1];s-=bit
            return mask==full
        for mask in pred:
            assert dom(mask)
            assert all(not dom(mask^(1<<i)) for i in range(m*n) if (mask>>i)&1)
        if m==3 and n>=6:
            assert sorted(set(k for k,v in theoretical_coeff(m,n).items() if v))==[3,4,n]
    print(f'VERIFY_OK exhaustive_instances={len(cases)} candidate_subsets={subsets} dominating_sets={dominating} minimal_sets={mins} generated_instances={len(extra)} families=PASS coefficients=PASS gap_spectrum=PASS')

if __name__=='__main__':main()
