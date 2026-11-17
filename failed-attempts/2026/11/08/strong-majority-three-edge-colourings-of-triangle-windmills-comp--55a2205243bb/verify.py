"""Direct-definition checker for named strong-majority edge colourings of triangular windmills."""
from itertools import product
from collections import Counter

def make_graph(m):
    edges=[]
    for i in range(m):
        a,b=2*i+1,2*i+2
        edges.extend(((0,a),(0,b),(a,b)))
    adjacent=[]
    for i,e in enumerate(edges):
        adjacent.append(tuple(j for j,f in enumerate(edges) if i!=j and len(set(e)&set(f))>0))
    return edges,adjacent

def directly_valid(seq,adj,k):
    for ns in adj:
        cnt=[0]*k
        for j in ns:
            cnt[seq[j]]+=1
        if max(cnt)*2>len(ns): return False
    return True

def structural(seq,m):
    misses=set()
    for i in range(m):
        a,b=seq[3*i],seq[3*i+1]
        if a==b:return False
        misses.add(3-a-b)  # for distinct 0,1,2
    for i in range(m):
        if seq[3*i+2] not in misses:return False
    return True

def formula(m):
    return (2**m)*(9**m-3*6**m+3*4**m+3*3**m-6*2**m+3)

def main():
    for m in range(1,5):
        E,adj=make_graph(m)
        d=s=0
        for seq in product(range(3),repeat=3*m):
            a=directly_valid(seq,adj,3)
            b=structural(seq,m)
            if a!=b:
                raise AssertionError(('classification fails',m,seq,a,b))
            d+=a;s+=b
        assert d==s==formula(m),(m,d,s,formula(m))
        assert all(not directly_valid(seq,adj,2) for seq in product(range(2),repeat=3*m))
        print('DIRECT_DEFINITION_AND_CLASSIFICATION_OK',m, 'named_colorings',d)
    # Independent grouped combinatorial count, without using closed form.
    for m in range(1,9):
        grouped=sum((2**m)*len(set(q))**m for q in product(range(3),repeat=m))
        assert grouped==formula(m),(m,grouped,formula(m))
    print('FINITE_GROUPED_FORMULA_OK through m=8')
    print('VERIFY_OK')
if __name__=='__main__':main()
