"""Two separately implemented finite checks of the sharp longest minimal-absent-subsequence law.
All tests use explicit finite words or a separately implemented local-state DP.
They are corroboration; the unbounded statement relies on the written proof.
"""
from itertools import product

def embeds(u,w):
    i=0
    for x in w:
        if i<len(u) and x==u[i]: i+=1
    return i==len(u)

def longest_formula(q,k):
    t,r=divmod(k-1,q+1)
    return k+1+(q-1)*t+min(r,q-1)

def structural(u,k):
    if len(u)<2:return False
    flags=[int(u[i]>=u[i+1]) for i in range(len(u)-1)]
    return (sum(flags)==k and flags[0]==flags[-1]==1
            and all(flags[i-1]+flags[i]-int(u[i-1]>=u[i+1])==1 for i in range(1,len(u)-1)))

def literal(u,w):
    if embeds(u,w):return False
    return all(embeds(u[:j]+u[j+1:],w) for j in range(len(u)))

def test_exhaustive():
    configs=0; words=0
    for q,maxk in [(2,5),(3,4),(4,3),(5,2)]:
        for k in range(1,maxk+1):
            host=tuple(range(q))*k
            observed=0
            for L in range(2,2*k+2):
                if q**L>150000:break
                for u in product(range(q),repeat=L):
                    truth=literal(u,host)
                    assert truth==structural(u,k),(q,k,u,truth)
                    if truth: observed=max(observed,L)
                    words+=1
            assert observed==longest_formula(q,k),(q,k,observed)
            configs+=1
    return configs,words

def test_dp():
    configs=0
    for q in range(2,10):
      maxk=17
      states={(a,b,1):1 for a in range(q) for b in range(q) if a>=b}
      observed=[0]*(maxk+1)
      for L in range(2,2*maxk+1):
        for (a,b,d),count in states.items():
            if a>=b and d<=maxk: observed[d]=max(observed[d],L)
        new={}
        for (a,b,d),count in states.items():
            for c in range(q):
                d2=d+int(b>=c)
                if d2>maxk:continue
                if int(a>=b)+int(b>=c)-int(a>=c)!=1:continue
                key=(b,c,d2)
                new[key]=new.get(key,0)+count
        states=new
      for k in range(1,maxk+1):
          assert observed[k]==longest_formula(q,k),(q,k,observed[k])
          configs+=1
    return configs

if __name__=='__main__':
    c,w=test_exhaustive(); d=test_dp()
    print('PASS',c,'literal host configurations;',w,'candidate strings;',d,'independent dynamic configurations')
