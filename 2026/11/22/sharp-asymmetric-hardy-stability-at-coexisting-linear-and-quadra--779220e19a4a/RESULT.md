# Sharp asymmetric Hardy stability at coexisting linear and quadratic nilpotent extremizers

## Finding

Let
\[
A=\begin{pmatrix}0&\sqrt3&0\\0&0&1\\0&0&0\end{pmatrix}.
\]
For a scalar Schur function \(f\) with \(f(0)=0\), set
\[
\delta(f)=3-\|f(A)\|^2,\qquad x(f)=|f'(0)|^2,\qquad
d_j(f)=\inf_{|\omega|=1}\|f-\omega z^j\|_{H^2}\quad(j=1,2).
\]
Then the global mixing estimate
\[
\boxed{\delta(f)\ge 2x(f)(1-x(f))}
\]
has sharp coefficient \(2\). The two classes \(\{\omega z:|\omega|=1\}\) and \(\{\omega z^2:|\omega|=1\}\) are exactly the cases \(\delta(f)=0\). Their optimal local stability coefficients are different:
\[
\lim_{\eta\downarrow0}\sup_{\substack{0<\delta(f)<\eta\\d_1(f)<d_2(f)}}
\frac{d_1(f)}{\sqrt{\delta(f)}}=\frac1{\sqrt3},\qquad
\lim_{\eta\downarrow0}\sup_{\substack{0<\delta(f)<\eta\\d_2(f)<d_1(f)}}
\frac{d_2(f)}{\sqrt{\delta(f)}}=1.
\]
Consequently \(\min\{d_1(f),d_2(f)\}/\sqrt{\delta(f)}\) has optimal limiting supremum \(1\) as the positive deficit tends to zero. Every asymptotically extremal sequence has distance tending to zero from the **union** of the two circles. On a subsequence belonging to one nearest class, suitable unimodular factors give convergence to its monomial. An asymptotically extremal sequence can alternate between the classes, so convergence to a single class is not asserted.

## Assumptions and scope

The norm on matrices is the Euclidean operator norm and \(H^2\) has the coefficient-square norm. The numerical range of \(A\) is the closed unit disk: diagonal unitary conjugation realizes rotations, and the largest eigenvalue of \((A+A^*)/2\) is \(\sqrt{3+1}/2=1\). The functional calculus uses just two Taylor coefficients since \(A^3=0\) and \(f(0)=0\). The results concern arbitrary scalar anchored Schur functions, not only polynomials or functions continuous on the closed disk.

## Proof

Write \(f(z)=zg(z)\) with \(g\) a Schur function by Schwarz's lemma. Put \(b=g(0)\), \(c=g'(0)\), \(x=|b|^2\), \(y=|c|\). Schwarz–Pick gives \(0\le x\le1\), \(0\le y\le1-x\). Deleting the zero row and column of \(bA+cA^2\) and adjusting phases gives the same norm as
\[
B(x,y)=\begin{pmatrix}\sqrt{3x}&\sqrt3\,y\\0&\sqrt x\end{pmatrix}.
\]
The squared singular values have sum \(4x+3y^2\) and product \(3x^2\). The norm of the nonnegative matrix is nondecreasing in \(y\) because the supremum of the associated bilinear form can be taken over nonnegative unit vectors. Set \(H=B(x,1-x)^*B(x,1-x)\), with eigenvalues \(\lambda_-\le\lambda_+\). The trace and product just computed give
\[
\det(3I-H)=9-3[4x+3(1-x)^2]+3x^2=6x(1-x).
\]
For \(0<x<1\), the first diagonal entry of \(3I-H\) is \(3(1-x)>0\), so \(3I-H\) is positive definite, and the endpoints are positive semidefinite by continuity. Since \(\lambda_-\ge0\), for interior \(x\),
\[
3-\|f(A)\|^2\ge3-\lambda_+=\frac{6x(1-x)}{3-\lambda_-}\ge 2x(1-x).
\]
The endpoint inequality follows from positive semidefiniteness and monotonicity. If \(\delta=0\), then \(x=1\) or \(x=0\). For \(x=1\), Schwarz's lemma for \(f\) forces a linear monomial up to phase; for \(x=0\), the norm condition gives \(y=1\), so Schwarz's lemma for \(g\) gives a quadratic monomial up to phase. Both classes attain equality.

