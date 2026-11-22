# A finite shear ceiling and detached contractivity window for second-order Runge–Kutta on three-state Jordan chains

## Finding

Write \(N_3=\begin{psmallmatrix}0&1&0\\0&0&1\\0&0&0\end{psmallmatrix}\), \(A_\gamma=-I_3+\gamma N_3\), \(\gamma\geq0\), and \(R_2(z)=1+z+z^2/2\). For a constant timestep \(h\geq0\), the completed two-stage, order-two explicit Runge–Kutta step is \(T_{h,\gamma}=R_2(hA_\gamma)\). Define

\[
F(h)=\frac{(2-h)^2(h^2-2h+4)}{6h^2-12h+8},\qquad 0\leq h\leq2.
\]

**Exact contractivity criterion:** for every \(\gamma\geq0\) and \(h\geq0\),

\[
\boxed{\|T_{h,\gamma}\|_2\leq1\iff h=0\ \text{or}\ (0<h\leq2\ \text{and}\ \gamma^2\leq F(h)).}
\]

Let \(\theta\in(0,2)\) be the unique root of \(3h^3-12h^2+20h-8=0\), and let \(\gamma_*^2=F(\theta)\). Then \(\theta=0.563885669879039\ldots\), \(\gamma_*=1.447277013648391\ldots\), and \(\gamma_*^2\) is the unique positive root of \(81z^3-126z^2-80z-24=0\). The complete nonexpansive-step sets are:

- \(0\leq\gamma\leq\sqrt2\): one interval \([0,h_+(\gamma)]\), where \(h_+(0)=2\), and otherwise \(h_+(\gamma)\in(\theta,2)\) is the unique solution of \(F(h)=\gamma^2\).
- \(\sqrt2<\gamma<\gamma_*\): \(\{0\}\cup[h_-(\gamma),h_+(\gamma)]\), with \(0<h_-<\theta<h_+<2\) the two solutions of \(F(h)=\gamma^2\).
- \(\gamma=\gamma_*\): exactly \(\{0,\theta\}\).
- \(\gamma>\gamma_*\): exactly \(\{0\}\).

The exact continuous flow \(e^{tA_\gamma}\) is Euclidean contractive at all times precisely when \(\gamma\leq\sqrt2\). Thus the nonempty detached interval for \(\sqrt2<\gamma\leq\gamma_*\) is a **false numerical contractivity window**, not a faithful representation of physical energy decay. An exact rational witness is \(\gamma=10/7\), \(h=1/2\): the continuous flow initially expands some vectors, yet the order-two Runge–Kutta step strictly contracts all nonzero vectors because \(\gamma^2=100/49<F(1/2)=117/56\).

## Assumptions and scope

All vector spaces and matrices are real, all norms are standard Euclidean operator norms, and \(\gamma,h\) range over the nonnegative reals. The statement concerns **one completed step** of any two-stage second-order explicit Runge–Kutta method on this fixed, three-dimensional, autonomous, homogeneous linear ODE. The Jordan shift \(N_3\) is nilpotent of index three. Every eigenvalue of \(A_\gamma\) equals \(-1\); eigenvalue stability alone cannot decide Euclidean nonexpansion. No claim is made about internal-stage contractivity, arbitrary matrices, or numerical error accuracy. The statement includes the zero-step identity and both threshold equalities.

## Proof

**1. Exact matrix.** Since \(N_3^3=0\), polynomial calculus gives

\[
T_{h,\gamma}=\begin{pmatrix}r&b&c\\0&r&b\\0&0&r\end{pmatrix},\quad
r=1-h+\frac{h^2}{2},\quad b=\gamma h(1-h),\quad c=\frac{\gamma^2h^2}{2}.
\]

Here \(r=(1+(h-1)^2)/2>0\). For \(h>2\), \(r>1\), whence \(\|T\|_2\geq r>1\). At \(h=0\), \(T=I_3\). For \(h=2\), \(r=1\) and any \(\gamma>0\) produces an off-diagonal entry, so the norm exceeds one; at \(\gamma=0\), \(T=I_3\). It remains to classify \(0<h<2\).

**2. A single exact singular-norm crossing.** Put \(S=I_3-T^{\mathsf T}T\). Direct multiplication and determinant expansion yield

\[
\det S=\frac{h^3(h-2)}{64}
\underbrace{\big[6\gamma^2h^2+(h^2-2h+4)^2\big]}_{>0}
\big[(6h^2-12h+8)\gamma^2-(2-h)^2(h^2-2h+4)\big].\tag{1}
\]

For fixed \(0<h<2\), the quantity \(\|T_{h,\gamma}\|_2\) is continuous and strictly increasing in \(\gamma\geq0\): conjugating by \(\operatorname{diag}(1,-1,1)\), when necessary, replaces \(b\) by \(|b|\) without changing \(c\), so the matrix becomes entrywise nonnegative. The largest singular value of a nonnegative matrix is monotone in its nonnegative entries, and strictly grows with the strictly increasing \(c\) for \(\gamma>0\); the case \(h=1\), for which \(b=0\), follows from the positive two-by-two corner. At \(\gamma=0\), the norm equals \(r<1\); as \(\gamma\to\infty\), it diverges. Therefore the norm crosses one exactly once. At that crossing, \(\det S=0\). In (1), the first bracket is strictly positive and \(6h^2-12h+8=2(3(h-1)^2+1)>0\), so the unique crossing is precisely \(\gamma^2=F(h)\). Before it the norm is strictly less than one and afterward strictly greater than one. This proves the boxed criterion, including equality.

