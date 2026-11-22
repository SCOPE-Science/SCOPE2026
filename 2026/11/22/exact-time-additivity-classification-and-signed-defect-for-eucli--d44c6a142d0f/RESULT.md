# Exact time-additivity classification and signed defect for Euclidean \(\ell_p\) proximal maps

## Finding

Let \(n\ge 2\), \(1\le p\le\infty\), and for every \(t\ge 0\) define the Euclidean proximal map
\[
P_t^{(p)}(x)=\operatorname*{argmin}_{z\in\mathbb R^n}
\left\{\frac12\|z-x\|_2^2+t\|z\|_p\right\}.
\]
The family has exact parameter additivity,
\[
P_s^{(p)}\!\left(P_t^{(p)}(x)\right)=P_{s+t}^{(p)}(x)
\quad\text{for every }x\in\mathbb R^n,\ s,t\ge0,
\]
**if and only if** \(p\in\{1,2,\infty\}\).

The negative direction is quantitative. For \(1<p<\infty\), \(p\ne2\), put \(u=(1,2,1,\ldots,1)\in\mathbb R^n\). Then as \(h\downarrow0\),
\[
\left[P_h^{(p)}(P_h^{(p)}(u))-P_{2h}^{(p)}(u)\right]_1
= c_{n,p}h^2+O_{n,p}(h^3),
\]
where
\[
c_{n,p}=-(p-1)(n-1+2^p)^{2/p-3}\bigl(2^p-2^{2p-2}\bigr).
\]
This coefficient is strictly negative when \(1<p<2\) and strictly positive when \(2<p<\infty\). In particular, the composition identity fails at this one explicit positive input for every finite non-Hilbert exponent.

## Assumptions and scope

The ambient fidelity term is always the *Euclidean* quadratic \(\|z-x\|_2^2/2\), independent of the penalty exponent. The results hold for every real input, all nonnegative times, and every finite dimension at least two. The first coordinate of \(u\) is the initial entry equal to one. The asymptotic remainder is for fixed \(n,p\), not uniform in either variable. For \(n=1\) all these norms equal absolute value and the exact semigroup identity holds for every exponent.

## Proof

Strict convexity of the quadratic term and continuity/convexity of the penalty give a unique minimizer for every parameter and input. The cases \(p=1\) and \(p=2\) have the standard explicit forms
\[
(P_t^{(1)}(x))_i=\operatorname{sgn}(x_i)(|x_i|-t)_+,
\quad
P_t^{(2)}(x)=\left(1-\frac{t}{\|x\|_2}\right)_+x
\]
(the second is zero at \(x=0\)). Soft-thresholding and radial shrinkage each compose by addition of their thresholds.

For \(p=\infty\), convex duality and the Euclidean projection identity give \(P_t^{(\infty)}(x)=x-\Pi_{tB_1}(x)\), with \(B_1=\{v:\|v\|_1\le1\}\). Write \(a_i=|x_i|\) and \(M=\sum_i a_i\). If \(0<t<M\), there is a unique clipping level \(\lambda_t\ge0\) satisfying \(\sum_i(a_i-\lambda_t)_+=t\), and
\[
(P_t^{(\infty)}(x))_i=\operatorname{sgn}(x_i)\min(a_i,\lambda_t).
\]
At \(t=0\), choose \(\lambda_0=\max_i a_i\). If \(t\ge M\), the proximal output is zero. For \(0\le\mu\le\lambda\) the elementary identity
\[
(a-\mu)_+=(a-\lambda)_++(\min(a,\lambda)-\mu)_+
\]
holds for every \(a\ge0\). Summing, it shows that the additional \(s\)-clipping of the vector after \(t\)-clipping is exactly the \((s+t)\)-clipping of the original vector. If \(s+t\ge M\), both procedures yield zero. Hence the identity holds also for \(p=\infty\).

