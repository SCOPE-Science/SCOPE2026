# Exact Fourier nullity and endpoint stability for seven-vertex noncrossing trees

## Finding

Let \(V=\{0,1,\ldots,6\}\) be the vertices of a convex heptagon in cyclic order and let \(E=\{\{i,j\}:0\le i<j\le6\}\). Write \(G=\mathbb F_2^E\), so \(|G|=2^{21}\). Let \(\mathcal T\subset G\) be the indicator vectors of all crossing-free (straight-line) spanning trees on \(V\); then \(|\mathcal T|=1428\). Define

\[
W(K)=\sum_{T\in\mathcal T}(-1)^{|K\cap T|},\qquad K\subseteq E.
\]

**Exact heptagon theorem.** Among the \(2^{21}=2097152\) characters, exactly \(160484\) have \(W(K)=0\). The unnormalized counting convolution \(C_f g(x)=\sum_{y\in G}f(y)g(x+y)\), with \(f=\mathbf1_{\mathcal T}\), therefore has rank \(1936668\). Every Walsh multiplier is divisible by four, and \(\min_{W(K)\ne0}|W(K)|=4\); hence \(\|C_f^\dagger\|_{2\to2}=1/4\) and the positive-spectrum condition number is \(1428/4=357\).

The smallest support of a zero character has size two. There are precisely fourteen such characters, all in one orbit of the dihedral group of order fourteen, represented by the two-edge support \(K=\{\{0,1\},\{2,5\}\}\). In particular, no support of size zero or one is a zero.

Let \(P\) denote the orthogonal projection in \(\ell^2(G)\) onto the range of \(C_f\). Its exact endpoint operator norms are

\[
\boxed{\|P\|_{\ell^1\to\ell^1}=\|P\|_{\ell^\infty\to\ell^\infty}=\frac{39113019}{262144}}.
\]

The accompanying `spectrum_levels.csv` is an exact 169-level signed Fourier multiplicity table, and `pair_orbits.csv` lists all twenty-one dihedral orbits of two-edge supports and their multipliers. These are parts of this one finite claim, not independent additional findings.

## Assumptions and scope

Vertices are *labelled*, cyclically ordered, and in strictly convex position; chords meeting only at a common endpoint are not considered crossing. The full edge universe consists of all twenty-one unordered pairs, including polygon sides. Character frequencies are all binary edge subsets, not only planar edge subsets. Every tree has exactly six edges. No claim is made for other polygon sizes, arbitrary point configurations, or other normalizations.

All Fourier transforms use unnormalized \(\pm1\) characters. The inverse transform carries the factor \(2^{-21}\). Convolution is unnormalized counting convolution on the Boolean additive group. The \(\ell^2\) pseudoinverse norm is the inverse of the smallest nonzero *absolute* multiplier; projection endpoint norms use counting measure, on which the usual convolution \(\ell^1\) norm formula is valid.

## Proof

**(1) Exhaustive finite domain.** The classical noncrossing-tree enumeration formula gives

\[
|\mathcal T|=\frac{1}{2(7)-1}\binom{3(7)-3}{7-1}=1428.
\]

Independently of that formula, the program `check_prufer.cpp` enumerates all \(7^{5}=16807\) Prüfer codes, which bijectively encode labelled seven-vertex trees, and rejects an edge set exactly when it contains two cyclically interleaving chords. It obtains exactly \(1428\) distinct admissible trees. The independent program `check_subsets.py` enumerates all \(\binom{21}{6}=54264\) six-edge subsets, first rejects crossing pairs, and then uses a disjoint-set union test to ensure the chosen six edges form a tree; it finds exactly the same cardinality. Both algorithms terminate after explicitly given finite loops and test a complete domain.

**(2) The sharp divisibility.** A direct complete chord-incidence count (also checked by the two programs) shows that each fixed edge is contained in exactly \(728\), \(286\), or \(210\) noncrossing trees according as its shorter cyclic span is \(1\), \(2\), or \(3\). All three counts are even. For any frequency \(K\), the elementary expansion

\[
W(K)=\sum_{T\in\mathcal T}\prod_{e\in K}(1-2\mathbf1_{e\in T})
\equiv |\mathcal T|-2\sum_{e\in K}|\{T\in\mathcal T:e\in T\}|\equiv0\pmod4
\]

proves universal divisibility by four. The complete integer Fourier calculation described below exhibits coefficients of absolute magnitude four, proving that the gcd of *all* multipliers and the least positive absolute multiplier are both exactly four.

**(3) The first cancellation is structural.** At frequency \(K=\{e\}\), the multiplier is \(1428-2N_e\), giving exactly \(-28\), \(856\), and \(1008\) for the three cyclic chord lengths. Thus there is no degree-one zero. For two edges \(e,d\), inclusion-exclusion yields

\[
W(\{e,d\})=1428-2(N_e+N_d)+4N_{e,d},
\]

