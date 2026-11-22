# Sharp fixed-energy Fourier-ratio frontier and a four-mode condensate on square grids

## Finding

Write \(G_N=(\mathbb Z/N\mathbb Z)^2\), with \(N\ge4\), and use the unitary Fourier transform on \(G_N\). For a nonzero mean-zero function \(g:G_N\to\mathbb C\), define its Fourier ratio and scaled discrete Dirichlet-energy quotient by
\[
R(g)=\frac{\|\widehat g\|_{\ell^1}}{\|\widehat g\|_{\ell^2}},\qquad
\mathcal E_N(g)=\frac{N^2\sum_{j=1}^2\|g(\cdot+e_j)-g\|_{\ell^2}^2}{\|g\|_{\ell^2}^2}.
\]
For \(E\ge\Lambda_N=4N^2\sin^2(\pi/N)\), let \(K_N(E)\) denote the maximum of \(R(g)\) subject to \(\mathcal E_N(g)\le E\) and \(\widehat g(0)=0\). Define \(\lambda_{N,k}=4N^2[\sin^2(\pi k_1/N)+\sin^2(\pi k_2/N)]\), and let all sums below run over nonzero \(k\in G_N\).

**Exact frontier and all optimizers.** The smallest eigenvalue is \(\Lambda_N\), with multiplicity exactly four, and the arithmetic mean of the nonzero eigenvalues is \(\overline\Lambda_N=4N^4/(N^2-1)\). The exact classification is
\[
K_N(\Lambda_N)=2,\qquad K_N(E)=\sqrt{N^2-1}\quad(E\ge\overline\Lambda_N).
\]
For \(\Lambda_N<E<\overline\Lambda_N\), a unique \(t<\Lambda_N\) solves
\[
E=\frac{\sum_k\lambda_{N,k}(\lambda_{N,k}-t)^{-2}}{\sum_k(\lambda_{N,k}-t)^{-2}},
\qquad
K_N(E)=\frac{\sum_k(\lambda_{N,k}-t)^{-1}}{[\sum_k(\lambda_{N,k}-t)^{-2}]^{1/2}}.
\]
In that interior regime, *every* maximizing Fourier-magnitude profile is exactly \(|\widehat g(k)|=c/(\lambda_{N,k}-t)\), with arbitrary coefficient phases and positive \(c\). At the minimal budget, exactly the four first-eigenvalue modes are used with equal magnitudes; at and above the arithmetic-mean budget, all nonzero Fourier modes have equal magnitudes. In each case the real-valued constraint leaves the same optimum if the phases obey Fourier conjugacy.

**Sharp fixed-energy critical law.** Fix any real \(E>4\pi^2\). Define \(\Delta_N=E-\Lambda_N\), and let \(H_N\) be the set of nonzero frequencies other than the four lowest ones. Put
\[
S_N=\sum_{k\in H_N}\frac1{\lambda_{N,k}-\Lambda_N},\qquad
T_N=\sum_{k\in H_N}\frac1{(\lambda_{N,k}-\Lambda_N)^2}.
\]
Then \(S_N=(2\pi)^{-1}\log N+O(1)\), \(T_N\to T_\infty\in(0,\infty)\), and, for sufficiently large \(N\),
\[
0\le2+\sqrt{\Delta_N S_N}-K_N(E)
\le2-2\sqrt{1-\Delta_N T_N/S_N}=O_E((\log N)^{-1}).
\]
In particular,
\[
\boxed{K_N(E)=\sqrt{\frac{E-4\pi^2}{2\pi}\log N}+2
+O_E((\log N)^{-1/2}).}
\]
The additive constant \(2\) is the square root of the first positive Laplacian eigenvalue's multiplicity, rather than an unspecified bounded error.

