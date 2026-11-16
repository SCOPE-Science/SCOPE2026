# Complete Walsh spectrum and sharp range-projection norm for Petersen spanning trees

## Finding

Let \(P=KG(5,2)\) be the Petersen graph, with vertices the ten unordered pairs from \(\{0,1,2,3,4\}\) and edges between disjoint pairs. Order the 15 graph edges lexicographically by their endpoint indices, and set \(G=\mathbb F_2^{15}\). Let \(\mathcal T\subseteq G\) be the set of incidence vectors of spanning trees of \(P\), let \(f=\mathbf1_{\mathcal T}\), and use **unnormalized** Walsh coefficients
\[
W(s)=\sum_{t\in\mathcal T}(-1)^{\langle s,t\rangle},\qquad s\in G.
\]
For the counting-convolution operator \(C_f:h\mapsto f*h\) on real or complex functions on \(G\), the complete **absolute** multiplier distribution is:

| \(|W(s)|\) | number of frequencies |
| ---: | ---: |
| 0 | 13912 |
| 16 | 11710 |
| 48 | 1140 |
| 64 | 4160 |
| 80 | 914 |
| 112 | 120 |
| 128 | 240 |
| 144 | 360 |
| 240 | 60 |
| 256 | 120 |
| 400 | 30 |
| 2000 | 2 |

In particular, the Fourier rank of \(C_f\) is exactly \(18856\), its nullity is \(13912\), the greatest common divisor of its integer multipliers and the smallest positive multiplier magnitude are both \(16\), its largest magnitude is \(2000\), and its recoverable-space condition number is \(125\). The Hilbert-space Moore–Penrose inverse norm is \(1/16\).

Let \(E=\operatorname{ran}C_f\). Among **all** real linear projections of \(\ell^1(G)\) onto \(E\), and independently among all real linear projections of \(\ell^\infty(G)\) onto \(E\), the exact minimum norm is
\[
\boxed{\Lambda_1(E)=\Lambda_\infty(E)=\frac{36651}{1024}.}
\]
The corresponding complex-space minima have the same value. The translation-invariant spectral projection attains all four minima.

## Assumptions and scope

The graph is the single labelled Petersen graph \(KG(5,2)\), with no loops, parallel edges, variable edge weights or other graph orders. Its 15 edges are identified with the ordered coordinates described above. The Fourier normalization is \(\widehat f(s)=\sum_x f(x)(-1)^{\langle s,x\rangle}\). Convolution is unnormalized counting convolution \((f*h)(x)=\sum_y f(y)h(x+y)\), while inverse Walsh transform includes \(2^{-15}\). The range is a subspace of all \(2^{15}\)-coordinate functions, not the span of individual spanning-tree characters. All numerical assertions concern this exact finite domain.

## Proof

**Tree indicator.** A spanning tree is a connected, acyclic, nine-edge subset of the Petersen graph. Enumerate all \(\binom{15}{9}=5005\) candidate subsets and reject those creating a cycle by union–find. Exactly 2000 remain. Independently, \(P\) is strongly regular with adjacency eigenvalues \(3\) (once), \(1\) (five times), and \(-2\) (four times), hence the ordinary Matrix-Tree Theorem gives \(2^5 5^4/10=2000\) spanning trees.

**Fourier coefficients.** The unnormalized Walsh transform of the tree indicator is precisely \(W\). The 15-stage butterfly recursion sends each pair \((a,b)\) to \((a+b,a-b)\), uses only integers, and evaluates all \(2^{15}=32768\) characters. The attached `certificates/petersen_absolute_spectrum.csv` records the resulting complete histogram; its counts sum to 32768. As a genuinely different check, for each signing \(\sigma_e=(-1)^{s_e}\), form the nine-by-nine reduced matrix from the **weighted** Laplacian
\[
L_\sigma=\sum_{e=uv}\sigma_e(\mathbf e_u-\mathbf e_v)(\mathbf e_u-\mathbf e_v)^\mathsf T.
\]
The weighted Matrix-Tree Theorem gives \(W(s)=\det L_\sigma^{[9]}\), where the last row and column are removed. Exact integer fraction-free Bareiss elimination agrees with the butterfly values at **all 32768 signings**. In particular the histogram is exhaustive, not a sample or floating-point approximation. Both \(\sum_s W(s)^2=2^{15}\cdot2000\) and \(W(0)=2000\) are checked. For additional compression, all \(120\) permutations of the underlying five points induce graph automorphisms; their action has exactly 396 edge-signing orbits. The attached orbit table lists the smallest mask of each orbit, its cardinality, and signed multiplier, accounting for all 32768 frequencies. Every Fourier coefficient is invariant under this **graph-automorphism** action. The histogram therefore determines rank, exact gap, gcd and \(\ell^2\) pseudoinverse norm as asserted.

