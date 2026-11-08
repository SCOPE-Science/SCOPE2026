#!/usr/bin/env python3
"""Exact cellular-cochain checks for dihedral actions on polygonal moment-angle manifolds.

The squarefree cellular differential model has u_i of degree 1 and v_i of
 degree 2, with d u_i = v_i, u_i^2=v_i^2=u_i*v_i=0. A product of v's
 is permitted only when its support is a face of the cycle complex.
 All counts and traces here are exact integers; no floating point arithmetic.
"""
from itertools import combinations
from math import comb

def sign_of_images(indices, g):
    a=[g(x) for x in indices]
    inv=sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))
    return -1 if inv%2 else 1

def maps(n):
    return [(('r',a),lambda x,a=a:(x+a)%n) for a in range(n)]+[(('s',a),lambda x,a=a:(a-x)%n) for a in range(n)]

def edge(n,a,b): return (a-b)%n in (1,n-1)

def subset_trace(n,g,k,degree):
    """Trace on cochains in multi-degree k (size of u/v support) and total degree.
    v-support must be a face; u-support sorted and supplies Koszul sign.
    """
    result=0
    for I in combinations(range(n),k):
        if frozenset(map(g,I))!=frozenset(I): continue
        num_v=degree-k
        for V in combinations(I,num_v):
            if num_v>2: continue
            if num_v==2 and not edge(n,*V):continue
            if frozenset(map(g,V))!=frozenset(V): continue
            U=tuple(x for x in I if x not in V)
            if frozenset(map(g,U))!=frozenset(U):continue
            result+=sign_of_images(U,g)
    return result

def character(n,g,k):
    # The 2/3-vertex multidegree complexes are exact except in degree k+1:
    # their cochain alternating trace gives that homology trace.
    return subset_trace(n,g,k,k+1)-subset_trace(n,g,k,k)-subset_trace(n,g,k,k+2)

def predicted_3(n,label):
    kind,a=label
    if kind=='r':
        if a==0:return n*(n-3)//2
        return n//2 if n%2==0 and a==n//2 else 0
    if n%2:return (n-3)//2
    return n//2 if a%2==0 else n//2-2

def predicted_4(n,label):
    kind,a=label
    if kind=='r':
        if a==0:return n*(n-2)*(n-4)//3
        return -n//3 if n%3==0 and (3*a)%n==0 and a%n else 0
    return -1 if n%2 else 0

def rank_modp(a,p=1000003):
    a=[[x%p for x in row] for row in a]
    if not a:return 0
    rows=len(a);cols=len(a[0]);r=0
    for j in range(cols):
        pivot=next((i for i in range(r,rows) if a[i][j]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][j],-1,p);a[r]=[(q*inv)%p for q in a[r]]
        for i in range(r+1,rows):
            q=a[i][j]
            if q:a[i]=[(x-q*y)%p for x,y in zip(a[i],a[r])]
        r+=1
        if r==rows:break
    return r

def check_differential(n):
    # For each triple I, d:C^k->C^(k+1) is a nonzero 1-column map,
    # and d:C^(k+1)->C^(k+2) has rank equal to induced-edge count.
    for I in combinations(range(n),3):
        e=[E for E in combinations(I,2) if edge(n,*E)]
        d0=[(-1)**i for i in range(3)]
        assert rank_modp([d0])==1
        # Differential should square to zero; direct formula for d1 adapted
        # only modulo choice of vertex-orientation basis. Here test d via
        # cellular wedge-derivation directly using exact signed monomials.
        # In u-complement basis C^(k+1), d0 has entries (-1)^position
        # and d1(E,j) is sign(position of remaining u removed from U)
        actual=[]
        for E in e:
            row=[]
            for j in I:
                if j not in E:row.append(0)
                else:
                    U=[x for x in I if x!=j]
                    remaining=next(x for x in E if x!=j)
                    row.append((-1)**U.index(remaining))
            actual.append(row)
        assert all(sum(x*y for x,y in zip(row,d0))==0 for row in actual)
        assert rank_modp(actual)==len(e)

def main():
    checks=0
    print('polygonal complex moment-angle exact low-degree equivariant checks')
    for n in range(4,19):
        if n<=12:check_differential(n)
        for label,g in maps(n):
            assert character(n,g,2)==predicted_3(n,label),(n,label,'H3',character(n,g,2),predicted_3(n,label))
            assert character(n,g,3)==predicted_4(n,label),(n,label,'H4',character(n,g,3),predicted_4(n,label))
            checks+=2
        b3=sum(predicted_3(n,label) for label,_ in maps(n))//(2*n)
        b4=sum(predicted_4(n,label) for label,_ in maps(n))//(2*n)
        want3=n//2-1
        want4=((n-2)*(n-4)-3*(n%2)-2*(n%3==0))//6
        assert b3==want3 and b4==want4,(n,b3,b4,want3,want4)
        print('n=%2d: ordinary=(%d,%d), quotient=(%d,%d), all=%d symmetries verified'%(
            n, n*(n-3)//2, n*(n-2)*(n-4)//3, b3,b4,2*n))
    print('PASS: %d exact character tests; all quotient averages and multi-degree rank checks pass.'%checks)
if __name__=='__main__':main()
