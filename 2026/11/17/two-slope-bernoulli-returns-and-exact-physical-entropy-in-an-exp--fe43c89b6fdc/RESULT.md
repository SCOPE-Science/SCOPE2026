# Two-slope Bernoulli returns and exact physical entropy in an expanding border-collision focus

## Finding
For each integer \(d\ge2\), consider the continuous planar border-collision map
\[
F_d(x,y)=\begin{cases}(x+y+1,0),&x\le0,\\
(y+1,-dx),&x\ge0.
\end{cases}
\]
There is a compactly supported ergodic invariant probability \(\mu_d\) with a positive-two-dimensional-Lebesgue-measure basin. On the section \(C=\{(x,0):0<x<1\}\) its first return induces the uniform Lebesgue law and independent branch choices with exactly \(2d-1\) full branches of two different absolute slopes, \(d^2\) and \(d\). The corresponding roof (return time) distribution is given explicitly in the proof.

Its positive Lyapunov exponent and metric entropy have the exact common value
\[
\boxed{\chi^+(\mu_d)=h_{\mu_d}(F_d)=\frac{2\log d}{3d+1}.}
\]
Its other Lyapunov exponent is \(-\infty\). For stationary visits \(N_n=\sum_{k=0}^{n-1}{\bf1}_{C}(F_d^kz)\), one has
\[
\frac{N_n-n/m_d}{\sqrt n}\ \Longrightarrow\ \mathcal N(0,\sigma_d^2),\quad
m_d=\frac{(d+1)(3d+1)}{2d},\quad
\sigma_d^2=\frac{2d(d-1)(d^2-2d+3)}{3(d+1)^2(3d+1)^3}.
\]
This yields an explicit nontrivial statistical description of a focus-type normal form with an expanding, nonzero-determinant right branch.

## Assumptions and scope
The integer \(d\) is at least two. All conclusions concerning time averages and Lyapunov exponents hold for the constructed invariant measure, and hence for Lebesgue-a.e. point in its specified positive-area basin, rather than for every planar orbit. The section \(C\) is a *half-open interval up to null endpoints*: for measure-theoretic calculations endpoints and their preimages are discarded. The stationary CLT is under \(\mu_d\); for initial conditions sampled from the normalized section law, the same limiting variance holds. The positive Lyapunov exponent is the exponent transverse to the uniformly collapsed direction along almost every orbit.

## Proof
**1. Exact return partition.** Put \(c(x)=(x,0)\) for \(0<x<1\). Then for every \(x\),
\[
F_d(c(x))=(1,-dx),\qquad F_d^2(c(x))=(1-dx,-d).
\]
If \(0<x<1/d\), the next two iterates are
\[
F_d^3(c(x))=(1-d,-d(1-dx)),\quad
F_d^4(c(x))=(2-2d+d^2x,0).
\]
For \(j=0,\ldots,d-1\), writing \(d^2x=j+u\) with \(0<u<1\), the fourth iterate is \((2-2d+j+u,0)\). It is nonpositive for all these \(j\), and precisely \(2d-2-j\) further left-branch iterates (each adds one to the first coordinate) bring it to \((u,0)\in C\). There was no earlier return to \(C\). Thus on
\[
A_j=(j/d^2,(j+1)/d^2),\qquad j=0,\ldots,d-1,
\]
the first-return map and roof are
\[
H_d(x)=d^2x-j,\qquad T_d(x)=2d+2-j.
\]
If \(1/d<x<1\), the third iterate instead is \((2-d-dx,0)\). On
\[
B_j=((j+1)/d,(j+2)/d),\qquad j=0,\ldots,d-2,
\]
write \(dx=1+j+u\), \(0<u<1\). Then the third iterate has first coordinate \(1-d-j-u<0\); exactly \(d+j\) left-branch translations give \((1-u,0)\in C\). Consequently
\[
H_d(x)=j+2-dx,\qquad T_d(x)=d+3+j
\]
on \(B_j\). These intervals cover \((0,1)\) apart from finitely many endpoints. Each branch is bijective onto \((0,1)\), with constant slopes \(d^2\) on the \(A_j\) and \(-d\) on the \(B_j\). Their lengths are respectively \(d^{-2}\) and \(d^{-1}\), and their sum equals one.

**2. Exact Bernoulli induced law.** The inverse branches of \(H_d\) are similarities of ratios \(1/d^2\) or \(1/d\), each mapping the whole interval onto its branch cell. A cylinder with prescribed successive branch labels therefore has Lebesgue length equal to the product of the branch lengths. Hence the labels are independent with probabilities
\[
\Pr(A_j)=d^{-2}\ (0\le j<d),\qquad
\Pr(B_j)=d^{-1}\ (0\le j<d-1).
\]
The partition cylinders shrink uniformly because all inverse contractions are bounded by \(1/d\). Thus the induced system is measurably isomorphic to a one-sided Bernoulli shift, has unique absolutely continuous invariant probability equal to normalized Lebesgue on \((0,1)\), and has entropy
\[
h_{\mathrm{Leb}}(H_d)
=-d\frac1{d^2}\log\frac1{d^2}-(d-1)\frac1d\log\frac1d
=\left(1+\frac1d\right)\log d.
\]
Uniqueness follows also from exactness: an invariant density on this full-branch uniformly expanding map must be constant. No claim of uniqueness among *all* invariant measures is made.

