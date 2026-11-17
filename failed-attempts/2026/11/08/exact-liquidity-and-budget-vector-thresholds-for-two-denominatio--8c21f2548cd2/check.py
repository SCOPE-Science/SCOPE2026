from functools import lru_cache
from itertools import product
from math import floor, comb

@lru_cache(None)
def direct(caps,t,u,h):
    if not caps: return t==0 and u==0
    c=caps[0]
    for a in range(min(t,c//h)+1):
        for b in range(min(u,c-h*a)+1):
            if direct(caps[1:],t-a,u-b,h):return True
    return False

def test():
 count=0; minchecks=0
 for n in range(2,5):
  for h in range(2,6):
   for t in range(0,5):
    for u in range(0,5):
     if not (t+u):continue
     W=h*t+u;q,r=divmod(W,n);s=q%h; delta=max(0,t-n*(q//h));Bstar=max(r,(h-s)*delta)
     for bs in product(range(3),repeat=n):
      caps=tuple(q+b for b in bs)
      predicted=sum(caps)>=W and sum(c//h for c in caps)>=t
      actual=direct(caps,t,u,h)
      assert predicted==actual,(n,h,t,u,bs,predicted,actual)
      count+=1
     if Bstar<=8:
      for B in range(Bstar+1):
       found=False
       for bs in product(range(B+1),repeat=n):
        if sum(bs)!=B:continue
        caps=tuple(q+b for b in bs)
        if direct(caps,t,u,h):found=True;break
       assert found==(B>=Bstar),(n,h,t,u,B,Bstar)
       minchecks+=1
 tailchecks=0
 for n in range(2,7):
  for h in range(2,6):
   for t in range(0,5):
    for u in range(0,5):
     if not t+u:continue
     W=h*t+u;q,r=divmod(W,n);s=q%h;H0=n*(q//h)
     frequencies=[0]*(n+1)
     for bs in product((0,1),repeat=n):
      if direct(tuple(q+b for b in bs),t,u,h):frequencies[sum(bs)]+=1
     if s==h-1:
      K=max(r,t-H0)
      predicted=[comb(n,j) if j>=K else 0 for j in range(n+1)]
     elif t>H0:
      predicted=[0]*(n+1)
     else:
      predicted=[comb(n,j) if j>=r else 0 for j in range(n+1)]
     assert frequencies==predicted,(n,h,t,u,frequencies,predicted)
     tailchecks+=1
 print('exact individual-budget tests',count,'minimum budget levels',minchecks,'Bernoulli enumerations',tailchecks)

if __name__=='__main__':test()
