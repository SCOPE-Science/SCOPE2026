# Sharp anisotropy and periodic-size laws for Crank–Nicolson positivity on honeycomb diffusion graphs

## Finding

Consider the infinite honeycomb graph with vertex sets \(A_{i,j},B_{i,j}\), \((i,j)\in\mathbb Z^2\), and edges \(A_{i,j}B_{i,j}\), \(A_{i,j}B_{i-1,j}\), \(A_{i,j}B_{i,j-1}\) of respective conductances \(a,b,c>0\). Let \(S=a+b+c\), let \(L_{a,b,c}\) be its weighted combinatorial Laplacian, and put
\[
C(s)=(I+sL_{a,b,c})^{-1}(I-sL_{a,b,c}),\qquad s\geq0.
\]
Entrywise nonnegativity of this bounded operator's kernel holds precisely for \(0\leq s\leq\sigma_\infty(a,b,c)\), where \(\sigma_\infty\) is the unique positive solution of \(g_\infty(s;a,b,c)=1/2\) and
\[
g_\infty(s;a,b,c)=\frac{1}{(2\pi)^2}\int_{-\pi}^{\pi}\int_{-\pi}^{\pi}
\frac{1+sS}{(1+sS)^2-s^2\lvert a+b e^{i\theta}+c e^{i\phi}\rvert^2}\,d\theta\,d\phi.
\]
For fixed \(S\), the sharp horizon \(\sigma_\infty\) is *strictly Schur-convex* in the three conductances: if one positive triple majorizes another and they are not permutations, its horizon is strictly larger. Consequently equal weights are the unique minimizer up to permutation. The sharp budget-normalized lower bound over all positive triples is
\[
\boxed{S\sigma_\infty(a,b,c)\geq 3\sigma_0,
\quad\sigma_0=0.41705524440007830387\ldots,}
\]
with equality exactly when \(a=b=c=S/3\). The value \(\sigma_0\) is the unique solution of the displayed integral with \(a=b=c=1\), and it is rigorously enclosed by
\[
0.41705524440007830<\sigma_0<0.41705524440007831.
\]
If \(a=S-\varepsilon\), \(b,c>0\), and \(b+c=\varepsilon\downarrow0\), the horizon diverges with the universal asymptotic law
\[
\boxed{\sigma_\infty(a,b,c)\sim\frac{1}{\sqrt{2S\varepsilon}},}
\]
uniformly in the split of the weak conductance between \(b\) and \(c\).

For the periodic quotient \(H_n\) obtained by reducing both cell indices modulo \(n\geq2\), the same update is entrywise nonnegative exactly for \(0\leq s\leq\sigma_n(a,b,c)\), with \(\sigma_n\) the unique root of
\[
g_n(s)=\frac1{n^2}\sum_{j,k=0}^{n-1}
\frac{1+sS}{(1+sS)^2-s^2\lvert a+b e^{2\pi i j/n}+c e^{2\pi i k/n}\rvert^2}=\frac12.
\]
For every positive triple and every finite \(n\geq2\),
\[
\sigma_n(a,b,c)>\sigma_\infty(a,b,c),\qquad
\sigma_n(a,b,c)\longrightarrow\sigma_\infty(a,b,c).
\]
More quantitatively, at each fixed \(s>0\), with \(q(s)=sS/(1+sS)\),
\[
0<g_n(s)-g_\infty(s)\leq q(s)^{2n},
\quad\sigma_n-\sigma_\infty=O\!\left(q(\sigma_\infty)^{2n}\right).
\]
In particular, **the sharp universal positivity condition for every periodic honeycomb size and every positive direction allocation of total conductance \(S\)** is
\[
\boxed{sS\leq1.25116573320023491161\ldots.}
\]
This boundary cannot be increased: larger products fail on sufficiently large isotropically weighted tori. Throughout, \(s\) is the *half-step* parameter; the corresponding physical time-step parameter is \(h=2s\).

## Assumptions and scope

The infinite vertex space is \(\ell^2(\mathbb Z^2\times\{A,B\})\). All three conductances are strictly positive; a coordinate direction is repeated uniformly throughout the graph. Each periodic quotient has \(2n^2\) vertices and the same three directional conductances. All nonnegativity claims concern **all matrix/kernel entries**, not spectral stability or local truncation error. The asymptotic near a matching keeps the total \(S>0\) fixed and makes the sum of the other two rates \(\varepsilon\) tend to zero, with no assumption on their ratio except positivity. Strict Schur-convexity is claimed for the infinite lattice, not for individual nonsymmetric finite quotients.

## Proof

