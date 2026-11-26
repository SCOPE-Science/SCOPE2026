# A three-sector Walsh spectrum for harmonic star completion in a binary cube

## Finding
For each integer \(d\ge2\), let \(Q_d\) be the unweighted binary cube with vertices \(\mathbb F_2^d\), adjacent when exactly one coordinate differs. Identify the star \(K_{1,d}\) with the Hamming-radius-one subset \(B=\{0,e_1,\ldots,e_d\}\). Let \(H_d:\mathbb C^B\to\mathbb C^{\mathbb F_2^d}\) be the unique extension reproducing the input on \(B\) and harmonic at every vertex outside \(B\), for the combinatorial graph Laplacian. All Hilbert norms here are unweighted counting norms.

Define
\[
\Lambda_d=\frac{2^{d-2}(d-1)}{(2^{d-1}-1)^2}\sum_{k=1}^{d-1}\frac{\binom{d-1}{k}}{k},
\qquad U_d=\frac{2^d-1}{d}.
\]
The full spectrum of the positive frame operator \(H_d^*H_d\), including multiplicities, is
\[
\boxed{1\ \text{(once)},\quad \Lambda_d\ \text{(}\,d-1\,\text{ times)},\quad U_d\ \text{(once)}.}
\]
For \(d=2\), the first two spectral values coincide at \(1\). For every \(d\ge3\), they are strictly ordered as \(1<\Lambda_d<U_d\). In particular the optimal squared frame bounds are exactly \(1\) and \((2^d-1)/d\), and the singular-value condition number is \(\sqrt{(2^d-1)/d}\). The intermediate eigenvalue has the asymptotic law
\[
\Lambda_d=1+\frac1{d-1}+O(d^{-2})\quad(d\to\infty).
\]
The three invariant data subspaces are respectively the center-only signal, the zero-center leaf-contrast space \(\sum_{i=1}^d b_i=0\), and the zero-center equal-leaf space. This spectrum holds unchanged for the graph-analysis family obtained by first applying \(H_d\) and then **any** Parseval analysis map \(W\) on the host, since \((WH_d)^*(WH_d)=H_d^*H_d\).

## Assumptions and scope
For every \(d\ge2\), the ambient host is exactly \(Q_d\) with its unit-conductance nearest-neighbor edges; its size is \(2^d\). The star's center is the vertex \(0\) and its leaves are the standard basis vectors, with no additional boundary sites. This is the minimal-dimensional embedding among **Cartesian hypercube** hosts: distinct center-to-leaf edges require distinct cube coordinate directions. More compact embeddings exist in binary Cayley graphs with composite generating sets, which are outside this theorem. Harmonicity means
\[
d\,u(x)=\sum_{i=1}^d u(x+e_i)\quad\text{whenever }x\notin B.
\]
Because the cube is connected and \(B\ne\varnothing\), the grounded Laplacian on the complement is positive definite and \(H_d\) exists uniquely. The complex inner products are the standard unnormalized sums over vertices, both on the boundary and the host. The optional Parseval host map \(W\) can be the unitary Walsh transform or a full-translation normalized spectral-filter-bank analysis satisfying \(W^*W=I\). No claim is made for weighted cubes, alternative star embeddings, minimum-dimension hosts, or partially sampled host filters.

## Proof
**1. Decoupling and sharp extremal eigenvalues.** Every path in \(Q_d\) from \(x\ne0\) to \(0\) hits some \(e_i\) before reaching \(0\). Consequently the harmonic extension of center-only data \((a,0,\ldots,0)\) is \(a\mathbf 1_{\{0\}}\), orthogonal to all leaf-data extensions. For leaf data \(b=(b_i)\), the maximum principle gives nonnegative harmonic measures \(w_i(x)\), with \(\sum_iw_i(x)=1\), so
\[
(H_d(0,b))(x)=\sum_{i=1}^dw_i(x)b_i\quad(x\ne0).
\]
Coordinate-permutation symmetry implies
\[
\sum_{x\ne0}w_i(x)=\frac{2^d-1}{d}\quad\text{for every }i.
\]
Convexity of squared modulus now yields
\[
\|H_d(a,b)\|_2^2\le |a|^2+\frac{2^d-1}{d}\sum_{i=1}^d|b_i|^2
\le U_d\bigl(|a|^2+\|b\|_2^2\bigr).
\]
The reproduction identity \(H_d|_B=I\) gives the reverse lower frame inequality \(\|H_d(a,b)\|_2^2\ge|a|^2+\|b\|_2^2\). The center-only direction attains the lower bound. Constant leaf data with zero center extend to \(b\) on every nonzero host vertex and attain the upper bound. These give exact eigenvalues \(1\) and \(U_d\).

