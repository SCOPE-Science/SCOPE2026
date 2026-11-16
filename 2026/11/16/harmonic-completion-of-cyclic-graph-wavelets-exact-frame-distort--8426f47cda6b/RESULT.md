# Harmonic completion of cyclic graph wavelets: exact frame distortion and a quadratic Dirichlet obstruction

## Finding
Let \(n\geq3\), \(L=2n-2\), and embed the path \(P_n\) as the consecutive vertices \(B=\{0,\ldots,n-1\}\) of the unit cycle \(C_L\). This is an isometric graph-metric embedding. Let \(E_h:\mathbb C^n\to\mathbb C^L\) be the unique extension that agrees with the data on \(B\) and is graph-harmonic on \(I=C_L\setminus B\). Let \(\{\psi_\alpha\}\) be **any** Parseval frame of the cycle signal space, including a normalized cyclic-Fourier wavelet filter bank, and analyze path data with \(T s=(\langle E_hs,\psi_\alpha\rangle)_\alpha\).

The squared analysis singular spectrum, with multiplicities, is exactly
\[
\operatorname{spec}(T^*T)=\left\{1\ (n-2\text{ times}),\ \frac{n(n+1)}{6(n-1)},\ \frac n2\right\}.
\]
Thus the sharp path-data frame bounds are \(A=1\), \(B=n/2\), and their ratio is \(n/2\), independent of the particular Parseval bank. Perfect host reconstruction followed by restriction still reconstructs the path data exactly, but these coefficients are not a tight frame on the path.

For the Dirichlet solve that computes the completion, the entire spectrum and the exact spectral condition number are
\[
\operatorname{spec}(L_{II})=\left\{2-2\cos\frac{j\pi}{n-1}:1\leq j\leq n-2\right\},\qquad
\kappa_2(L_{II})=\cot^2\!\frac{\pi}{2(n-1)}\sim\frac{4(n-1)^2}{\pi^2}.
\]
The forcing associated with a unit impulse at either path endpoint has a nonzero component in **every** Dirichlet eigenmode. Conjugate gradients initialized at zero consequently takes exactly \(n-2\) iterations to reach the exact solution in exact arithmetic.

The condition-number obstruction persists for every fixed Cartesian dimension \(d\geq1\): the isometric inclusion of \(P_n^{\square d}\) into \(C_{2n-2}^{\square d}\) has occupancy fraction \((n/(2n-2))^d\geq2^{-d}\), yet its complementary grounded Dirichlet Laplacian has \(\kappa_2=\Theta_d(n^2)\), equivalently \(\Theta_d(N^{2/d})\) in the host vertex count \(N=(2n-2)^d\). This supplies an explicit counterexample, even with fixed dimension and occupancy bounded below, to the polylogarithmic-conditioning conjecture for such compact abelian hosts stated in Section 7 of Souop and Bitjoka (2026).

## Assumptions and scope
All graph Laplacians are the combinatorial unit-edge Laplacians; the inner product is ordinary counting-measure \(\ell^2\). The path includes all its \(n\) vertices, the host cycle has \(2n-2\) vertices, and the host frame is Parseval in this Hilbert norm. The first spectral formula applies to **every** Parseval host frame, not only Fourier wavelets. The higher-dimensional statement fixes \(d\) while letting \(n\to\infty\), and refers to the Laplacian on the entire host with the graph vertices grounded. The graph isometry is the usual shortest-path isometry in the Cartesian graph metric.

## Proof
**Isometry and extension.** Two embedded path sites are at cycle separation \(k\leq n-1=L/2\), hence the shorter cycle arc has length \(k\). Set \(m=n-1\). The missing vertices, in traversal order from the right endpoint toward the left, are \(m+j\), \(1\leq j\leq m-1\). The unique discrete-harmonic completion is the linear interpolant
\[
(E_hs)_{m+j}=\frac jm s_0+\left(1-\frac jm\right)s_m.
\]
It uniquely satisfies \(L_{II}(E_hs)_I=-L_{IB}s\), because the grounded path Laplacian is positive definite.

**Frame spectrum.** If \(W\) denotes analysis by the host Parseval family, then \(W^*W=I\) and \(T=WE_h\), so \(T^*T=E_h^*E_h\). The latter is the identity except for the two endpoint coordinates. With
\[
a=\sum_{j=1}^{m-1}\frac{j^2}{m^2}=\frac{(m-1)(2m-1)}{6m},\qquad
b=\sum_{j=1}^{m-1}\frac{j(m-j)}{m^2}=\frac{m^2-1}{6m},
\]
the endpoint block is \(\left(\begin{smallmatrix}1+a&b\\ b&1+a\end{smallmatrix}\right)\). Its symmetric and antisymmetric eigenvalues are \(1+a+b=n/2\) and \(1+a-b=n(n+1)/(6(n-1))\). The \(n-2\) interior coordinates have eigenvalue one. All displayed values lie between one and \(n/2\), proving the sharp bounds, including \(n=3\). In fact for **any** linear completion \(E=\binom{I}{F}\) into this cycle, \(E^*E=I+F^*F\). If it were scalar, \(F^*F=(c-1)I\); because \(F\) has only \(n-2<n\) rows, this forces \(c=1\) and \(F=0\). Thus zero-padding is the unique completion that makes the induced path frame tight, whereas harmonic completion minimizes Dirichlet energy.

