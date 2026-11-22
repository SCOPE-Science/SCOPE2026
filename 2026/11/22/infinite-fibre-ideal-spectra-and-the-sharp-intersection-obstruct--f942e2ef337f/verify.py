"""Finite quotient checks for omega-accumulation image and intersection criterion.

The countably infinite topological fibers are represented by Boolean flags recording
which fibers meet a set infinitely; these checks do not substitute for the proof.
"""
from itertools import product


def relations(n):
    pairs = [(i,j) for i in range(n) for j in range(i+1,n)]
    for choices in product((0,1,2),repeat=len(pairs)):
        leq=[[i==j for j in range(n)] for i in range(n)]
        for (i,j),c in zip(pairs,choices):
            if c == 1:leq[i][j]=True
            elif c == 2:leq[j][i]=True
        if all(not (leq[i][j] and leq[j][k]) or leq[i][k]
               for i in range(n) for j in range(n) for k in range(n)):
            yield leq


def down(leq,S):
    return frozenset(x for x in range(len(leq)) if any(leq[x][y] for y in S))


def main():
    tested=0
    bad=0
    for n in range(1,5):
        for leq in relations(n):
            for bits in range(1<<n):
                I=frozenset(x for x in range(n) if bits>>x&1)
                ideals={frozenset(x for x in I if any(leq[x][y] for y in J))
                        for Jbits in range(1<<n)
                        for J in [frozenset(y for y in I if Jbits>>y&1)]}
                outputs={down(leq,J) for J in ideals}
                assert len(outputs)==len(ideals)
                assert {frozenset(out & I) for out in outputs} == ideals
                # Omega on any saturated output S is down( S intersect I ); it is idempotent.
                assert all(down(leq,out & I)==out for out in outputs)
                # Condition: each c's infinite classes above it are empty or have a least element.
                property_ok = all(
                    not (above:=set(i for i in I if leq[c][i]))
                    or any(all(leq[j][u] for u in above) for j in above)
                    for c in range(n))
                closed = all(a & b in outputs for a in outputs for b in outputs)
                assert closed == property_ok, (n,leq,I)
                if not closed:bad+=1
                tested+=1
    # Minimal failure: 0 below incomparable 1,2, only 1,2 infinite.
    leq=[[1,1,1],[0,1,0],[0,0,1]]
    I=frozenset((1,2))
    aa=down(leq,{1});bb=down(leq,{2})
    assert aa=={0,1} and bb=={0,2} and aa&bb=={0}
    assert {0} not in {down(leq,J) for J in (set(),{1},{2},{1,2})}
    print(f'VERIFY_OK cases={tested} non_intersection_closed={bad}')

if __name__=='__main__':main()
