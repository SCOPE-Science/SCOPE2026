"""Exact small-dimensional checks for the cube packet optimizer classification."""
from itertools import permutations, product
from math import factorial

def det_int(A):
    n=len(A)
    if n==1:return A[0][0]
    if n==2:return A[0][0]*A[1][1]-A[0][1]*A[1][0]
    return sum((-1)**j*A[0][j]*det_int([row[:j]+row[j+1:] for row in A[1:]]) for j in range(n))

def row_types(d):
    R=[]
    for i in range(d):
        for sign in (-1,1):
            v=[0]*d;v[i]=sign;R.append(tuple(v))
    for i in range(d):
        for j in range(d):
            if i!=j:
                v=[0]*d;v[i]=1;v[j]=-1;R.append(tuple(v))
    return sorted(R)

def row_span(a,perm):
    partial=0;xs=[0]
    for j in perm:
        partial+=a[j];xs.append(partial)
    return max(xs)-min(xs)

def test():
    checks=0
    for d in range(1,5):
        typ=row_types(d)
        assert len(typ)==d*(d+1)
        ordered=0;detvals=set();nonzero_det=0
        for rows in product(typ,repeat=d):
            determinant=det_int(rows)
            if determinant:
                ordered+=1;detvals.add(determinant)
                assert abs(determinant)==1
            # This class is ALL integer matrices having coordinate packet radius <=1/2,
            # not just all integer matrices with entries +/- 1.
            checks+=1
        expected= (2**d)*((d+1)**(d-1))*factorial(d)
        assert ordered==expected,(d,ordered,expected)
        print('dimension',d,'rows',len(typ),'matrices',len(typ)**d,'independent ordered',ordered,'unordered',ordered//factorial(d),'det',detvals)
    for d in range(1,6):
        for row in product((-2,-1,0,1,2),repeat=d):
            exact=max(row_span(row,perm) for perm in permutations(range(d)))
            claimed=max(sum(max(x,0) for x in row),sum(max(-x,0) for x in row))
            assert exact==claimed
            checks+=1
    print('CUBE_PACKET_EXACT_CHECKS_OK',checks)
if __name__=='__main__':test()
