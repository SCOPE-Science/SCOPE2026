# Complete dihedral characters in the nonshellable fifth-power cycle three-cut window

## Finding
Let \(G_n=C_n^5\) be the fifth power of the cycle on \(V_n=\mathbb Z/n\mathbb Z\), and let \(X_n=\Delta_3(G_n)\) be its **ordinary** three-cut complex: facets are the complements of disconnected induced three-vertex sets. For each \(13\le n\le20\), the dihedral group \(D_n=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle\) acts by \(r(j)=j+1\) and \(s(j)=-j\).

**Theorem.** Each \(X_n\) has reduced rational homology in exactly one degree \(e_n\), with rank \(b_n\), as in the table. Its **complete rational dihedral character** \(\chi_n\) is given by the two exact integer vectors listed in the table: the first has entries \(\chi_n(r^k)\), the second has entries \(\chi_n(r^k s)\), both for \(k=0,\ldots,n-1\). The final columns give the rational reduced Betti ranks of the genuine geometric quotients under the rotation subgroup and the full dihedral group. All other reduced rational homology of these quotients is zero.

| \(n\) | \(e_n\) | \(b_n\) | \(\chi_n(r^k),\;0\le k<n\) | \(\chi_n(r^k s),\;0\le k<n\) | \(\dim \widetilde H_{e_n}(X_n/C_n;\mathbb Q)\) | \(\dim \widetilde H_{e_n}(X_n/D_n;\mathbb Q)\) |
|---:|---:|---:|---|---|---:|---:|
|13|5|1|\(1\) for all \(k\)|\(-1\) for all \(k\)|1|0|
|14|6|1|\((-1)^k\)|\((-1)^{k+1}\)|0|0|
|15|9|21|\(21\) at \(k=0\); \(6\) at \(k=5,10\); \(1\) otherwise|\(-3\) for all \(k\)|3|0|
|16|10|101|\((101,-1,1,-1,-3,-1,1,-1,5,-1,1,-1,-3,-1,1,-1)\)|\(-3\) for even \(k\), \(7\) for odd \(k\)|6|4|
|17|11|52|\(52\) at \(k=0\); \(1\) otherwise|\(4\) for all \(k\)|4|4|
|18|12|19|\(19\) at \(k=0\); \((-1)^k\) otherwise|\(1\) for even \(k\), \(-3\) for odd \(k\)|1|0|
|19|13|1|\(1\) for all \(k\)|\(-1\) for all \(k\)|1|0|
|20|15|4|\(4\) if \(k\equiv0\pmod{10}\); \(-4\) if \(k\equiv5\pmod{10}\); \(-1\) for other even \(k\); \(1\) otherwise|\(0\) for all \(k\)|0|0|

In particular, **the full dihedral quotient retains positive-degree rational homology precisely for \(n=16,17\)**, and then the surviving rank is exactly four. At \(n=20\), the four-dimensional rational homology representation is \(\rho_2\oplus\rho_6\), where \(\rho_j\) denotes the real two-dimensional dihedral representation with rotation eigenvalues \(\exp(\pm 2\pi i j/20)\), and each reflection has trace zero. The nonequivariant ranks appearing in the table were known from earlier computational literature and are not claimed as new.

## Assumptions and scope
All graphs are finite, simple and unweighted. For each \(n\), adjacency in \(G_n\) means that the minimum cyclic distance lies in \(\{1,2,3,4,5\}\). A triple induces a disconnected graph if and only if it has **at most one graph edge**. For \(13\le n\le20\), define the simplicial Alexander dual \(K_n=X_n^*\) on the same vertex set. Then
\[
K_n=\{S\subseteq V_n:\text{no disconnected induced triple is contained in }S\}.
\]
All relevant integral chain computations use the standard increasing vertex ordering and the augmented simplicial boundary. We calculate the natural action on rational homology; no integral equivariant lattice decomposition, integral quotient homology or simple-homotopy-equivariant splitting is asserted.

## Proof
**1. Exact reduction of the dual.** For each \(n=13,\ldots,20\), enumerate every disconnected induced triple \(T\) using cyclic distances. Generate every face of \(K_n\) by adding vertices in increasing order while rejecting any superset of a forbidden triple. Form the integer augmented simplicial boundaries \(\partial_q:C_q(K_n;\mathbb Z)\to C_{q-1}(K_n;\mathbb Z)\), with \(C_{-1}\cong\mathbb Z\). Every boundary-square relation is explicitly checked.

An entry \(\pm1\) in \(\partial_q\) permits a unimodular basis change and exact cancellation of one degree-\(q\) generator with one degree-\(q-1\) generator. If the pivot is \(a=\pm1\) and the block decomposition has complementary block \(D\), the new boundary block is \(D-ca^{-1}b\) over the integers. The two adjacent boundaries are updated by deletion of the paired basis vectors. This is an integral chain-homotopy equivalence and cannot conceal torsion. Repeating such cancellations through degree zero produces **zero residual boundary maps** and the following positive-degree critical generator counts:

| \(n\) | Forbidden triples | Faces of \(K_n\), including empty | Highest face cardinality | Nonzero reduced integral homology of \(K_n\) | Unimodular cancellation pairs |
|---:|---:|---:|---:|---|---:|
|13|13|2757|8|\(\widetilde H_5\cong\mathbb Z\)|1378|
|14|42|2045|7|\(\widetilde H_5\cong\mathbb Z\)|1022|
|15|90|1711|7|\(\widetilde H_3\cong\mathbb Z^{21}\)|845|
|16|160|1605|7|\(\widetilde H_3\cong\mathbb Z^{101}\)|752|
|17|255|1650|7|\(\widetilde H_3\cong\mathbb Z^{52}\)|799|
|18|366|1711|7|\(\widetilde H_3\cong\mathbb Z^{19}\)|846|
|19|494|1787|7|\(\widetilde H_3\cong\mathbb Z\)|893|
|20|640|1876|7|\(\widetilde H_2\cong\mathbb Z^4\)|936|

