#!/usr/bin/env python3
"""Independent finite enumeration of square-zero similarity classes over length-two rings."""
from itertools import product
from collections import Counter, deque

class Ring:
    def __init__(self, q, kind):
        self.q, self.kind = q, kind
        self.order = q*q
        if kind == 'integers':
            assert q in (2,3)
            self.add = lambda a,b: (a+b)%(q*q)
            self.mul = lambda a,b: (a*b)%(q*q)
            self.units = [x for x in range(q*q) if x%q]
            self.inverse = lambda a: pow(a,-1,q*q)
            self.residue = lambda a: a%q
        else:
            assert kind == 'dual' and q in (2,3)
            self.add = lambda a,b: ((a%q+b%q)%q)+q*((a//q+b//q)%q)
            self.mul = lambda a,b: ((a%q)*(b%q)%q)+q*(((a%q)*(b//q)+(a//q)*(b%q))%q)
            self.units = [a for a in range(q*q) if a%q]
            self.inverse = lambda a: (pow(a%q,-1,q)+q*((-(a//q))*pow(a%q,-2,q)%q))
            self.residue = lambda a: a%q

def matrix_mul(a,b,n,R):
    plus,times=R.add,R.mul
    return tuple(_dot(i,j,a,b,n,plus,times) for i in range(n) for j in range(n))

def _dot(i,j,a,b,n,plus,times):
    x=0
    for k in range(n):
        x=plus(x,times(a[i*n+k],b[k*n+j]))
    return x

def rank_mod(a,n,R):
    q=R.q
    rows=[[R.residue(a[i*n+j]) for j in range(n)] for i in range(n)]
    rank=0
    for j in range(n):
        pivot=next((k for k in range(rank,n) if rows[k][j]),None)
        if pivot is None:continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]
        inv=pow(rows[rank][j],-1,q)
        rows[rank]=[(v*inv)%q for v in rows[rank]]
        for i in range(n):
            if i!=rank:
                c=rows[i][j]
                rows[i]=[(x-c*y)%q for x,y in zip(rows[i],rows[rank])]
        rank+=1
    return rank

def elementary_generators(n,R):
    I=lambda: [int(i==j) for i in range(n) for j in range(n)]
    gens=[]
    for i in range(n):
        for j in range(n):
            if i==j:continue
            P=I();Pinv=I()
            P[i*n+j]=1
            Pinv[i*n+j]=R.add(0,R.order-1) if R.kind=='integers' else (R.q-1)
            gens.append((tuple(P),tuple(Pinv)))
    for i in range(n):
        for unit in R.units:
            if unit==1:continue
            P=I();Pinv=I()
            P[i*n+i]=unit
            Pinv[i*n+i]=R.inverse(unit)
            gens.append((tuple(P),tuple(Pinv)))
    return gens

def count_orbits(n,R):
    zero=(0,)*(n*n)
    solutions={M for M in product(range(R.order),repeat=n*n) if matrix_mul(M,M,n,R)==zero}
    total=len(solutions)
    gens=elementary_generators(n,R)
    counts=Counter(); sizes=[]
    while solutions:
        a=next(iter(solutions));solutions.remove(a)
        rank=rank_mod(a,n,R);size=0
        Q=deque([a])
        while Q:
            X=Q.popleft();size+=1
            for P,Pinv in gens:
                Y=matrix_mul(matrix_mul(P,X,n,R),Pinv,n,R)
                if Y in solutions:
                    solutions.remove(Y);Q.append(Y)
        counts[rank]+=1;sizes.append(size)
    return total,counts,sizes

def similarity_classes_field(q,upto):
    # Rational canonical form: generating product prod_{j>=1} (1-q*z^j)^-1.
    coef=[1]+[0]*upto
    for j in range(1,upto+1):
        for k in range(j,upto+1):coef[k]+=q*coef[k-j]
    return coef

def main():
    cases=[(2,'integers',1),(2,'integers',2),(2,'integers',3),
           (2,'dual',1),(2,'dual',2),(2,'dual',3),
           (3,'integers',1),(3,'integers',2),(3,'dual',1),(3,'dual',2)]
    for q,kind,n in cases:
        R=Ring(q,kind)
        total,counts,sizes=count_orbits(n,R)
        c=similarity_classes_field(q,n)
        expected={r:c[n-2*r] for r in range(n//2+1)}
        assert dict(counts)==expected,(q,kind,n,dict(counts),expected)
        print(f'field={q} ring={kind} n={n} labeled={total} similarity_classes={sum(counts.values())} by_reduction_rank={dict(sorted(counts.items()))} OK')
    print('SQUARE_ZERO_SIMILARITY_CLASSIFICATION_FINITE_CHECKS_PASSED')

if __name__=='__main__':main()
