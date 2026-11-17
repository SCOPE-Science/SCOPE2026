"""Exact-rational checks for sharp weighted-variation isotonic projection.
Only Python standard library required. Run: python verify_weighted_isotonic.py.
"""
from fractions import Fraction as Q
from itertools import product


def weighted_pav(data, mass):
    blocks=[]
    for i,(z,m) in enumerate(zip(data,mass)):
        blocks.append([i,i,m,m*z])
        while len(blocks)>1 and blocks[-2][3]/blocks[-2][2]>blocks[-1][3]/blocks[-1][2]:
            v=blocks.pop(); blocks[-1][1]=v[1];blocks[-1][2]+=v[2];blocks[-1][3]+=v[3]
    result=[None]*len(data)
    for l,r,m,s in blocks:
        for i in range(l,r+1):result[i]=s/m
    return result


def variation(x,w):
    return sum(w[i]*abs(x[i+1]-x[i]) for i in range(len(w)))


def formula(mass,w):
    n=len(mass)
    mw=[Q(0)]+list(w)+[Q(0)]
    cum=[Q(0)]
    for t in mass:cum.append(cum[-1]+t)
    terms=[]
    for e in range(1,n):
        for j in range(e):
            for k in range(e+1,n+1):
                interp=((cum[k]-cum[e])*mw[j]+(cum[e]-cum[j])*mw[k])/(cum[k]-cum[j])
                terms.append((interp/mw[e],j,e,k))
    return max([Q(1)]+[v[0] for v in terms]), terms


def matrix_partition_norm(mass,w,cuts):
    n=len(mass)
    blocks=[];left=0
    for k in range(n-1):
        if cuts[k]:blocks.append((left,k));left=k+1
    blocks.append((left,n-1))
    answers=[]
    for e in range(1,n):
        h=[Q(0) if i<e else Q(1) for i in range(n)]
        out=h.copy()
        for l,r in blocks:
            avg=sum((mass[i]*h[i] for i in range(l,r+1)),Q(0))/sum(mass[l:r+1])
            for i in range(l,r+1):out[i]=avg
        answers.append(variation(out,w)/w[e-1])
    return max(answers)


def concavity(mass,w):
    a=[Q(0)]+list(w)+[Q(0)]
    return all((a[i]-a[i-1])/mass[i-1] >=(a[i+1]-a[i])/mass[i] for i in range(1,len(mass)))


def upper_hull_constant(mass,w):
    # Independent O(n) upper-concave-hull computation, no chord enumeration.
    y=[Q(0)]
    for m in mass:y.append(y[-1]+m)
    h=[Q(0)]+list(w)+[Q(0)]
    hull=[]
    for i in range(len(y)):
        hull.append(i)
        while len(hull)>=3:
            a,b,c=hull[-3:]
            if (h[b]-h[a])*(y[c]-y[b]) < (h[c]-h[b])*(y[b]-y[a]):
                hull.pop(-2)
            else:
                break
    t=0;best=Q(1)
    for i in range(1,len(mass)):
        while t+1<len(hull)-1 and i>hull[t+1]:t+=1
        a,b=hull[t],hull[t+1]
        top=((y[b]-y[i])*h[a]+(y[i]-y[a])*h[b])/(y[b]-y[a])
        best=max(best,top/h[i])
    return best,hull

count=0
witness_count=0
for n in range(2,8):
    mprofiles=[tuple(Q(1) for _ in range(n)),tuple(Q(1+(i*3)%7) for i in range(n)),tuple(Q(2+(i*5)%9) for i in range(n))]
    wprofiles=[tuple(Q(1) for _ in range(n-1)),tuple(Q(1+(i*5)%8) for i in range(n-1)),tuple(Q(2+(i*3)%9) for i in range(n-1))]
    for mass in mprofiles:
      for w in wprofiles:
        exact,terms=formula(mass,w)
        partitions=max(matrix_partition_norm(mass,w,cuts) for cuts in product((0,1),repeat=n-1))
        assert partitions==exact,(n,mass,w,partitions,exact)
        assert (exact==1)==concavity(mass,w)
        assert upper_hull_constant(mass,w)[0]==exact
        count+=1
        eps=Q(1,10000000)
        for val,j,e,k in terms:
            # Block [j+1,k] in one-based notation, crossing edge e.
            l=j; r=k-1
            y=[Q(i-l) if i<l else (Q(0) if i<=r else Q(i-r)) for i in range(n)]
            data=y.copy();data[l]+=Q(1)/mass[l];data[r]-=Q(1)/mass[r]
            assert weighted_pav(data,mass)==y,(n,j,e,k,'base')
            h=[Q(0) if i<e else Q(1) for i in range(n)]
            perturbed=[data[i]+eps*h[i] for i in range(n)]
            out=weighted_pav(perturbed,mass)
            t=sum(mass[e:r+1])/sum(mass[l:r+1])
            expected=[y[i]+eps*(t if l<=i<=r else h[i]) for i in range(n)]
            assert out==expected,(n,mass,w,j,e,k,out,expected)
            assert variation([out[i]-y[i] for i in range(n)],w)/(eps*w[e-1])==val
            witness_count+=1
print('EXACT_ALL_BLOCK_PARTITION_NORMS_PASSED',count)
print('EXACT_ALL_ACTIVE_BLOCK_WITNESSES_PASSED',witness_count)
print('EXACT_MASS_AWARE_CONCAVITY_EQUIVALENCE_PASSED')
print('LINEAR_TIME_LEAST_CONCAVE_MAJORANT_FORMULA_PASSED')
print('ALL_WEIGHTED_ISOTONIC_VARIATION_CHECKS_PASSED')