An entirely separate bit-exact Gaussian elimination of **the original unreduced boundary maps over \(\mathbb F_2\)** reproduces those ranks. Simplicial Alexander duality and universal coefficients give \(\widetilde H_{e_n}(X_n;\mathbb Z)\cong\mathbb Z^{b_n}\), where \(e_n=n-d_n-3\) for the dual's unique degree \(d_n\), and all other reduced groups vanish. This reproduces, rather than establishes priority for, published nonequivariant homology data.

**2. Two ways to obtain every character value.** For an element \(g\in D_n\), the reduced Hopf trace formula evaluates
\[
L(g,K_n)=-1+\sum_{\varnothing\ne S\in K_n,\,gS=S}(-1)^{|S|-1}\operatorname{sgn}(g|_S).
\]
Here \(\operatorname{sgn}(g|_S)\) is the sign of the permutation taking the ordered vertices of \(S\) to their images. Because the dual has reduced homology only in degree \(d_n\), its trace there is \((-1)^{d_n}L(g,K_n)\). Equivariant combinatorial Alexander duality twists by the orientation of the ambient vertex permutation, so the character on \(X_n\) is
\[
\chi_n(g)=\operatorname{sgn}(g|_{V_n})\,(-1)^{d_n}L(g,K_n).
\]
All \(264=2\sum_{n=13}^{20}n\) values are enumerated exactly. As an **independent normalization check**, we enumerate the unions of vertex orbits for each \(g\), test whether each invariant subset is a face of \(X_n\) by its complement, and compute its signed reduced Lefschetz sum *directly on the original cut complex*. All 264 direct values agree with the duality-derived formula; the resulting arrays are those in the theorem.

**3. Orbit-space calculation.** After barycentric subdivision, a finite group action is cellular without inversions. Its rational quotient chains are the coinvariants of the original rational chains. Averaging makes coinvariants and invariants isomorphic in homology. Hence for every integer \(j\),
\[
\widetilde H_j(|X_n|/D_n;\mathbb Q)\cong\widetilde H_j(X_n;\mathbb Q)^{D_n}.
\]
The two columns of invariant dimensions are therefore the exact character averages \(n^{-1}\sum_{k=0}^{n-1}\chi_n(r^k)\) and \((2n)^{-1}\sum_{k=0}^{n-1}(\chi_n(r^k)+\chi_n(r^ks))\). Their integer values in the table follow by direct summation.

## Verification
Run `python3 -I verify_fifth_power_cut.py` from the directory containing the checker, using Python 3.10 or newer and only the standard library. The checker re-enumerates the complete dual face sets for each of the eight inputs; verifies every initial integer chain identity; performs and checks every integral unit-pivot contraction through the augmentation; independently computes every unreduced mod-two boundary rank; checks all 264 dihedral character values **twice by distinct original/dual fixed-face formulas**; and verifies the resulting invariant dimensions. `verification_output.txt` is the exact replay output. No timeout, stochastic choice, incomplete search, or floating-point rank calculation is used. The finite exact enumeration is exhaustive over the specified eight orders, and does not assert a result for other orders.

## Relationship to prior work
Chauhan, Shukla and Vinayak (2024/2025) explicitly list **the same integral Betti ranks** for the ordinary three-cut complexes of fifth-power cycles in their Table 2 and conjecture associated homotopy types. We claim neither those numerical ranks nor an independently new nonequivariant sphere decomposition. Chauhan and Shukla (2026) prove shellability and top-degree sphere counts for \(n\ge6p-3\), which for \(p=5\) begins at \(n=27\), not in the present range. A later published sharp fifth-power shellability classification handles shellability for \(13\le n\le20\) and shellings for \(n\ge21\), but does not state or determine the dihedral homology character of the nonshellable window. The published general full dihedral character for cycle-power three-cut complexes also assumes \(n\ge6p-3\). The new contribution here is precisely the complete **dihedral action and orbit-space rational homology** in the complementary eight-order range.

## Limitations
The result is a finite, natural parameter-window classification for exactly \(13\le n\le20\) and \(p=5\). It says nothing about integer torsion in the geometric quotients, the full integral \(D_n\)-lattices, or homology actions outside this window. The nonequivariant Betti numbers were already published. Equivalence to an unindexed equivariant computation remains a residual bibliographic risk; no independent mathematical audit has been performed.

## References
1. P. Chauhan and S. Shukla, *Shellability of 3-cut complexes of powers of cycle graphs*, arXiv:2603.23155, initial public 2026-03-24, Theorem 1.4 and Section 4, https://arxiv.org/abs/2603.23155.
2. P. Chauhan, S. Shukla and K. Vinayak, *Shellability of 3-Cut Complexes of Squared Cycle Graphs*, arXiv:2406.01979, initial public 2024-06-04, version 2 Table 2 and Conjecture 4.2, https://arxiv.org/html/2406.01979v2.
3. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, initial public 2023-04-26, https://arxiv.org/abs/2304.13675.
4. *Sharp three-cut shellability threshold for fifth-power cycles*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-three-cut-shellability-threshold-for-fifth-power-cycles--5cedad4bd12d.
5. *Complete dihedral rational homology characters of three-cut complexes of cycle powers*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-complete-dihedral-rational-homology-characters-of-three-cut-comp--f07e0bb07df6.
