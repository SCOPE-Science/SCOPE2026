# Sharp exponential conditioning gains from balanced endpoint sampling on finite paths

## Finding
For each integer \(m\ge2\), put \(N=2m\) and let \(P_N\) be the path with vertices \(0,1,\ldots,N-1\). Let \(S_N=D^{-1/2}AD^{-1/2}\) denote its symmetric normalized adjacency, where \(A\) is the unweighted adjacency and \(D\) the degree matrix. Observe a signal \(f\in\mathbb C^N\) under adjacency evolution in either of two equal-budget designs:
\[
W_N f=\bigl((S_N^t f)_0\bigr)_{t=0}^{N-1},\qquad
B_N f=\Bigl(\bigl((S_N^t f)_0\bigr)_{t=0}^{m-1},\ \bigl((S_N^t f)_{N-1}\bigr)_{t=0}^{m-1}\Bigr).
\]
Both are invertible \(N\times N\) linear measurement operators. Write \(\kappa_2(T)=\|T\|_{2\to2}\|T^{-1}\|_{2\to2}\). Their **exact exponential condition-number rates** are
\[
\boxed{\lim_{m\to\infty}\kappa_2(W_{2m})^{1/(2m)}=1+\sqrt2,\qquad
\lim_{m\to\infty}\kappa_2(B_{2m})^{1/(2m)}=\sqrt{1+\sqrt2}.}
\]
In particular,
\[
\boxed{\lim_{m\to\infty}\left(\frac{\kappa_2(W_{2m})}{\kappa_2(B_{2m})}\right)^{1/(2m)}=\sqrt{1+\sqrt2}.}
\]
Thus splitting the same \(N\) measurements between the two endpoints halves the *logarithmic exponential conditioning rate*. This is not a claim about arbitrary sensor placements or evolution filters.

There are exact reconstruction formulas. Define the ordinary first-kind Chebyshev polynomials by \(T_0(z)=1\), \(T_1(z)=z\), and \(T_{j+1}(z)=2zT_j(z)-T_{j-1}(z)\). Write \(T_j(z)=\sum_{t=0}^j a_{j,t}z^t\). If the two blocks of \(B_N f\) are denoted by \(y^L_t,y^R_t\), then for every \(0\le j<m\),
\[
\boxed{f_j=c_j\sum_{t=0}^j a_{j,t}y^L_t,\qquad
f_{N-1-j}=c_j\sum_{t=0}^j a_{j,t}y^R_t,\quad c_0=1,\ c_j=\sqrt2\ (j\ge1).}
\]
The corresponding one-end formula is \(f_j=c'_j\sum_{t=0}^ja_{j,t}(W_Nf)_t\), with \(c'_0=c'_{N-1}=1\) and \(c'_j=\sqrt2\) for \(1\le j\le N-2\). The balanced two-end matrix also has the finite-degree exact determinant
\[
\boxed{|\det B_{2m}|=2^{-(m-1)^2}.}
\]
For context, the previously established single-end identity is \(|\det W_N|=2^{-N(N-2)/2}\). That earlier identity is not claimed as a new contribution here.

## Assumptions and scope
The graph is precisely the unweighted even path, there are no self-loops, and the dynamics is **the normalized adjacency itself**, not normalized heat flow. Measurements start at time zero, are taken at every consecutive integer time, and are unweighted. The full signal space is \(\mathbb C^{2m}\) (no low-pass restriction); the norm and condition numbers use ordinary Euclidean norms for both the signal and the complete measurement vector. The two designs use the same total number of scalar samples but different spatial and temporal allocations. "Sharp exponential" refers only to the limits of the \(N\)-th roots, not to multiplicative prefactors or finite-size optimality against all possible designs.

