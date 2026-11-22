"""Exact arithmetic checks for random-repartition minibatch reshuffling.

Python 3 standard library only; run: python verify.py
This finite checker supplements rather than replaces the infinite-series proof.
"""
from fractions import Fraction as Q
from itertools import permutations, combinations, product
from math import factorial

nchecks = 0

def eq(x, y, label):
    global nchecks
    assert x == y, (label, x, y)
    nchecks += 1


def mean(vals):
    return sum(vals, Q(0)) / len(vals)


def var(vals):
    u = mean(vals)
    return mean([(x-u)**2 for x in vals])


def ordered_batch_noise(data, b, q, perm):
    eta = 1-q
    m = len(data)//b
    Z = [mean([data[j] for j in perm[k*b:(k+1)*b]]) for k in range(m)]
    return eta * sum((q**(m-1-k)*Z[k] for k in range(m)), Q(0))


def formula_epoch_variance(data, b, q):
    n=len(data);m=n//b
    v=mean([z*z for z in data])*Q(n-b, b*(n-1))
    w=[q**j for j in range(m)]
    return (1-q)**2*v*(Q(m,m-1)*sum((x*x for x in w),Q(0))-sum(w,Q(0))**2/Q(m-1))

for data,b in [([Q(1),Q(1),Q(-1),Q(-1)],2),
               ([Q(3),Q(-2),Q(-1),Q(3),Q(-2),Q(-1)],3),
               ([Q(1),Q(2),Q(3),Q(-1),Q(-2),Q(-3)],2)]:
    n=len(data);m=n//b
    eq(sum(data),Q(0),'centered')
    allperms=list(permutations(range(n)))
    for q in [Q(-1,2),Q(0),Q(1,3),Q(1,2),Q(2,3)]:
        vals=[ordered_batch_noise(data,b,q,p) for p in allperms]
        eq(mean(vals),Q(0),'noise mean')
        v=formula_epoch_variance(data,b,q)
        eq(var(vals),v,'exact unconditional variance')
        for k in range(1,8):
            eta=1-q
            r=q**m
            expected=v*sum((r**(2*j) for j in range(k)), Q(0))
            closed=v*(1-r**(2*k))/(1-r*r) if r*r!=1 else v*k
            eq(expected,closed,'exact finite horizon')

# Three equiprobable set partitions of four points into two unordered pairs:
data=(Q(1),Q(1),Q(-1),Q(-1))
parts=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
for p in parts:
    sorted_groups=tuple(sorted(tuple(sorted(z)) for z in p))
    eq(sorted_groups,tuple(sorted(tuple(sorted(z)) for z in p)),'partition canonical')
for q in [Q(-1,2),Q(0),Q(1,3),Q(1,2),Q(2,3)]:
    eta=1-q;r=q*q
    vlist=[]
    for pairs in parts:
        z=[mean([data[i] for i in group]) for group in pairs]
        noise=[eta*(q*z[0]+z[1]), eta*(q*z[1]+z[0])]
        if pairs==parts[0]:
            eq(set(noise),{eta*eta,-eta*eta},'aligned noise')
            eq(var(noise),eta**4,'aligned noise variance')
        else:
            eq(noise,[Q(0),Q(0)],'mixed pair cancellation')
            eq(var(noise),Q(0),'mixed variance')
        vlist.append(var(noise))
    eq(mean(vlist),eta**4/Q(3),'annealed variance')
    # Current-epoch law from all six equally weighted outcomes
    choices=[]
    for pairs in parts:
        z=[mean([data[i] for i in group]) for group in pairs]
        choices += [eta*(q*z[0]+z[1]),eta*(q*z[1]+z[0])]
    eq(choices.count(Q(0)),4,'fresh zero digit frequency')
    eq(choices.count(eta**2),1,'fresh positive frequency')
    eq(choices.count(-eta**2),1,'fresh negative frequency')
    for k in range(1,7):
        # E[X_k^2] from i.i.d. centered epochs
        variance=(eta**4/Q(3))*sum((r**(2*j) for j in range(k)),Q(0))
        expected_fixed=Q(1,3)*eta**4*sum((r**(2*j) for j in range(k)),Q(0))
        eq(variance,expected_fixed,'fresh versus frozen horizon')

# Exact IFS separation criterion for support hull [-delta/(1-r),delta/(1-r)].
for r in [Q(1,10),Q(1,4),Q(1,3),Q(2,5),Q(1,2)]:
    M=Q(1)/(1-r)
    # right endpoint of the left interval and left endpoint of central interval
    right_left=-1+r*M
    left_mid=-r*M
    gap=left_mid-right_left
    eq(gap,(1-3*r)/(1-r),'three-map gap')
    eq((gap>0),(r<Q(1,3)),'strict Cantor separation')
    eq((gap==0),(r==Q(1,3)),'critical interval touching')

print('VERIFY_OK',nchecks)
