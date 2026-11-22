# Three equiangular quartic-harmonic embeddings and the complete type-\(A\) root sampling spectrum

## Finding
For each integer \(n\ge4\), let \(V_n=\{x\in\mathbb R^n:\sum_{i=1}^n x_i=0\}\) with its Euclidean metric, and set
\[
X_n=\left\{r_{ij}=\frac{e_i-e_j}{\sqrt2}:1\le i<j\le n\right\}\subset S(V_n)\cong S^{n-2}.
\]
There are \(N=\binom n2\) points, one from each antipodal pair of type-\(A_{n-1}\) roots. Let \(\mathcal H_4\) be the complex space of restrictions of degree-four homogeneous harmonic polynomials on \(V_n\), equipped with normalized spherical-probability \(L^2\) inner product, and let \(h_n=\dim\mathcal H_4\). Define \(E_n:\mathcal H_4\to\mathbb C^N\) by \((E_nf)_{ij}=h_n^{-1/2}f(r_{ij})\).

The entire squared singular-value spectrum of \(E_n\), equivalently the spectrum of \(G_n=E_nE_n^*\), is
\[
\begin{array}{c|c}
\text{value}&\text{multiplicity}\\\hline
\displaystyle\lambda_0(n)=\frac{(n-3)(n+3)}{8n}&1\\[4pt]
\displaystyle\lambda_1(n)=\frac{(n+1)(n^2-9n+36)}{16n(n-2)}&n-1\\[4pt]
\displaystyle\lambda_2(n)=\frac{(n+1)(7n-3)}{8n(n-2)}&\displaystyle\frac{n(n-3)}2.
\end{array}
\]
All are positive, so every prescribed set of \(N\) complex data values is interpolated by a quartic harmonic. The exact least eigenvalue lies in the constant-edge sector at \(n=4\), in the constant and standard sectors jointly at \(n=5\), in the standard sector for \(6\le n\le20\), in the standard and two-row sectors jointly at \(n=21\), and in the two-row sector for \(n\ge22\). In particular, the sharp bound uniform over \(n\ge4\) is \(\lambda_{\min}\ge7/32\), with equality exactly at \(n=4\); restricted to \(n\ge5\), the sharp lower bound is \(11/35\), attained exactly at \(n=7\).

Write \(k_{ij}\) for the unit-norm degree-four reproducing-kernel vector at \(r_{ij}\). The \(N\) kernel **lines are equiangular**, meaning \(|\langle k_{ij},k_{pq}\rangle|\) is constant over distinct pairs, **if and only if** \(n\in\{5,15,21\}\). Their respective cardinalities and absolute correlations are \((10,1/5)\), \((105,1/65)\) and \((210,1/133)\). The final case has the stronger property that all distinct inner products are \(+1/133\), and hence
\[
G_{21}=\frac{132}{133}I_{210}+\frac1{133}J_{210}.
\]
Thus the large eigenvalue is \(18/7\) (multiplicity one) and the other eigenvalue \(132/133\) has multiplicity \(209\).

## Assumptions and scope
The sphere has intrinsic dimension \(n-2\), but ambient Euclidean dimension \(D=n-1\); Gegenbauer normalization and the number of harmonics use \(D\). The positive roots are just one chosen representative from each antipodal pair. The diagonal of \(G_n\) is exactly one, not the harmonic-space dimension. The sampling statement is *surjectivity onto* \(\mathbb C^N\), not injectivity on all of \(\mathcal H_4\). Every theorem quantifier is over integers \(n\ge4\) and distinct unordered edge pairs, with no asymptotic or genericity assumption.

