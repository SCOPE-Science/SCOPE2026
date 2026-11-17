# Exact period-two census and supercritical onset in a finite-memory fractional logistic map

## Finding

For every fractional order \(0<q\leq1\), every positive integer memory length \(M\), and every real control parameter \(r>0\), consider the finite-memory Grünwald–Letnikov logistic recurrence defined below. Its primitive period-two orbits are classified completely: there are none at or below the known fixed-point flip parameter \(r_*\), and exactly one unordered primitive period-two orbit above it. The orbit is explicit, both values lie strictly between zero and one, and its onset is a **genuine, nondegenerate supercritical flip for every \(q,M\)**: the critical multiplier is simple, all other multipliers are strictly within the unit disk, and the newly born two-cycle attracts locally. The result does not assert stability of the two-cycle for arbitrary large \(r\).

Define
\[
G=\sum_{j=1}^{M}g_j,\quad H=\sum_{j=1}^{M}(-1)^{1-j}g_j,
\quad R=2+G,\quad r_*=2R-H.
\]
The unique unordered two-cycle for \(r>r_*\) has scalar phases
\[
\boxed{x_{\pm}=\frac{r-H\pm\sqrt{(r-H)(r-r_*)}}{2r}.}
\]
Thus its half-separation obeys the exact, all-memory law
\[
\boxed{d^2=\frac{(r-H)(r-r_*)}{4r^2}},\qquad
\boxed{\lim_{r\downarrow r_*}\frac{d^2}{r-r_*}
=\frac{r_*-H}{4r_*^2}>0.}
\]

There is also an explicit exact certificate of the noncritical spectral gap. Put \(b_j=-g_j\) and, for \(1\leq k\leq M-1\),
\[
c_k=\sum_{j=k+1}^{M}(-1)^{j-k-1}b_j,
\quad S=1-\sum_{k=1}^{M-1}(-1)^kc_k.
\]
Then \(0<S\), every noncritical eigenvalue at \(r=r_*\) has modulus less than one, and the critical multiplier has derivative \(-1/S\) with respect to \(r\). The critical center-map cubic coefficient, with critical coordinate normalized by the first component of the alternating eigenvector, is
\[
\boxed{L=\frac{4r_*^2}{S(r_*-H)}>0.}
\]
The critical two-step Floquet multiplier of the new two-cycle is
\[
\boxed{\Lambda_2(r)=1-\frac{4(r-r_*)}{S}
+O((r-r_*)^{3/2})}\qquad(r\downarrow r_*).
\]

## Assumptions and scope

The recurrence is
\[
\sum_{j=0}^{M}g_jx_{n+1-j}=r x_n(1-x_n)-x_n,
\quad g_0=1,\quad g_j=(-1)^j\binom qj.
\]
For arbitrary real initial history this is the autonomous real \(M\)-dimensional companion map, whose first coordinate is \(x_n\). A primitive period-two orbit means a pair of distinct states exchanged by this map. The shift coordinates force its scalar values to alternate between exactly two numbers. No assumption is made about the orbit's basin of attraction, and arbitrary initial histories need not be biological.

For \(0<q<1\), the weights satisfy \(b_j>0\), \(b_{j+1}<b_j\) and \(\sum_{j=1}^{\infty}b_j=1\). For \(q=1\), \(b_1=1\) and the remaining weights vanish. In both cases \(H<0\), \(R>0\), \(R-H>0\), and \(R+H\geq0\). Empty sums are zero, including when \(M=1\).

## Proof

**1. Classification by the two phase equations.** Write any primitive period-two scalar sequence as \(x_n=m+(-1)^nd\), where \(d\ne0\). The mean and alternating parts of the recurrence are precisely
\[
Rm=r\{m(1-m)-d^2\},\qquad H=r(1-2m).
\]
The second equation gives \(m=(r-H)/(2r)\), and substitution into the first gives
\[
d^2=\frac{(r-H)(r+H-2R)}{4r^2}
=\frac{(r-H)(r-r_*)}{4r^2}.
\]
Since \(r-H>0\) for all \(r>0\), a nonzero real \(d\) exists if and only if \(r>r_*\). It is unique up to exchanging the phases. Conversely, the two displayed phase equations guarantee the entire original recurrence at both phases, and the shift coordinates provide the corresponding \(M\)-state orbit, proving sufficiency and completeness.

For \(r>r_*\), both phases lie in the open unit interval. Indeed,
\[
m^2-d^2=\frac{(r-H)(R-H)}{2r^2}>0
\]
and
\[
(1-m)^2-d^2=\frac{r(R+H)+H(H-R)}{2r^2}>0.
\]
Here \(m\in(0,1)\), \(R+H\ge0\), \(H<0\), and \(H-R<0\). These inequalities give \(0<m-d<m+d<1\).