**3. Finite-return suspension and physicality.** The roof takes values between \(d+3\) and \(2d+2\), so is integrable. Define the orbit-suspension probability for continuous test functions \(\varphi\) by
\[
\int\varphi\,d\mu_d
=\frac1{m_d}\int_0^1\sum_{k=0}^{T_d(x)-1}
\varphi(F_d^k(x,0))\,dx,
\quad m_d=\int_0^1T_d(x)\,dx.
\]
The first-return identity and Lebesgue invariance of \(H_d\) imply \(F_d\)-invariance by telescoping the orbit sum; ergodicity follows from ergodicity of \(H_d\). Since every roof length is at most \(2d+2\), the support is contained in the compact union of closures of \(F_d^k(C)\) for those finitely many iterates. The open region \(\{(x,y):-1<x<0,\ -x-1<y<-x\}\) has positive planar area and its first iterate lies in \(C\). Its intersection with the preimage of the Lebesgue-generic set of \(H_d\) has full area in that region because the map \((x,y)\mapsto x+y+1\) has nonzero gradient. Thus \(\mu_d\) is physical on a positive-area set.

**4. Exact mean, variance, and entropy.** The roof distribution in Step 2 gives
\[
\begin{aligned}
m_d&=\frac1{d^2}\sum_{j=0}^{d-1}(2d+2-j)
 +\frac1d\sum_{j=0}^{d-2}(d+3+j)
 =\frac{(d+1)(3d+1)}{2d},\\
\operatorname{Var}(T_d)&=\frac{(d-1)(d+1)(d^2-2d+3)}{12d^2}.
\end{aligned}
\]
The induced Bernoulli entropy and Abramov's return-entropy formula give
\[
h_{\mu_d}(F_d)=\frac{h_{\mathrm{Leb}}(H_d)}{m_d}=\frac{2\log d}{3d+1}.
\]
On full-measure return cylinders, the derivative of \(F_d^{T_d(x)}\) along the section is \(H_d'(x)\), giving \(\log|H_d'|=2\log d\) on \(A_j\) and \(\log d\) on \(B_j\). Division by mean return time gives the stated positive exponent. Every such return contains a left-branch derivative of rank one, so all sufficiently long matrix derivative products have rank at most one; the second exponent is \(-\infty\). The tangent section direction is nonzero under each return, so the positive exponent is genuine.

**5. Visit-count CLT.** With return times sampled under Lebesgue on \(C\), the roof process is iid with the displayed mean and variance. The classical iid central-limit theorem for partial sums followed by inversion of the renewal counting process gives the stationary renewal variance \(\operatorname{Var}(T_d)/m_d^3\), exactly \(\sigma_d^2\) above. For the stationary suspension law, the initial partial roof and terminal incomplete roof are bounded by \(2d+2\); their effects vanish under normalization by \(\sqrt n\). This establishes the stated convergence under \(\mu_d\).

## Verification
The standalone Python 3 standard-library checker `check.py` enumerates all \(2d-1\) return intervals and tests four rational interior points on each for every integer \(2\le d\le24\), comparing the actual planar orbit with the displayed roof and affine return formulas. It checks the probabilities, mean and variance in exact rational arithmetic and checks the entropy identity numerically. Run `python3 check.py`. It reports `VERIFY_OK exact_rational_orbit_checks=2300 integer_parameters=23`. These finite checks do not prove the all-integer result, which follows from the symbolic orbit and renewal arguments above.

## Relationship to prior work
Simpson (2026) establishes the general Farey-ordered configuration of one-dimensional first-return intervals in the zero-left-determinant border-collision family when the right fixed point is an expanding focus. That theorem includes the present parameters but does not assert a stationary Bernoulli law, exact branch-weighted roof moments, physical entropy or return-visit CLT. This result specializes the map to \(\tau_L=1,\tau_R=0,\delta_R=d\) with integer \(d\ge2\), producing two different full-branch slopes and all the quantitative invariants above. Simpson (2024/2025) broadly classifies qualitative bifurcations rather than these exact invariant statistics. Glendinning (2014) concerns absolutely continuous *planar* measures in regions where the normal form branches are nonsingular, whereas here the constructed measure is singular relative to planar area and absolutely continuous only on the return section. The standard Bernoulli/Abramov and renewal theorems are used as classical tools, not claimed as original. Related published integer-slope rank-one normal forms with **both** branch determinants zero have different induced maps and do not imply the present expanding-focus results.

## Limitations
The claim is restricted to this exact integer-parameter slice and the constructed physical measure. It does not give the full basin, uniqueness of all invariant measures, topological entropy, results for nonintegral determinants, or generic persistence under perturbation. Exceptional endpoints of branches can have different orbits, but constitute a null set for all probabilistic assertions. The variance is a stationary distributional asymptotic, not a uniform error estimate. Historical priority remains provisional until an independent literature audit; the highly relevant prior return-map theorem gives the branch setup and could permit alternative deductions of some individual formulas.

## References
1. D. J. W. Simpson, *One-dimensional first return maps for the two-dimensional border-collision normal form with a zero determinant*, arXiv:2606.08901v1, first public 2026-06-08, https://arxiv.org/html/2606.08901v1, particularly Sections 2 and 5.
2. D. J. W. Simpson, *The two-dimensional border-collision normal form with a zero determinant*, arXiv:2408.04790v1, first public 2024-08-08; SIAM J. Appl. Dyn. Syst. 24 (2025), 2205–2245, https://arxiv.org/html/2408.04790v1.
3. P. Glendinning, *Invariant measures for the n-dimensional border collision normal form*, Int. J. Bifurcation Chaos (2014), https://eprints.maths.manchester.ac.uk/2252/.
4. L. M. Abramov, *The entropy of a derived automorphism*, Dokl. Akad. Nauk SSSR 128 (1959), 647–650 (classical induced-entropy formula).
