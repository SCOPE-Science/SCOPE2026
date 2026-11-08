# An exact finite-angle law and logarithmic mean-risk penalty for Gaussian randomized Rayleigh–Ritz refinement

## Finding

The same Gaussian square-compression procedure that admits high-probability quadratic eigenvalue refinement has an exactly solvable **different unconditional risk scale** on a fixed Hermitian example. For a simple interior eigenvalue with trial-space angle \(\varepsilon\), the refined eigenvalue has exact finite-angle cumulative distribution, and its expected absolute error scales as \(8\varepsilon^2\log(1/\varepsilon)\), while its root-mean-square error scales as \(2\varepsilon\). The ordinary deterministic Rayleigh–Ritz value on that very subspace has error \(2\varepsilon^2+O(\varepsilon^4)\). The distinction is between high-probability estimates and unconditional moments: neither contradicts the other.

## Assumptions and scope

For every \(0<\varepsilon<\pi/4\), work in \(\mathbb C^4\) with the fixed Hermitian matrix
\[
 A=\operatorname{diag}(-1,0,1,2),\qquad \lambda=0,\quad v=e_2.
\]
The target eigenvalue is simple and interior to the spectrum. Put
\[
 w=\cos\varepsilon\,e_2+\sin\varepsilon\,e_4,
 \quad u=-\sin\varepsilon\,e_2+\cos\varepsilon\,e_4,
 \quad W=[w,e_3].
\]
The columns of \(W\) are orthonormal and \(\angle(e_2,\operatorname{ran}W)=\varepsilon\). Draw \(\Omega\in\mathbb C^{4\times2}\) with independent entries whose real and imaginary parts are independent \(N(0,1/2)\). Solve the **square** randomized Petrov–Galerkin eigenproblem
\[
 \Omega^*AWy=\mu\,\Omega^*Wy.
\]
Select the eigenvalue branch \(\mu_\varepsilon\) tending to zero for almost every fixed draw as \(\varepsilon\downarrow0\); select its eigenvector \(y_\varepsilon\), and refine via the ordinary Hermitian Rayleigh quotient \(\rho_\varepsilon=(Wy_\varepsilon)^*A(Wy_\varepsilon)/\|Wy_\varepsilon\|^2\). Branch selection is part of the statement; arbitrary wanted-pair selectors are not analyzed.

Define \(d=2\sin^2\varepsilon\), \(b=\sin(2\varepsilon)\), and \(t=b^2\in(0,1)\). If \(Z_0,Z_1,Z_2\) are independent standard circular complex Gaussians, then the raw selected value and the refined normalized error have exact laws
\[
 \mu_\varepsilon\stackrel{d}=d+bZ_1/Z_0,\qquad
 R_\varepsilon:=\frac{\rho_\varepsilon-d}{1-d}
 \stackrel{d}=\frac{t|Z_2|^2}{|Z_0|^2+t|Z_2|^2}.
\]
Here the \(Z_0\) in the second **marginal law** can be taken as an independent standard complex Gaussian; the two displayed identities are not asserted as a joint coupling. Consequently for \(x\in[0,1]\) and \(y\in[d,1]\),
\[
 \Pr(R_\varepsilon\le x)=\frac{x}{t+(1-t)x},\qquad
 \Pr(\rho_\varepsilon\le y)=\frac{y-d}{t(1-d)+(1-t)(y-d)}.
\]
The distribution has no atoms. Defining
\[
 F_1(t)=\frac{t(t-1-\log t)}{(1-t)^2},\qquad
 F_2(t)=\frac{t(1+2t\log t-t^2)}{(1-t)^3},
\]
one has the exact formulas
\[
 \mathbb E\rho_\varepsilon=d+(1-d)F_1(t),\quad
 \mathbb E\rho_\varepsilon^2=d^2+2d(1-d)F_1(t)+(1-d)^2F_2(t).
\]
For \(\varepsilon\downarrow0\),
\[
 \mathbb E\rho_\varepsilon=8\varepsilon^2\log(1/\varepsilon)+O(\varepsilon^2),\qquad
 (\mathbb E\rho_\varepsilon^2)^{1/2}=2\varepsilon+o(\varepsilon).
\]
Since \(0<d\le\rho_\varepsilon\le1\), the mean is also the expected absolute error from zero. In contrast \(W^*AW=\operatorname{diag}(d,1)\), so the standard Rayleigh–Ritz value near zero is deterministically \(d=2\varepsilon^2+O(\varepsilon^4)\).