## Proof
**1. Chebyshev propagation.** Write \(e_j\) for the standard coordinate vectors. The normalized path has edge weight \(2^{-1/2}\) at each endpoint edge and \(1/2\) at every interior edge. Direct use of the three-term recurrence and these edge weights gives
\[
T_0(S_N)e_0=e_0,\qquad
T_j(S_N)e_0=2^{-1/2}e_j\quad(1\le j\le N-2),\qquad
T_{N-1}(S_N)e_0=e_{N-1}.
\]
The induction starts with \(S_Ne_0=2^{-1/2}e_1\). In the first recurrence step the \(e_0\) term cancels, at each subsequent interior step the \(e_{j-1}\) term cancels, and in the last step the weight \(2^{-1/2}\) at the far endpoint gives the final coefficient \(1\). Reflection of the path gives the analogous identities starting at \(e_{N-1}\). These are exact finite-matrix identities, including the endpoint normalization.

Since \(S_N\) is self-adjoint, taking inner products with \(f\) and expanding each \(T_j\) into powers of \(S_N\) proves all displayed reconstruction formulas. It follows in particular that \(W_N\) is invertible. For \(B_N\), finite propagation gives \((S_N^t)_{0,j}=0\) for \(j>t\), and \((S_N^t)_{N-1,j}=0\) for \(N-1-j>t\). Since \(t<m\), the left measurements see only vertices \(0,\ldots,m-1\) and the right measurements see only vertices \(m,\ldots,2m-1\). After reflecting the last \(m\) coordinates, \(B_N\) is a direct sum of two identical triangular \(m\times m\) matrices \(C_m\), and the Chebyshev reconstruction formulas give \(C_m^{-1}\) row by row.

**2. Exact determinant.** The diagonal entry of \(C_m\) at time \(t\) is \((S_N^t)_{0,t}\). It equals \(1\) for \(t=0\) and \(2^{-(t-1/2)}\) for \(1\le t\le m-1\), the product of weights along the unique shortest path from \(0\) to \(t\). Hence
\[
|\det C_m|=\prod_{t=1}^{m-1}2^{-(t-1/2)}=2^{-(m-1)^2/2},
\]
and the two-block formula yields \(|\det B_N|=2^{-(m-1)^2}\). The same shortest-path computation, including the final right-end weight, gives the previously known one-end determinant.

**3. Coefficient growth.** Put \(\rho=1+\sqrt2\) and let \(a_j=(a_{j,0},\ldots,a_{j,j})\) be the monomial coefficient vector of \(T_j\). The exact Chebyshev identity
\[
T_j(z)=\frac{w^j+w^{-j}}2,\qquad w+w^{-1}=2z
\]
holds for either inverse-paired choice of \(w\). For \(|z|=1\), select \(|w|\ge1\). The reverse triangle inequality gives \(|w|-|w|^{-1}\le2\), hence \(|w|\le\rho\), so \(\max_{|z|=1}|T_j(z)|\le\rho^j\). Parseval on the unit circle gives \(\|a_j\|_2\le\rho^j\). At \(z=i\) the choice \(w=i\rho\) gives \(|T_j(i)|\ge(\rho^j-\rho^{-j})/2\), while Cauchy--Schwarz gives \(|T_j(i)|\le\sqrt{j+1}\,\|a_j\|_2\). Thus the explicit two-sided estimate
\[
\boxed{\frac{\rho^j-\rho^{-j}}{2\sqrt{j+1}}\le\|a_j\|_2\le\rho^j}\qquad(j\ge0)
\]
proves \(\lim_{j\to\infty}\|a_j\|_2^{1/j}=\rho\). The upper estimate and this coefficient growth are classical in the theory of polynomial basis conversion; the new assertion concerns their effect on the two *specified graph observation designs*.

