"""Exact-rational checks for the star-graph rooted-forest trace estimator."""
from fractions import Fraction as F
from itertools import product
from math import comb

CHECKS = 0

def check(x, y, context):
    global CHECKS
    assert x == y, (context, x, y)
    CHECKS += 1


def closed(k, q):
    v = q*(k-1)/(q+1)**2 + q*(k+1)/(q+k+1)**2
    cov = k*(k+2*q+1)/((q+1)*(q+k+1))
    vc = k*(2*k*q+k+2*q*q+4*q+3)/(q*(q+1)*(k+q+1))
    a = cov/vc
    return v, cov, vc, a


def enum(k, q):
    # Each tuple encodes a directed rooted forest on a unit-edge star.
    # Case A: center rooted, each leaf either rooted or directed to center.
    # Case B: center directed to exactly one rooted leaf, every other leaf
    # either rooted or directed to center.
    moments = [F(0),F(0),F(0),F(0),F(0),F(0)]
    weights = F(0)
    for center in [-1]+list(range(k)):
        for bits in product((0,1),repeat=k):
            if center>=0 and bits[center]!=1: continue
            j=sum(bits)
            r = j+(center<0)
            # Number of cross-root incidences at the root vertices:
            if center<0:
                boundary=2*j
            else:
                boundary=j-1
            c=F(r-(k+1),1)+F(boundary,1)/q
            w=q**r
            weights+=w
            for ix,val in enumerate((r,r*r,c,c*c,r*c,1)):
                moments[ix]+=w*val
    moments=[v/weights for v in moments]
    er,er2,ec,ec2,erc,_=moments
    return weights,er,er2-er**2,erc-er*ec,ec2-ec**2,ec

for k in range(1,9):
    for q in (F(1,3),F(1,2),F(1),F(7,4),F(3),F(10)):
        Z,er,v,cov,vc,ec=enum(k,q)
        vv,cc,vcc,a=closed(k,q)
        check(Z,q*(q+1)**(k-1)*(q+k+1),('partition',k,q))
        check(v,vv,('root variance',k,q))
        check(cov,cc,('covariance',k,q))
        check(vc,vcc,('control variance',k,q))
        check(ec,F(0),('control mean',k,q))
        check(er,F(1)+(k-1)*q/(q+1)+q/(q+k+1),('mean roots',k,q))
        check((v-2*a*cov+a*a*vc),v-cov*cov/vc,('optimal risk',k,q))
        ah=q/(q+F(2*k,k+1))
        check((v-2*ah*cov+ah*ah*vc)>=(v-cov*cov/vc),True,('minimum',k,q))
        if k >= 2:
            check((v-cov*cov/vc)>0,True,('strict residual',k,q))

# A large irregular star: effectiveness deteriorates for the degree-mean setting.
for q_int in (10,100,1000):
    q=F(q_int);k=q_int*q_int
    v,cov,vc,a=closed(k,q)
    ah=q/(q+F(2*k,k+1))
    ratio_opt=(v-cov*cov/vc)/v
    ratio_h=(v-2*ah*cov+ah*ah*vc)/v
    check(F(0)<ratio_opt<ratio_h<F(1),True,('double-scaling finite',q_int))
print('VERIFIED exact rational assertions:',CHECKS)
print('The checker does not assert infinite-parameter claims from finite tests.')
