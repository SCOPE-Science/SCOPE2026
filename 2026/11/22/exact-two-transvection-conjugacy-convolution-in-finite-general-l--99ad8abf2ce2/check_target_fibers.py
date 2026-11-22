"""Full-pair direct product-fiber check in three small general linear groups."""
from itertools import product
from collections import Counter
from check_transvections import Field

def multiply(f,a,b,n):
    out=[]
    for i in range(n):
        for j in range(n):
            v=0
            for k in range(n):v=f.A[v][f.M[a[i*n+k]][b[k*n+j]]]
            out.append(v)
    return tuple(out)

def identity(n):return tuple(int(i==j) for i in range(n) for j in range(n))

def class_type(f,g,n):
    e=identity(n)
    k=[[f.A[g[i*n+j]][f.M[f.p-1][e[i*n+j]]] for j in range(n)] for i in range(n)]
    r=f.rank(k)
    t=0
    for i in range(n):t=f.A[t][k[i][i]]
    if t:return ('t',t)
    if r==0:return ('I',0)
    if r==1:return ('J2',0)
    k2=[[f.dot(k[i],[k[h][j] for h in range(n)]) for j in range(n)] for i in range(n)]
    return ('J22',0) if all(x==0 for row in k2 for x in row) else ('J3',0)

def test(p,d,n):
    f=Field(p,d);q=f.q
    vectors=[v for v in product(range(q),repeat=n) if any(v)]
    ts=set()
    for v in vectors:
       for psi in vectors:
          if f.dot(v,psi):continue
          g=[]
          for i in range(n):
             for j in range(n):g.append(f.A[int(i==j)][f.M[v[i]][psi[j]]])
          ts.add(tuple(g))
    c=Counter();groups={}
    for a in ts:
      for b in ts:
       g=multiply(f,a,b,n)
       c[g]+=1
    types={g:class_type(f,g,n) for g in c}
    # For every conjugacy-type stratum, every individual matrix must have the same fiber size.
    bytype={}
    for g,num in c.items():bytype.setdefault(types[g],set()).add(num)
    assert all(len(x)==1 for x in bytype.values()),(p,d,n,bytype)
    T=len(ts)
    expected={'I':1,'J2':2*q**(n-1)-q-2,'J3':2*(q**(n-1)-q)*q**(n-2),
              'J22':0 if n<=3 else (q**(n-1)-q)*(q**(n-2)-q)//(q-1)}
    for cat in list(expected):
        mass=sum(num for g,num in c.items() if types[g][0]==cat)
        assert mass==T*expected[cat],(p,d,n,cat,mass,T*expected[cat])
    for t in range(1,q):
        mass=sum(num for g,num in c.items() if types[g]==('t',t))
        assert mass==T*q**(2*n-3),(p,d,n,t,mass)
    print('PASS FULL PAIRS',f'q={q}',f'n={n}',f'num_factors={T}',f'num_pairs={T*T}',f'num_outputs={len(c)}',f'types={len(bytype)}')

if __name__=='__main__':
 for args in ((2,1,2),(2,1,3),(2,1,4),(3,1,2),(2,2,2)):
   test(*args)
 print('ALL FULL-PAIR CHECKS PASS')