**Spectral condensation.** For each interior maximizing Fourier profile, normalize \(\sum_{k\ne0}|\widehat g(k)|^2=1\). Let \(Q_N=\sum_{k\in H_N}|\widehat g(k)|^2\) be its off-first-eigenspace mass. As \(N\to\infty\) at the same fixed \(E>4\pi^2\),
\[
\boxed{(\log N)Q_N\longrightarrow2\pi(E-4\pi^2)T_\infty,\quad
T_\infty=\sum_{k\in\mathbb Z^2\setminus\{0,(\pm1,0),(0,\pm1)\}}
\frac1{[4\pi^2(|k|^2-1)]^2}.}
\]
The four lowest modes each carry squared mass \(1/4+O_E(1/\log N)\). Under centered integer representatives, the conditional distribution of the squared Fourier mass on \(H_N\) converges in \(\ell^1(\mathbb Z^2)\) to the probability mass function proportional to \([4\pi^2(|k|^2-1)]^{-2}\). This limits only Fourier magnitudes, not arbitrary maximizing phases.

## Assumptions and scope

All spatial and Fourier norms are unnormalized counting-measure norms; the Fourier transform includes factor \(N^{-1}\). The discrete gradient is the forward periodic difference. The admissible class consists of nonzero, complex (or real) mean-zero grid functions with a *relative* first-difference energy upper bound; the zero-frequency term is excluded. No nonzero mean-zero function is admissible when \(E<\Lambda_N\). The asymptotic statements fix \(E>4\pi^2\) independent of \(N\); they do not assert a uniform result as \(E\downarrow4\pi^2\) or \(E\) grows with \(N\).

## Proof

**1. Fourier reduction.** Parseval and the Fourier multiplier of a forward difference give
\[
N^2\sum_j\|g(\cdot+e_j)-g\|_2^2
=\sum_{k\ne0}\lambda_{N,k}|\widehat g(k)|^2.
\]
Write \(p_k=|\widehat g(k)|^2/\|\widehat g\|_2^2\). The desired maximum equals the maximum of \(\sum_{k\ne0}\sqrt{p_k}\) over the compact convex polytope \(p_k\ge0\), \(\sum p_k=1\), \(\sum\lambda_{N,k}p_k\le E\). The objective is strictly concave. The minimum eigenvalue occurs exactly at \((\pm1,0),(0,\pm1)\) for \(N\ge4\). Since \(\sum_{k\ne0}\lambda_{N,k}=4N^4\), the mean is \(4N^4/(N^2-1)\).

At \(E=\Lambda_N\), the admissible spectra are supported on the four minimal modes, and Cauchy–Schwarz gives maximum \(2\), with equality at equal magnitudes. At \(E\ge\overline\Lambda_N\), unrestricted Cauchy–Schwarz gives \(\sqrt{N^2-1}\), attained uniquely in magnitudes at the uniform profile. If \(\Lambda_N<E<\overline\Lambda_N\), the energy constraint is active: otherwise the unique unconstrained maximum would be the infeasible uniform profile. Every optimal \(p_k\) is strictly positive. Indeed, a zero coordinate can be populated by an arbitrarily small positive amount while adjusting two existing positive coordinates to preserve both affine constraints (or using energy slack); its positive square-root gain dominates all changes on already positive coordinates. Existence of an interior feasible profile follows from a sufficiently small mixture of the uniform profile and the uniform distribution on the lowest four modes.

The Lagrange equations for strictly positive \(p_k\) therefore give \(1/(2\sqrt{p_k})=a+b\lambda_{N,k}\). As the energy bound is active strictly below the uniform mean, \(b>0\) and \(t=-a/b<\Lambda_N\). Normalization yields \(p_k=(\lambda_{N,k}-t)^{-2}/\sum_j(\lambda_{N,j}-t)^{-2}\). The weighted mean of the eigenvalues is a strictly decreasing function of \(t\): its derivative is twice the strictly negative covariance of \(\lambda\) and \((\lambda-t)^{-1}\) under weights proportional to \((\lambda-t)^{-2}\). Its limits as \(t\to-\infty\) and \(t\uparrow\Lambda_N\) are respectively \(\overline\Lambda_N\) and \(\Lambda_N\). Thus \(t\) exists uniquely, and the asserted formula and all equality magnitudes follow. For real-valued functions choose conjugate-paired phases, possible because \(\lambda_{N,-k}=\lambda_{N,k}\).