## Proof

**1. Exact pencil reduction.** Direct calculation gives \(Aw=dw+bu\), \(Ae_3=e_3\), and \(u\perp\operatorname{ran}W\). Write \(G=\Omega^*W\in\mathbb C^{2\times2}\), \(h=\Omega^*u\in\mathbb C^2\). Orthogonal invariance of circular complex Gaussians makes the entries of \(G\) and \(h\) jointly independent, standard circular complex Gaussians. The square matrix \(G\) is invertible almost surely, and the compressed matrix is precisely
\[
 G^{-1}\Omega^*AW=
 \begin{pmatrix}d+bU_1&0\\ bU_2&1\end{pmatrix},
 \qquad U=G^{-1}h.
\]
Thus its eigenvalues are \(d+bU_1\) and \(1\). For every fixed sketch with \(G\) invertible, the first tends to \(0\) and the latter stays \(1\), proving the asserted almost-sure branch characterization. Except on a null set the corresponding eigenvector is \(y=(1,z)^\mathsf T\) with
\[
 z=-\frac{bU_2}{1-d-bU_1}.
\]
Its refined Rayleigh quotient is \(\rho=(d+|z|^2)/(1+|z|^2)\).

**2. Complex-Gaussian ratio lemma.** For \(G\in\mathbb C^{2\times2}\), \(h\in\mathbb C^2\) with six independent standard circular Gaussian entries, the vector \(G^{-1}h\) has the same law as \((Z_1/Z_0,Z_2/Z_0)\) for three independent standard circular complex Gaussians. Indeed the one-dimensional nullspace of the iid Gaussian \(2\times3\) matrix \([G,-h]\) is unitarily invariant and therefore Haar-uniform in complex projective two-space; the null direction has homogeneous coordinates \([Z_0,Z_1,Z_2]\) and, almost surely, a nonzero first coordinate. The null equation gives precisely the displayed affine ratios. This argument is purely a distributional statement, not a pathwise identification with the original sketch.

The first coordinate is a standard complex Cauchy quotient, so \(\mu-d\) has planar density
\[
 f(v)=\frac{b^2}{\pi(b^2+|v|^2)^2},\qquad v\in\mathbb C.
\]
Polar integration shows \(\mathbb E|\mu-d|^p<\infty\) exactly for \(0\le p<2\) (and it is infinite for \(p\ge2\)); shifting by finite \(d\) does not change this threshold for \(\mathbb E|\mu|^p\).

**3. Distribution of the refined value.** Substitute the Gaussian-ratio representation into \(z\):
\[
 z\stackrel d=-\frac{bZ_2}{(1-d)Z_0-bZ_1}.
\]
Because \(1-d=\cos(2\varepsilon)\) and \((1-d)^2+b^2=1\), the denominator is standard circular complex Gaussian and independent of \(Z_2\). Therefore \(|z|^2\stackrel d=tX/Y\), with \(X,Y\) independent unit-rate exponentials. In particular
\[
 R=\frac{|z|^2}{1+|z|^2}\stackrel d=\frac{tX}{Y+tX}.
\]
The independent-exponential ratio \(V=X/(X+Y)\) is uniform on \([0,1]\), and \(R=tV/[1-(1-t)V]\). Solving this increasing map for \(V\) yields the exact cumulative distribution \(\Pr(R\le x)=x/[t+(1-t)x]\) for \(0\le x\le1\). The affine map \(\rho=d+(1-d)R\) gives the stated law of \(\rho\).