**Optimal projection.** Define the spectral support \(S=\{s:W(s)\ne0\}\). The translation-invariant Fourier range projection \(P_E\) has convolution kernel
\[
k(x)=2^{-15}\sum_{s\in S}(-1)^{\langle s,x\rangle}.
\]
The same integer butterfly transform, applied to \(\mathbf1_S\), gives a numerator function \(H\) with \(\sum_x|H(x)|=1172832\) and \(H(0)=18856\). Consequently its exact \(\ell^1\) and \(\ell^\infty\) convolution norms equal \(1172832/32768=36651/1024\). For any linear projection \(Q\) onto \(E\), average its conjugates under all translations of \(G\). Each conjugate is a projection onto \(E\) and fixes \(E\); their average maps into \(E\), fixes \(E\), and commutes with translations, so it is the unique translation-invariant projection onto \(E\), namely \(P_E\). Translation operators are isometries in either endpoint norm, proving \(\|P_E\|\le\|Q\|\). This argument is valid over real and complex scalars.

## Verification

Run `python3 verification/check_petersen.py` with standard Python 3. The script regenerates all tree incidences, all Walsh coefficients, all 32768 exact weighted determinants, all 396 signing-orbit representatives, and both supplied CSV certificates. It checks the full absolute histogram, two Parseval identities, the exact norm numerator, sign-complement antipodality, and an explicit demonstration that signed tree coefficients are **not switching-invariant**. The expected success line is `PETERSEN_TREE_WALSH_PASS trees=2000 signings=32768 orbits=396 rank=18856 gcd=16 projection=36651/1024`. Integer-only computations do not rely on floating-point rounding. The mathematical proof uses finite exhaustion over a fixed domain together with the general Fourier-diagonalization and translation-averaging arguments; it does not extrapolate beyond the Petersen graph.

## Relationship to prior work

The weighted Matrix-Tree Theorem and the ordinary count of 2000 Petersen spanning trees are prior mathematics. Martin and Reiner (2003) study weighted tree enumerators of Cartesian products of complete graphs, not a evaluated distribution of all 15 independent Petersen edge-signings. Zaslavsky (2012; later open preprint 2013) classifies signed Petersen graphs up to **switching isomorphism**, with frustration and coloring invariants. Beck and collaborators (2013) evaluate signed chromatic polynomials, also switching-invariant. The present signed tree sum is generally **not invariant under vertex switching** and its 396 ordinary automorphism orbits cannot be collapsed to those six switching classes. No cited prior theorem supplies the evaluated exact frequency distribution or minimum Fourier-range projection norm. This comparison identifies a distinct invariant, not a claim of exhaustive historical uniqueness.

## Limitations

The theorem is an exact, independently reproducible finite classification for the Petersen graph only. It establishes no recurrence or formula for general cubic graphs, generalized Petersen graphs, or larger graph orders. General signed graph coloring, frustration and switching invariants cannot be substituted for the weighted tree-sign sum. Historical priority has been checked against relevant accessible sources but not exhaustively; the general 2003 tree-enumerator paper was available only through its abstract in this comparison. Independent mathematical audit has not been performed.

## References

1. J. L. Martin and V. Reiner, *Factorizations of some weighted spanning tree enumerators*, arXiv:math/0302213, first public preprint 2003-02-18, https://arxiv.org/abs/math/0302213.
2. T. Zaslavsky, *Six signed Petersen graphs, and their automorphisms*, Discrete Mathematics 312 (2012), 1558–1583, DOI:10.1016/j.disc.2011.12.010; lawful open manuscript https://arxiv.org/abs/1303.3347.
3. M. Beck, E. Meza, B. Nevarez, A. Shine, and M. Young, *The Chromatic Polynomials of Signed Petersen Graphs*, first public preprint 2013-11-07, https://arxiv.org/abs/1311.1760.