## Proof
**1. Zonal harmonic and exact Gram entries.** For \(D=n-1\), the unique normalized degree-four zonal kernel is
\[
P_{n,4}(t)=\frac{(n+1)(n+3)t^4-6(n+1)t^2+3}{n(n-2)},\qquad P_{n,4}(1)=1.
\]
This follows by applying the Euclidean Laplacian to
\[
(x\cdot y)^4-\frac6{D+4}|x|^2(x\cdot y)^2+\frac3{(D+2)(D+4)}|x|^4
\]
for each unit \(y\), verifying it is harmonic, then normalizing at \(x=y\). The spherical addition theorem gives \(G_n=(P_{n,4}(\langle r_{ij},r_{pq}\rangle))\), because \(E_n\) includes the factor \(h_n^{-1/2}\). Any distinct root representatives have inner product \(0\) (disjoint edges) or \(\pm1/2\) (incident edges). Since \(P_{n,4}\) is even, putting
\[
a_n=P_{n,4}(1/2)=\frac{n^2-20n+27}{16n(n-2)},\quad b_n=P_{n,4}(0)=\frac3{n(n-2)},
\]
and letting \(A_n\) be the Johnson graph adjacency matrix on the two-subsets of \(\{1,\ldots,n\}\), gives
\[
G_n=(1-b_n)I+(a_n-b_n)A_n+b_nJ.
\]

**2. All eigenvalues, multiplicities and rank.** The unsigned vertex-edge incidence matrix \(C\) of the complete graph obeys \(C^TC=2I+A_n\) and \(CC^T=(n-2)I+J_n\). Consequently the \(A_n\) eigenvalues are \(2(n-2)\), \(n-4\) and \(-2\), on the constant, standard and orthogonal two-row subspaces, respectively, of dimensions \(1\), \(n-1\), and \(N-n=n(n-3)/2\). Substitution into the matrix identity and exact simplification gives precisely the three displayed rational functions. Positivity follows from \(n>3\), \(7n-3>0\), and \(n^2-9n+36=(n-9/2)^2+63/4>0\). Therefore \(G_n\) is invertible for all \(n\ge4\). For any desired edge data \(y\), the explicit interpolant
\[
f_y(x)=\sum_{i<j}(G_n^{-1}y)_{ij}\,P_{n,4}(\langle x,r_{ij}\rangle)
\]
is a degree-four spherical harmonic with \(f_y(r_{ij})=y_{ij}\). The full root orbit carries antipodally symmetric degree-four data, so the representative formulation loses no independent sample constraints.

**3. Sharp smallest-eigenvalue sector and global lower bound.** Direct subtraction gives
\[
\lambda_0-\lambda_1=\frac{(n-5)(n+9)}{16(n-2)},\quad
\lambda_1-\lambda_2=\frac{(n-21)(n+1)}{16n},\quad
\lambda_0-\lambda_2=\frac{(n-1)(n^2-8n-21)}{8n(n-2)}.
\]
These identities prove every sector ordering and every stated sector crossover, including the isolated ties at \(n=5\) and \(n=21\). The first expression puts \(\lambda_0\) lowest only at \(n=4\), tied at \(n=5\), and strictly above \(\lambda_1\) afterwards; the second puts \(\lambda_1\) below \(\lambda_2\) until \(n=21\), then above it. For the dimension-uniform assertions, \(\lambda_0\) increases on \(n\ge4\) and its first value is \(7/32\). The branch \(\lambda_2\) strictly decreases with \(n>2\) to \(7/8\). Finally
\[
\lambda_1(n+1)-\lambda_1(n)=\frac{n^4-2n^3-16n^2-85n+36}{16n(n-2)(n-1)(n+1)}.
\]
Its numerator is negative at integers \(n=5,6\), positive at \(n=7\), and strictly increasing for all real \(n\ge7\) (by two derivatives). Thus \(\lambda_1\) is minimized over integers \(n\ge5\) uniquely at \(n=7\), where it is \(11/35\). The preceding branch ordering completes both sharp uniform bounds.

