from itertools import combinations,permutations
from math import factorial,comb

def inv(f,n):
    out=set(f)
    starts=[v for v in range(n) if v not in set(f.values())]
    seen=set(); paths=[]; cycles=[]
    for s in starts:
        x=s; sz=0
        while x not in seen:
            seen.add(x); sz+=1
            if x not in f: break
            x=f[x]
        paths.append(sz)
    for x in range(n):
        if x in seen:continue
        v=x; sz=0
        while v not in seen:
            seen.add(v);sz+=1;v=f[v]
        assert v==x
        cycles.append(sz)
    assert len(seen)==n
    u=sum(t%2 for t in paths);v=len(paths)-u
    return u,v,cycles

def odd_count(f,n):
    dom=set(f); ran=set(f.values())
    missing_dom=sorted(set(range(n))-dom)
    missing_ran=sorted(set(range(n))-ran)
    assert len(missing_dom)==len(missing_ran)
    ct=0
    for images in permutations(missing_ran):
        p=dict(f);p.update(zip(missing_dom,images))
        visited=set();valid=True
        for i in range(n):
            if i in visited:continue
            cur=i;s=0
            while cur not in visited:
                visited.add(cur);s+=1;cur=p[cur]
            assert cur==i
            if s%2==0:
                valid=False;break
        ct+=valid
    return ct

def predicted(u,v,cycles):
    if any(c%2==0 for c in cycles):return 0
    if u+v==0:return 1
    if u==0:return 0
    j=u//2
    a=u*comb(2*j,j)*factorial(u+v-1)
    b=4**j
    assert a%b==0
    return a//b

ctr=0
for n in range(1,6):
    for k in range(n+1):
      for D in combinations(range(n),k):
       for R in combinations(range(n),k):
        for pi in permutations(R):
          f=dict(zip(D,pi)); u,v,cs=inv(f,n)
          ans=predicted(u,v,cs); observed=odd_count(f,n)
          assert ans==observed,(f,n,u,v,cs,ans,observed)
          ctr+=1
    print('checked n',n,'cases',ctr)
print('ALL_CHECKS_OK',ctr)

# Verify the sharp one-new-point case and its factorial multiplicity.
one_point=0
for n in range(1,6):
    for k in range(n+1):
        for D in combinations(range(n),k):
            for R in combinations(range(n),k):
                for pi in permutations(R):
                    f=dict(zip(D,pi))
                    u,v,cs=inv(f,n)
                    if not any(c%2==0 for c in cs) and u==0 and v>0:
                        assert odd_count(f,n)==0
                        assert odd_count(f,n+1)==factorial(v)
                        one_point+=1
print('ONE_POINT_CHECKS_OK',one_point)
