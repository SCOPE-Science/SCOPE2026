#!/usr/bin/env python3
"""Independent finite-field checks for commuting tuples in rectangular-band semigroup algebras."""
from itertools import product


def add(a, b, q):
    return (a ^ b) if q == 4 else (a + b) % q


def mul(a, b, q):
    if q != 4:
        return a*b % q
    if not a or not b: return 0
    if a == 1: return b
    if b == 1: return a
    return {(2,2):3,(2,3):1,(3,2):1,(3,3):2}[(a,b)]


def matrix_product(x, y, a, b, q):
    # Basis multiplication e_{ij}e_{h\ell}=e_{i\ell}, not using a margin theorem.
    out = [0]*(a*b)
    for i in range(a):
        for j in range(b):
            xij=x[i*b+j]
            if xij:
                for h in range(a):
                    for ell in range(b):
                        term=mul(xij,y[h*b+ell],q)
                        out[i*b+ell]=add(out[i*b+ell],term,q)
    return tuple(out)


def sum_field(values,q):
    out=0
    for v in values: out=add(out,v,q)
    return out


def prediction(a,b,m,q):
    k=(a-1)*(b-1)
    n=q**(a+b-1)-q**(a-1)-q**(b-1)+1
    assert n%(q-1)==0
    return q**(m*k)*(q**(m*(b-1))+q**(m*(a-1))-1+(n//(q-1))*(q**m-1))


def exhaustive(a,b,m,q):
    elements=list(product(range(q),repeat=a*b))
    total=0
    # Build commutativity directly from the semigroup multiplication table.
    comm=[]
    for x in elements:
        row=[]
        for y in elements:
            row.append(matrix_product(x,y,a,b,q)==matrix_product(y,x,a,b,q))
        comm.append(row)
    if m==2:
        total=sum(v for row in comm for v in row)
        k=(a-1)*(b-1)
        for i,x in enumerate(elements):
            rowm=[0]*a
            colm=[0]*b
            for ii in range(a):
                for jj in range(b):
                    rowm[ii]=add(rowm[ii],x[ii*b+jj],q)
                    colm[jj]=add(colm[jj],x[ii*b+jj],q)
            uz=all(t==0 for t in rowm)
            vz=all(t==0 for t in colm)
            if uz and vz: exponent=a*b
            elif uz: exponent=k+b-1
            elif vz: exponent=k+a-1
            else: exponent=k+1
            assert sum(comm[i])==q**exponent,(a,b,q,i,exponent)
        for i,x in enumerate(elements):
            for j,y in enumerate(elements):
                if not comm[i][j]: continue
                def margin(z):
                    rr=tuple(sum_field((z[ii*b+jj] for jj in range(b)),q) for ii in range(a))
                    cc=tuple(sum_field((z[ii*b+jj] for ii in range(a)),q) for jj in range(b))
                    return rr,cc
                ux,vx=margin(x);uy,vy=margin(y)
                linear_u=all(t==0 for t in ux+uy)
                linear_v=all(t==0 for t in vx+vy)
                # For a two-row matrix, rank<=1 iff all 2x2 minors vanish.
                w1=ux+vx;w2=uy+vy
                rank1=all(mul(w1[h],w2[l],q)==mul(w1[l],w2[h],q)
                          for h in range(len(w1)) for l in range(h+1,len(w1)))
                assert rank1 or linear_u or linear_v,(a,b,q,i,j)
    elif m==3:
        for i in range(len(elements)):
            neighbors=[j for j in range(len(elements)) if comm[i][j]]
            for j in neighbors:
                total+=sum(comm[j][h] for h in neighbors)
    else:
        raise ValueError('m must be 2 or 3')
    return total


def main():
    cases=[(2,2,2,2),(2,2,3,2),(2,3,2,2),(2,3,3,2),
           (3,2,2,2),(3,3,2,2),(2,2,2,3),(2,2,3,3),
           (2,3,2,3),(2,2,2,4),(2,2,2,5)]
    for a,b,m,q in cases:
        actual=exhaustive(a,b,m,q)
        expected=prediction(a,b,m,q)
        assert actual==expected,(a,b,m,q,actual,expected)
        print('OK a=%s b=%s m=%s q=%s count=%s'%(a,b,m,q,actual))
    print('RECTANGULAR_BAND_COMMUTING_TUPLES_OK',len(cases))


if __name__=='__main__':main()