1. **Resolvent reduction and exact Bloch formula.** Write \(R(s)=(I+sL)^{-1}\). The algebraic identity \(C(s)=2R(s)-I\) holds for \(s\geq0\). At \(s>0\), every off-diagonal entry of \(R\) is strictly positive: since \(L=S(I-P)\) for the nearest-neighbor stochastic transition operator \(P\), the uniformly convergent Neumann expansion
\[
R(s)=\frac1{1+sS}\sum_{m=0}^{\infty}\left(\frac{sS}{1+sS}\right)^m P^m
\]
contains a positive term joining any two vertices. The diagonal is constant by translation and sublattice-exchange symmetry. The two-sublattice Fourier symbol of \(I+sL\) has diagonal entries \(1+sS\) and off-diagonal entries \(-s(a+b e^{i\theta}+c e^{i\phi})\), up to complex conjugation. Its inverse therefore has diagonal entry \((1+sS)/[(1+sS)^2-s^2\lvert a+b e^{i\theta}+c e^{i\phi}\rvert^2]\), yielding the asserted integral and Fourier sum. Entrywise nonnegativity is equivalent to the single condition \(g(s)\geq1/2\).

2. **Unique horizon.** The resolvent return is continuous and strictly decreasing on positive \(s\):
\[
\frac{d}{ds}\langle e,R(s)e\rangle
=-\langle R(s)e,L R(s)e\rangle<0.
\]
It starts at \(g(0)=1\). For the infinite honeycomb, the Bloch eigenvalues are \(S\pm\lvert a+b e^{i\theta}+c e^{i\phi}\rvert\). The smaller eigenvalue vanishes only at a measure-zero set because \(a,b,c>0\); dominated convergence in the spectral integral gives \(g(s)\to0\). For finite connected quotients, \(g_n(s)\to1/(2n^2)<1/2\). Thus each root exists uniquely, and the stated intervals, including endpoints, are exact.

3. **Strict Schur-convexity.** Fix \(s>0\). For a nonzero real directional perturbation \(\delta=(\delta a,\delta b,\delta c)\) with \(\delta a+\delta b+\delta c=0\), differentiating the bounded resolvent twice yields
\[
\frac{d^2}{dt^2}\bigg\vert_{t=0}
\langle e,(I+sL_{(a,b,c)+t\delta})^{-1}e\rangle
=2s^2\langle L_\delta R(s)e,R(s)L_\delta R(s)e\rangle>0.
\]
For strictness, the Bloch transform of \(R(s)e_A\) has nonzero \(A\)-component \((1+sS)/D(\theta,\phi)\) at every Bloch angle; the \(B\)-component of \(L_\delta R(s)e_A\) contains its product with the nonzero trigonometric polynomial \(-\delta a-\delta b e^{-i\theta}-\delta c e^{-i\phi}\). This polynomial cannot vanish almost everywhere unless \(\delta=0\). Since the inverse resolvent is positive definite, the quadratic expression is strictly positive. The honeycomb automorphisms fixing a vertex permute its three edge directions arbitrarily, so the return function is symmetric in \(a,b,c\). Strict convexity on each fixed-sum plane plus symmetry implies strict Schur-convexity under nontrivial majorization. Comparing the unique roots transfers the strict order to \(\sigma_\infty\); averaging any triple over the six permutations proves the unique equal-weight minimum.

4. **Torus comparison and exponential bound.** A return walk on the infinite graph projects to a return walk on \(H_n\), preserving its probability weight. The converse fails for some positive-weight winding walks, hence \((P_{H_n}^{m})_{oo}\geq(P_{\infty}^{m})_{oo}\) for every \(m\), strictly for at least one \(m\). A winding return needs at least \(n\) two-step cell moves, hence at least \(2n\) original steps. Comparing the two Neumann expansions gives the strict bound \(0<g_n(s)-g_\infty(s)\leq q(s)^{2n}\). The roots are strictly ordered as asserted. Uniform convergence of returns and their first derivatives on compact positive \(s\)-intervals, followed by the mean-value theorem at the simple infinite root, gives the stated \(O(q(\sigma_\infty)^{2n})\) root error.