By coefficient orthogonality and the bound \(\|f\|_{H^2}\le1\),
\[
d_1^2=1+\|f\|_{H^2}^2-2\sqrt x\le 2(1-\sqrt x),\qquad
d_2^2=1+\|f\|_{H^2}^2-2y\le 2(1-y).
\]
For \(\delta\to0\), the mixing inequality forces the distance of \(x\) to \(\{0,1\}\) to tend to zero. On a subsequence with \(x\to0\), the trace bound \(3-\delta\le4x+3y^2\) gives \(y\to1\). Hence \(d_2\to0\) and, since \(y>\sqrt x\) eventually, \(d_2<d_1\). On a subsequence with \(x\to1\), we have \(y\le1-x\to0\), so \(d_1\to0\) and \(d_1<d_2\) eventually. These are the only accumulation cases. In particular ties are absent at sufficiently small positive deficits, and each nearer-class condition selects the associated limit. This proves convergence in distance to the union.

Near the quadratic class, write \(s=1-y\), so \(0\le x\le s\to0\). The trace of the actual squared singular-value matrix is \(3-6s+4x+3s^2\) and its smaller eigenvalue is \(O(x^2)\) by the determinant and the fact that the larger eigenvalue tends to \(3\). Uniformly in this class,
\[
\delta=6s-4x+O(s^2)\ge 2s-O(s^2),\qquad d_2^2\le 2s.
\]
This gives upper limiting squared ratio \(1\).

Near the linear class, put \(h=1-x\), so \(y\le h\to0\). The actual matrix \(B(x,y)^*B(x,y)\) has diagonal entries \(3x\) and \(x+3y^2\) with gap tending to \(2\), and off-diagonal magnitude \(3\sqrt x\,y\). The two-by-two eigenvalue formula then gives larger eigenvalue \(3x+O(y^2)\), uniformly. Thus
\[
\delta=3h+O(h^2),\qquad d_1^2\le 2(1-\sqrt{1-h})=h+O(h^2).
\]
This gives upper limiting squared ratio \(1/3\).

For sharpness use the inner functions \(f_t(z)=z(z-t)/(1-tz)\) for \(0<t<1\). Their parameters satisfy \(x=t^2\), \(y=1-t^2\); their squared distances are \(d_2^2=2t^2\), \(d_1^2=2(1-t)\). As \(t\downarrow0\), \(\delta=2t^2+O(t^4)\), thus both the coefficient in the global estimate and the quadratic-class coefficient are optimal. As \(t\uparrow1\), \(\delta=3(1-t^2)+O((1-t^2)^2)\), giving the claimed linear-class optimum. Taking the larger of the two branch coefficients gives the optimum for the distance to the union. Alternating the two parameter limits also illustrates why an extremizing sequence need not converge to a single monomial class even after rephasing.

## Verification

The determinant identity, coefficient estimates and uniform eigenvalue bounds above apply to all admissible Schur functions. The supplementary Python script `check_critical_nilpotent.py` is unchanged and checks the symbolic determinant, samples the matrix deficit, and checks the asymptotic ratios on selected Blaschke parameters. Its recorded output is `CRITICAL_NILPOTENT_TWO_WELL_CHECK_OK 3975` (NumPy and SymPy required). These finite diagnostics are not a proof and do not test convergence to any single class.

## Relationship to prior work and limitations

Crouzeix and Greenbaum establish the optimal disk functional calculus norm as a maximum of power norms for the relevant weighted shifts, so the constant \(\sqrt3\) and attainment by powers are background. The general dimension-three Crouzeix inequality and its equality theory concern a different universal threshold. Earlier sharp Hardy-space stability for \(\sqrt2J_3\) has a unique quadratic extremizer class and a different normalization. Here the quantitative conclusions concern the deficit penalizing mixing at the critical unequal weights and the unequal sharp local coefficients for the two classes. No optimal all-deficit Hardy constant, off-critical law, or result for unanchored or matrix-valued functions is asserted. Historical priority outside the directly compared results is not certified.

## References

1. M. Crouzeix and A. Greenbaum, *A New Proof that the Numerical Range is a Complete 2-Spectral Set for Weighted Shift Matrices*, [arXiv:2508.12768v1](https://arxiv.org/abs/2508.12768v1), Lemma 1.
2. P. Åhag, R. Czyż, A. Perälä and J. Virtanen, *Square Functions and the Complete Crouzeix Conjecture in Dimension Three*, [arXiv:2608.27346v1](https://arxiv.org/abs/2608.27346v1), Theorem 1.1 and Section 10.
3. S. Looi, *A short proof of the complete Crouzeix inequality in dimension three*, [arXiv:2611.01416v1](https://arxiv.org/abs/2611.01416v1).
4. [*Sharp Hardy-space stability at the extremal three-site nilpotent spectral-set constant*](https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-sharp-hardy-space-stability-at-the-extremal-three-site-nilpotent--273e463de3d2), 17 November 2026.
5. K. Bickel, G. Corbett, A. Glenning, C. Guan and M. Vollmayr-Lee, *Crouzeix's conjecture, compressions of shifts, and classes of nilpotent matrices*, [arXiv:2312.04537](https://arxiv.org/abs/2312.04537).
