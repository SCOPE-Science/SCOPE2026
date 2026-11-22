# Exact two-order singular spectra and displacement reversal for affine Fock composition products

## Finding

Let \(\mathcal F^2\) be the standard one-variable Gaussian Fock space. For arbitrary \(a,c,b,d\in\mathbb C\) with \(|a|<1\) and \(|c|<1\), put \(\varphi(z)=az+b\), \(\psi(z)=cz+d\), \(q=a\overline c\), and \(\Delta=1-|q|^2\). Define the two cross-adjoint products
\[
P=C_\varphi C_\psi^*,\qquad R=C_\psi^*C_\varphi.
\]
Their complete singular-value multisets, in decreasing order, are
\[
s_n(P)=e^{\Lambda_P}|q|^n,\qquad s_n(R)=e^{\Lambda_R}|q|^n,\qquad n=0,1,2,\ldots,
\]
where
\[
\Lambda_P=\operatorname{Re}(b\overline d)+\frac{|bc|^2}{2}
 +\frac{|a|^2|d+|c|^2b|^2}{2\Delta},\qquad
\Lambda_R=\frac{|b|^2}{2}+\frac{|\overline d+q\overline b|^2}{2\Delta}.
\]
These expressions include the rank-one case \(q=0\), interpreted as a single nonzero singular value and all subsequent singular values zero. For every real \(p>0\), both products belong to the Schatten ideal \(\mathcal S_p\), with exact quasi-norms
\[
\|P\|_{\mathcal S_p}=\frac{e^{\Lambda_P}}{(1-|q|^p)^{1/p}},\qquad
\|R\|_{\mathcal S_p}=\frac{e^{\Lambda_R}}{(1-|q|^p)^{1/p}}.
\]
In particular, the ratio of the two Schatten quasi-norms, for every \(p>0\), equals their operator-norm ratio and is independent of \(p\):
\[
\frac{\|R\|_{\mathcal S_p}}{\|P\|_{\mathcal S_p}}
=\exp\!\left(\frac{(1-|c|^2)|b|^2+(1-|a|^2)|d|^2
-2\operatorname{Re}((1-\overline q)b\overline d)}{2\Delta}\right).
\]
When \(a=c\), this ratio is \(\exp(|b-d|^2/[2(1+|a|^2)])\ge1\), with equality exactly when \(b=d\). When \(a\ne c\), for these same fixed slopes, varying \(b,d\) realizes each of the strict inequalities \(\|R\|_{\mathcal S_p}>\|P\|_{\mathcal S_p}\) and \(\|R\|_{\mathcal S_p}<\|P\|_{\mathcal S_p}\), and also equality; the order transition is governed by a nondegenerate indefinite Hermitian form.

## Assumptions and scope

The Hilbert space is
\[
\mathcal F^2=\{f:\mathbb C\to\mathbb C\text{ entire}:\ \pi^{-1}\!\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z)<\infty\}.
\]
Its reproducing kernel is \(K_w(z)=e^{z\overline w}\); \(e_n(z)=z^n/\sqrt{n!}\), for \(n\ge0\), is an orthonormal basis. The operators \(C_\varphi f=f\circ\varphi\) and \(C_\psi f=f\circ\psi\) are bounded (indeed compact) because the slopes are strictly contractive. Complex translations \(b,d\) are unrestricted. Every assertion holds simultaneously for all such quadruples and every \(p>0\). No spectral statements for noncompact boundary slopes or for nonlinear inducing maps are asserted.

## Proof

**1. Reduction to Gaussian weighted compositions.** Density of the span of the kernels \(K_w\) and the adjoint relation \(C_\psi^*K_w=K_{\psi(w)}\) give the exact identities
\[
(Pf)(z)=e^{b\overline d+a\overline d\,z}
f(qz+b\overline c),\qquad
(Rf)(z)=e^{\overline d\,z}f(qz+b).
\]
They can be verified on every kernel and then extend by boundedness. Thus both are instances of
\[
(W_{\beta,q,t,\gamma}f)(z)=e^{\gamma+\beta z}f(qz+t),\qquad |q|<1,
\]
with respective parameter tuples
\[
(\beta,t,\gamma)_P=(a\overline d,b\overline c,b\overline d),\qquad
(\beta,t,\gamma)_R=(\overline d,b,0).
\]

**2. Exact Weyl factorization.** For \(u\in\mathbb C\), define the unitary Fock displacement
\[
(U_u f)(z)=e^{-|u|^2/2+\overline u z}f(z-u),
\]
and set \((D_qf)(z)=f(qz)\). A direct substitution shows
\[
U_uD_qU_v f(z)=
\exp\!\left(-\frac{|u|^2+|v|^2}{2}-q\overline v u
+(\overline u+q\overline v)z\right)f(qz-qu-v).
\]
For arbitrary \(\beta,t\), choose the unique
\[
\overline u=\frac{\beta+q\overline t}{\Delta},\qquad v=-t-qu.
\]
Then \(\overline u+q\overline v=\beta\) and \(-qu-v=t\), so
\[
W_{\beta,q,t,\gamma}=\kappa U_uD_qU_v,
\quad \kappa=\exp\!\left(\gamma+\frac{|u|^2+|v|^2}{2}+q\overline v u\right).
\]
A direct completion of squares, or expansion using the two displayed equations, yields
\[
\log|\kappa|=\operatorname{Re}\gamma+
\frac{|t|^2}{2}+\frac{|\beta+q\overline t|^2}{2\Delta}.
\]
Since \(D_qe_n=q^ne_n\) and both exterior Weyl factors are unitary, every singular value of \(W\) is exactly \(|\kappa||q|^n\). There are no unlisted singular values. This remains true when \(q=0\), when \(D_q\) has rank one.

