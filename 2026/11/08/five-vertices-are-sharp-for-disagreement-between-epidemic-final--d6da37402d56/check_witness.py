"""Independent exact-rational SIR moment recurrence for a five-vertex graph.
Python 3 standard library only. Run: python check_witness.py
"""
from functools import cache
from fractions import Fraction as Q

N=5;EDGES=((0,1),(1,3),(1,4),(2,3),(2,4),(3,4));BETA=Q(2)
ADJ=[set() for _ in range(N)]
for i,j in EDGES:ADJ[i].add(j);ADJ[j].add(i)
@cache
def laws(S,I,H):
    # conditional expectation of final ever-infected and running maximum infectives
    if not I:return Q(N-len(S)),Q(H)
    outcomes=[(Q(1),S,I-{u},H) for u in I]
    for u in S:
        k=len(ADJ[u]&I)
        if k:outcomes.append((BETA*k,S-{u},I|{u},max(H,len(I)+1)))
    rate=sum(o[0] for o in outcomes)
    ans=[Q(0),Q(0)]
    for w,s,i,h in outcomes:
        a,b=laws(frozenset(s),frozenset(i),h)
        ans[0]+=(w/rate)*a
        ans[1]+=(w/rate)*b
    return tuple(ans)

def at(v):return laws(frozenset(set(range(N))-{v}),frozenset({v}),1)

def main():
    e=[at(i) for i in range(N)]
    assert e[1]==(Q(2617,675),Q(5176097,1559250)),e[1]
    assert e[3]==(Q(3679,945),Q(16018271,4851000)),e[3]
    assert e[4]==e[3]
    assert e[1][0]<e[3][0]
    assert e[1][1]>e[3][1]
    assert {i for i in range(N) if e[i][0]==max(x[0] for x in e)}=={3,4}
    assert {i for i in range(N) if e[i][1]==max(x[1] for x in e)}=={1}
    print('PASS witness: seed 1 uniquely maximizes expected peak, seeds 3 and 4 maximize final size')
    for i,x in enumerate(e):print(i,str(x[0]),str(x[1]))
    print('memoized exact states:',laws.cache_info().currsize)
if __name__=='__main__': main()
