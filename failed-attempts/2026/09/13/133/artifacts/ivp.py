import numpy as np, sys
sys.path.insert(0,'output/artifacts')
from fastdelta import Delta_grid
# Interval evaluation of a single Delta pair over box: Delta(x;a,b) = sum of r at affine images.
# r(y)=1+0.04 sin(2pi y1)+0.03 cos(2pi y2); constants cancel in quadrilateral combo.
# Implement interval arithmetic (numpy vectorized over corners of boxes? rigorous: use single box with monotonicity splitting).
# Simpler rigorous approach: Lipschitz bound. P(x)=Delta(x;a,b). |grad P| <= L computable in closed form:
# grad P = sum over orbit terms of corner Jacobians: each forward term k: grad = (B^k)^T [dr(c1)-dr(c2)-dr(c3)+dr(c4)]... bound each |dr|<=2pi*(0.04,0.03).
# Corner differences: |dr(c_i)-dr(c_j)| <= Lip(dr)*dist(c_i,c_j); forward dist contracts for stable-separated corners, expands for unstable.
# Actually simplest: each summand S_k(x) = r(B^k(x+aeu+bes)) - ... ; grad S_k = (B^k)^T v_k where v_k = dr(p1)-dr(p2)-dr(p3)+dr(p4), |v_k| <= 2*min(Lip stuff).
# Bound: |v_k| <= 2pi*0.08*pi*|b|*mu^k*C1 ... let's just carefully derive below and get numeric L.
# dr(y) = (0.08 pi cos(2pi y1), -0.06 pi sin(2pi y2)). Lip constant of dr (operator norm) = max(0.16 pi^2, 0.12 pi^2) = 0.16 pi^2 ~ 1.579.
Ldr = 0.16*np.pi**2
lam = (3+np.sqrt(5))/2; mu=(3-np.sqrt(5))/2
print("Ldr",Ldr,"lam",lam,"mu",mu)
# S_k^fwd(x) = r(B^k xu)-r(B^k xus)-r(B^k x)+r(B^k xs), xu=x+aeu, xs=x+bes, xus=x+aeu+bes.
# grad S_k = (B^k)^T [dr(B^k xu)-dr(B^k xus)-dr(B^k x)+dr(B^k xs)].
# Pair as [dr(B^k xu)-dr(B^k xus)] - [dr(B^k x)-dr(B^k xs)]: each difference across stable separation b*mu^k (B^k contracts es by mu^k).
# |each| <= Ldr*|b|*mu^k. So |w_k| <= 2*Ldr*|b|*mu^k. |grad S_k| <= ||B^k|| * 2 Ldr |b| mu^k = lam^k * 2 Ldr |b| mu^k = 2 Ldr |b| (lam mu)^k = 2 Ldr |b|.
# That does NOT decay -> sum over k diverges. Need better: pair across unstable separation instead? [dr(xu)-dr(x)] - [dr(xus)-dr(xs)]: each across a*lam^k, grows. Worse.
# Mixed pairing with second-difference bound: |w_k| <= L2 *|a|lam^k*|b|mu^k = L2|ab| (second derivative bound), L2 = max|D2r| = 0.16 pi^2 same. Then |grad S_k| <= lam^k L2 |ab|. Grows! Hmm, grad of each term genuinely grows like lam^k; sum of grads diverges termwise but true grad converges (cancellation across k? no...).
# Wait — true P(x) = sum_k S_k(x) with S_k decaying like mu^k uniformly, but grad S_k ~ O(1) (first pairing) so sum of grad bounds diverges. True Lipschitz must come from differentiating the CONVERGED representation differently (e.g. split: differentiate stable-holonomy part along stable gives contraction...). Standard: temporal function is only Holder, but here r is smooth and B linear: P(x) is actually C^1? Each S_k smooth; sum of grads O(1) each -> may genuinely diverge (P only Holder-continuous in x along unstable direction?). Hmm, but P involves B^k x with k->inf: high-frequency oscillations, like Weierstrass: P might be nowhere-differentiable! Lipschitz grid certification then needs modulus of continuity, not gradient.
# Modulus: |S_k(x)-S_k(z)| <= min(2*|S_k| sup bound ~ C|ab|mu^k*?, Lip*|x-z| lam^k).
# sup|S_k| <= 2*Ldr*|b|mu^k*? Let's bound: |S_k| <= |r(B^k xu)-r(B^k xus)| + |r(B^k x)-r(B^k xs)| <= 2*Lip(r)*|b|*mu^k, Lip(r)=max|dr|=0.08pi~0.251.
Lipr = 0.08*np.pi
print("Lipr",Lipr)
# |S_k(x)-S_k(z)| <= Lip(S_k)|x-z|, Lip(S_k) <= lam^k * 4*max|dr| = lam^k*4*Lipr? grad S_k = (B^k)^T w, |w|<=4 max|dr| = 4*Lipr? max|dr| = sqrt((0.08pi)^2+...)? bound 0.08pi+0.06pi ~ use 0.32. Lip(S_k)<= lam^k * 4*0.32 ~ lam^k*1.28.
# modulus per k: min(4*Lipr*|b|mu^k, 1.28 lam^k d). Sum over k: split at K*: standard Holder estimate.
# Similarly backward terms with |a| and Bi.
# This gives Holder-1/2-type modulus ~ C sqrt(|ab| d)? Let's just implement: W(d) = sum_{k>=0} min(Uk, Lk d) + sum_{j>=1} min(Uj', Lj' d).
def modulus(d, a, b, K=200):
    tot=0.0
    Mdr = np.sqrt((0.08*np.pi)**2+(0.06*np.pi)**2)  # max |dr|
    for k in range(K+1):
        Uk = 4*Mdr*abs(b)*mu**k  # sup bound via stable pairing... check factor: two differences each <= Lipr|b|mu^k with Lipr=max|dr|; use Mdr
        Lk = 4*Mdr*lam**k
        tot += min(Uk, Lk*d)
    for j in range(1,K+1):
        Uj = 4*Mdr*abs(a)*mu**j
        Lj = 4*Mdr*lam**j
        tot += min(Uj, Lj*d)
    return tot
for d in [1e-4, 5e-4, 1e-3, 2e-3]:
    print("d",d,"W",modulus(d,0.05,0.05))