For the converse take any finite \(1<p<\infty\). On the strictly positive orthant let \(f(x)=\|x\|_p\), \(S=\sum_j x_j^p\), \(g=\nabla f\), and \(H=\nabla^2 f\). Both are smooth near \(u\), and
\[
g_i=S^{1/p-1}x_i^{p-1},\qquad
(Hg)_i=(p-1)S^{2/p-3}x_i^{p-1}
\left(Sx_i^{p-2}-\sum_j x_j^{2p-2}\right).
\]
For small positive \(h\), the proximal point stays in this orthant. Its first-order optimality equation is \(z+h g(z)=x\); the implicit function theorem and Taylor expansion give
\[
P_h^{(p)}(x)=x-hg(x)+h^2H(x)g(x)+O_x(h^3).
\]
Applying the same expansion twice (including the change in \(g\) at the intermediate argument) gives
\[
P_h^{(p)}(P_h^{(p)}(x))=x-2hg(x)+3h^2H(x)g(x)+O_x(h^3),
\]
whereas \(P_{2h}^{(p)}(x)=x-2hg(x)+4h^2H(x)g(x)+O_x(h^3)\). Their difference is therefore \(-h^2H(x)g(x)+O_x(h^3)\).

At \(u=(1,2,1,\ldots,1)\), \(S=n-1+2^p\) and \(\sum_j u_j^{2p-2}=n-1+2^{2p-2}\). The displayed expression for \(c_{n,p}\) follows. Since \(2^p=2^{2p-2}\) for \(p>1\) only if \(p=2\), it is nonzero precisely for the claimed excluded exponents. The sign follows by comparing \(p\) and \(2\). Thus for each excluded exponent every sufficiently small \(h>0\) violates the semigroup identity, completing the proof.

## Verification

The accompanying standalone `CHECK.py` uses only the Python standard library. Running `python3 CHECK.py` tests all three exact semigroup cases over 6,120 deterministic random combinations, and verifies signed second-order discrepancies and proximal optimality residuals at positive inputs for additional cases. It reports 6,360 passing numerical checks. These finite checks supplement but do not establish the universal theorem, which follows from the exact identities and Taylor argument above.

## Relationship to prior work

The proximal/resolvent framework and strongly continuous semigroup limits are established in Bërdëllima–Steidl [1], particularly Section 6.2. Their construction obtains a semigroup as the limit of many short resolvent steps; it does not assert that each *single* finite-step resolvent already has time-additivity. Bungert–Burger–Chambolle–Novaga [2], Sections 4.2 and 5.2–5.3, treats one-homogeneous gradient flows and establishes the flow/variational equivalence under geometric conditions, explicitly including \(L^1\) and \(L^\infty\) examples. The positive endpoint cases and conventional shrinkage/projection identities are not claimed as independently new. The specific finite-dimensional all-exponent necessity classification and the sign-resolved local discrepancy coefficient are the additional conclusions here. Vilches [3] studies how convex functions are determined by proximal mappings, but not this exact time-additivity classification.

## Limitations

This is a real finite-dimensional Euclidean-fidelity result. It does not characterize arbitrary norms, weighted \(\ell_p\) penalties, non-Euclidean fidelity, or infinite-dimensional proximal semigroups. Time-additivity is stronger than the existence of the limiting gradient-flow semigroup, which holds much more broadly. Equivalent results in older or unindexed resolvent literature may exist; literature search is not a priority certification. No independent verification has been performed.

## References

1. A. Bërdëllima and G. Steidl, *On \(\alpha\)-Firmly Nonexpansive Operators in \(r\)-Uniformly Convex Spaces*, arXiv:2104.05304 (first posted 2021-04-12), especially §6.2; https://arxiv.org/abs/2104.05304; DOI 10.1007/s00025-021-01481-8.
2. L. Bungert, M. Burger, A. Chambolle and M. Novaga, *Nonlinear Spectral Decompositions by Gradient Flows of One-Homogeneous Functionals*, arXiv:1901.06979 (first posted 2019-01-21), especially §§4.2, 5.2–5.3; https://arxiv.org/abs/1901.06979.
3. E. Vilches, *Proximal Determination of Convex Functions*, arXiv:2007.03798 (first posted 2020-07-07); https://arxiv.org/abs/2007.03798.