**Perfect reconstruction without tightness.** Let \(R:\mathbb C^L\to\mathbb C^n\) restrict to \(B\). Although \(T^*T\ne I\), the host Parseval synthesis followed by restriction obeys \(RW^*Ts=RE_hs=s\). The synthesis \(RW^*\) is a left inverse, not generally the adjoint of \(T\). This distinguishes exact recovery from a Parseval identity for the graph-data norm.

**Grounded spectrum and iteration count.** The interior block \(L_{II}\) is the \((n-2)\)-by-\((n-2)\) tridiagonal matrix with diagonal two and adjacent entries minus one. The sine vectors \(u_j(k)=\sin(jk\pi/(n-1))\), \(1\leq k\leq n-2\), give the distinct eigenvalues displayed above. Their smallest and largest eigenvalues yield the cotangent condition number. A path endpoint impulse produces a right-hand side equal to a first or last coordinate vector on \(I\); its inner product with every sine vector is nonzero. The resulting Krylov space has full minimal-polynomial degree \(n-2\), so zero-initialized exact-arithmetic conjugate gradients cannot terminate sooner and does terminate in \(n-2\) steps.

**Higher-dimensional obstruction.** Write \(\Gamma=C_L^{\square d}\), \(B=\{0,\ldots,n-1\}^d\), \(I=\Gamma\setminus B\), and \(\varepsilon=|B|/|\Gamma|=(n/L)^d\). Both the graph isometry and occupancy claim follow coordinatewise. The full host Laplacian has spectral gap \(\lambda_{\rm gap}=4\sin^2(\pi/L)\). If \(u\) vanishes on \(B\), the Cauchy–Schwarz inequality gives \(\|u-\overline u\|_2^2\geq\varepsilon\|u\|_2^2\), so
\[
\lambda_{\min}(L_{II})\geq4\varepsilon\sin^2\frac{\pi}{L}.
\]
Conversely, the box \(J=\{n,\ldots,L-1\}^d\subset I\) supports the product of first Dirichlet sine modes, giving the Rayleigh bound
\[
\lambda_{\min}(L_{II})\leq2d\left(1-\cos\frac\pi{n-1}\right).
\]
A coordinate unit vector has Rayleigh quotient \(2d\), and the full host spectrum is contained in \([0,4d]\). Thus \(2d\leq\lambda_{\max}(L_{II})\leq4d\), whence explicitly
\[
\frac1{1-\cos(\pi/(n-1))}\leq \kappa_2(L_{II})\leq\frac d{\varepsilon\sin^2(\pi/L)}.
\]
For every fixed \(d\), these bounds establish \(\Theta_d(n^2)\), rather than any polylogarithmic bound in \(N=L^d\).

## Verification
The standalone program `verification/check.py` tests the harmonic normal equations, full path frame spectrum, cycle Fourier-Parseval normalization, full grounded spectrum, exact endpoint Gram identities using rational arithmetic, dimension-two/three grounded-eigenvalue bounds, and exact integer Krylov ranks. It passed 544 deterministic checks on the actual included program. The proof above establishes the statements for all \(n\) and each fixed \(d\); the finite tests are supplementary, not an exhaustive infinite certificate.

Run with Python 3 and the packages listed in `verification/requirements.txt`: `python verification/check.py`.

## Relationship to prior work
Souop and Bitjoka, arXiv:2607.14168v1 (July 15, 2026), prove host-Parseval wavelet analysis (Theorem 1), uniqueness of harmonic completion as a Dirichlet minimizer (Theorem 5), and use the path-into-cycle embedding and its Cartesian square in their image experiment (Section 8.3). Their Section 7 posits polylogarithmic grounded-solver conditioning on compact low-dimensional hosts with occupancy bounded below. None of those stated results gives the induced path-data frame spectrum or the quadratic counterfamily; the crucial distinction is between host tightness and the analysis norm of a nonisometric completion. The graph reconstruction statement remains correct because restriction after host synthesis is an oblique left inverse.

Ghandehari, Guillot and Hollingsworth, arXiv:2009.06058v2 (2021), develop general graph Gabor-type frame bounds on the graph itself, but do not examine this harmonic completion or derive this obstruction. Classical Dirichlet path eigenvalues and standard frame-operator identities are foundational tools here, not claimed as new. General oblique dual-frame theory predates this result. Related formulations may exist under equivalent discrete-boundary or frame-transfer terminology; no absolute uniqueness of the observation is asserted.

## Limitations
The exact frame spectrum uses this particular minimal cycle host and counting normalization. Other graph embeddings, weighting choices, and preconditioned solvers are not classified. The higher-dimensional result gives the sharp growth order, not sharp leading constants. The conjugate-gradient iteration statement concerns exact arithmetic and a specified zero initialization; it does not establish an analogous wall-clock lower bound at fixed numerical tolerance. The counterexample addresses the broad conjecture as worded with fixed low dimension and occupancy bounded below; adding further geometric constraints could lead to a different valid conjecture. Novelty assessment is relative to the inspected sources and searchable records, and independent external validation has not occurred.

## References
1. R. Fokam Souop and L. Bitjoka, *Tight Wavelet Frames on Graphs via Isometric Group Embedding*, arXiv:2607.14168v1, first submitted July 15, 2026, https://arxiv.org/html/2607.14168.
2. M. Ghandehari, D. Guillot and K. Hollingsworth, *Gabor-type frames for signal processing on graphs*, arXiv:2009.06058v2, https://arxiv.org/html/2009.06058v2.
3. O. Christensen and Y. C. Eldar, *Oblique dual frames and shift-invariant spaces*, Applied and Computational Harmonic Analysis 17 (2004), 48–68, https://doi.org/10.1016/j.acha.2003.12.003.