**2. The critical lattice sums.** Choose the symmetric representatives of \(G_N\) with each coordinate of size at most \(N/2\). Every nonminimal nonzero mode has \(\lambda_{N,k}\ge2\Lambda_N\): either both coordinates are nonzero or one has absolute value at least two, and \(\sin(2\pi/N)^2\ge2\sin(\pi/N)^2\) for \(N\ge4\). The elementary sine bounds show \(\lambda_{N,k}\ge16|k|^2\), so \(\lambda_{N,k}-\Lambda_N\ge8|k|^2\) on \(H_N\). Also
\[
\lambda_{N,k}=4\pi^2|k|^2+O(|k|^4/N^2),\qquad
\Lambda_N=4\pi^2+O(N^{-2}).
\]
Consequently, uniformly on \(H_N\),
\[
\left|\frac1{\lambda_{N,k}-\Lambda_N}-\frac1{4\pi^2|k|^2}\right|
\le C\bigl(|k|^{-4}+N^{-2}\bigr).
\]
The error sums to \(O(1)\). The elementary square-lattice annulus count gives \(\sum_{0<|k|\lesssim N}|k|^{-2}=2\pi\log N+O(1)\), proving \(S_N=(2\pi)^{-1}\log N+O(1)\). The bound \((\lambda_{N,k}-\Lambda_N)^{-2}\le(8|k|^2)^{-2}\), together with pointwise convergence for each fixed \(k\), proves the displayed limit \(T_N\to T_\infty\) by dominated convergence.

**3. Sharp two-scale estimate.** Normalize \(\|\widehat g\|_2=1\), and write \(q=\sum_{H_N}|\widehat g(k)|^2\). The four minimal modes contribute at most \(2\sqrt{1-q}\le2\) to the Fourier \(\ell^1\) norm. The spectral-gap-subtracted energy obeys
\[
\sum_{k\in H_N}(\lambda_{N,k}-\Lambda_N)|\widehat g(k)|^2\le\Delta_N.
\]
Weighted Cauchy–Schwarz gives \(\sum_{k\in H_N}|\widehat g(k)|\le\sqrt{\Delta_N S_N}\). This proves the upper bound. To obtain a matching lower bound, put Fourier magnitude \(\sqrt{\Delta_N/S_N}/(\lambda_{N,k}-\Lambda_N)\) on each \(k\in H_N\). Its total squared mass is \(q_0=\Delta_N T_N/S_N<1\) for all sufficiently large \(N\). Put the remaining mass equally on the four first modes. The constructed profile has *exactly* energy \(E\) and Fourier \(\ell^1\) norm \(\sqrt{\Delta_N S_N}+2\sqrt{1-q_0}\). The two-sided displayed inequality follows, with error \(O_E(1/\log N)\). Substituting the lattice asymptotics and \(\Lambda_N=4\pi^2+O(N^{-2})\) proves the main critical law, including its additive constant.

