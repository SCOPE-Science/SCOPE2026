#!/usr/bin/env python3
"""Exact independent checks for the characteristic-13 Picard Cartier stratification.
Runs with Python 3 standard library only. All arithmetic is exact.
"""
from collections import Counter
P = 13

def add(f,g):
    z=f.copy()
    for k,v in g.items():
        z[k]=(z.get(k,0)+v)%P
    return {k:v for k,v in z.items() if v}

def neg(f): return {k:(-v)%P for k,v in f.items()}

def sub(f,g): return add(f,neg(g))

def mul(f,g):
    z={}
    for (i,j,k),c in f.items():
        for (u,v,w),d in g.items():
            key=(i+u,j+v,k+w)
            z[key]=(z.get(key,0)+c*d)%P
    return {k:v for k,v in z.items() if v}

def power(f,n):
    z={(0,0,0):1}
    while n:
        if n&1: z=mul(z,f)
        f=mul(f,f);n>>=1
    return z

def coeff(f,k): return {(i,j):v for (i,j,t),v in f.items() if t==k}

def p2mul(f,g):
    z={}
    for (i,j),c in f.items():
        for (u,v),d in g.items():
            key=(i+u,j+v)
            z[key]=(z.get(key,0)+c*d)%P
    return {k:v for k,v in z.items() if v}

def p2sub(f,g):
    z=f.copy()
    for k,v in g.items():z[k]=(z.get(k,0)-v)%P
    return {k:v for k,v in z.items() if v}

def p2mulconst(f,c):return {k:(v*c)%P for k,v in f.items() if v*c%P}

def p2shift(f,i,j=0):return {(a+i,b+j):c for (a,b),c in f.items()}

def polynomial_data():
    F={(0,0,4):1,(1,0,2):1,(0,1,1):1,(0,0,0):1}
    f4=power(F,4);f8=power(F,8)
    d=coeff(f4,12)
    h00=coeff(f8,12);h01=coeff(f8,11)
    h10=coeff(f8,25);h11=coeff(f8,24)
    det=p2sub(p2mul(h00,h11),p2mul(h01,h10))
    # Divide by a^2-8 using monic long division over F13[b].
    r=det.copy();quot={}
    while r:
        degree=max(i for i,j in r)
        if degree<2:break
        terms={(i,j):v for (i,j),v in r.items() if i==degree}
        term={(i-2,j):v for (i,j),v in terms.items()}
        quot=p2sub(quot,p2mulconst(term,-1))
        r=p2sub(r,p2sub(p2shift(term,2),p2mulconst(term,8)))
    assert not r, 'determinant not divisible by a^2-8'
    assert d=={(2,0):6,(0,0):4},'scalar Cartier term'
    # Discriminant of X^4+a X^2+b X+1
    disc={(4,0):3,(3,2):9,(2,0):2,(1,2):1,(0,4):12,(0,0):9}
    reduced=p2sub(quot,p2mulconst(p2mul(disc,disc),4))
    # Verify P = 4 discriminant^2 modulo (a^2-8).
    while reduced:
        degree=max(i for i,j in reduced)
        if degree<2:break
        terms={(i,j):v for (i,j),v in reduced.items() if i==degree}
        term={(i-2,j):v for (i,j),v in terms.items()}
        reduced=p2sub(reduced,p2sub(p2shift(term,2),p2mulconst(term,8)))
    assert not reduced,'boundary congruence failed'
    return d,(h00,h01,h10,h11),det,quot,disc

def make_field(nonsquare):
    # IDs 0..168 represent u+13*v with alpha^2=nonsquare, so two independent bases.
    Q=169
    adds=[[0]*Q for _ in range(Q)]
    mults=[[0]*Q for _ in range(Q)]
    for x in range(Q):
        a,b=x%13,x//13
        for y in range(Q):
            c,d=y%13,y//13
            adds[x][y]=((a+c)%13)+13*((b+d)%13)
            mults[x][y]=((a*c+nonsquare*b*d)%13)+13*((a*d+b*c)%13)
    powers=[]
    for z in range(Q):
        arr=[1]
        for _ in range(14): arr.append(mults[arr[-1]][z])
        powers.append(arr)
    return Q,adds,mults,powers

def evaluate(poly,x,y,adds,mults,powers):
    res=0
    xx=powers[x];yy=powers[y]
    for (i,j),c in poly.items():
        res=adds[res][mults[c][mults[xx[i]][yy[j]]]]
    return res

def evaluate_count(poly,disc,nonsquare):
    Q,adds,mults,powers=make_field(nonsquare)
    count=Counter()
    for x in range(Q):
        xx=powers[x]
        dvalue=adds[mults[6][xx[2]]][4]
        for y in range(Q):
            if not evaluate(disc,x,y,adds,mults,powers):count['singular']+=1
            elif dvalue==0:count['a2']+=1
            elif evaluate(poly,x,y,adds,mults,powers)==0:count['a1']+=1
            else:count['a0']+=1
    assert sum(count.values())==Q*Q
    return count

def main():
    d,M,det,quot,disc=polynomial_data()
    # independent modulus-13 hand check at b=0,a^2=8:
    # Hasse-Cartier scalar=0, M=diag(0,2).
    print('COEFFICIENT_CARTIER_IDENTITY_OK')
    print('P_MONOMIALS',sorted((i,j,c if c<=6 else c-13) for (i,j),c in quot.items()))
    for ns in (8,2):
        res=evaluate_count(quot,disc,ns)
        print('F169_REPRESENTATION',ns,'counts',dict(sorted(res.items())))
    # Prime-field census independently by direct integer evaluations.
    count=Counter()
    for a in range(13):
        for b in range(13):
            discval=sum(c*pow(a,i,13)*pow(b,j,13) for (i,j),c in disc.items())%13
            pval=sum(c*pow(a,i,13)*pow(b,j,13) for (i,j),c in quot.items())%13
            if not discval:count['singular']+=1
            elif (a*a-8)%13==0:count['a2']+=1
            elif not pval:count['a1']+=1
            else:count['a0']+=1
    print('F13_COUNTS',dict(sorted(count.items())))
    assert count=={'a0':159,'singular':10}
    print('PICARD13_CARTIER_VERIFIED')

if __name__=='__main__':main()
