"""Exact row/column-cardinality rectangle shattering tests; Python 3 standard library."""
from collections import Counter
from itertools import combinations, product
from math import comb


def star_types(edges):
    left={i for i,j in edges}; right={j for i,j in edges}
    dl={i:0 for i in left}; dr={j:0 for j in right}
    for i,j in edges:
        dl[i]+=1;dr[j]+=1
    if any(dl[i]>1 and dr[j]>1 for i,j in edges):return None
    seen=set(); ans=[]
    for i,j in edges:
        if ('L',i) in seen or ('R',j) in seen:continue
        if dr[j]>1:
            c=('R',j); leaves=[('L',ii) for ii,jj in edges if jj==j]
            ans.append(('R',len(leaves)))
        else:
            c=('L',i); leaves=[('R',jj) for ii,jj in edges if ii==i]
            ans.append(('L',len(leaves)))
        seen.add(c);seen.update(leaves)
    return ans


def inventory_test(edges,m,n,r,s):
    types=star_types(edges)
    if types is None:return False
    l=len({i for i,j in edges});t=len({j for i,j in edges})
    if l>r or t>s:return False
    outer=(m-l,n-t)
    for hvec in product(*(range(d+1) for _,d in types)):
        # Count only possible row/column selected totals, not their multiplicities.
        states={(a,b) for a in range(min(r,outer[0])+1)
                      for b in range(min(s,outer[1])+1)}
        for (orientation,d),h in zip(types,hvec):
            if h: choices=[(1,h)] if orientation=='L' else [(h,1)]
            elif orientation=='L': choices=[(0,i) for i in range(d+1)]+[(1,0)]
            else: choices=[(i,0) for i in range(d+1)]+[(0,1)]
            states={(a+c,b+e) for a,b in states for c,e in choices
                    if a+c<=r and b+e<=s}
        if (r,s) not in states:return False
    return True


def direct_test(edges,m,n,r,s):
    visible=set()
    for A in combinations(range(m),r):
        for B in combinations(range(n),s):
            visible.add(tuple(int(i in A and j in B) for i,j in edges))
    return len(visible)==2**len(edges)


def stable_component_formula(m,n,r,s):
    # Independent labeled enumeration of all connected-star-forest types on
    # a chosen active-vertex set, rather than enumerating grid supports.
    coef=Counter({0:1})
    for l in range(1,r+1):
        for t in range(1,s+1):
            active=list(product(range(l),range(t)))
            w=comb(m,l)*comb(n,t)
            for mask in range(1,1<<len(active)):
                E=[e for k,e in enumerate(active) if mask>>k&1]
                if len({i for i,j in E})<l or len({j for i,j in E})<t:continue
                if star_types(E) is not None:coef[len(E)]+=w
    return dict(sorted(coef.items()))


def main():
    for m,n,r,s in [(2,3,1,1),(3,3,2,2),(4,4,2,3),(4,5,2,3)]:
        q=min(r+s-1,m*n)
        seen=0
        for k in range(q+1):
            for E in combinations(product(range(m),range(n)),k):
                assert inventory_test(E,m,n,r,s)==direct_test(E,m,n,r,s)
                seen+=1
        print('EXACT_COEFFICIENT_TEST',m,n,r,s,'supports',seen)
    for m,n,r,s,expected in [(4,6,2,3,{0:1,1:24,2:276,3:800}),
                              (6,6,3,3,{0:1,1:36,2:630,3:6240,4:3600})]:
        v=stable_component_formula(m,n,r,s)
        assert v==expected,(v,expected)
        print('STABLE_FOREST_COUNT',m,n,r,s,repr(v))
    print('INVENTORY_PASS')

if __name__=='__main__':main()
