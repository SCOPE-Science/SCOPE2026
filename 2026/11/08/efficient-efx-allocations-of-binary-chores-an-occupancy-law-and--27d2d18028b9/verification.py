#!/usr/bin/env python3
"""Independent small-instance brute-force checks for cost-0 private and cost-1 common chores."""
from itertools import product
from math import factorial, comb

def formula(n,h,u):
    ans=0
    for v in product(range(u+1),repeat=n):
        if sum(v)!=u: continue
        if all(v[i]-(1 if h[i]==0 else 0)<=v[j]+h[j] for i in range(n) for j in range(n) if i!=j):
            den=1
            for x in v:den*=factorial(x)
            ans+=factorial(u)//den
    return ans

def brute(n,h,u):
    items=[i for i in range(n) for _ in range(h[i])]+[-1]*u
    all_alloc=[]
    for assignment in product(range(n),repeat=len(items)):
        costs=tuple(sum(int(t!=i) for t,j in zip(items,assignment) if j==i) for i in range(n))
        all_alloc.append((assignment,costs))
    cv=set(c for a,c in all_alloc)
    efficient={a for a in cv if not any(all(b[i]<=a[i] for i in range(n)) and b!=a for b in cv)}
    cnt=0
    for assignment,costs in all_alloc:
        if costs not in efficient:continue
        ok=True
        for i in range(n):
            own=[k for k,j in enumerate(assignment) if j==i]
            for j in range(n):
                if i==j:continue
                other_cost=sum(int(items[k]!=i) for k,x in enumerate(assignment) if x==j)
                for k in own:
                    if costs[i]-int(items[k]!=i)>other_cost:
                        ok=False;break
                if not ok: break
            if not ok:break
        cnt+=ok
    return cnt

def run():
    tested=0; allocations=0
    for n,max_h,max_u in [(2,2,6),(3,1,5),(4,1,3)]:
        for h in product(range(max_h+1),repeat=n):
            for u in range(max_u+1):
                if sum(h)+u>9: continue
                got=brute(n,h,u)
                exp=formula(n,h,u)
                assert got==exp,(n,h,u,got,exp)
                tested+=1;allocations+=n**(sum(h)+u)
    print('PASS exact direct brute Pareto+EFX checks:',tested,'instances;',allocations,'complete labeled allocations')
    for u in range(1,9):
        no=formula(2,(0,0),u); plus=formula(2,(1,0),u)
        exp_no=(2*comb(u,u//2) if u%2 else comb(u,u//2))
        exp_plus=(comb(u,u//2) if u%2 else comb(u,u//2)+comb(u,u//2-1))
        assert (no,plus)==(exp_no,exp_plus)
        print('u=',u, 'before=',no, 'after=',plus)
    for n in range(2,6):
        for h in range(1,5):
            for u in range(0,11):
                f=formula(n,(h,)*n,u)
                s=0
                for c in product(range(u+1),repeat=n):
                    if sum(c)==u and max(c)-min(c)<=h:
                        den=1
                        for x in c:den*=factorial(x)
                        s+=factorial(u)//den
                assert f==s
    print('PASS symmetric occupancy identity: 176 parameter combinations')
if __name__=='__main__':run()
