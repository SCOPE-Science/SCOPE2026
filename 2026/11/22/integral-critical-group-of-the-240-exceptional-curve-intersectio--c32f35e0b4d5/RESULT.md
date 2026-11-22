# Integral critical group of the 240 exceptional-curve intersection-one graph

## Finding

Let \(S\) be any smooth degree-one del Pezzo surface over an algebraically closed field of characteristic zero. Define \(G(S)\) to have one vertex for each of the \(240\) exceptional curves on \(S\); two distinct vertices are joined by one edge precisely when the corresponding intersection number is \(1\). This definition uses the intersection *number*, not the full weighted intersection graph.

Then \(G(S)\) is a connected simple \(126\)-regular graph on \(240\) vertices, with \(15120\) edges. Its integral critical group, the torsion subgroup of the cokernel of its graph Laplacian, is

\[
\begin{aligned}
K(G(S))\cong{}& (\mathbb Z/3)^{48}\oplus(\mathbb Z/9)^{35}\oplus\mathbb Z/63\\
&\oplus(\mathbb Z/252)^9\oplus(\mathbb Z/504)^{26}\oplus\mathbb Z/1008\\
&\oplus(\mathbb Z/5040)^{48}\oplus\mathbb Z/15120\\
&\oplus(\mathbb Z/60480)^{26}\oplus(\mathbb Z/120960)^8.
\end{aligned}
\]

The complete Smith form of any reduced \(239\)-by-\(239\) Laplacian has \(36\) unit factors in addition to the \(203\) nontrivial invariant factors displayed above. In particular the group exponent is \(120960\), and its order (the spanning-tree count) is

\[
|K(G(S))|=\tau(G(S))=2^{508}3^{393}5^{83}7^{120}.
\]

## Assumptions and scope

The base field is algebraically closed of characteristic zero, and the surface is a smooth degree-one del Pezzo surface. In the classical \(E_8\) correspondence, an exceptional class \(E\) determines the root \(r=E+K_S\) of squared length \(2\) in the positive-definite root lattice; the bilinear form satisfies

\[
E\cdot F=1-\langle r,s\rangle.
\]

Consequently the graph is canonically isomorphic to the graph on all \(240\) \(E_8\) roots in which distinct roots are adjacent exactly when they are orthogonal. This correspondence, rather than any particular moduli point of the surface, establishes independence from \(S\). The graph critical group is not the Néron–Severi discriminant group, the Picard group, or the generalized Jacobian of a curve.

## Proof

**1. Root and graph model.** Use doubled integer coordinates for the roots. The first \(112\) are the vectors with exactly two nonzero coordinates, each independently \(\pm2\); the remaining \(128\) have eight coordinates \(\pm1\), with an even number of negative entries. All have doubled squared norm \(8\). Join two distinct roots when their doubled dot product is zero. The above correspondence shows this adjacency is precisely \(E\cdot F=1\). Direct exhaustive integer evaluation of all distinct pairs gives degree \(126\) at every vertex and \(15120\) edges.

**2. Exact spectral and determinant certificate.** Let \(A\) be the resulting \(240\)-square zero-one adjacency matrix. Integer multiplication establishes

\[
A^4-114A^3-1620A^2+13608A=0.
\]

The same exact construction verifies connectedness, \(\operatorname{tr}(A)=0\), and \(\operatorname{tr}(A^2)=30240\). As \(A\) is symmetric, its only possible eigenvalues are \(126,6,-18,0\). Connectedness and regularity make the multiplicity of \(126\) equal to one. The three remaining multiplicities are uniquely determined by the dimension, trace and square-trace equations. The exact adjacency spectrum is therefore

\[
126^{[1]},\quad 6^{[84]},\quad (-18)^{[35]},\quad 0^{[120]}.
\]

Thus for \(L=126I-A\) the nonzero eigenvalues are \(120^{[84]},126^{[120]},144^{[35]}\). The matrix-tree theorem yields

\[
\tau(G(S))=\frac{120^{84}126^{120}144^{35}}{240}
=2^{508}3^{393}5^{83}7^{120}.
\]

In particular, no prime other than \(2,3,5,7\) divides the critical-group order.

