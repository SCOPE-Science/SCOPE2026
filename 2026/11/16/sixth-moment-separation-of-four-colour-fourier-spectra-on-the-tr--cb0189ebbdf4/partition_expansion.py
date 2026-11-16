"""Independent exact proof certificate using connected-component expansions.
No colouring enumeration, trigonometry, FFT, or nonstandard dependencies.
Run with: python3 partition_expansion.py
"""
from collections import Counter
from itertools import product

N=6
EDGES=((0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(0,3),(1,4),(2,5))
EXPECT={
    'cyclic':{0:3072,8:348,24:399,40:198,56:30,72:9,88:39,264:1},
    'klein':{0:3072,8:408,24:291,40:258,56:18,72:9,88:39,264:1},
}

def partitions_of_edge_subsets():
    terms=[]
    for mask in range(1<<len(EDGES)):
        parent=list(range(N))
        def find(x):
            while parent[x]!=x:
                x=parent[x]
            return x
        for j,(a,b) in enumerate(EDGES):
            if (mask>>j)&1:
                ra,rb=find(a),find(b)
                parent[ra]=rb
        roots={}
        for i in range(N):roots.setdefault(find(i),[]).append(i)
        comps=tuple(tuple(part) for part in roots.values())
        signed=(-1 if mask.bit_count()&1 else 1) * 4**len(comps)
        terms.append((comps,signed))
    assert len(terms)==512
    return terms

def spectrum(group,terms):
    hist=Counter()
    for freq in product(range(4),repeat=N):
        value=0
        for comps,coeff in terms:
            if group=='cyclic':
                allowed=all(sum(freq[i] for i in part)%4==0 for part in comps)
            else:
                allowed=True
                for part in comps:
                    x=0
                    for i in part:x ^= freq[i]
                    if x:
                        allowed=False
                        break
            if allowed:value+=coeff
        hist[abs(value)]+=1
    return dict(sorted(hist.items()))

def main():
    terms=partitions_of_edge_subsets()
    for group in ['cyclic','klein']:
        h=spectrum(group,terms)
        assert h==EXPECT[group],(group,h)
        assert sum(h.values())==4**N
        assert 4**N-h[0]==1024
        assert max(h)==264 and min(k for k in h if k)>0 and min(k for k in h if k>0)==8
        E2=sum(c*k*k for k,c in h.items())//4**N
        E4=sum(c*k**4 for k,c in h.items())//4**N
        E6=sum(c*k**6 for k,c in h.items())//4**N
        assert E2==264 and E4==2044416
        assert E6==(87824400384 if group=='cyclic' else 87789010944)
        print(group,'spectrum',h,'moments',(E2,E4,E6))
    print('PASS: independent 512-subgraph inclusion-exclusion certificate')

if __name__=='__main__':main()