**3. Substitution and all Schatten indices.** Insert the parameter tuples from Step 1 into the last modulus formula. For \(P\), note
\[
\beta+q\overline t=a(\overline d+|c|^2\overline b),
\]
which gives \(\Lambda_P\); for \(R\), \(\beta+q\overline t=\overline d+q\overline b\) gives \(\Lambda_R\). As \(|q|<1\), summing \(\sum_{n\ge0}s_n^p\) is an ordinary geometric series. Its \(p\)-th root proves both quasi-norm identities for every \(p>0\); the operator norms are the first singular values.

**4. The order-reversal phase.** Expanding and cancelling the squared moduli gives
\[
2\Delta(\Lambda_R-\Lambda_P)
=(1-|c|^2)|b|^2+(1-|a|^2)|d|^2
-2\operatorname{Re}((1-\overline q)b\overline d)=:Q(b,d).
\]
If \(a=c\), then \(q=|a|^2\) and \(Q=(1-|a|^2)|b-d|^2\), proving the equality and rigidity assertions. Otherwise, the Hermitian matrix of \(Q\) has positive leading diagonal entry \(1-|c|^2\) and determinant
\[
(1-|a|^2)(1-|c|^2)-|1-a\overline c|^2=-|a-c|^2<0.
\]
It has one positive and one negative eigenvalue. More explicitly, take any \(d\ne0\). The choice \(b=0\) yields \(Q>0\), while \(b=(1-q)d/(1-|c|^2)\) yields \(Q=-|a-c|^2|d|^2/(1-|c|^2)<0\). Continuity on the line segment supplies \(Q=0\) as well. Consequently all three norm-order relations occur and are independent of the Schatten index. This finishes the proof.

## Verification

The self-contained `verification.py` checks the analytic logarithmic ratio against the expanded Hermitian form for one hundred pseudorandom complex parameter quadruples, as well as six representative special cases. It also constructs finite orthonormal-basis sections of both cross products and compares their leading five singular values to the closed forms. Running it with Python and NumPy gave 166 successful finite assertions. The Weyl factorization above, not the finite tests, proves the infinite-dimensional assertion.

For reproduction, run `python verification.py` in a directory containing that file with NumPy installed. No external datasets or network requests are needed.

## Relationship to prior work

Tian [1], especially Propositions 3.5–3.6 and Corollary 3.7, characterizes compactness of these cross-product orders but does not give their complete singular-value lists, exact Schatten quasi-norms, or the displacement-dependent sign transition between orders. Dong and Zhu [2] obtain exact geometric singular values for a two-parameter class of canonical Gaussian Fock integral transforms: this already covers special centered, zero-displacement Gaussian situations, and their results are not claimed as new here. Their studied kernel class lacks the unrestricted affine translations responsible for the order-reversal form above. Leng and Zhao [3] study Schatten membership of cross products on Hardy and Bergman *disk* spaces, not this Fock geometry. Johnson [4] provides general compactness and singular-value decay estimates for pullbacks between Bargmann spaces, rather than an exact two-order cross-product singular spectrum. Searches for equivalent Gaussian integral-kernel and Weyl formulations found no published implication of the full stated phase classification; that is a bounded literature conclusion, not an exhaustive originality guarantee.

## Limitations

This theorem concerns one complex dimension and strictly contractive unweighted affine composition symbols. It does not classify the spectra (as opposed to singular values) of the nonnormal cross products, noncompact boundary slopes, or nonlinear inducing maps. It uses familiar Weyl covariance; an equivalent calculation under a different Gaussian-operator convention could predate the inspected sources. Numerical finite sections are corroborative and cannot establish infinite-dimensional claims. Independent external validation has not been performed.

## References

[1] X. Tian, *Weighted composition operators on the Fock space*, arXiv:2610.29786, first posted 21 October 2026. https://arxiv.org/abs/2610.29786

[2] X. Dong and K. Zhu, *Canonical integral operators on the Fock space II*, arXiv:2509.16672, first posted 20 September 2025. https://arxiv.org/abs/2509.16672

[3] Q. Leng and X. Zhao, *Schatten class membership of products of composition operators and their adjoints*, arXiv:2610.15472, first posted 11 October 2026. https://arxiv.org/abs/2610.15472

[4] R. Johnson, *Pullback operators on Bargmann spaces*, arXiv:2403.13227, first posted 20 March 2024. https://arxiv.org/abs/2403.13227