**3. Integral local Smith calculation.** Delete one vertex from \(L\), giving a nonsingular \(239\)-square integral matrix \(R\). For each prime in \(\{2,3,5,7\}\), calculate Smith valuations over sufficiently precise prime-power residue rings. At each stage a unit pivot is brought into the upper-left corner of the remaining block using invertible row and column permutations; its row and column are eliminated by invertible operations. When every entry in the remaining block is divisible by the prime, divide that block by the prime, reduce precision and increase the valuation level. All \(239\) pivots are resolved strictly below the starting precision, giving the following complete counts (omitted valuations occur zero times):

| Prime | Smith valuation : multiplicity |
|---|---|
| \(2\) | \(0:120,\ 2:9,\ 3:26,\ 4:50,\ 6:26,\ 7:8\) |
| \(3\) | \(0:36,\ 1:48,\ 2:120,\ 3:35\) |
| \(5\) | \(0:156,\ 1:83\) |
| \(7\) | \(0:119,\ 1:120\) |

The precise initial moduli used were \(2^9,3^5,5^3,7^3\). As a second check, the full calculation is performed again after deleting a vertex from the *other* type of \(E_8\) root in the coordinate enumeration; the valuation tables agree. All divisions are performed only after every residual entry is divisible, and every pivot is a unit at its current precision, so the steps preserve the local equivalence class and rigorously compute Smith valuations.

Sorting each prime's elementary divisors in nondecreasing order and multiplying them coordinatewise gives the displayed invariant factors. The resulting factors form a divisibility chain and their product equals the independently derived spanning-tree count; hence these factors are the complete integral Smith form.

## Verification

The companion `verify_e8.py` is self-contained Python 3 code requiring no third-party packages or data files. Run `python3 verify_e8.py` from the directory containing this document. It generates all \(240\) roots, all \(28680\) unordered distinct root pairs, and the exact adjacency matrix; checks the polynomial identity and connectedness; performs prime-local integer reductions for both choices of deleted vertex; checks the complete invariant-factor chain; and verifies its product against the matrix-tree formula. A successful run prints `E8_DEL_PEZZO_240_CRITICAL_GROUP_OK`.

These finite computations are **exhaustive for the fixed finite graph**, not probabilistic sampling. Their application to all smooth degree-one del Pezzo surfaces uses the classical uniform root–exceptional-curve correspondence. No statements about an unbounded graph family are inferred from a sample.

## Relationship to prior work

Serganova and Skorobogatov (first public posting 2010-05-07) identify the \(240\) exceptional curves with the roots in the adjoint \(E_8\) model. Winter and van Luijk's open-access paper studies the complete colored \(E_8\) root graph, Weyl-group orbits and cliques, and explains the same intersection-pairing correspondence. Desjardins and Winter study concurrence of exceptional curves, including subgraphs of their weighted intersection configuration. These are the geometric inputs, not claimed new here.

The result here concerns the **full integral Laplacian cokernel of the single color-zero orthogonality graph**, including all prime-power elementary divisors. The inspected source results and appendices on root orbits, subgraph cliques, exceptional-curve concurrence, and geometry do not state this Smith decomposition; their assertions do not imply its integral invariant factors from the supplied statements. The graph spectrum and tree count, even if previously known, are not by themselves a determination of the critical group. This is a best-knowledge originality comparison, not proof of historical priority.

## Limitations

The statement is about the unweighted graph of pairs with intersection number exactly one; it does not describe the full weighted intersection matrix or any embedding-dependent intersection loci. Its group is a graph-theoretic divisor-class invariant, not a Picard-theoretic invariant of the surface itself. Although the proof is fully reproducible by finite exact arithmetic, an old table or paper computing the same Smith form under the alternate name \(E_8\) orthogonality graph could affect priority.

## References

1. V. Serganova and A. Skorobogatov, *Adjoint representation of E8 and del Pezzo surfaces of degree 1*, arXiv:1005.1272 (first posted 2010-05-07), https://arxiv.org/abs/1005.1272.
2. R. Winter and R. van Luijk, *The Action of the Weyl Group on the E8 Root System*, *Graphs and Combinatorics* 37 (2021), 1965–2064, DOI 10.1007/s00373-021-02315-8, https://link.springer.com/article/10.1007/s00373-021-02315-8.
3. J. Desjardins and R. Winter, *Torsion points and concurrent exceptional curves on del Pezzo surfaces of degree one*, arXiv:2210.11659 (first posted 2022-10-21), https://arxiv.org/abs/2210.11659; *Canadian Mathematical Bulletin* 68 (2025), 634–652.
4. Standard Smith normal form and matrix-tree theorem; the particular finite calculation is supplied in `verify_e8.py`.
