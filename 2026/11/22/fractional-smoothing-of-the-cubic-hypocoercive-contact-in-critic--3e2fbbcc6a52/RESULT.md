# Fractional smoothing of the cubic hypocoercive contact in critical Jordan chains

## Finding

Let \(n\ge 2\) be an integer, \(a>0\), \(\theta=\pi/(n+1)\), and let \(N_n\in\mathbb R^{n\times n}\) have ones on the first superdiagonal and zeroes elsewhere. Put
\[
G_n=-aI_n+\frac{a}{\cos\theta}N_n,
\qquad
F_{\alpha}(t)=E_{\alpha}(t^{\alpha}G_n),
\qquad 0<\alpha\le1,
\]
where \(E_{\alpha}(z)=\sum_{j=0}^{\infty}z^j/\Gamma(1+\alpha j)\), and all operator norms are Euclidean spectral norms. Define
\[
q_n=\frac{n-1}{n+1}a^2\tan^2\theta,
\qquad
h_n=\frac{2a^3\tan^2\theta}{n+1},
\qquad
V_{\alpha}=\frac{2}{\Gamma(1+2\alpha)}-\frac{1}{\Gamma(1+\alpha)^2}.
\]
**Theorem (sharp small-time transition).** The following assertions hold.

1. The propagators are strictly contractive for every \(t>0\): \(\|F_{\alpha}(t)\|<1\). For each fixed \(0<\alpha<1\), their sharp first nonzero small-time norm deficit is
   \[
   1-\|F_{\alpha}(t)\|=\frac{q_nV_{\alpha}}2\,t^{2\alpha}+O_{n,a,\alpha}(t^{3\alpha}),
   \qquad V_{\alpha}>0.
   \]
2. At the classical endpoint \(\alpha=1\), the sharp deficit instead begins cubically:
   \[
   1-\|F_1(t)\|=\frac{h_n}{12}t^3+O_{n,a}(t^4)
   =\frac{a^3\tan^2\theta}{6(n+1)}t^3+O_{n,a}(t^4).
   \]
3. The two laws are linked **uniformly**. Write \(s=t^{\alpha}\) and \(\varepsilon=1-\alpha\). For every fixed \(\alpha_0\in(0,1)\), as \(s\downarrow0\), uniformly for \(\alpha\in[\alpha_0,1]\),
   \[
   1-\|E_{\alpha}(sG_n)\|
   =\frac{q_nV_{\alpha}}2s^2+\frac{h_n}{12}s^3
   +O_{n,a,\alpha_0}(\varepsilon s^3+s^4).
   \]
   Moreover \(V_{\alpha}=\varepsilon+O(\varepsilon^2)\). Consequently, along any joint limit \(\alpha\uparrow1\), \(s\downarrow0\) with \(\varepsilon/s\to\rho\in[0,\infty)\),
   \[
   \frac{1-\|E_{\alpha}(sG_n)\|}{s^3}
   \longrightarrow\frac{q_n\rho}{2}+\frac{h_n}{12}.
   \]
   When instead \(\varepsilon/s\to\infty\), the normalized deficit \((1-\|E_{\alpha}(sG_n)\|)/(\varepsilon s^2)\) tends to \(q_n/2\). Thus the sharp crossover occurs at \(1-\alpha\asymp t^{\alpha}\), not merely at a fixed fractional order.

The gamma-function factor \(V_{\alpha}\) is exactly the variance of the positive subordination random time \(Y_{\alpha}\) characterized by \(\mathbb E[Y_{\alpha}^{j}]=j!/\Gamma(1+\alpha j)\). At the ordinary-semigroup endpoint, this random time is identically one. The transition therefore quantifies how temporal mixing removes the classical cubic contact and creates an earlier quadratic deficit.

## Assumptions and scope

All matrices are finite-dimensional, acting on complex Euclidean Hilbert space; the specified entries and couplings are real. Integers \(n\ge2\), damping \(a>0\), orders \(0<\alpha\le1\), and physical times \(t\ge0\) are arbitrary. The coupling \(a\sec(\pi/(n+1))\) is the exact dissipativity threshold. The statements concern the spectral norm of the Mittag--Leffler matrix function, **not** the individual norm of a selected trajectory, the resolvent norm, a Kreiss constant or an optimal control problem. The big-O constants are not asserted to be uniform as \(n\to\infty\) or \(a\to\infty\). The joint expansion is uniform only for fixed \(n,a,\alpha_0\).

## Proof

