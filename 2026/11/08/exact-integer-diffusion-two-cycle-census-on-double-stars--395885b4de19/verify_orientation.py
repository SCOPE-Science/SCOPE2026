#!/usr/bin/env python3
"""Enumerate edge signs and admissible gap multiplicities on double-stars."""
from itertools import product

def predicted(a,b):
    main=(a+b+1)*(a+1)**a*(b+1)**b
    near1=max(0,a-b+1)*(a+1)**a*(b-1)**b
    near2=max(0,b-a+1)*(a-1)**a*(b+1)**b
    return 1+2*(main+near1+near2)+(2*a**(a+b) if a==b else 0)

def orientation_sum(a,b):
    edges=[(0,1)]+[(0,2+i) for i in range(a)]+[(1,2+a+j) for j in range(b)]
    total=0
    for signs in product((-1,0,1),repeat=len(edges)):
        delta=[0]*(a+b+2)
        for (u,v),s in zip(edges,signs):
            delta[u]+=s;delta[v]-=s
        weight=1
        for (u,v),s in zip(edges,signs):
            if s==0:
                weight*=int(delta[u]==delta[v])
            else:
                weight*=max(0,s*(delta[u]-delta[v])-1)
            if weight==0: break
        total+=weight
    return total

def main():
    for a in range(1,6):
        for b in range(1,6):
            if a+b>10: continue
            count=orientation_sum(a,b)
            assert count==predicted(a,b),(a,b,count,predicted(a,b))
            print(f'a={a} b={b} normalized_fixed_by_F2={count} primitive_orbits={(count-1)//2}')
    print('PASS: all 25 labelled double-star parameter families match formula')
if __name__=='__main__': main()
