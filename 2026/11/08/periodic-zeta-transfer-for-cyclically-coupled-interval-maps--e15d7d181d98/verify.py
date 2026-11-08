"""Finite-state checks for cyclically permuted products and transfer traces.
Requires Python 3 standard library; a passing finite check is not a proof.
"""
from itertools import product
from math import gcd

def iterate_count(f,n):
    q=len(f)
    y=list(range(q))
    for _ in range(n):
        y=[f[t] for t in y]
    return sum(i==y[i] for i in range(q))

def cyclic_step(functions, state):
    s=len(state)
    return (functions[-1][state[-1]],) + tuple(functions[i][state[i]] for i in range(s-1))

def composed_1d(functions):
    q=len(functions[0]); ys=[]
    for x in range(q):
        y=x
        for f in functions:
            y=f[y]
        ys.append(y)
    return tuple(ys)

def finite_test(s,q,range_m):
    funcs=list(product(range(q),repeat=q))
    checks=0
    for family in product(funcs, repeat=s):
        composite=composed_1d(family)
        states=list(product(range(q),repeat=s))
        points=states[:]
        for m in range(1,range_m+1):
            points=[cyclic_step(family,p) for p in points]
            observed=sum(p==start for p,start in zip(points,states))
            d=gcd(s,m)
            predicted=iterate_count(composite,m//d)**d
            assert observed==predicted,(s,q,family,m,observed,predicted)
            checks+=1
    return checks

def trace(A,n):
    r=len(A)
    p=[[int(i==j) for j in range(r)] for i in range(r)]
    for _ in range(n):
        p=[[sum(p[i][k]*A[k][j] for k in range(r)) for j in range(r)] for i in range(r)]
    return sum(p[i][i] for i in range(r))

def swap_transfer(A):
    r=len(A); B=[[0]*(r*r) for _ in range(r*r)]
    for i in range(r):
      for j in range(r):
        for k in range(r):
          # B(e_i tensor e_j) = (A e_j) tensor e_i
          B[k*r+i][i*r+j]=A[k][j]
    return B

def tensor_transfer(A,s):
    r=len(A)
    N=r**s
    B=[[0]*N for _ in range(N)]
    for idx in product(range(r),repeat=s):
        j=0
        for t in idx: j=j*r+t
        for k in range(r):
            out=(k,)+idx[:-1]
            i=0
            for t in out: i=i*r+t
            B[i][j]=A[k][idx[-1]]
    return B

def run():
    checks=0
    for s,q,m in ((2,2,10),(2,3,8),(2,4,7),(3,2,10),(3,3,7),(4,2,9)):
        n=finite_test(s,q,m)
        print('finite cyclic test:',s,q,m,n)
        checks+=n
    matrices=([[1,1],[1,0]],[[2,0],[0,1]],[[2,1,0],[0,0,1],[0,1,1]])
    for A in matrices:
        B=swap_transfer(A)
        for n in range(1,13):
            d=gcd(n,2)
            assert trace(B,n)==trace(A,n//d)**d
            assert (trace(A,n)**2-trace(A,2*n))%2==0
            checks+=2
    for A,s in (([[1,1],[1,0]],3),([[2,0],[0,1]],4)):
        B=tensor_transfer(A,s)
        for n in range(1,12):
            d=gcd(n,s)
            assert trace(B,n)==trace(A,n//d)**d
            checks+=1
    print('VERIFY_OK checks='+str(checks))
if __name__=='__main__':
    run()
