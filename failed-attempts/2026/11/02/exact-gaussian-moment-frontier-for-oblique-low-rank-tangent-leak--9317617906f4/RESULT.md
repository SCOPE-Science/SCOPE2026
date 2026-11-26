# Exact Gaussian moment frontier for oblique low-rank tangent leakage

## Finding

Fix integers \(1\le r<\min(m,n)\), and let \(U\in\mathbb R^{m\times r}\), \(V\in\mathbb R^{n\times r}\) have orthonormal columns. Let \(Z\in\mathbb R^{m\times n}\) be a fixed, nonzero **normal residual** at the rank-\(r\) matrix \(Y=U\Sigma V^{\mathsf T}\):
\[
U^{\mathsf T}Z=0,\qquad ZV=0.
\]
Independently draw standard real Gaussian sketches \(\Theta\in\mathbb R^{\ell_L\times m}\), \(\Omega\in\mathbb R^{\ell_R\times n}\), with integers \(r\le\ell_L\le m\), \(r\le\ell_R\le n\). Define the one-sided oblique projectors
\[
H_L=U(\Theta U)^\dagger\Theta,\qquad H_R=V(\Omega V)^\dagger\Omega,
\]
and the two-sided oblique tangent projector, as in the sketch-Galerkin formulation of Carrel and Grigori,
\[
\mathcal P_{\rm obl}(B)=H_LB+BH_R^{\mathsf T}-H_LBH_R^{\mathsf T}.
\]
Its **spurious tangent leakage** of \(Z\) is \(E=\mathcal P_{\rm obl}(Z)\). The ordinary Euclidean tangent projector annihilates \(Z\).

**Theorem.** For every choice above, \(\Pr(E\ne0)=1\). For every real \(q>0\),
\[
\boxed{\quad\mathbb E\|E\|_F^q<\infty\quad\Longleftrightarrow\quad
q<\min\{\ell_L-r+1,\ell_R-r+1\}.\quad}
\]
In particular, the exact mean-square leakage is infinite if either sketch has at most one row beyond the rank. Otherwise, with
\[
\alpha=\frac r{\ell_L-r-1},\qquad \beta=\frac r{\ell_R-r-1},
\]
one has the dimension-free exact identity
\[
\boxed{\quad\mathbb E\|E\|_F^2=(\alpha+\beta+\alpha\beta)\|Z\|_F^2.\quad}
\]
For \(\ell_L,\ell_R\ge r+1\), the vector-valued mean exists and is \(\mathbb E E=0\), even at the infinite-variance boundary \(\ell_L=r+1\) or \(\ell_R=r+1\). The sketches and the fixed matrix \(Z\) are sampled independently; no adaptive dependence on the sketches is allowed.

For equal sketches of size \(\ell_L=\ell_R=2r\), the mean square is infinite at rank one. At every rank \(r\ge2\), its ratio to \(\|Z\|_F^2\) is exactly \((1+r/(r-1))^2-1\), which tends to \(3\) as the rank grows. At fixed \(r\), requiring \(\mathbb E\|E\|_F^2\le\varepsilon^2\|Z\|_F^2\) for equal sketches is equivalent to
\[
\ell\ge r+1+\frac{r}{\sqrt{1+\varepsilon^2}-1},
\]
subject to the integer and ambient-dimension constraints.

## Assumptions and scope

The matrices \(U,V,Z\) are deterministic or fixed before the independent Gaussian sketches are drawn. \(\Sigma\) is any invertible \(r\)-by-\(r\) matrix and affects the tangent space only through \(U,V\). Gaussian entries may have any common positive variance on each side, because each pseudo-inverse projector is invariant under scalar rescaling of its sketch. Both \(\Theta U\) and \(\Omega V\) have full column rank almost surely. The result describes a **single fixed-state projector evaluation in exact arithmetic**, not accumulated integration error along a sketch-dependent trajectory.

## Proof

