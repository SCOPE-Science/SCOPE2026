# Sharp asymmetric Hardy stability at coexisting linear and quadratic nilpotent extremizers

## Finding

Consider the numerical-range normalized nilpotent weighted shift
\[
A=\begin{pmatrix}0&\sqrt3&0\\0&0&1\\0&0&0\end{pmatrix}.
\]
Its numerical range is the closed unit disk. For each scalar Schur function \(f\in H^\infty(\mathbb D)\) with \(\|f\|_\infty\le1\) and \(f(0)=0\), set
\[
\delta(f)=3-\|f(A)\|^2,\qquad x(f)=|f'(0)|^2,
\qquad d_k(f)=\inf_{|\omega|=1}\|f-\omega z^k\|_{H^2}\quad(k=1,2).
\]
Here \(H^2\) carries its usual coefficient-square norm. The exact optimal anchored spectral-set constant \(\sqrt3\) and its two monomial extremizer classes already follow from earlier weighted-shift spectral-set results; they are background, not the novel assertion.

**Global mixing deficit.** Every admissible function satisfies
\[
\boxed{\delta(f)\ge 2x(f)(1-x(f)).}
\]
The coefficient \(2\) is sharp as \(f\) approaches a quadratic monomial through finite Blaschke products.

**Sharp two-well stability.** Among functions near equality, those closer in \(H^2\) to the linear extremizer class satisfy the optimal asymptotic estimate
\[
\lim_{\eta\downarrow0}\sup_{\substack{0<\delta(f)<\eta\\d_1(f)<d_2(f)}}
\frac{d_1(f)}{\sqrt{\delta(f)}}=\frac1{\sqrt3}.
\]
Those closer to the quadratic class satisfy the different optimal estimate
\[
\lim_{\eta\downarrow0}\sup_{\substack{0<\delta(f)<\eta\\d_2(f)<d_1(f)}}
\frac{d_2(f)}{\sqrt{\delta(f)}}=1.
\]
Consequently the union of the two circles of extremizers has optimal local \(H^2\) distance-to-deficit coefficient \(1\). In particular, all asymptotically extremal Schur functions converge in \(H^2\), up to phases, to one of the two monomials.

## Assumptions and scope

All matrices and functions are complex. The operator norm is the Euclidean spectral norm. The numerical radius of the displayed weighted shift is \(\sqrt{3+1}/2=1\): unitary diagonal conjugation makes every rotation of the shift similar, and the maximal eigenvalue of its Hermitian part is \(\sqrt{3+1}/2\). All claims concern scalar \(H^\infty\) Schur functions vanishing at zero; no boundary regularity or polynomial restriction is imposed. Holomorphic functional calculus is determined by the first two coefficients because \(A^3=0\). In the local suprema, the condition distinguishing the nearer extremizer class is meaningful for sufficiently small positive deficits, as proved below.

## Proof