**1. Dissipative edge and the unique contact vector.** Write \(G=G_n\), \(H=(G+G^*)/2\), and \(R=-H\). The tridiagonal adjacency matrix \(N_n+N_n^*\) has eigenvalues \(2\cos(j\pi/(n+1))\), so \(H\le0\) and its zero eigenvalue is simple. Its normalized real eigenvector is
\[
v_j=\sqrt{\frac{2}{n+1}}\sin(j\theta),\qquad j=1,\ldots,n.
\]
The vector \(Gv\) is orthogonal to \(v\), since \(\langle Gv,v\rangle=\langle Hv,v\rangle=0\), and is nonzero. More precisely,
\[
(Gv)_j=\frac{a}{\cos\theta}\sqrt{\frac2{n+1}}\sin\theta\cos(j\theta).
\]
The elementary trigonometric sums
\[
\sum_{j=1}^n\cos^2(j\theta)=\frac{n-1}{2},\quad
\sum_{j=1}^{n-1}\cos(j\theta)\cos((j+1)\theta)=\frac{(n-3)\cos\theta}{2}
\]
give
\[
\|Gv\|^2=q_n,\qquad \langle R Gv,Gv\rangle=h_n>0.
\]
Thus \(\ker R=\mathbb Cv\), while \(Gv\notin\ker R\). The energy identity
\[
\|e^{tG}x\|^2=\|x\|^2-2\int_0^t\langle R e^{uG}x,e^{uG}x\rangle\,du
\]
shows \(\|e^{tG}\|<1\) for \(t>0\): equality would force the entire orbit of some nonzero unit vector to remain in \(\ker R\); its initial derivative contradicts \(Gv\notin\ker R\). For \(0<\alpha<1\), the positive probability-density subordination formula \(E_{\alpha}(sG)=\int_0^\infty e^{usG}m_{\alpha}(u)\,du\), with \(u>0\), gives \(\|E_{\alpha}(sG)\|<1\) for every \(s>0\); for \(\alpha=1\) it is already proved.