Choose orthogonal completions \([U\ U_\perp]\) and \([V\ V_\perp]\). The normal-space assumptions give a unique nonzero \(C\in\mathbb R^{(m-r)\times(n-r)}\) with \(Z=U_\perp CV_\perp^{\mathsf T}\). By orthogonal invariance of Gaussian matrices, the pairs
\[
G=\Theta U,\quad K=\Theta U_\perp,\qquad
J=\Omega V,\quad M=\Omega V_\perp
\]
consist of independent standard Gaussian matrices of the indicated shapes (independently also between sides). Set \(A=G^\dagger K\) and \(B=J^\dagger M\). Relative to the orthogonal bases, \(H_L\) has block form \(\bigl(\begin{smallmatrix}I&A\\0&0\end{smallmatrix}\bigr)\) and \(H_R\) has the analogous form with \(B\). Thus
\[
[U\ U_\perp]^{\mathsf T}E[V\ V_\perp]=
\begin{pmatrix}-ACB^{\mathsf T}&AC\\CB^{\mathsf T}&0\end{pmatrix}.
\]
The three displayed nonzero blocks occupy mutually orthogonal Frobenius subspaces. Consequently, for every draw,
\[
\|E\|_F^2=\|AC\|_F^2+\|CB^{\mathsf T}\|_F^2+\|ACB^{\mathsf T}\|_F^2.\tag{1}
\]

We next establish the moment boundary rather than inferring it from finite simulations. For any nonzero fixed \(c\in\mathbb R^{m-r}\), \(Kc/\|c\|\) is an independent standard normal vector in \(\mathbb R^{\ell_L}\). Conditional on \(G\), the vector \(Ac/\|c\|=G^\dagger(Kc/\|c\|)\) is Gaussian with covariance \((G^{\mathsf T}G)^{-1}\). The Gram matrix has the \(r\)-dimensional Wishart law with \(\ell_L\) degrees of freedom. Integrating its density against this conditional Gaussian density (using the matrix determinant lemma) gives the exact radial density
\[
f(x)=\frac{\Gamma((r+\nu_L)/2)}{\pi^{r/2}\Gamma(\nu_L/2)}
(1+\|x\|_2^2)^{-(r+\nu_L)/2},\qquad
\nu_L=\ell_L-r+1.
\]
This is the unit-scale multivariate Student law. Its polar integral yields, for \(0<q<\nu_L\),
\[
\mathbb E\|Ac\|_2^q=\|c\|_2^q
\frac{\Gamma((r+q)/2)\Gamma((\nu_L-q)/2)}
{\Gamma(r/2)\Gamma(\nu_L/2)},
\]
while the same radial integral diverges for \(q\ge\nu_L\). The corresponding right-side law has \(\nu_R=\ell_R-r+1\). Since \(C\ne0\), it has a nonzero column \(c\) and a nonzero row \(d^{\mathsf T}\). Equation (1) then forces \(\mathbb E\|E\|_F^q=\infty\) whenever \(q\ge\nu_L\) or \(q\ge\nu_R\), and also proves \(\Pr(E\ne0)=1\).

Conversely, when \(0<q<\min\{\nu_L,\nu_R\}\), each of the finitely many entries of \(A\) and \(B\) has a finite absolute \(q\)-moment by the same Student law. Therefore \(\mathbb E\|A\|_F^q\) and \(\mathbb E\|B\|_F^q\) are finite. The two matrices are independent, so \(\mathbb E(\|A\|_F\|B\|_F)^q\) is also finite. The triangle inequality and \((x+y+z)^q\le\max\{1,3^{q-1}\}(x^q+y^q+z^q)\) then prove finiteness of \(\mathbb E\|E\|_F^q\) from (1). This establishes the if-and-only-if threshold.