**3. A unique interior shear ceiling.** Exact differentiation gives

\[
F'(h)=\frac{h(h-2)(3h^3-12h^2+20h-8)}{(3h^2-6h+4)^2}.
\]

The cubic \(C(h)=3h^3-12h^2+20h-8\) is strictly increasing because \(C'(h)=9(h-4/3)^2+4>0\); \(C(0)=-8\) and \(C(2)=8\). Thus it has precisely one root \(\theta\in(0,2)\), \(F\) strictly rises on \((0,\theta)\), then strictly falls on \((\theta,2)\). Also \(F(0)=2\), \(F(2)=0\), and \(F(h)>0\) inside. These facts yield every level-set case in the finding, with no additional contractivity islands. Eliminating \(h\) from \(C(h)=0\) and \(z(6h^2-12h+8)=(2-h)^2(h^2-2h+4)\) gives the resultant \(512(81z^3-126z^2-80z-24)\); Descartes' sign rule shows the displayed cubic has one positive root, which must equal \(F(\theta)\). Since \(F(\theta)>2\), the false interval is nonempty. The maximum is nondegenerate, so its endpoints coalesce in a square-root fold as \(\gamma\uparrow\gamma_*\).

**4. Physical contrast.** The symmetric part of \(A_\gamma\) has eigenvalues \(-1+\gamma/\sqrt2,-1,-1-\gamma/\sqrt2\), by the three-site tridiagonal cosine spectrum. A continuous-time linear semigroup is Euclidean nonexpansive for every nonnegative time exactly when its symmetric generator part is negative semidefinite; this is equivalent to \(\gamma\leq\sqrt2\). For \(\gamma>\sqrt2\), its largest logarithmic norm is positive, so there are nonzero initial vectors whose norm initially increases. The rational witness follows by direct substitution: \(F(1/2)-100/49=133/2744>0\). This completes the proof.

## Verification

The companion `verify.py` uses only the Python standard library. It checks the matrix polynomial, the determinant factorization on a rational interpolation grid sufficient to establish the bivariate polynomial identity, the derivative identity, exact rational witness, the cubic root brackets, and supplementary finite parameter comparisons using a symmetric Jacobi eigenvalue solver. Run `python3 verify.py`. The universal sign and monotonicity arguments are given above; finite samples alone are not used to prove infinitely many cases. The dimensionless numerical values are \(\theta\approx0.563885669879039\), \(\gamma_*^2\approx2.094610754235005\), \(\gamma_*\approx1.447277013648391\).

## Relationship to prior work

Sun and Shu [1], Ranocha and Ketcheson [2], Sun, Wei and Wu [3], and Achleitner, Arnold and Jüngel [4] give general energy-stability or strong-stability frameworks for explicit Runge–Kutta methods; these do not supply the exact three-state Jordan shear region or its algebraic critical ceiling. Related published special-family results include the explicit second-order damped-oscillator energy frontier [5], involving a different two-dimensional (not Jordan) system, and a fourth-order planar Jordan shear classification [6]. The latter yields a false contraction interval for arbitrary large shear because the fourth-order derivative vanishes at one step; the present **second-order, nilpotency-index-three** criterion instead has a finite algebraic ceiling, so neither result implies the other. The familiar scalar order-two stability polynomial and symmetric-part logarithmic-norm test are used as background, not claimed new. The historical priority assessment is qualified; a specialized source outside the inspected material could have an equivalent result.

## Limitations

The false window should not be used as evidence of faithful physical energy evolution or good approximation error. The theorem is restricted to a homogeneous, three-state Jordan chain with equal diagonal damping and a single common superdiagonal shear. It does not classify larger Jordan blocks, arbitrary nonnormal matrices, or nonlinear equations. The reproduced algebra and numerical checks do not constitute independent human validation, and historical priority is not conclusively certified.

## References

[1] Z. Sun and C.-W. Shu, *Strong stability of explicit Runge–Kutta time discretizations*, arXiv:1811.10680v1 (first public 2018-11-26), https://arxiv.org/abs/1811.10680 .

[2] H. Ranocha and D. I. Ketcheson, *Energy stability of explicit Runge–Kutta methods for non-autonomous or nonlinear problems*, arXiv:1909.13215 (first public 2019-09-29), https://arxiv.org/abs/1909.13215 .

[3] Z. Sun, Y. Wei, and K. Wu, *On energy laws and stability of Runge–Kutta methods for linear seminegative problems*, arXiv:2201.06501v1 (first public 2022-01-17), https://arxiv.org/abs/2201.06501 .

[4] F. Achleitner, A. Arnold, and A. Jüngel, *Necessary and sufficient conditions for strong stability of explicit Runge–Kutta methods*, arXiv:2308.05689v1 (first public 2023-08-10), https://arxiv.org/abs/2308.05689 .

[5] *A sharp energy-contraction frontier for explicit RK2 on damped oscillators*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-energy-contraction-frontier-for-explicit-rk2-on-damped-o--c4ff16d39c20 .

[6] *A sharp false-contractivity island for classical fourth-order Runge–Kutta on planar Jordan shears*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-false-contractivity-island-for-classical-fourth-order-ru--8fe2a7f6e756 .