**2. Quadratic fractional deficit.** For \(s\ge0\), put \(A_{\alpha}=1/\Gamma(1+\alpha)\), \(B_{\alpha}=1/\Gamma(1+2\alpha)\). The entire-function series, uniformly for \(\alpha\) in compact subintervals of \((0,1]\), gives
\[
E_{\alpha}(sG)=I+A_{\alpha}sG+B_{\alpha}s^2G^2+O(s^3),
\]
and hence, with \(M_{\alpha}(s)=E_{\alpha}(sG)^*E_{\alpha}(sG)\),
\[
M_{\alpha}(s)=I+2A_{\alpha}sH+s^2\big[B_{\alpha}(G^2+G^{*2})+A_{\alpha}^2G^*G\big]+O(s^3).
\]
Because \(H\) has a **simple** top eigenvalue zero and all its other eigenvalues are strictly negative, the top eigenpair of \((M_{\alpha}(s)-I)/s\) extends real-analytically from \(s=0\), with normalized eigenvector tending to \(v\). As \(G^*v=-Gv\),
\[
\langle v,(G^2+G^{*2})v\rangle=-2\|Gv\|^2.
\]
No eigenvector correction contributes to the coefficient of \(s^2\) in the top eigenvalue, since the first-order eigenvector already lies in the nullspace of \(H\). Therefore
\[
\lambda_{\max}(M_{\alpha}(s))=1-(2B_{\alpha}-A_{\alpha}^2)q_n s^2+O(s^3),
\]
and taking the positive square root proves the first deficit formula. Complete monotonicity identifies \(2B_{\alpha}-A_{\alpha}^2=\operatorname{Var}(Y_{\alpha})\). Alternatively, strict positivity for \(\alpha<1\) follows from the strict increase of \(\Gamma(1+2\alpha)/\Gamma(1+\alpha)^2\) from one to two as \(\alpha\) moves from zero to one: its logarithmic derivative is \(2[\psi(1+2\alpha)-\psi(1+\alpha)]>0\). Direct differentiation with \(\psi(3)-\psi(2)=1/2\) gives \(V_1=0\) and \(V'_{\alpha}|_{\alpha=1}=-1\).

**3. Cubic ordinary-semigroup contact.** For \(\alpha=1\), let \(x(s)\) be a top right singular vector of \(e^{sG}\), with phase chosen continuously so that \(x(0)=v\). Analytic perturbation of \((e^{sG^*}e^{sG}-I)/s\) permits \(x(s)=v+sw+O(s^2)\) after normalization, with \(w\perp v\). Insert this into the exact energy identity and use \(Rv=0\):
\[
1-\|e^{sG}x(s)\|^2
=2s^3\left[\langle Rw,w\rangle+\Re\langle Rw,Gv\rangle+\frac13\langle RGv,Gv\rangle\right]+O(s^4).
\]
The bracket equals \(\langle R(w+Gv/2),w+Gv/2\rangle+h_n/12\). Its minimum is attained at \(w=-Gv/2\), which is perpendicular to \(v\); the trial vector \((v-sGv/2)/\|v-sGv/2\|\) proves this optimum is attainable to leading order. Thus
\[
1-\|e^{sG}\|^2=\frac{h_n}{6}s^3+O(s^4),
\]
and the square-root identity gives the coefficient \(h_n/12\). The cubic law is a specialized instance of the established hypocoercivity-index-one short-time phenomenon; no novelty is attributed to that phenomenon alone.

**4. Uniform crossover.** For \(\alpha\in[\alpha_0,1]\), the entries of the power-series matrix \(M_{\alpha}(s)\) and its derivatives through any fixed order depend continuously differentiably on \(\alpha\) and analytically on \(s\), with uniform local bounds. The zero eigenvalue of \(2A_{\alpha}H\) remains simple and separated by a positive gap from the others. The analytic top-eigenvalue expansion consequently gives
\[
1-\|E_{\alpha}(sG)\|=\frac12 q_n V_{\alpha}s^2+k(\alpha)s^3+O_{n,a,\alpha_0}(s^4),
\]
where \(k\) is continuously differentiable in \(\alpha\), and part 3 proves \(k(1)=h_n/12\). It follows that \(k(\alpha)=h_n/12+O(1-\alpha)\), which proves the uniform expansion. Dividing by the specified powers of \(s\), using \(V_{\alpha}/(1-\alpha)\to1\), yields both two-scale limits and identifies the transition scale. The remainder estimates use fixed \(n,a\), not any finite experiment.

## Verification

The accompanying standard-library program `check.py` directly computes matrix Mittag--Leffler series, symmetric Gram matrices and their largest eigenvalues by Jacobi rotations. Running `python3 check.py` produced `FRACTIONAL_JORDAN_BOUNDARY_DIAGNOSTIC_OK 465`. It samples dimensions \(2\) through \(9\), three damping values, several fractional orders, both limiting regimes and the exact independent two-by-two exponential norm \(e^{-at+\operatorname{arsinh}(at)}\). These numerical checks are diagnostic, **not** a substitute for the proof above. The proof covers every declared dimension, damping value, order and sufficiently small time, with the strict contractivity assertion covering every positive time.

## Relationship to prior work

Kostić, Mangi and Uzelac Bujišić, arXiv:2611.19352v1, establish fractional Kreiss comparisons, normal/numerical-range bounds, subordination, an initial first-order norm slope, and strong-coupling Jordan amplification estimates. The present theorem uses their fractional propagator setting but instead resolves the sharp **small-time norm contact at the dissipativity threshold** and its double limit in time and fractional order. Achleitner, Arnold and Carlen, arXiv:2109.10784v1 (2021), characterize classical semigroup short-time exponents via the hypocoercivity index. Arnold, Egger, Mehrmann and Nigsch, arXiv:2601.09656v2, give classical semigroup coefficients and discrete Cayley analogues. The **cubic endpoint** is therefore credited as an instance of established theory. Neither classical result supplies the positive fractional variance term or its uniform approach to the endpoint. Originality is asserted only for the combined fractional sharp coefficients and crossover, conditional on the literature comparison reported in `AUDIT.json`.

## Limitations

This result does not classify general Mittag--Leffler propagators, nonuniform Jordan chains, noncritical couplings or infinite-dimensional generators. Constants in the uniform error depend on the fixed matrix size and damping. Neither the bound on a finite grid nor literature searching establishes originality by itself. A potentially broader theorem on fractional subordination and boundary norm contact could imply parts of this result; this remains a bibliographic risk. The statement is a mathematical result with an analytic derivation and self-review, not an independent audit or a certification of priority.

## References

1. V. R. Kostić, J. P. Mangi and I. Uzelac Bujišić, *A Kreiss theorem for fractional Cauchy problems with a finite slow component*, arXiv:2611.19352v1, first public 14 November 2026. https://arxiv.org/html/2611.19352v1
2. F. Achleitner, A. Arnold and E. A. Carlen, *The hypocoercivity index for the short time behavior of linear time-invariant ODE systems*, arXiv:2109.10784, first public 22 September 2021. https://arxiv.org/pdf/2109.10784
3. A. Arnold, S. Egger, V. Mehrmann and E. A. Nigsch, *Connection of hypocoercivity and hypocontractivity via the Cayley transform*, arXiv:2601.09656v2, 4 November 2026 revision (first public 14 January 2026). https://arxiv.org/html/2601.09656v2