When both \(\nu_L,\nu_R>2\), the usual inverse-Wishart expectation is
\[
\mathbb E(G^{\mathsf T}G)^{-1}=\frac{I_r}{\ell_L-r-1},\qquad
\mathbb E(J^{\mathsf T}J)^{-1}=\frac{I_r}{\ell_R-r-1}.
\]
Conditioning first on \(G\), the independent columns of \(K\) give \(\mathbb E[A^{\mathsf T}A]=\alpha I_{m-r}\). Similarly \(\mathbb E[B^{\mathsf T}B]=\beta I_{n-r}\). Independence of the sides then yields
\[
\mathbb E\|AC\|_F^2=\alpha\|C\|_F^2,\quad
\mathbb E\|CB^{\mathsf T}\|_F^2=\beta\|C\|_F^2,\quad
\mathbb E\|ACB^{\mathsf T}\|_F^2=\alpha\beta\|C\|_F^2.
\]
Equation (1), together with \(\|C\|_F=\|Z\|_F\), proves the exact second moment. At the boundary \(\nu=2\), the Student law still has finite first absolute moment and zero mean, so independence of the two sides gives \(\mathbb E E=0\) whenever both degrees exceed one. All corollaries follow by substitution and algebra. \(\square\)

## Verification

The standalone verifier `verification/check_gaussian_oblique.py` uses two genuinely different formulas: the full matrix pseudo-inverse projector and an orthogonal-block representation. It checked 210 independent Gaussian sketches across three matrix/rank regimes; compared the full projector to the orthogonal-block formula and checked the Frobenius identity (420 algebraic assertions); and checked gamma moments and large independent Monte Carlo means away from the heavy-tail boundary. The executed version passed 460 recorded assertions (420 algebraic, 4 simulation, 36 gamma-moment). These computations support the algebra and normalizations; the all-dimension moment classification follows from the analytic proof above, not from finite sampling. Run with `python verification/check_gaussian_oblique.py` (NumPy required).

## Relationship to prior work

Carrel and Grigori, arXiv:2607.03402v1, Lemma 4.2, define the oblique tangent projector, and Proposition 4.4 specifies when the sketched and classical Galerkin dynamics coincide. They identify the large perpendicular-residual mechanism but do not give the above Gaussian all-moment frontier or the exact two-sided mean-square leakage factor. Our analysis fixes a state and a normal residual independent of both sketches, a narrower probabilistic experiment than their sketch-dependent trajectories.

The inverse-Wishart identity and oversampling effects are classical. Kressner and Lam (2024), Theorem 9, derive an exact one-stage expected-error multiplier for a different generalized Nyström reconstruction, and Lam, Ceruti and Kressner (2025), Theorem 2, give moment bounds for a randomized low-rank Runge–Kutta construction. These results explain why Gaussian pseudo-inverse tails are plausible but do not, as stated, classify every moment of the present *two-sided tangent leakage* or yield formula (1). No assertion of definitive historical priority is made.

## Limitations

The result is pointwise and concerns an independent, fixed normal residual. It makes no statement about adaptively chosen bases, time-correlated sketches, error propagation through an integrator, or physical invariants over a trajectory. It concerns real Gaussian sketches and the specified canonical oblique lift; replacing Gaussian sketches by structured random embeddings or regularizing pseudo-inverses changes the laws. Exact finite-rank inverse-Wishart facts are established literature; the distinct claim here is their consequence for this specific two-sided tangent projector. An older equivalent specialized statement has not been ruled out independently.

## References

1. B. Carrel and L. Grigori, *Sketch low-rank dynamics: orthogonal vs. oblique projections*, arXiv:2607.03402v1, first posted 2026-07-03. https://arxiv.org/abs/2607.03402
2. D. Kressner and H. Y. Lam, *Randomized low-rank approximation of parameter-dependent matrices*, Numerical Linear Algebra with Applications 31 (2024), e2576, Theorems 8–9 and Lemma 2. https://doi.org/10.1002/nla.2576
3. H. Y. Lam, G. Ceruti and D. Kressner, *Randomized Low-Rank Runge–Kutta Methods*, SIAM Journal on Matrix Analysis and Applications 46 (2025), 1587–1615, Theorem 2. https://doi.org/10.1137/24M1692691
4. N. Halko, P.-G. Martinsson and J. A. Tropp, *Finding structure with randomness: probabilistic algorithms for constructing approximate matrix decompositions*, SIAM Review 53 (2011), 217–288, Gaussian pseudo-inverse moments. https://doi.org/10.1137/090771806
