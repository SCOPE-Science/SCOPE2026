"""Independent exact-arithmetic checks for the metric loop-with-arms distance law."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from random import Random


def atoms(h, aa):
    k=len(aa)
    z=Counter()
    for a in aa:
        z[a]-=k
        z[a+h]+=2
    for a,b in combinations(aa,2):
        z[a+b]+=1
    return Counter({x:y for x,y in z.items() if y})


def recover(h, k, nu):
    z=Counter(nu)
    known=[]
    for _ in range(k):
        z=Counter({x:y for x,y in z.items() if y})
        if not z: raise AssertionError('ran out of atoms')
        x=min(z)
        coeff=z[x]
        assert coeff<0 and coeff%k==0, (h,known,x,coeff,z)
        # A repeated atom is identified in one operation.
        mul=-coeff//k
        new=[x]*mul
        assert len(known)+mul<=k
        for a in new:
            z[a]+=k
            z[a+h]-=2
        for a,b in combinations(new,2):
            z[a+b]-=1
        for a in known:
            for b in new: z[a+b]-=1
        known.extend(new)
        if len(known)==k:
            assert not any(z.values()), z
            return sorted(known)
    raise AssertionError('unfinished')


def density(r,h,aa):
    c=2*h; L=c+sum(aa); k=len(aa)
    def pos(x): return max(x,F(0))
    g=c*int(r<h)
    for a in aa:
        g+=pos(a-r)
        g+=2*(pos(r)-pos(r-a)-pos(r-h)+pos(r-a-h))
    for a,b in combinations(aa,2):
        g+=pos(r)-pos(r-a)-pos(r-b)+pos(r-a-b)
    return 2*g/(L*L)

rng=Random(21)
tested=0
for k in range(1,9):
    for j in range(120):
        h=F(rng.randrange(1,9),rng.randrange(1,6))
        aa=sorted(F(rng.randrange(1,13),rng.randrange(1,7)) for _ in range(k))
        nu=atoms(h,aa)
        got=recover(h,k,nu)
        assert got==aa,(h,aa,got)
        L=2*h+sum(aa)
        assert density(F(0),h,aa)==F(2,L)
        t=min([h]+aa)/100
        slope=(density(t,h,aa)-density(F(0),h,aa))/t
        assert slope==F(k*(k+1),L*L)
        tested+=1
# The density has precisely one discontinuity; only the loop-loop contribution jumps.
for h,aa in [(F(1),[F(1),F(1),F(2)]),(F(2),[F(2),F(1),F(1),F(3)]),(F(7,4),[F(1,2),F(5,4)])]:
    L=2*h+sum(aa)
    eps=F(1,10**7)
    left=density(h-eps,h,aa);right=density(h+eps,h,aa)
    assert abs((left-right)-F(4*h,L*L))< F(1,10000)
# Compute a direct Euclidean-length-or-circle geodesic simulation against formula's cdf.
import numpy as np
h=1.7
lengths=[0.4,0.9,2.3]
c=2*h
L=c+sum(lengths)
rngnp=np.random.default_rng(77)
N=350000
u=rngnp.random((N,2))*L
bounds=np.cumsum([c]+lengths)
ids=np.searchsorted(bounds,u,side='right')
def point_params(v,ii):
    return v-np.where(ii==0,0,np.r_[0,bounds[:-1]][ii])
v=point_params(u,ids)
res=np.empty(N)
both_circle=(ids[:,0]==0)&(ids[:,1]==0)
res[both_circle]=np.minimum(np.abs(v[both_circle,0]-v[both_circle,1]),c-np.abs(v[both_circle,0]-v[both_circle,1]))
both_same_arm=(ids[:,0]==ids[:,1])&(ids[:,0]!=0)
res[both_same_arm]=np.abs(v[both_same_arm,0]-v[both_same_arm,1])
cc=(ids[:,0]==0)^(ids[:,1]==0)
res[cc]=np.where(ids[cc,0]==0,np.minimum(v[cc,0],c-v[cc,0])+v[cc,1],np.minimum(v[cc,1],c-v[cc,1])+v[cc,0])
others=~(both_circle|both_same_arm|cc)
res[others]=v[others,0]+v[others,1]
maxdiff=0.
from scipy.integrate import quad
for threshold in [0.18,0.5,0.95,1.4,2.1,2.9,3.8]:
    analytic=quad(lambda r: float(density(F(str(r)),F('1.7'),[F('0.4'),F('0.9'),F('2.3')])),0,threshold,points=[x for x in [0.4,0.9,1.7,2.1,2.3,2.6,3.2,3.4,4] if 0<x<threshold],epsabs=1e-9)[0]
    empirical=float(np.mean(res<=threshold))
    maxdiff=max(maxdiff,abs(analytic-empirical))
    assert abs(analytic-empirical)<0.006, (threshold,analytic,empirical)
print('VERIFY_OK exact_reconstructions=',tested,'continuity_collision_cases=3 direct_pairs=',N,'max_cdf_discrepancy=',round(maxdiff,6),sep='')
