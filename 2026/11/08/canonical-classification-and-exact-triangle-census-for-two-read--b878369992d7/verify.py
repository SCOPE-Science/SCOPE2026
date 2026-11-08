#!/usr/bin/env python3
"""Independent finite checks of a q-ary two-read deletion graph triangle theorem.

Run: python3 verify.py
Uses only the Python standard library. Every direct graph edge is computed
from *sets* of distinct one-deletion descendants, not from the theorem.
"""
from itertools import product
from collections import defaultdict

def formula(q,n):
    return q*(q-1)*sum((n-L+1)*(L-3)*q**(n-L)
                       for L in range(4,n+1))

def root_test(words,vertices,n):
    candidates=[]
    for pivot in vertices:
        other=[v for v in vertices if v!=pivot]
        blocks=[]
        for v in other:
            dif=[k for k in range(n) if words[v][k]!=words[pivot][k]]
            if len(dif)<2 or dif != list(range(dif[0],dif[-1]+1)):
                break
            blocks.append((dif[0],dif[-1],v))
        else:
            blocks.sort()
            i,j,y=blocks[0]
            k,l,z=blocks[1]
            if j+1!=k or words[pivot][j]!=words[pivot][k]:
                continue
            alphabet=set(words[pivot][i:j+1])
            if len(alphabet)!=2 or set(words[pivot][k:l+1])!=alphabet:
                continue
            x=words[pivot]
            if any(x[t]==x[t+1] for t in range(i,j)):continue
            if any(x[t]==x[t+1] for t in range(k,l)):continue
            if any(words[y][t]==x[t] for t in range(i,j+1)):continue
            if any(words[z][t]==x[t] for t in range(k,l+1)):continue
            candidates.append(pivot)
    return len(candidates)==1

def test_case(q,n):
    words=list(product(range(q),repeat=n))
    inverse=defaultdict(list)
    for i,w in enumerate(words):
        for descendant in {w[:j]+w[j+1:] for j in range(n)}:
            inverse[descendant].append(i)
    intersections=defaultdict(int)
    for idx in inverse.values():
        for p,j in enumerate(idx):
            for i in idx[:p]: intersections[(i,j)]+=1
    assert max(intersections.values(),default=0)<=2
    adjacent=[set() for _ in words]
    for (i,j),count in intersections.items():
        if count==2:
            adjacent[i].add(j)
            adjacent[j].add(i)
    triangles=0
    for i in range(len(words)):
        for j in adjacent[i]:
            if i>=j: continue
            for k in adjacent[i].intersection(adjacent[j]):
                if j>=k:continue
                triangles+=1
                assert root_test(words,(i,j,k),n),(q,n,i,j,k)
    assert triangles==formula(q,n),(q,n,triangles,formula(q,n))
    return triangles

def main():
    checks=[(2,n) for n in range(1,12)] + [(3,n) for n in range(1,8)] + [(4,n) for n in range(1,7)]
    for q,n in checks:
        val=test_case(q,n)
        print('q={} n={} triangles={}'.format(q,n,val))
    for n in range(1,25):
        q=2
        assert formula(q,n)==(n-5)*2**(n-1)+2*n+2
    print('VERIFY_OK cases={} root_unique=all_triangles generating_coefficients=24'.format(len(checks)))
if __name__=='__main__':main()