where \(N_{e,d}\) counts trees containing both edges. The twenty-one dihedral orbits and their exact inclusion counts are enumerated in `pair_orbits.csv` and independently reconstructed and compared in `check_subsets.py`. Exactly one orbit has zero multiplier: the orbit of \(\{\{0,1\},\{2,5\}\}\), with \(N_e=728\), \(N_d=210\), and \(N_{e,d}=112\). This orbit has fourteen supports, and its cancellation is \(1428-2(728+210)+4(112)=0\). Every other orbit entry is nonzero.

**(4) Entire Fourier nullity.** Place one at each of the \(1428\) distinct incidence vectors and zero elsewhere in a length-\(2097152\) integer array. At each of the twenty-one coordinates apply the exact butterfly

\[
(a,b)\longmapsto(a+b,a-b).
\]

The resulting array is precisely \(W(K)\) by induction on the coordinates. Both independently enumerated tree lists produce exactly \(160484\) zero coefficients, a nonzero minimum magnitude of four, and the attached complete signed-level histogram. The Parseval checksum is

\[
\sum_{K\subseteq E} W(K)^2=2^{21}\cdot1428=2994733056.
\]

Consequently the range of counting convolution, which diagonalizes with these multipliers, has dimension \(2^{21}-160484=1936668\). Its maximum multiplier modulus is \(1428\), achieved at the empty character, and its least nonzero magnitude is four, proving the Hilbert-space norm statements.

**(5) Exact endpoint projection norm.** Let \(h(K)=\mathbf1_{W(K)\ne0}\). The projection \(P\) is convolution with

\[
p(x)=2^{-21}\sum_{K\in G}h(K)(-1)^{\langle K,x\rangle}.
\]

A second complete integer butterfly transform of \(h\), implemented independently in each verifier, gives the exact absolute-sum certificate

\[
\sum_{x\in G}\left|\sum_{K\in G}h(K)(-1)^{\langle K,x\rangle}\right|=312904152.
\]

The \(\ell^1\)-convolution operator norm is \(\sum_x|p(x)|\): the triangle inequality gives the upper bound, attained on a point mass. By duality, the \(\ell^\infty\) operator norm is equal. Dividing the absolute sum by \(2^{21}\) and reducing yields \(39113019/262144\), as asserted.

## Verification

Two executable integer-arithmetic routes are supplied. Run `c++ -O2 -std=c++17 check_prufer.cpp -o check_prufer && ./check_prufer` from the file directory, and `python check_subsets.py` (Python 3 with NumPy). Both require only the included files and the stated standard compiler/interpreter library dependency. The second checker additionally validates every entry of `pair_orbits.csv` and `spectrum_levels.csv` against independently constructed tree supports. All assertions in both programs were executed successfully, including the full Fourier nullity, least nonzero multiplier, first-zero orbit, Parseval sum, and projection absolute sum. The exact integer inputs fit in signed 32-bit arrays during the transforms; the absolute-sum accumulation uses 64-bit integers.

## Relationship to prior work

Flajolet and Noy established the noncrossing-tree counting formula and degree/leaf refinements; Okoth and Wagner established local-orientation degree-sequence refinements. Wettstein gave algorithms for enumeration of general crossing-free geometric spanning trees. These support the object and finite enumeration but do not, in the inspected passages, give the seven-vertex all-character edge-incidence Walsh nullity, the two-chord zero orbit, or its sharp projection endpoint norm. Those are different invariants: neither the total tree count nor a distribution of vertex degrees determines all joint edge-incidence parity correlations. Existing spectra for convex polygon triangulations, noncrossing *perfect matchings*, and unrestricted spanning-tree families concern distinct edge-set distributions and cannot be substituted without a coefficient-preserving map.

## Limitations

This is an exact finite heptagon result, not an infinite-family theorem. The computer-checked parts of the proof rely on exhaustive arithmetic over exactly \(2^{21}\) Fourier characters; the attached code and two independent enumeration routes make the computation reproducible, but do not supply an external mathematical audit. Beyond the pair-support classification, no concise classification of every zero character is asserted, only its exact total and signed multiplier table. Literature comparisons are bounded; older unindexed tables or equivalent computations may exist.

## References

1. I. O. Okoth and S. Wagner, *Locally Oriented Noncrossing Trees*, Electronic Journal of Combinatorics 22(3), P3.36 (2015), https://doi.org/10.37236/5164 (published 2015-09-11).
2. P. Flajolet and M. Noy, *Analytic Combinatorics of Non-crossing Configurations*, Discrete Mathematics 204 (1999), 203–229, https://web.mat.upc.edu/marc.noy/uploads/2013/05/NC-configurations.pdf.
3. M. Wettstein, *Counting and Enumerating Crossing-free Geometric Graphs*, arXiv:1604.05350 (first version 2016-04-18), https://arxiv.org/abs/1604.05350.