5. **Dimer-limit coefficient.** Set \(a=S-\varepsilon\) and retain the strong-weight perfect matching alone, with Laplacian \(L_a\) and resolvent \(R_a\). At one matching endpoint \(e_A\), the vector \(R_a e_A\) has values \(x=(1+sa)/(1+2sa)\) and \(y=sa/(1+2sa)\) on the matching pair, vanishing elsewhere. Hence its return is \(1/2+1/[2(1+2sa)]\). The weak-edge Laplacian \(L_w\) has norm at most \(2\varepsilon\), and
\[
\langle R_a e_A,L_w R_a e_A\rangle=\varepsilon(x^2+y^2)
=\frac{\varepsilon}{2}\left(1+\frac{1}{(1+2sa)^2}\right).
\]
The resolvent identity with \(s\varepsilon=o(1)\) gives a remainder \(O(s^2\varepsilon^2)\), uniformly over the split \(b+c=\varepsilon\). Substituting \(s=t/\sqrt{S\varepsilon}\) for fixed \(t>0\),
\[
g_\infty(s)-\frac12
=\sqrt{\frac{\varepsilon}{S}}\left(\frac{1}{4t}-\frac{t}{2}\right)+O(\varepsilon).
\]
The sign changes at \(t=1/\sqrt2\); strict monotonicity of the return traps its unique root between any two fixed constants on either side, proving the claimed equivalent.

6. **Exact isotropic scalar certificate.** At \(a=b=c=1\), let \(z=(s/(1+3s))^2\). Counting closed alternating walks gives
\[
g_\infty(s;1,1,1)=\frac{1}{1+3s}\sum_{m=0}^{\infty}A_m z^m,
\quad A_m=\sum_{j=0}^{m}\binom mj^2\binom{2(m-j)}{m-j}.
\]
All coefficients are nonnegative and \(A_m\leq9^m\). Truncation after index \(M\) has absolute tail at most \((9z)^{M+1}/[(1-9z)(1+3s)]\). Exact rational evaluation with \(M=45\) proves the displayed seventeen-decimal-place bracket. Since the minimum over fixed \(S\) is attained at equal rates and finite tori lie strictly above their infinite-cover threshold, the displayed universal bound and its sharpness follow.

## Verification

The standalone `verify.py` uses only Python 3 standard-library modules. Running `python3 verify.py` checks the exact-rational interval certificate, early lattice-walk moments, exact rational resolvent matrices of \(2n^2\)-vertex tori against independent Fourier sums, positivity of inverse entries, finite-size thresholds, strict majorization examples and weak-edge asymptotic samples. It reports 537 supplementary checks passed. These finite checks do not replace the arguments proving the statements for every size and every positive parameter triple.

The root bracket is an exact-rational inequality, not a floating-point confidence interval. Numerical quadrature estimates are reported only for orientation; the mathematical constant is defined by its unique integral root.

## Relationship to prior work

Faragó and Horváth (2006) establish general discrete nonnegativity criteria and a priori restrictions for parabolic theta schemes (Theorems 5.2 and 6.1–6.2), not a sharp anisotropic honeycomb allocation or torus-uniform frontier. Higueras and Roldán (2023) analyze the one-dimensional Dirichlet Crank–Nicolson problem. Marris, Sarvaharman and Giuggioli (2023) obtain honeycomb random-walk propagators and periodic-image representations for isotropic jumping; these entail related Green-function machinery but do not state the step-size or directional-majorization theorem. Gan, Ouvry and Polychronakos (2022) enumerate honeycomb closed walks and allow weighted hopping amplitudes in a magnetic Hamiltonian; the walk-moment technology is prior, not claimed here as a novel general technique. The general resolvent-return criterion and sharp degree-bound results are likewise existing inputs; the asserted contribution is the exact budget-normalized honeycomb optimum, strict anisotropy ordering, singular matching regime, and all-periodic-quotient comparison.

## Limitations

The claim does not address nonperiodic boundary conditions, variable weights within an edge class, non-honeycomb planar meshes, higher-order time integrators, approximation error, or arbitrary directed chains. A source could establish the same special consequences without using the term “Crank–Nicolson”; the literature comparison does not certify publication priority. Independent audit has not been performed. The proof of the infinite-lattice result is analytic; computational examples are only corroborative.

## References

- I. Faragó and R. Horváth, “Discrete Maximum Principle and Adequate Discretizations of Linear Parabolic Problems,” *SIAM Journal on Scientific Computing* 28 (2006), 2313–2336, DOI: https://doi.org/10.1137/050627241 (first public online 2006-12-21).
- I. Higueras and T. Roldán, “A new insight on positivity and contractivity of the Crank–Nicolson scheme for the heat equation,” arXiv:2301.01066 (first submitted 2023-01-03), https://arxiv.org/abs/2301.01066.
- D. Marris, S. Sarvaharman and L. Giuggioli, “Exact Spatio-Temporal Dynamics of Lattice Random Walks in Hexagonal and Honeycomb Domains,” arXiv:2305.08868 (first submitted 2023-05-11), https://arxiv.org/abs/2305.08868.
- L. Gan, S. Ouvry and A. P. Polychronakos, “Algebraic area enumeration of random walks on the honeycomb lattice,” arXiv:2107.10851 (first submitted 2021-07-22), https://arxiv.org/abs/2107.10851.