**2. The complete spectrum at the first flip.** The nonzero fixed branch \(x_*(r)=1-R/r\) exists around \(r_*\). Its companion characteristic polynomial is
\[
P_r(z)=z^M-\bigl(2R-r-1+b_1\bigr)z^{M-1}
-\sum_{j=2}^{M}b_jz^{M-j}.
\]
At the established threshold \(r_*\), direct multiplication gives
\[
P_{r_*}(z)=(z+1)Q(z),\qquad
Q(z)=z^{M-1}-\sum_{k=1}^{M-1}c_kz^{M-1-k}.
\]
The alternating tails \(c_k\) are nonnegative because \(b_j\) is nonincreasing. A finite interchange of summations yields the sharper identity
\[
\sum_{k=1}^{M-1}c_k=\sum_{\substack{2\leq j\leq M\\j\text{ even}}}b_j<1.
\]
Consequently, if \(Q(z)=0\) and \(|z|\ge1\), then
\[
|z|^{M-1}\le\sum_kc_k|z|^{M-1-k}
\le|z|^{M-1}\sum_kc_k<|z|^{M-1},
\]
a contradiction. Thus every root of \(Q\) is strictly in the open unit disk; \(-1\) is simple. Because \(Q(-1)=(-1)^{M-1}S\) and \(S>0\), implicit differentiation of \(P_r(z)=0\) gives
\[
\left.\frac{dz}{dr}\right|_{r_*}=-\frac1S<0.
\]
This also covers \(M=1\), with \(Q=1\). It proves that no hidden unit multiplier or higher-dimensional resonance occurs at the onset.

**3. Supercriticality and local attraction.** Standard one-dimensional center-manifold and flip normal-form reduction applies to this polynomial map, because precisely one simple multiplier equals \(-1\) while all others have modulus below one. Choose a center coordinate \(w\) with linear first-coordinate normalization one and eliminate its quadratic term. With \(\mu=r-r_*\), the reduced map has the form
\[
w_{n+1}=-\left(1+\frac\mu S+O(\mu^2)\right)w_n
+Lw_n^3+O(w_n^4+|\mu|w_n^2+\mu^2|w_n|).
\]
The explicit two-cycle has half-separation \(d^2=K\mu+O(\mu^2)\), where \(K=(r_*-H)/(4r_*^2)>0\). Its two center coordinates equal \(\pm d+O(\mu)\), because the critical right eigenvector has first component one and alternating shift components. Substitution into the two-cycle equation for the center map forces the resonant coefficient to equal \(L=(1/S)/K=4r_*^2/[S(r_*-H)]>0\). The two-step derivative along this branch therefore equals \(1-4\mu/S+O(\mu^{3/2})\). The other two-step eigenvalues remain strictly in the disk by continuity from the eigenvalues of the square of the fixed-point Jacobian. Hence the two-cycle attracts locally for all sufficiently small positive \(\mu\), and the flip is nondegenerate and supercritical.

## Verification

Run `python3 check_period2.py` with Python 3 and NumPy. The standalone program verifies rational coefficients and the polynomial factorization exactly using fractions; it also checks exact rational phase identities and open-interval inequalities, and performs finite numerical spectrum and local multiplier checks. Its expected summary is `VERIFY_OK exact_fraction_cases=48 exact_period2_instances=144 spectral_cases=36 local_multiplier_cases=108`. The exhaustive statements follow from the preceding proof, not from these finite tests.

For example, at \(q=1/2\), \(M=2\), one obtains \(G=-5/8\), \(H=-3/8\), \(R=11/8\), \(r_*=25/8\), \(S=9/8\), and the two-cycle is present exactly for \(r>25/8\). The critical leading normal-form coefficient is \(L=625/63\). For \(q=1\), the theorem reduces to the classical logistic first flip at \(r_*=3\), with \(L=9\).

## Relationship to prior work

Dong, Li, Li and Xie (2026) introduced the finite-memory Grünwald–Letnikov logistic Floquet formulation and proved the fixed-point \(-1\) threshold formula, which is used here as established mathematics. They gave a periodic/antiperiodic reduction for arbitrary periods and numerical studies of subsequent doublings, but not the present closed all-parameter primitive period-two classification, all-memory spectral separation, or universally positive center-map cubic coefficient. The present argument solves and sharpens the first branch of that framework rather than claiming the threshold formula as new.

Edelman, Helman and Smidtaite (2023) studied generalized fractional maps with nontruncated history and asymptotically periodic trajectories; those are not the exact periodic orbits of the finite-dimensional truncated recurrence. Standard flip normal-form theory supplies the local reduction, not the problem-specific sign or exact phase law proved here.

## Limitations

The result proves local attraction only sufficiently close to the first flip, not beyond later bifurcations. It does not establish attraction for arbitrary histories or a global invariant biological state cube. No assertion is made for infinite memory, for orders outside \(0<q\le1\), or about exact period four and higher. Historical priority is assessed relative to the material specifically inspected; exhaustive priority and independent mathematical validation have not been established.

## References

1. Z. Dong, H. Li, S. Li, and Y. Xie, *Memory-Dependent Shifts of the Period-Doubling Cascade in the Finite-Memory Grünwald–Letnikov Fractional Logistic Map*, preprint posted July 20, 2026, https://www.preprints.org/manuscript/202607.1375; published in *Mathematics* 14 (2026), 3032, doi:10.3390/math14173032.
2. M. Edelman, A. B. Helman, and R. Smidtaite, *Bifurcations and transition to chaos in generalized fractional maps of the orders 0 < alpha < 1*, arXiv:2303.02501 (2023), https://arxiv.org/abs/2303.02501.
3. Standard finite-dimensional discrete flip-bifurcation center-manifold theory, used only after verifying a simple isolated critical multiplier and an exact nonzero branch-opening coefficient.
