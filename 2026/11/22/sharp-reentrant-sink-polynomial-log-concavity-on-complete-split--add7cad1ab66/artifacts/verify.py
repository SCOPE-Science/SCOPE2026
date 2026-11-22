from collections import Counter
from math import factorial,comb

def graph(k,r):
    n=k+r
    return [(i,j) for i in range(n) for j in range(i+1,n) if i<k or j<k]

def enumerate_sinks(k,r):
    edges=graph(k,r); n=k+r; A=Counter(); B=Counter()
    for m in range(1<<len(edges)):
        outs=[0]*n; indeg=[0]*n; outnbr=[[] for _ in range(n)]
        for b,(u,v) in enumerate(edges):
            if (m>>b)&1: u,v=v,u
            outs[u]+=1;indeg[v]+=1;outnbr[u].append(v)
        sinks=sum(d==0 for d in outs);B[sinks]+=1
        q=[v for v in range(n) if indeg[v]==0]
        visited=0
        while q:
            v=q.pop();visited+=1
            for w in outnbr[v]:
                indeg[w]-=1
                if indeg[w]==0:q.append(w)
        if visited==n:A[sinks]+=1
    return A,B

def form(k,r):
    A=Counter({i:factorial(k)*comb(r,i)*k**(r-i) for i in range(r+1)})
    A[0]-=factorial(k)*k**r
    A[1]+=factorial(k)*k**r
    B=Counter({i:(2**comb(k,2))*comb(r,i)*(2**k-1)**(r-i) for i in range(r+1)})
    C=k*2**(comb(k-1,2)+(k-1)*r)
    B[0]-=C;B[1]+=C
    return Counter({x:y for x,y in A.items() if y}),Counter({x:y for x,y in B.items() if y})

def check():
    cases=[(k,r) for k in range(1,4) for r in range(0,5) if len(graph(k,r))<=15]
    for k,r in cases:
        got=enumerate_sinks(k,r);expect=form(k,r)
        assert got==expect,(k,r,got,expect)
        print('OK',k,r,'edges',len(graph(k,r)),'acyclic',sorted(got[0].items()),'all',sorted(got[1].items()))
    for k in range(1,20):
      for r in range(3,40):
       coeff=form(k,r)[0]; vals=[coeff[i] for i in range(r+1)]
       logconcave=all(vals[i]**2>=vals[i-1]*vals[i+1] for i in range(1,r))
       assert logconcave==(r*(r+1)>=2*k*(r-2)),(k,r)
    for k in range(2,35):
      for r in range(1,25):
       a,b=form(k,r)
       assert sum(a.values())==factorial(k)*(k+1)**r,(k,r,'acyclic count')
       assert sum(b.values())==2**(comb(k,2)+k*r),(k,r,'all count')
       if r>=3:
        vals=[b[j] for j in range(r+1)]
        logconcave=all(vals[j]**2>=vals[j-1]*vals[j+1] for j in range(1,r))
        rhs=2*(r-2)*k*2**((k-1)*(r-1))
        lhs=r*(r+1)*(2**k-1)**(r-1)
        assert logconcave==(lhs>=rhs),(k,r,'all logconcavity')
    for r in range(1,41):
      a,b=form(6,r)
      ac_lc=all(a[j]**2>=a[j-1]*a[j+1] for j in range(1,r))
      assert ac_lc==(r<=3 or r>=8),(r,'reentrance')
    for k in range(2,36):
      a,b=form(k,3)
      all_lc=all(b[j]**2>=b[j-1]*b[j+1] for j in (1,2))
      assert all_lc==(k<=23),(k,'all threshold')
    print('CHECKED_EXACT_POLYNOMIALS_AND_ALL_LOGCONCAVITY_CASES_PASS',len(cases))
    print('VERIFY_OK')
if __name__=='__main__':check()