**4. Condensate and universal tail profile.** For fixed \(E>4\pi^2\), the exact finite-grid optimizer is in the interior regime for all large \(N\). Write the parameter as \(t_N=\Lambda_N-\varepsilon_N\), and set \(d_{N,k}=\lambda_{N,k}-\Lambda_N\),
\[
A_N(\varepsilon)=\sum_{H_N}(d_{N,k}+\varepsilon)^{-2},\qquad
B_N(\varepsilon)=\sum_{H_N}d_{N,k}(d_{N,k}+\varepsilon)^{-2}.
\]
The exact energy equation is
\[
\Delta_N=\frac{B_N(\varepsilon_N)}{4\varepsilon_N^{-2}+A_N(\varepsilon_N)}.
\]
For any fixed positive \(\varepsilon\), \(A_N(\varepsilon)=O(1)\) while \(B_N(\varepsilon)=S_N+O_\varepsilon(1)\to\infty\). Monotonicity from the finite-grid frontier therefore forces \(\varepsilon_N\to0\). Uniform domination and the inequality \(0\le S_N-B_N(\varepsilon)\le2\varepsilon T_N\) imply \(A_N(\varepsilon_N)\to T_\infty\), \(B_N(\varepsilon_N)=S_N+o(1)\), and \(4\varepsilon_N^{-2}\sim S_N/\Delta_N\). Consequently
\[
\varepsilon_N\sqrt{\log N}\to2\sqrt{2\pi(E-4\pi^2)},\qquad
Q_N=\frac{\Delta_N A_N(\varepsilon_N)}{B_N(\varepsilon_N)}
\sim\frac{(E-4\pi^2)T_\infty}{S_N}.
\]
Thus the limiting logarithmic mass law holds. Each of the four minimal modes has squared mass \((1-Q_N)/4\). Finally, after dividing the off-first-eigenspace probabilities by \(Q_N\), their weights are exactly \((d_{N,k}+\varepsilon_N)^{-2}/A_N(\varepsilon_N)\). They converge pointwise to \([4\pi^2(|k|^2-1)]^{-2}/T_\infty\), and the uniform summable \(O(|k|^{-4})\) envelope promotes this to \(\ell^1\) convergence.

## Verification

The standalone `check.py` calculates the exact eigenvalues, solves the one-variable energy equation by bisection, checks the two endpoint frontiers, and compares with randomly generated feasible Fourier-magnitude profiles. It also constructs both sides of the sharp two-scale inequality for multiple grid sizes. All supplementary assertions passed on the saved code. The proof above, not these finite tests, establishes the statements for all grid sizes and the limiting law.

## Relationship to prior work

Alberti, Housholder, Iosevich, Miller and Palsson (arXiv:2611.19755v1, publicly available 2026-11-15), Section 2.1, Proposition 2.1, establishes a discrete gradient-energy Fourier-ratio upper bound via weighted Cauchy–Schwarz, and Section 4.1, Theorem 4.3, gives order-sharp logarithmic critical behavior with reciprocal-eigenvalue examples on manifolds. Those results do not state the fixed relative-energy sharp finite-grid frontier, the sharp constant and additive four-mode term, or the conditional limiting tail distribution. The present result uses their natural Fourier-ratio functional and discrete-difference normalization.

Bartuccelli, Deane and Zelik (arXiv:1012.2061v1), Section 2, Theorem 2.3, find related resolvent extremizers on the *continuous* two-torus under a fixed pair of first- and second-derivative energies, with Fourier magnitudes proportional to \([|k|^2(1+\mu|k|^2)]^{-1}\). These are different constraints and a different spectral family; their theorem does not directly imply the present sharp finite-grid classification and fourfold low-mode condensation. The general Fourier-ratio recovery framework of Burstein, Iosevich and Nathan (arXiv:2601.16345v1) does not formulate this Dirichlet-energy optimization.

## Limitations

The strongest novelty comparison remains conditional on the inspected literature: an equivalent extremal formulation could exist in older Sobolev interpolation or graph spectral optimization literature. The exact formula here does not claim new random-sensor recovery thresholds. The fixed-energy large-grid law does not apply uniformly to varying budgets, and the limiting tail law addresses magnitudes only. No independent mathematical validation has been performed.

## References

1. N. Alberti, C. Housholder, A. Iosevich, S. J. Miller and E. A. Palsson, *Fourier Ratio Bounds and Sensitivity to Sensor Placement*, arXiv:2611.19755v1 (2026), https://arxiv.org/html/2611.19755v1 .
2. M. V. Bartuccelli, J. H. B. Deane and S. Zelik, *Asymptotic expansions and extremals for the critical Sobolev and Gagliardo–Nirenberg inequalities on a torus*, arXiv:1012.2061v1 (2010), https://arxiv.org/html/1012.2061v1 .
3. W. Burstein, A. Iosevich and H. S. Nathan, *The Fourier Ratio: A Unifying Measure of Complexity for Recovery, Localization, and Learning*, arXiv:2601.16345v1 (2026), https://arxiv.org/html/2601.16345v1 .