**4. Exactly three equiangular harmonic embeddings.** The unit reproducing kernels have mutual inner products \(P_{n,4}(\langle r_e,r_f\rangle)\). For every \(n\ge4\), both incident and disjoint pairs exist, so equiangularity is equivalent to \(|a_n|=|b_n|\), since \(b_n>0\). Exact factorization yields
\[
a_n-b_n=\frac{(n-21)(n+1)}{16n(n-2)},\qquad
a_n+b_n=\frac{(n-5)(n-15)}{16n(n-2)}.
\]
The only admissible roots are \(n=5,15,21\). Direct substitution gives correlations \(1/5,1/65,1/133\). At \(n=21\), \(a_n=b_n=1/133\), so every off-diagonal entry of \(G_{21}\) equals \(1/133\); the rank-one formula and multiplicities follow. Positivity above ensures the kernel lines are distinct and nonzero.

## Verification
Run `python3 check_quartic_A.py` from the same directory as this document. It uses only the Python standard library and checks the independent Gegenbauer recurrence against the harmonic-projection polynomial at five rational arguments for all \(4\le n\le25\). It constructs full exact rational Gram matrices for \(4\le n\le12\), verifies their actions on constant, vertex-star-difference and four-cycle test vectors, and checks multiplicity-weighted trace and positivity for \(4\le n\le25\). It also checks all three exceptional equiangular dimensions and the exact \(n=21\) coalescence. It exits with `QUARTIC_A_EXACT_CHECK_OK` if all checks pass. The proof's universal statements rest on the symbolic identities in the previous sections, not on this finite sweep.

## Relationship to prior work
Spherical-harmonic addition formulas, Johnson graph eigenspaces and harmonic-index design theory are classical; they are inputs, not claimed innovations. Zandieh–Han–Avron (arXiv:2202.12995, first available 2022-02-25) study robust sampling of spherical-harmonic expansions using approximately optimal sample counts but do not classify this deterministic root orbit. Mohammadpour–Waldron (arXiv:2308.02499, first available 2023-07-21) study complex spherical designs from group orbits, not the explicit real quartic-edge Gram spectrum. Previously published type-\(A_4\) and type-\(A_5\) root sampling classifications cover individual ranks, and published cubic/quintic simplex-root results cover the indicated odd degrees for all ranks; neither statement implies the all-rank degree-four spectrum, the three equiangular dimensions, or the dimension-21 multiplicity-209 collapse. A type-\(D\) quartic-root spectrum uses a different configuration and adjacency scheme. The relevant general Johnson and Gegenbauer formulas permit a new direct calculation here; no priority is claimed for those tools themselves.

## Limitations
This is a finite-degree quartic statement on the positive roots of the \(A_{n-1}\) system; it does not claim an optimal packing, a spherical design of arbitrary strength, or injective recovery of every harmonic coefficient. The equiangular property concerns kernel vectors in the high-dimensional quartic harmonic space, not the original root vectors. The novelty comparison is bounded by inspected indexed literature and published related records; an earlier equivalent association-scheme computation or table may exist. No independent mathematical audit has been performed.

## References
1. A. Zandieh, I. Han, H. Avron, *Near Optimal Reconstruction of Spherical Harmonic Expansions*, arXiv:2202.12995, public 2022-02-25, https://arxiv.org/abs/2202.12995.
2. M. Mohammadpour, S. Waldron, *Complex spherical designs from group orbits*, arXiv:2308.02499, public 2023-07-21, https://arxiv.org/abs/2308.02499.
3. E. Bannai, T. Okuda, M. Tagami, *Spherical designs of harmonic index t*, arXiv:1308.5101, https://arxiv.org/abs/1308.5101 (background only).
4. Y. Zhu, E. Bannai, E. Bannai, K.-T. Kim, W.-H. Yu, *More on spherical designs of harmonic index t*, arXiv:1507.05373, https://arxiv.org/abs/1507.05373 (background only).
5. M. Krebs, A. Shaheen, *On the spectra of Johnson graphs*, Electronic Journal of Linear Algebra 17 (2008), https://doi.org/10.13001/1081-3810.1256 (classical graph-spectrum background).
