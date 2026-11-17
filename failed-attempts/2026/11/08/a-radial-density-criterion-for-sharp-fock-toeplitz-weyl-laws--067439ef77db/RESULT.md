# A radial-density criterion for sharp Fock Toeplitz Weyl laws

## Finding
For every integer \(d\ge1\) and exponent \(\beta>0\), consider a radial weighted Fock Hilbert space with uniformly positive and bounded real Hessian, and the positive Toeplitz operator with symbol \(f_\beta(z)=(1+|z|^2)^{-\beta/2}\). If the radial weight is \(\Phi(|z|)\), set \(a(r)=\Phi'(r)/r\). Then the singular values determine exactly the tail oscillation of \(a\):
\[
\operatorname{Clust}_{n\to\infty}\left\{(d!n)^{\beta/(2d)}s_n(T_{f_\beta})\right\}
=\left[(\liminf_{r\to\infty}a(r))^{\beta/2},\ (\limsup_{r\to\infty}a(r))^{\beta/2}\right].
\]
For the counting function \(N_\beta(t)=\#\{n:s_n(T_{f_\beta})>t\}\),
\[
\operatorname{Clust}_{t\downarrow0}\left\{t^{2d/\beta}N_\beta(t)\right\}
=\left[\frac{(\liminf_{r\to\infty}a(r))^d}{d!},\frac{(\limsup_{r\to\infty}a(r))^d}{d!}\right].
\]
Here \(\operatorname{Clust}\) denotes the set of all finite subsequential limits. Consequently, a sharp positive finite Weyl coefficient exists for **one (equivalently every)** \(\beta>0\) exactly when \(\lim_{r\to\infty}\Phi'(r)/r=\ell\) exists. The coefficient is then \(\ell^d/d!\), and \(s_n(T_{f_\beta})\sim(\ell^d/(d!n))^{\beta/(2d)}\).

In particular, the radial potential
\[
\Phi_\varepsilon(r)=\frac{r^2}{2}\left(1+\varepsilon\sin\log(1+r^2)\right),\qquad\varepsilon=\frac1{10},
\]
has real Hessian between \(0.6I\) and \(1.4I\), but its counting coefficients fill the *entire* interval
\[
\left[\frac{(1-\sqrt2/10)^d}{d!},\frac{(1+\sqrt2/10)^d}{d!}\right]
\]
for every \(d\ge1\) and every \(\beta>0\). No single Weyl constant exists for this weight.

## Assumptions and scope
Let \(\Phi:[0,\infty)\to\mathbb R\) be \(C^2\), with \(\Phi'(0)=0\), and assume that its radial extension to \(\mathbb R^{2d}\) is \(C^2\), with
\[
mI_{2d}\le \nabla^2_{\mathbb R}\Phi(|z|)\le MI_{2d}\quad(z\in\mathbb C^d),
\]
for constants \(0<m\le M<\infty\). Equivalently, \(m\le\Phi''(r),\Phi'(r)/r\le M\) for \(r>0\). Write \(\mathcal F^2_\Phi\) for the closed entire-function subspace of \(L^2(\mathbb C^d,e^{-2\Phi(|z|)}dV(z))\). Let \(P_\Phi\) be the orthogonal projection and define \(T_{f_\beta}=P_\Phi M_{f_\beta}\) on \(\mathcal F^2_\Phi\). The symbol is positive, radial, bounded and strictly decreasing in radius. Eigenvalues, and hence singular values, are listed with multiplicities in nonincreasing order. The endpoint constants \(a_-\) and \(a_+\) are strictly positive and finite by the Hessian bounds.

## Proof
**1. Exact diagonalization and multiplicities.** Rotational unitary invariance makes the homogeneous-polynomial spaces mutually orthogonal, and Schur's lemma or the monomial angular integral shows that \(T_{f_\beta}\) is scalar in total degree \(k\). Its eigenvalue and multiplicity are
\[
\lambda_k=\frac{\int_0^\infty(1+r^2)^{-\beta/2}r^{2k+2d-1}e^{-2\Phi(r)}\,dr}{\int_0^\infty r^{2k+2d-1}e^{-2\Phi(r)}\,dr},\qquad
m_k=\binom{k+d-1}{d-1},\quad B_k=\sum_{j=0}^km_j=\binom{k+d}{d}.
\]
The ratio is positive; it tends to zero as \(k\to\infty\), by the localization below, hence the operator is compact. Let \(R_k\) have the probability density proportional to \(r^{2k+2d-1}e^{-2\Phi(r)}\). The distribution of \(R_{k+1}\) is the size bias of \(R_k\) by the strictly increasing function \(r^2\). Thus, by strict negative covariance with the strictly decreasing \((1+r^2)^{-\beta/2}\), one has \(\lambda_{k+1}<\lambda_k\) for every \(k\). Therefore the blocks of the nonincreasing singular-value sequence coincide exactly with the homogeneous degrees; in particular, \(s_n=\lambda_k\) for \(B_{k-1}<n\le B_k\).

**2. A uniform saddle-point estimate.** Define \(h_k(r)=(2k+2d-1)\log r-2\Phi(r)\). Its second derivative obeys
\[
h_k''(r)=-\frac{2k+2d-1}{r^2}-2\Phi''(r)\le-2m.
\]
The unique maximizing radius \(\rho_k>0\) solves
\[
\rho_k\Phi'(\rho_k)=k+d-\tfrac12,
\qquad
\sqrt{(k+d-\tfrac12)/M}\le\rho_k\le\sqrt{(k+d-\tfrac12)/m}.
\]
For all large \(k\), the upper Hessian bound implies \(h_k''(r)\ge-C\) on \(|r-\rho_k|\le1\), with \(C\) depending only on \(m,M,d\). Hence the integral of \(e^{h_k-h_k(\rho_k)}\) over \([0,\infty)\) is bounded below by a positive constant; strong concavity bounds it above by a Gaussian integral. The same Gaussian upper bound shows
\[
\mathbb E|R_k-\rho_k|=O(1),\qquad
\mathbb P(|R_k-\rho_k|>\rho_k/2)=O(e^{-c\rho_k^2}).
\]
On the central interval \(|r-\rho_k|\le\rho_k/2\), the derivative of the logarithm of the symbol has absolute value at most \(2\beta/\rho_k\). Consequently, comparing the symbol at \(R_k\) and \(\rho_k\), and treating the Gaussian tails separately, yields
\[
\lambda_k=(1+\rho_k^2)^{-\beta/2}\bigl(1+O(k^{-1/2})\bigr),
\qquad
k^{\beta/2}\lambda_k=a(\rho_k)^{\beta/2}+O(k^{-1/2}).
\]
All constants may depend on \(m,M,d,\beta\), but not on \(k\). The second formula follows from \(\rho_k^2a(\rho_k)=k+d-1/2\), with \(a(\rho_k)\in[m,M]\).

**3. Recovering every radial-density cluster value.** The derivative
\[
a'(r)=\frac{r\Phi''(r)-\Phi'(r)}{r^2}
\]
obeys \(|a'(r)|\le2M/r\) for \(r>0\). The function \(q(r)=r\Phi'(r)\) satisfies \(2mr\le q'(r)\le2Mr\), so consecutive saddle points have \(\rho_{k+1}-\rho_k=O(k^{-1/2})\). For any large \(r\), choose \(k\) with \(q(\rho_k)\le q(r)<q(\rho_{k+1})\). Then \(|a(r)-a(\rho_k)|=O(k^{-1})\). Therefore the values \(a(\rho_k)\) and the continuous function \(a(r)\) have the same cluster set at infinity. For a bounded continuous real function on a connected ray, that cluster set is precisely the interval between its liminf and limsup. Inserting the saddle estimate proves the cluster formula for \(k^{\beta/2}\lambda_k\).

**4. Singular-value and counting clusters.** Since \(B_k=k^d/d!+O(k^{d-1})\), for every \(B_{k-1}<n\le B_k\) one has
\[
(d!n)^{\beta/(2d)}s_n=a(\rho_k)^{\beta/2}+o(1).
\]
This proves the first claimed interval. Moreover, the saddle estimates and \(|a(\rho_{k+1})-a(\rho_k)|=O(k^{-1})\) imply \(\lambda_{k+1}/\lambda_k\to1\). For \(\lambda_{k+1}<t\le\lambda_k\), \(N_\beta(t)\) differs from \(B_k\) by at most one degree block and \(t^{2d/\beta}/\lambda_k^{2d/\beta}\to1\), uniformly in this interval. Thus
\[
t^{2d/\beta}N_\beta(t)=\frac{a(\rho_k)^d}{d!}+o(1),
\]
which gives the second cluster interval and the claimed necessary-and-sufficient Weyl criterion. (At thresholds exactly equal to an eigenvalue, the strict greater-than convention shifts the count by one block, an asymptotically negligible amount.)

**5. Uniformly convex oscillatory example.** With \(u=\log(1+r^2)\) and \(v=r^2/(1+r^2)\), differentiation yields
\[
\frac{\Phi_\varepsilon'(r)}r=1+\varepsilon(\sin u+v\cos u),\qquad
\Phi_\varepsilon''(r)=1+\varepsilon\big[(1-2v^2)\sin u+(5v-2v^2)\cos u\big].
\]
For \(0\le v\le1\), the first sine coefficient has modulus at most one and the cosine coefficient lies between zero and three. With \(\varepsilon=1/10\), both radial and tangential real Hessian eigenvalues lie in \([0.6,1.4]\). As \(r\to\infty\), \(v\to1\), and \(u\) traverses every phase modulo \(2\pi\) repeatedly. Hence the liminf and limsup of the slope are \(1\mp\sqrt2/10\), proving the displayed full counting cluster interval.

## Verification
All saddle estimates are analytic uniform estimates, not consequences of finite sampling. A standalone standard-library checker, `checker.py`, validates exact multiplicity identities, the explicit radial Hessian formula, saddle-point equations, finite-dimensional quadrature versus the predicted eigenvalue localization, and cumulative block counts. It reports 188 successful finite assertions; the mathematical proof of all tail statements is given above. In the Gaussian case \(\Phi(r)=\ell r^2/2\), the predicted coefficient reduces to \(\ell^d/d!\), agreeing with the explicit quadratic-weight Weyl coefficient.

## Relationship to prior work
Xu and Dong, *IDA symbols and Schatten--Lorentz theory for Toeplitz operators on weighted Fock spaces*, arXiv:2609.16970 (publicly submitted 2026-09-15), prove a Weyl coefficient for quadratic weights and exhibit a radial uniformly Hessian-bounded potential where a general Weyl coefficient fails (Theorem 5.2 and Proposition 5.3). The present assertion goes beyond those statements by giving an if-and-only-if geometric criterion for all such radial weights, the entire possible cluster interval, all dimensions, and every positive decay exponent. Bdarneh, arXiv:2609.20652 (2026-09-17), provides radial Toeplitz diagonalizations and spectral representations, but not this coefficient-recovery or inverse criterion. The published logarithmic spectral-filter example for radial Toeplitz operators on the *fixed Gaussian* Fock space concerns oscillations of the **symbol** and Dixmier traces; it does not imply the present criterion for oscillations of the **underlying Hilbert-space weight** with a fixed monotone symbol. Huang, Wang and Zeng (2026) discuss broad singular-value rearrangement estimates on Fock-type spaces; a full-text comparison was unavailable, so any exact implication from their results remains a documented originality risk. The diagonalization step here is classical; the claim of new content is the exact two-sided inverse coefficient/cluster classification, not the known general radial spectral representation or the existence of some oscillatory counterexample.

## Limitations
The theorem requires rotational radiality, a uniformly positive/bounded **real** Hessian, and the specific radial probe family \((1+|z|^2)^{-\beta/2}\) with \(\beta>0\). It is not a result for arbitrary complex symbols, general nonradial weights, or merely plurisubharmonic potentials without real Hessian bounds. It proves no exact rates beyond the uniform \(O(k^{-1/2})\) saddle error. The priority comparison with the inaccessible full text of Huang--Wang--Zeng is unresolved; no independent audit or publication-priority certification is claimed.

## References
1. C. Xu and J. Dong, *IDA symbols and Schatten--Lorentz theory for Toeplitz operators on weighted Fock spaces*, arXiv:2609.16970v1, https://arxiv.org/abs/2609.16970 (first public 2026-09-15), Theorem 5.2 and Proposition 5.3.
2. K. Bdarneh, *Toeplitz C*-algebras on radially weighted Fock spaces: commutativity and spectral representation*, arXiv:2609.20652v1, https://arxiv.org/abs/2609.20652 (2026-09-17).
3. W. Huang, X. Wang and Z. Zeng, *Asymptotic behavior of singular values of Toeplitz and Hankel operators on Fock-type spaces*, *Banach Journal of Mathematical Analysis* 20 (2026), https://doi.org/10.1007/s43037-025-00477-8 (abstract consulted; full text unavailable).
4. *The logarithmic spectral filter for smooth radial Fock Toeplitz operators*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-logarithmic-spectral-filter-for-smooth-radial-fock-toeplitz--0bc5b54dc8b5 (full RESULT.md consulted for noncoverage).