**2. The remaining invariant sector.** The leaf-to-leaf block of \(H_d^*H_d\) commutes with all coordinate permutations. Therefore it has one eigenvalue on the constant vector and one eigenvalue on the \((d-1)\)-dimensional subspace of leaf values summing to zero. The latter eigenvalue, \(\Lambda_d\), may be evaluated using boundary data \(b_1=1,b_2=-1,b_i=0\) for \(i\ge3\), with center value zero. Swapping the first two coordinates changes the extension's sign. Thus it is zero on the two slices where the first two coordinates agree, and is \(v(z)\) and \(-v(z)\) respectively on the other two slices, where \(z\in\mathbb F_2^{d-2}\). At \(z=0\), \(v(0)=1\). At every other \(z\), the \(d\)-neighbor harmonic equation becomes
\[
\bigl(2I+L_{Q_{d-2}}\bigr)v(z)=0,
\]
where \(L_{Q_{d-2}}\) is the unweighted cube Laplacian. With \(G=(2I+L_{Q_{d-2}})^{-1}\mathbf1_{\{0\}}\), the unique solution is \(v=G/G(0)\). The boundary signal has squared norm \(2\), and the host signal consists of two opposite copies of \(v\); hence
\[
\Lambda_d=\frac{\|G\|_2^2}{|G(0)|^2}.
\]
The \(d-2\) dimensional Walsh characters diagonalize \(L_{Q_{d-2}}\), with eigenvalues \(2j\) at multiplicity \(\binom{d-2}{j}\). Consequently, on writing \(n=d-2\),
\[
G(0)=\frac1{2^n}\sum_{j=0}^n\frac{\binom nj}{2(j+1)},\quad
\|G\|_2^2=\frac1{2^n}\sum_{j=0}^n\frac{\binom nj}{4(j+1)^2}.
\]
The identities
\[
\sum_{j=0}^n\frac{\binom nj}{j+1}=\frac{2^{n+1}-1}{n+1},\qquad
\sum_{j=0}^n\frac{\binom nj}{(j+1)^2}=\frac1{n+1}\sum_{k=1}^{n+1}\frac{\binom{n+1}k}{k}
\]
then yield the displayed exact formula for \(\Lambda_d\). For \(d=2\), the resolvent is one-dimensional and \(\Lambda_2=1\). For \(d\ge3\), positivity of the shifted-cube Green function at some \(z\ne0\) shows \(\Lambda_d>1\), while strict Jensen inequality on nonconstant leaf data gives \(\Lambda_d<U_d\). All eigenvalues and multiplicities are accounted for.

**3. Large-dimension asymptotics.** Put \(m=d-1\) and let \(K\) have the binomial distribution \(\mathrm{Bin}(m,1/2)\). An equivalent exact formula is
\[
\Lambda_d=\frac m2(1-2^{-m})^{-2}\,\mathbb E\!\left[\frac{\mathbf1_{\{K\ge1\}}}{K}\right].
\]
Expanding \(1/K\) on \(\{|K-m/2|\le m/4\}\) through its cubic term and using \(\mathbb E(K-m/2)=\mathbb E(K-m/2)^3=0\), \(\mathbb E(K-m/2)^2=m/4\), and \(\mathbb E(K-m/2)^4=O(m^2)\), gives
\[
\mathbb E\!\left[\frac{\mathbf1_{\{K\ge1\}}}{K}\right]=\frac2m+\frac2{m^2}+O(m^{-3}).
\]
The omitted binomial tail is exponentially small by a standard exponential-moment bound, proving the asymptotic formula.

**4. Reconstruction interpretation.** If \(R\) restricts a host signal to \(B\), then \(RH_d=I\). Hence for any Parseval host analysis \(W\), \(R W^*(WH_d)=I\) exactly, while the graph-analysis map \(WH_d\) is not itself Parseval for \(d\ge2\). This distinguishes exact reconstruction from tight graph analysis.

## Verification
The standalone `verify_hypercube.py` uses only Python's standard library and rational arithmetic. For each \(d=2,3,4,5,6\), it independently solves the full grounded Dirichlet system on the \(2^d-(d+1)\) complementary vertices, assembles all \((d+1)\times(d+1)\) Gram entries, and compares them exactly with the asserted three-sector spectrum and with the independent one-dimensional recurrence for the leaf-contrast sector. The direct exact values of \(\Lambda_d\) are \(1,10/9,58/49,824/675,3548/2883\). The same checker verifies that the harmonicity equations hold at every interior vertex for all pair-difference modes. These finite computations check the formulas in small dimensions; the proof above establishes all integer dimensions.

## Relationship to prior work
Fokam Souop and Bitjoka (2026, arXiv:2607.14168) construct Parseval spectral-filter-bank wavelets on group hosts and prove that harmonic completion uniquely minimizes host Dirichlet energy. They do **not** compute the all-dimension Gram spectrum of harmonic completion for the canonical coordinate star in a binary cube. Their small-star numerical experiment uses a more compact host. Their companion dissertation (arXiv:2606.29391) proves that the minimum binary embedding dimension of a star is much smaller than the naive coordinate embedding; the present result concerns this canonical, hypercube-dimension-minimal embedding and is not a claim about optimal embeddings among all binary Cayley hosts. The use of maximum principles, symmetry and Walsh diagonalization is standard; the exact combined three-sector constants, multiplicities and large-dimension contrast are the specific calculation here. The same general completion framework can yield related calculations on other graphs, so an unlocated prior special-case evaluation is a residual bibliographic risk.

## Limitations
The analysis concerns complex-valued boundary data, unweighted edges, the specific coordinate embedding, full host Parseval filters and the squared Hilbert norms defined above. It does not show failure of the host synthesis-followed-by-restriction reconstruction (which remains exact), nor condition numbers for a minimal star embedding, nor stability of numerical Dirichlet solvers. The asymptotic term for the repeated leaf-contrast eigenvalue is proved only in the stated limit; no uniform claim is made for other host geometries.

## References
- R. Fokam Souop and L. Bitjoka, *Tight Wavelet Frames on Graphs via Isometric Group Embedding*, arXiv:2607.14168, first posted July 15, 2026, https://arxiv.org/abs/2607.14168 . In particular, Theorems 1 and 5 and Section 8.2.
- R. Fokam Souop and L. Bitjoka, *Minimal Isometric Embeddings of Graphs into Abelian Groups: Theory, Algorithms, and Applications to Signal Processing over Networks*, arXiv:2606.29391, first posted June 28, 2026, https://arxiv.org/abs/2606.29391 . In particular, Theorem 2.37 and Chapters 5–6.