**1. A two-by-two coefficient representation.** Schwarz's lemma writes \(f(z)=zg(z)\) with \(\|g\|_\infty\le1\). Put \(b=g(0)=f'(0)\), \(c=g'(0)\), \(x=|b|^2\), and \(y=|c|\). Schwarz–Pick gives
\[
0\le x\le1,\qquad 0\le y\le1-x.
\]
Deleting the zero first column and third row of \(f(A)\), and harmlessly adjusting row and column phases, leaves a two-by-two upper-triangular matrix with absolute entries
\[
B=\begin{pmatrix}\sqrt3\sqrt{x}&\sqrt3 y\\0&\sqrt{x}\end{pmatrix}.
\]
Its two squared singular values have sum \(4x+3y^2\) and product \(3x^2\). The norm is increasing in \(y\) for fixed \(x\): the norm of a matrix with nonnegative entries is monotone under entrywise increase, by taking entrywise absolute values of the maximizing vectors. Hence it suffices to bound the endpoint \(y=1-x\).

**2. Global deficit and rigidity.** Let \(H(x)=B(x,1-x)^*B(x,1-x)\). Its trace and determinant are
\[
\operatorname{tr}H(x)=4x+3(1-x)^2,\quad
\det H(x)=3x^2,\quad
\det(3I-H(x))=6x(1-x).
\]
Also \(3I-H(x)\) is positive semidefinite: for \(0<x<1\) its determinant is positive and its upper-left principal minor \(3-3x\) is positive; the endpoints follow by continuity. If its eigenvalues are \(3-\lambda_+(x)\) and \(3-\lambda_-(x)\), then \(0\le\lambda_-(x)\le\lambda_+(x)\le3\) and
\[
3-\lambda_+(x)=\frac{6x(1-x)}{3-\lambda_-(x)}\ge2x(1-x).
\]
Since \(\|f(A)\|^2\le\lambda_+(x)\), the claimed global mixing deficit follows. Equality \(\delta(f)=0\) requires \(x=0\) or \(x=1\). In the first case \(\|f(A)\|^2=3|c|^2\) forces \(|c|=1\), and Schwarz's lemma applied to \(g\) forces \(g(z)=\omega z\), giving \(f=\omega z^2\). In the second case Schwarz's lemma forces \(f=\omega z\). (The qualitative norm and equality cases are also contained in the earlier general weighted-shift power-bound result.)

**3. Local asymptotics near the quadratic well.** Write \(s=1-y\). If \(d_2(f)\to0\), then \(s\to0\) and \(0\le x\le s\). Since the trace is \(3-6s+4x+3s^2\) and the determinant is \(3x^2\), the larger eigenvalue uniformly satisfies
\[
\|f(A)\|^2=3-6s+4x+O(s^2),\qquad
\delta(f)=6s-4x+O(s^2)\ge2s-O(s^2).
\]
The use of equality here is justified because it is the actual two-by-two matrix with \(y=1-s\); for \(s\) small its top eigenvalue is separated from the second eigenvalue. Parseval and \(\|f\|_{H^2}\le1\) give
\[
d_2(f)^2=1+\|f\|_{H^2}^2-2y\le2s.
\]
Consequently \(\limsup d_2(f)^2/\delta(f)\le1\).

**4. Local asymptotics near the linear well.** If \(d_1(f)\to0\), put \(h=1-x\). Schwarz–Pick gives \(y\le h\). Perturbing the simple eigenvalue \(3\) of \(B(1,0)^*B(1,0)\), with off-diagonal entries of order \(h\), yields the uniform expansion
\[
\|f(A)\|^2=3-3h+O(h^2),\qquad
\delta(f)=3h+O(h^2).
\]
Furthermore
\[
d_1(f)^2=1+\|f\|_{H^2}^2-2\sqrt x\le2(1-\sqrt{1-h})=h+O(h^2).
\]
Therefore \(\limsup d_1(f)^2/\delta(f)\le1/3\).

**5. Branch separation and sharpness.** By Step 2, \(\delta(f)\downarrow0\) forces \(x\to0\) or \(x\to1\) along any sequence or subsequence. If \(x\to0\), the bound \(\|f(A)\|^2\le4x+3y^2\) forces \(y\to1\) and hence \(d_2(f)\to0\), while \(d_1(f)\not\to0\). If \(x\to1\), Parseval forces \(d_1(f)\to0\), while \(d_2(f)\not\to0\). Thus Steps 3–4 apply to every sufficiently near-extremizing sequence in the appropriate branch.

For \(0<t<1\), the degree-two Blaschke product
\[
f_t(z)=z\,\frac{z-t}{1-tz}
\]
is inner, so \(\|f_t\|_{H^2}=1\), \(b=-t\), \(c=1-t^2\), and
\[
d_2(f_t)^2=2t^2,\qquad d_1(f_t)^2=2(1-t).
\]
As \(t\downarrow0\), Step 3 gives \(\delta(f_t)=2t^2+O(t^4)\), proving the quadratic-well constant \(1\) and the sharpness of the global mixing coefficient \(2\). As \(t\uparrow1\), Step 4 gives \(\delta(f_t)=3(1-t^2)+O((1-t^2)^2)\), proving the linear-well constant \(1/\sqrt3\). Taking the larger of the branch constants proves the union-of-wells constant \(1\).

## Verification

The determinant identity and both uniform eigenvalue expansions are analytic identities/perturbation estimates proved above. The supplementary standalone checker `check_critical_nilpotent.py` verifies the exact symbolic identity, 3,960 finite real matrix tests of the global gap, and asymptotic numerical behavior in 14 Blaschke cases. It prints `CRITICAL_NILPOTENT_TWO_WELL_CHECK_OK 3975`. These tests are diagnostics only, not a substitute for the proof for all Schur functions.

## Relationship to prior work

Crouzeix and Greenbaum (2025, Lemma 1) already prove, for a broad family of weighted cyclic shifts including a nilpotent case, that the scalar disk functional calculus norm equals the largest norm of a matrix power; thus the exact \(\sqrt3\) value and the fact that a monomial attains it are **not** claimed as new. Åhag, Czyż, Perälä and Virtanen (2026) give the complete dimension-three Crouzeix inequality and equality classifications. Looi (2026) supplies a short alternative proof of the universal constant. A prior quantitative note establishes a sharp \(H^2\)-stability law for the **balanced** nilpotent \(\sqrt2J_3\), where the quadratic extremizer is unique up to phase. Here the matrix has unequal weights \(\sqrt3\) and \(1\), and two monomial extremizer classes coexist; the new quantitative object is their unequal sharp local stability constants and the global mixing deficit. The balanced constant does not imply either critical-well coefficient.

## Limitations

This theorem concerns only one critical weight ratio (and its reversed matrix by unitary equivalence), scalar symbols vanishing at the origin, and local \(H^2\) stability. The global inequality is not an exact characterization of all deficits, and no claim is made about the optimal all-deficit \(H^2\) constant, off-critical weights, arbitrary scalar functions with nonzero constant terms, or matrix-valued symbols. Broader unindexed symbol-stability arguments could implicitly subsume these local constants; publication-priority novelty is not guaranteed. Independent validation has not been performed.

## References

1. S. Looi, *A short proof of the complete Crouzeix inequality in dimension three*, arXiv:2611.01416v1 (first publicly submitted 1 November 2026), https://arxiv.org/abs/2611.01416.
2. M. Crouzeix and A. Greenbaum, *A New Proof that the Numerical Range is a Complete 2-Spectral Set for Weighted Shift Matrices*, arXiv:2508.12768v1 (18 August 2025), especially Lemma 1, https://arxiv.org/abs/2508.12768.
3. P. Åhag, R. Czyż, A. Perälä and J. Virtanen, *Square Functions and the Complete Crouzeix Conjecture in Dimension Three*, arXiv:2608.27346v1 (27 August 2026), especially Section 12, https://arxiv.org/abs/2608.27346.
4. *Sharp Hardy-space stability at the extremal three-site nilpotent spectral-set constant*, published mathematical note, 17 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-hardy-space-stability-at-the-extremal-three-site-nilpotent--273e463de3d2.
5. K. Bickel, G. Corbett, A. Glenning, C. Guan and M. Vollmayr-Lee, *Crouzeix's conjecture, compressions of shifts, and classes of nilpotent matrices*, arXiv:2312.04537, https://arxiv.org/abs/2312.04537.
