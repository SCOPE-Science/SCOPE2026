"""Independent exhaustive state-dynamics checks for one-way Greenberg-Hastings rings."""
from itertools import product
from math import comb

def step(x, q):
    n = len(x)
    return tuple((a+1)%q if a else int(x[(i-1)%n] == 1)
                 for i,a in enumerate(x))

def recurrent_count(n,q):
    return 1 + sum(n * comb(n-(q-1)*k-1,k-1)//k
                   for k in range(1,n//q+1))

def temporal_class(x,q):
    seen={}
    y=x
    while y not in seen:
        seen[y]=len(seen)
        y=step(y,q)
    return seen[y],len(seen)-seen[y]

def main():
    checked=0
    for q in range(4,8):
        for n in range(3,8):
            if q**n>130000:
                continue
            periodic=0
            max_entry=0
            for x in product(range(q),repeat=n):
                tau,p=temporal_class(x,q)
                max_entry=max(max_entry,tau)
                periodic += (tau==0)
                if tau > q+min(n,q-1)-2:
                    raise AssertionError(('bad entry bound',q,n,x,tau))
                checked+=1
            goal=q+min(n,q-1)-2
            assert max_entry==goal,(q,n,max_entry,goal)
            assert periodic==recurrent_count(n,q),(q,n,periodic,recurrent_count(n,q))
            print('q=%d n=%d checked=%d recurrent=%d sharp_entry=%d'%(
                q,n,q**n,periodic,goal))
    print('PASS exhaustive configurations:',checked)

if __name__=='__main__':main()
