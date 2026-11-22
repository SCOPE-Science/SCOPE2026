#!/usr/bin/env python3
"""Independent numerical cross-checks of the discrete Weibull innovation obstruction.

All mathematical claims concerning infinite parameter ranges are proved in RESULT.md.
This script uses standard-library Decimal arithmetic to replay finite examples.
"""
from decimal import Decimal, localcontext

D = Decimal

def pow_dec(x, y):
    return (x.ln() * y).exp()

def H(q, beta):
    a = pow_dec(D(2), beta)
    b = pow_dec(D(3), beta)
    return -q + 3*pow_dec(q,a)-2*pow_dec(q,b) -pow_dec(q,1+a)+2*pow_dec(q,1+b)-pow_dec(q,2*a)

def threshold(beta, iterations=160):
    lo, hi = D(0), D(1)
    for _ in range(iterations):
        mid=(lo+hi)/2
        if H(mid,beta)<0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

def probability(k,q,beta):
    if k==0:
        return 1-q
    return pow_dec(q,pow_dec(D(k),beta))-pow_dec(q,pow_dec(D(k+1),beta))

def innovation_one_ratio(q,beta,c,terms=20):
    z=1-c
    ps=[probability(k,q,beta) for k in range(terms+1)]
    g=sum((ps[k]*z**k for k in range(terms+1)),D(0))
    gp=sum((k*ps[k]*z**(k-1) for k in range(1,terms+1)),D(0))
    return ps[1]/ps[0]-c*gp/g

def main():
    with localcontext() as ctx:
        ctx.prec=65
        targets=[('0.1','0.0301941761806608078757'),
                 ('0.3','0.3375202296516113277270'),
                 ('0.5','0.6337051370046700169691'),
                 ('0.7','0.8367643571683214145836'),
                 ('0.9','0.9602044932971239673491'),
                 ('0.99','0.9965479122203029886301')]
        for bs,qs in targets:
            beta=D(bs)
            root=threshold(beta)
            assert abs(root-D(qs))<D('1e-19'), (bs,root)
            assert H(root-D('1e-7'),beta)<0 and H(root+D('1e-7'),beta)>0
            p0,p1,p2=[probability(i,root,beta) for i in range(3)]
            r1=p1/p0
            r2=2*p2/p0-r1*r1
            assert abs((r2-r1)-H(root,beta)/(1-root)**2) < D('1e-40')
            print('beta',bs,'q_star',root)
        beta=D('0.5'); q=D('0.8'); c=D('0.99')
        r1=(q-pow_dec(q,pow_dec(D(2),beta)))/(1-q)
        p2=probability(2,q,beta)
        r2=2*p2/(1-q)-r1*r1
        assert r2>r1
        ratio=innovation_one_ratio(q,beta,c)
        assert ratio < D('-0.0002'),ratio
        # For z=1-c=0.01, the missing PGF tail <= z^(terms+1),
        # and the missing first-derivative tail <= (terms+1)*z^terms.
        # Those bounds are many orders smaller than this negative margin.
        print('negative_one_count_ratio',ratio)
        C=10*D(2).ln()-6*D(3).ln()
        assert abs(C-D('0.3397980735907949458008498'))<D('1e-22')
        print('near_geometric_constant',C)
        print('PASS: six roots, signs, identity, first innovation and endpoint constant')

if __name__=='__main__':
    main()