**4. Moments and sharp asymptotics.** Differentiation gives density \(f_R(x)=t/[t+(1-t)x]^2\) on \((0,1)\). Direct elementary integration establishes
\[
 \mathbb ER=\int_0^1\frac{xt}{[t+(1-t)x]^2}\,dx=F_1(t),\quad
 \mathbb ER^2=\int_0^1\frac{x^2t}{[t+(1-t)x]^2}\,dx=F_2(t).
\]
The exact formulas for \(\mathbb E\rho\) and \(\mathbb E\rho^2\) follow by expanding \(\rho=d+(1-d)R\). As \(\varepsilon\downarrow0\), \(d=2\varepsilon^2+O(\varepsilon^4)\), \(t=4\varepsilon^2+O(\varepsilon^4)\), \(F_1(t)=t\log(1/t)+O(t)\), and \(F_2(t)=t+o(t)\). Substitution proves the two sharp rates and constants. Each step is an exact distributional calculation, not an extrapolation from finite-sample simulation.

## Verification

Run the standalone Python script \(\texttt{verify.py}\) using NumPy; it checks direct Gaussian pencil construction against the reduced algebra, evaluates exact moment integrals by deterministic Gaussian quadrature, and compares empirical cumulative distributions with the closed-form law at several fixed angles. It also checks the small-angle asymptotic constants analytically from the formulas at a decreasing sequence of angles. Finite computation corroborates but does not prove the preceding distributional and asymptotic assertions.

## Relationship to prior work

N. Shao, *Stabilizing the Rayleigh–Ritz procedure by randomization*, arXiv:2604.01037v4, Algorithm 1 and its convergence analysis, studies the same square complex Gaussian Petrov–Galerkin pencil and Rayleigh-quotient refinement, with **high-probability** guarantees. Those do not directly imply the unconditional expected and mean-square rates above. The source explicitly leaves selection of wanted eigenpairs to a user-specified criterion. The standard complex Gaussian-ratio / projective-Haar facts are classical and not claimed as new.

Y. Nakatsukasa and J. A. Tropp, *Fast and Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, SIAM J. Matrix Anal. Appl. 45 (2024), 1183–1214, Section 6, studies a related **oversampled least-squares sketched Rayleigh–Ritz** process, not this square-Gaussian distribution and its branch's unconditional moments. Earlier study of the small-angle **limiting** Gaussian-ratio tails for a different three-dimensional Hermitian plane did not determine this exact finite-angle cumulative law, logarithmic first-moment coefficient, or sharp first-order root-mean-square constant. This is a scope/implication comparison, not a claim that complex Cauchy variables are newly discovered.

## Limitations

The result is for one four-dimensional Hermitian matrix, one specific two-dimensional rotating plane, proper complex Gaussian square sketches, and the mathematically specified branch in exact arithmetic. It does not address automatic eigenpair selection, different sketch distributions, oversampling, finite-precision conditioning, iterative subspace generation, arbitrary matrix families, or practical average runtimes. The unrefined random eigenvalue has infinite variance, whereas the refined quotient is bounded, so the conclusions are not a blanket statement that randomized Rayleigh–Ritz fails. The leading mean and root-mean-square effects describe unconditional error and coexist with the published high-probability theory.

## References

1. N. Shao, *Stabilizing the Rayleigh–Ritz procedure by randomization*, arXiv:2604.01037 (first public version April 1, 2026; version 4 October 26, 2026), https://arxiv.org/abs/2604.01037.
2. Y. Nakatsukasa and J. A. Tropp, *Fast and Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, SIAM J. Matrix Anal. Appl. 45 (2024), 1183–1214, https://doi.org/10.1137/23M1565413; legal author-hosted full text https://tropp.caltech.edu/papers/NT24-Fast-Accurate-SIMAX.pdf.
