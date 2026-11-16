# Sharp Walsh conditioning of acyclic orientations of \(K_{3,n}\)

## Finding
For every integer \(n\ge 2\), encode each orientation of the edges of the complete bipartite graph \(K_{3,n}\) by a \(3\times n\) binary matrix: entry one means that the corresponding edge points from its right-part vertex to its left-part vertex. Let \(A_n\subseteq G_n=\mathbb F_2^{3n}\) be the acyclic-orientation vectors, and let \(T_n f=\mathbf1_{A_n}*f\) denote **unnormalized counting convolution** on \(\ell^2(G_n)\). For every frequency \(u\in G_n\), let
\[
W_n(u)=\sum_{x\in A_n}(-1)^{\langle u,x\rangle}.
\]
Then the following statements all hold for every \(n\ge2\):

1. The **complete signed Walsh multiplier function** is given by the thirteen-product formula below.
2. \(W_n(u)=0\) if and only if \(u\) has odd Hamming weight. Hence \(\operatorname{rank}T_n=2^{3n-1}\), and its range is precisely the functions invariant under translating by the all-ones vector.
3. Every nonzero \(W_n(u)\) is congruent to \(2\pmod4\). The smallest nonzero multiplier magnitude is exactly \(2\), and the largest is \(6\cdot4^n-6\cdot3^n+2^n\).
4. The inverse of \(T_n\) on its range has \(\ell^2\)-operator norm exactly \(1/2\), and the sharp nonzero-spectrum singular-value condition number is
\[
\kappa_2(T_n\vert_{\operatorname{ran}T_n})=3\cdot4^n-3\cdot3^n+2^{n-1}.
\]
The orthogonal Fourier-support projection is \(f(x)\mapsto(f(x)+f(x+\mathbf1))/2\), with optimal projection norm \(1\) in every \(\ell^p\), \(1\le p\le\infty\).

## Assumptions and scope
All group operations are over \(\mathbb F_2\). Number the three vertices of one bipartition \(0,1,2\) and the other bipartition \(1,\ldots,n\). Regard each column \(v\in\{0,\ldots,7\}\) as the three-bit vector with integer value \(v\), and let \(\chi_u(v)=(-1)^{\langle u,v\rangle}\) for three-bit columns.

For a permutation \(\pi=(\pi_1,\pi_2,\pi_3)\) of the three row indices, let
\[
C_\pi=\{0,2^{\pi_1},2^{\pi_1}+2^{\pi_2},7\}.
\]
For any nonempty subset \(C\subseteq\{0,\ldots,7\}\), set \(L_C(u)=\sum_{v\in C}\chi_u(v)\). For the column frequencies \(u=(u_1,\ldots,u_n)\), the exact formula is
\[
W_n(u)=\sum_{\pi\in S_3}\prod_{j=1}^nL_{C_\pi}(u_j)
-\sum_{v=1}^{6}\prod_{j=1}^nL_{\{0,v,7\}}(u_j)
+\prod_{j=1}^nL_{\{0,7\}}(u_j).
\]
There are six terms, six subtractive terms, and one corrective term, all integral. This formula specifies every multiplier without inspecting the exponentially large set of orientations.

## Proof
**Acyclicity and nested columns.** The matrix is an acyclic orientation if and only if all its column supports form a chain under containment. Indeed, two incomparable columns provide a pair of opposite \(2\times2\) patterns and hence a directed four-cycle. Conversely, in a complete bipartite graph any shortest directed cycle of length at least six has a chord between its bipartition classes. Either direction of that chord gives a shorter directed cycle, a contradiction. Thus a directed cycle forces a directed four-cycle, which forces incomparable columns. Every chain in the three-element Boolean lattice is contained in one of its six maximal chains \(C_\pi\).

**Thirteen-product formula.** For each maximal chain, the signed sum over all \(n\)-column matrices with columns in that chain factors as \(\prod_j L_{C_\pi}(u_j)\). Apply inclusion-exclusion to the union of these six product sets. Each intermediate three-element intersection \(\{0,v,7\}\), for \(1\le v\le6\), has aggregate coefficient \(-1\), while the common two-element intersection \(\{0,7\}\) has aggregate coefficient \(+1\). This gives the displayed identity, for every frequency and every positive integer \(n\).

**Unsigned count.** At zero frequency, each four-element chain contributes \(4^n\), each three-element intersection contributes \(3^n\), and the two-element intersection contributes \(2^n\). Therefore
\[
|A_n|=W_n(0)=6\cdot4^n-6\cdot3^n+2^n.
\]
For \(n\ge2\), this is congruent to \(2\pmod4\).

