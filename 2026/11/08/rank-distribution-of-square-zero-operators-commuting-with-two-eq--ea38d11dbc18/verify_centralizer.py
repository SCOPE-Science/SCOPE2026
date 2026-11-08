#!/usr/bin/env python3
"""Exact direct checks of square-zero commuting-operator rank polynomial.

Each 2x2 polynomial matrix over F_q[t]/(t^m) acts on a 2m-dimensional
F_q vector space; test its literal square and calculate rank independently.
Only finite experiments are performed by this program.
"""
from collections import Counter
from itertools import product

def mul_q(a,b,q):
    if q==4:
        x=0
        for i in range(2):
            for j in range(2):
                if (a>>i)&1 and (b>>j)&1: x^=1<<(i+j)
        if x&8:x^=0b1110
        if x&4:x^=0b111
        return x
    return (a*b)%q

def plus(a,b,q):
    return a^b if q==4 else (a+b)%q

def field_rank(cols, dim, q):
    rows=[[cols[j][i] for j in range(len(cols))] for i in range(dim)]
    lead=0
    for r in range(dim):
        if lead>=len(cols):break
        i=r
        while i<dim and rows[i][lead]==0:i+=1
        while i==dim:
            lead+=1
            if lead>=len(cols):return r
            i=r
            while i<dim and rows[i][lead]==0:i+=1
        rows[r],rows[i]=rows[i],rows[r]
        inv=next(t for t in range(1,q) if mul_q(rows[r][lead],t,q)==1)
        rows[r]=[mul_q(v,inv,q) for v in rows[r]]
        for j in range(r+1,dim):
            factor=rows[j][lead]
            if factor:
                # negate in odd characteristic, unchanged in characteristic two
                rows[j]=[plus(rows[j][k],mul_q((q-factor)%q if q!=4 else factor,rows[r][k],q),q) for k in range(len(cols))]
        lead+=1
    return sum(any(x!=0 for x in row) for row in rows)

def rank_f(mat,m,q):
    # columns: input basis vectors t^j e_i, output polynomial coeff arrays
    a,b,c,d=mat
    cols=[]
    for inp in range(2):
        for j in range(m):
            co=[]
            for out in range(2):
                poly=(a,c)[out] if inp==0 else (b,d)[out]
                co.extend([0]*j + list(poly[:m-j]))
            cols.append(co)
    return field_rank(cols,2*m,q)

def poly_mul(x,y,m,q):
    out=[0]*m
    for i in range(m):
        for j in range(m-i):
            out[i+j]=plus(out[i+j],mul_q(x[i],y[j],q),q)
    return tuple(out)

def poly_add(x,y,q):
    return tuple(plus(a,b,q) for a,b in zip(x,y))

def predicted(m,q):
    h=(m+1)//2
    s=m//2
    r1=(q*q-1)**2//(q-1)
    ans=Counter({0:1})
    for ell in range(1,s+1):
        ans[2*ell]+=q**(4*(ell-1))*(q*q-1)*(q*q-q)
        for d in range(1,ell):
            ans[2*ell-d]+=r1*q**(4*(ell-1)-d)*(q-1)
        ans[ell]+=r1*q**(3*(ell-1))
    ans[m]+=(q*q-1)*q**(2*m-2)
    for a in range(1,h):
        ans[m-a]+=(q*q-1)*q**(2*m-a-2)
        for c in range(a):
            ans[m-c]+=(q*q-1)*(q-1)*q**(2*m-c-3)
    return {x:ans[x] for x in range(m+1)}

def check_generic(m,q):
    pol=list(product(range(q),repeat=m))
    zero=(0,)*m
    observed=Counter()
    for a in pol:
      for b in pol:
       for c in pol:
        bc=poly_mul(b,c,m,q)
        for d in pol:
         ad=poly_add(a,d,q)
         if poly_add(poly_mul(a,a,m,q),bc,q)!=zero:continue
         if poly_mul(b,ad,m,q)!=zero:continue
         if poly_mul(c,ad,m,q)!=zero:continue
         if poly_add(poly_mul(d,d,m,q),bc,q)!=zero:continue
         observed[rank_f((a,b,c,d),m,q)]+=1
    want=predicted(m,q)
    assert dict(sorted(observed.items()))==want, (m,q,observed,want)
    return want

def check_binary(m):
    mask=(1<<m)-1
    def mul(x,y):
        o=0
        while y:
            if y&1:o^=x
            x<<=1;y>>=1
        return o&mask
    observed=Counter()
    for a in range(1<<m):
      for b in range(1<<m):
       for c in range(1<<m):
        bc=mul(b,c)
        if mul(a,a)!=bc:continue
        for d in range(1<<m):
         if mul(b,a^d)!=0 or mul(c,a^d)!=0 or mul(d,d)!=bc:continue
         cols=[mul(a,1<<j)|(mul(c,1<<j)<<m) for j in range(m)]
         cols += [mul(b,1<<j)|(mul(d,1<<j)<<m) for j in range(m)]
         piv={}
         for v in cols:
          while v:
           i=v.bit_length()-1
           if i in piv:v^=piv[i]
           else:piv[i]=v;break
         observed[len(piv)]+=1
    want=predicted(m,2)
    assert dict(sorted(observed.items()))==want,(m,observed,want)
    return want

if __name__=="__main__":
    for m in (1,2,3,4):
        d=check_binary(m)
        print(f"PASS q=2 m={m}: {d} total={sum(d.values())}")
    for q,m in ((3,1),(3,2),(4,1),(4,2),(5,1)):
        d=check_generic(m,q)
        print(f"PASS q={q} m={m}: {d} total={sum(d.values())}")
    print("ALL_EXACT_SQUARE_ZERO_CENTRALIZER_RANK_CHECKS_PASS")