**4. Sharp operator rates.** Each measurement row has norm at most \(1\), because \(\|S_N\|_{2\to2}=1\); a time-zero row has norm exactly \(1\). Consequently
\[
1\le\|W_N\|_{2\to2}\le\sqrt N,\qquad 1\le\|C_m\|_{2\to2}\le\sqrt m.
\]
The explicit inverse rows in Step 1, the coefficient bounds in Step 3, and the fact that the operator norm dominates every row norm and is bounded by the Frobenius norm imply
\[
\frac{\rho^{N-1}-\rho^{-(N-1)}}{2\sqrt N}\le\|W_N^{-1}\|_{2\to2}\le\sqrt{2N}\,\rho^{N-1},
\]
and
\[
\frac{\sqrt2(\rho^{m-1}-\rho^{-(m-1)})}{2\sqrt m}\le\|C_m^{-1}\|_{2\to2}\le\sqrt{2m}\,\rho^{m-1}.
\]
The two-end operator is unitarily equivalent (by coordinate permutations) to \(C_m\oplus C_m\), so \(\kappa_2(B_N)=\kappa_2(C_m)\). Taking \(N\)-th roots for \(W_N\), and \(m\)-th roots for \(C_m\), removes all polynomial factors and proves \(\rho\) in both respective dimensions. With \(N=2m\), the second rate becomes \(\sqrt\rho\) per original vertex. Dividing the positive condition numbers establishes the ratio limit. This completes the all-dimensional proof.

## Verification
Run `python CHECK.py` with Python 3, using only the standard library. It constructs normalized adjacency matrices for the even paths of lengths \(4,6,\ldots,16\), builds both observation matrices and their candidate Chebyshev inverses, and checks all entries of their products against the identity. It checks strict disjointness of the two endpoint observation supports, both determinant identities through their triangular diagonals, and the Chebyshev coefficient bounds. The executed checker reported `PATH_DOUBLE_ENDPOINT_CHEB_CHECKS_PASSED 2107`. These finite computations corroborate the exact constructions; the two limits for all \(m\) come from Steps 1–4, not from extrapolating the numerical experiments.

## Relationship to prior work
Bulai, Cabrelli, Cordero, Molter, and Saliani (arXiv:2609.25472v1, submitted September 21, 2026), Section 4.3, compare path-graph dynamical frames from one endpoint, both endpoints, and distributed sensors; their chosen evolution is heat-type and their experiments use a six-dimensional low-pass space on a 40-vertex path. Their general rank and frame formulation does not supply the present **full-band normalized-adjacency Chebyshev inversion** or either sharp growing-path condition-number base. The public result *Universal endpoint optimality for dynamical sampling on normalized paths* (October 11, 2026) proves the exact one-vertex Gram determinant and a vertex-placement theorem for full consecutive-time sampling; that determinant and its proof are acknowledged as existing and do not imply the present two-end smallest-singular-value asymptotic. Classical Chebyshev-to-monomial coefficient amplification (also discussed in older numerical-polynomial literature) explains the silver-ratio base at the coefficient level, but does not itself state this balanced two-sensor graph sampling comparison.

## Limitations
No assertion is made about sparse-band signals, general graph dynamics, Gaussian measurements, an optimal choice among arbitrary sensors, finite-size optimality of the two-end design, or a sharp polynomial prefactor multiplying the exponential condition number. The rate is for singular-value condition numbers; the corresponding frame-*Gram* condition numbers are their squares. The exponent may be derivable by combining older basis-conversion estimates with the Chebyshev path identity, so independent checking of older spectral-control and numerical-analysis literature remains a publication-priority risk.

## References
1. I. M. Bulai, C. Cabrelli, E. Cordero, U. Molter, and S. Saliani, *Dynamical Sampling in Graph Paley–Wiener Spaces*, arXiv:2609.25472v1 (2026-09-21), https://arxiv.org/html/2609.25472v1. Section 4.3 describes path sensor experiments and general frame formulae.
2. *Universal endpoint optimality for dynamical sampling on normalized paths*, public published-finding corpus mathematical record (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-universal-endpoint-optimality-for-dynamical-sampling-on-normaliz--d0ca7333cb0f. Its one-end determinant is explicitly credited.
3. Classical Chebyshev polynomial recurrence and coefficient basis-conversion estimates; see e.g. *Numerical experiments on the accuracy of the Chebyshev–Frobenius companion matrix method for finding the zeros of a truncated series of Chebyshev polynomials*, J. Comput. Appl. Math. (2007), https://doi.org/10.1016/j.cam.2006.05.006.
