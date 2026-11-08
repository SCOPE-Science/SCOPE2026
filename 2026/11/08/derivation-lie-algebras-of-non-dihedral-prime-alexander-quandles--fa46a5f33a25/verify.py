#!/usr/bin/env python3
"""Exact modular checks of derivations for connected prime Alexander-quandle algebras."""
from itertools import product

def basis_mul(i,j,p,a):
    return (a*i+(1-a)*j)%p

def rank_of_derivation_equations(p,a):
    # D(e_i) = sum_k d[k,i] e_k, with columns indexed by i.
    n=p*p
    pivots={}
    for i in range(p):
        for j in range(p):
            dest=basis_mul(i,j,p,a)
            for k in range(p):
                v={k*p+dest:1}
                # subtract D(e_i)*e_j and e_i*D(e_j)
                for t in range(p):
                    if basis_mul(t,j,p,a)==k:
                        h=t*p+i;v[h]=(v.get(h,0)-1)%p
                    if basis_mul(i,t,p,a)==k:
                        h=t*p+j;v[h]=(v.get(h,0)-1)%p
                v={h:z for h,z in v.items() if z%p}
                while v:
                    pivot=min(v)
                    if pivot not in pivots:
                        inv=pow(v[pivot],-1,p)
                        pivots[pivot]={h:z*inv%p for h,z in v.items() if z*inv%p}
                        break
                    coef=v[pivot]
                    for h,z in pivots[pivot].items():
                        v[h]=(v.get(h,0)-coef*z)%p
                        if v[h]==0:del v[h]
    return n-len(pivots)

def poly_mul(a,b,p):
    c=[0]*p
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b[:p-i]):
                if y:c[i+j]=(c[i+j]+x*y)%p
    return c

def poly_add(a,b,p): return [(x+y)%p for x,y in zip(a,b)]
def scale(a,c,p):return [(c*x)%p for x in a]
def qprod(a,b,p,s):
    o=[0]*p
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:o[basis_mul(i,j,p,s)]=(o[basis_mul(i,j,p,s)]+x*y)%p
    return o

def tlog(p):
    T=[0]*p
    power=[1]+[0]*(p-1)
    x=[0,1]+[0]*(p-2)
    for j in range(1,p):
        power=poly_mul(power,x,p)
        T=poly_add(T,scale(power,((-1)**(j+1))*pow(j,-1,p),p),p)
    return T

def derive_matrix_from_form(p,a,kind,exponent):
    # R=K[X]/(X^p-1), X=1+t, u basis X^i.
    # ordinary multiplier M_{T^exponent}, or E=T^exponent*d/dT (on T).
    T=tlog(p)
    powers=[[1]+[0]*(p-1)]
    for _ in range(1,p):powers.append(poly_mul(powers[-1],T,p))
    cols=[]
    for i in range(p):
        # (1+t)^i in t-coordinates
        from math import comb
        u=[comb(i,j)%p if j<=i else 0 for j in range(p)]
        if kind=='M':v=poly_mul(powers[exponent],u,p)
        else:
            du=[(j*u[j])%p for j in range(1,p)] + [0]
            # derivative wrt T = derivative wrt t * dt/dT = (1+t)* d/dt
            du=poly_mul(du,[1,1]+[0]*(p-2),p)
            v=poly_mul(powers[exponent],du,p)
        # Convert v(t) into X^j by substituting t=X-1
        Xcoeff=[0]*p
        for h,vh in enumerate(v):
            if not vh:continue
            for j in range(h+1):
                Xcoeff[j]=(Xcoeff[j]+vh*comb(h,j)*(-1)**(h-j))%p
        cols.append(Xcoeff)
    return cols

def is_derivation(cols,p,a):
    for i,j in product(range(p),repeat=2):
        k=basis_mul(i,j,p,a)
        rhs=poly_add(qprod(cols[i], [int(t==j) for t in range(p)],p,a),qprod([int(t==i) for t in range(p)],cols[j],p,a),p)
        if cols[k]!=rhs:return False,(i,j,k,cols[k],rhs)
    return True,None

for p in (3,5,7,11):
    for a in range(2,p):
        b=(1-a)%p
        if b==0:continue
        D=[d for d in range(1,p) if (pow(a,d,p)+pow(b,d,p))%p==1]
        E=[d for d in range(1,p) if (pow(a,d-1,p)==1 and pow(b,d-1,p)==1)]
        dim=rank_of_derivation_equations(p,a)
        assert dim==len(D)+len(E),(p,a,dim,D,E)
        for d in D:
            ok,err=is_derivation(derive_matrix_from_form(p,a,'M',d),p,a)
            assert ok,(p,a,'M',d,err)
        for d in E:
            ok,err=is_derivation(derive_matrix_from_form(p,a,'E',d),p,a)
            assert ok,(p,a,'E',d,err)
        print('EXACT_DERIVATION_DIM',p,'a',a,'b',b,'dimension',dim,'multiplier_degrees',D,'differential_degrees',E,'PASS')

for p,a in ((17,16),(17,3),(19,2),(31,30)):
    b=(1-a)%p
    D=[d for d in range(1,p) if (pow(a,d,p)+pow(b,d,p))%p==1]
    E=[d for d in range(1,p) if (pow(a,d-1,p)==1 and pow(b,d-1,p)==1)]
    for d in D:
        ok,err=is_derivation(derive_matrix_from_form(p,a,'M',d),p,a)
        assert ok,(p,a,'M',d,err)
    for d in E:
        ok,err=is_derivation(derive_matrix_from_form(p,a,'E',d),p,a)
        assert ok,(p,a,'E',d,err)
    print('CONSTRUCTION_CHECK',p,'a',a,'dimension_formula',len(D)+len(E),'D',D,'E',E,'PASS')

# Direct matrix-commutator checks of the claimed Lie-algebra structure.
def compose_cols(A,B,p):
    return [[sum(B[i][k]*A[k][j] for k in range(p))%p for j in range(p)] for i in range(p)]

def commutator_cols(A,B,p):
    AB=compose_cols(A,B,p); BA=compose_cols(B,A,p)
    return [[(AB[i][j]-BA[i][j])%p for j in range(p)] for i in range(p)]

def scale_cols(C,n,p):return [[(n*x)%p for x in row] for row in C]

def zero_cols(p):return [[0]*p for _ in range(p)]

for p,a in ((7,3),(7,4),(11,3),(17,16)):
    b=(1-a)%p
    D=[d for d in range(1,p) if (pow(a,d,p)+pow(b,d,p))%p==1]
    E=[d for d in range(1,p) if (pow(a,d-1,p)==1 and pow(b,d-1,p)==1)]
    MS={d:derive_matrix_from_form(p,a,'M',d) for d in D}
    ES={d:derive_matrix_from_form(p,a,'E',d) for d in E}
    for i in E:
        for j in D:
            got=commutator_cols(ES[i],MS[j],p)
            exp=scale_cols(MS[i+j-1],j,p) if i+j-1<p else zero_cols(p)
            assert got==exp,(p,a,'EM',i,j)
        for j in E:
            got=commutator_cols(ES[i],ES[j],p)
            exp=scale_cols(ES[i+j-1],j-i,p) if i+j-1<p else zero_cols(p)
            assert got==exp,(p,a,'EE',i,j)
    print('BRACKET_CHECK',p,'a',a,'PASS')

print('VERIFY_OK')