**Complete zero-set proof.** Reversing every edge maps \(x\in A_n\) to \(x+\mathbf1\in A_n\), without fixed points. A frequency of odd Hamming weight changes its sign under this involution, so its sum vanishes. For even Hamming weight the two terms in every reversing pair agree. There are exactly \(|A_n|/2\) such pairs, an odd number; hence their signs add to an odd integer and \(W_n(u)\equiv2\pmod4\). Therefore no even-weight frequency vanishes. The Fourier-support size is exactly half of \(|G_n|\).

**Sharp minimum and witnesses.** Put \(u^{(e)}_n=(1,\ldots,1,7)\) with \(n-1\) copies of the three-bit frequency \(1\), and put \(u^{(o)}_n=(2,3,1,\ldots,1)\) with \(n-2\) copies of \(1\). Directly substituting the three-bit character sums into the thirteen-product identity yields the exact all-order identities
\[
W_n(u^{(e)}_n)=1+(-1)^n,\qquad W_n(u^{(o)}_n)=(-1)^n-1.
\]
For even \(n\), the first is \(2\); for odd \(n\ge3\), the second is \(-2\). The congruence argument already proves every nonzero multiplier has absolute value at least two. Thus this is sharp for every \(n\ge2\).

**Spectral norms.** Walsh characters diagonalize counting convolution, with eigenvalues \(W_n(u)\). By the triangle inequality \(|W_n(u)|\le|A_n|\), with equality at frequency zero. The established smallest nonzero magnitude is two, so the inverse-on-range norm and condition number have the claimed values. The nonzero frequencies are exactly the even-weight frequencies, whose orthogonal projection is averaging over the two-element subgroup \(\{0,\mathbf1\}\). Averaging has norm at most one on each \(\ell^p\), and every projection onto a nonzero subspace has norm at least one, proving sharpness.

## Verification
The standalone standard-library Python program `check.py` independently tests acyclicity by directed topological sorting and by column-support comparability, with exact agreement for every orientation matrix at \(2\le n\le5\). It computes each complete signed Walsh transform using an integer butterfly transform and separately evaluates the thirteen-product formula at every frequency. These independent constructions agree at all 37,440 frequencies. It checks Parseval, the entire zero set, the minimum nonzero multiplier, and compares the complete signed-value histograms with `spectrum_n2_n5.csv`. Arbitrary-precision integer substitution additionally checks both explicit witness identities and the zero-frequency count through \(n=100\). These finite checks do not replace the symbolic all-order argument above.

Reproduce from the containing directory with `python3 check.py`. No external Python packages are required.

## Relationship to prior work
Cameron, Glass, Rekvényi and Schumacher (2014) establish the acyclic-orientation/lonesum-matrix bijection and enumerate these orientations via poly-Bernoulli numbers. Their unweighted enumeration is used here only as context: it does not specify the coordinatewise signed Walsh multipliers or the optimal inverse-on-range norm. Gebhard and Sagan (1999), building on Stanley's theorem, connect acyclic orientations to chromatic-polynomial and sink enumeration; these statements likewise do not give the present signed frequency formula.

Subsequent encoding work for complete multipartite orientations provides construction and enumeration, but not the specific sharp nonzero Walsh multiplier bound. Separate explicit results for the two-row family do not imply the three-row thirteen-product formula or its parity-dependent extremizing frequencies. The relevant distinction is between total enumeration and simultaneous independent sign choices on all graph edges.

## Limitations
The theorem is for three left-part vertices and at least two right-part vertices, with the specified edge-direction encoding and **unnormalized** group convolution. The formula and proof do not assert an analogous minimum-multiplier law for \(K_{m,n}\) with \(m\ge4\), nor a full spectral-value multiplicity formula in every dimension. The exact signed multiplier function is available, but obtaining its aggregated histogram for arbitrary \(n\) requires evaluating that formula. No claim of independent mathematical audit or exhaustive historical priority is made.

## References
- P. J. Cameron, C. A. Glass, K. Rekvényi and R. U. Schumacher, *Acyclic orientations and poly-Bernoulli numbers*, first posted 2014-12-11, arXiv:1412.3685, https://arxiv.org/abs/1412.3685.
- D. D. Gebhard and B. E. Sagan, *Sinks in Acyclic Orientations of Graphs*, first posted 1999-07-12, arXiv:math/9907078, https://arxiv.org/html/math/9907078v1.
- W. Carballosa, J. Khera and F. Reyes, *Encoding acyclic orientation of complete multipartite graphs*, first posted 2023-03-16, arXiv:2303.09021, https://arxiv.org/abs/2303.09021.
