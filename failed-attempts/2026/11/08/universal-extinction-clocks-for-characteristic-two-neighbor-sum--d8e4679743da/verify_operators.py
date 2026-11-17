#!/usr/bin/env python3
"""Independent verification using rooted up/down operators in characteristic two."""
import random

def generate(seed,h,max_branch=6):
    rng=random.Random(seed)
    parent=[-1];depth=[0]; frontier=[0]
    for level in range(h):
        new=[]
        for w in frontier:
            nc=2*rng.randrange(max_branch//2+1)
            if level==0 and h>0:nc=max(2,nc)
            for j in range(nc):
                parent.append(w);depth.append(level+1);new.append(len(parent)-1)
        if not new: break
        frontier=new
    return parent,depth

def run(parent,depth):
    n=len(parent);h=max(depth); children=[[] for _ in parent]
    for i,p in enumerate(parent):
        if p>=0:children[p].append(i)
    assert all(len(xs)%2==0 for xs in children)
    def up(v):
        w=[0]*n
        for j,p in enumerate(parent):
            if p>=0:w[j]=v[p]
        return w
    def down(v):
        w=[0]*n
        for i,chs in enumerate(children):
            for c in chs:w[i]^=v[c]
        return w
    def op(v):
        a=up(v);b=down(v)
        return [x^y for x,y in zip(a,b)]
    def power(fun,v,k):
        for i in range(k):v=fun(v)
        return v
    for u in range(n):
        e=[int(j==u) for j in range(n)]
        assert down(up(e))==[0]*n
        assert power(op,e,h+depth[u])==[int(t==h) for t in depth]
        assert power(op,e,h+depth[u]+1)==[0]*n
        for k in range(2*h+2):
            w=power(op,e,k)
            exp=[0]*n
            for a in range(k+1):
                b=k-a
                z=power(up,power(down,e,b),a)
                exp=[x^y for x,y in zip(exp,z)]
            assert w==exp,(u,k)
    return n,h

def main():
    checks=0; m=0
    for seed in range(250):
        parent,depth=generate(seed,1+seed%5,4)
        n,h=run(parent,depth);m=max(m,n);checks+=1
    print('VERIFY_OPERATORS_OK',checks,'irregular_even_child_trees','max_order',m)
if __name__=='__main__':main()
