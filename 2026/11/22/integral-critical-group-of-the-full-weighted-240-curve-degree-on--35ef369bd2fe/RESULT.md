# Integral critical group of the full weighted 240-curve degree-one del Pezzo intersection graph

## Finding

Let \(S\) be a smooth degree-one del Pezzo surface over an algebraically closed field of characteristic zero. Each of its 240 exceptional curves is a vertex of an abstract multigraph \(\Gamma_S\); distinct curves \(E,F\) are joined by precisely \(E\cdot F\) parallel edges. This retains all intersection multiplicities, rather than merely recording which intersection numbers equal one.

The complete critical group is
\[
K(\Gamma_S)\cong(\mathbb Z/240\mathbb Z)^{222}\oplus(\mathbb Z/72000\mathbb Z)^8.
\]
Its order is \(240^{222}72000^8=240^{230}300^8\) and its exponent is \(72000\). The exact Laplacian characteristic polynomial is
\[
\chi_L(t)=t(t-240)^{231}(t-300)^8.
\]
Thus the eight nonuniform invariant factors record an integral rank-eight correction from the \(E_8\) root lattice. The full weighted graph has no seven-primary critical-group torsion.

## Assumptions and scope

A degree-one del Pezzo surface over an algebraically closed field of characteristic zero has 240 exceptional (\((-1)\)-) curves. For two *distinct* curves, their intersection index lies in \(\{0,1,2,3\}\); this is a nonnegative integer. In the definition of \(\Gamma_S\) a weight of zero means no edge and weight three means three parallel edges. Loops are excluded. There are 6720 unordered pairs of weight zero, 15120 of weight one, 6720 of weight two, and 120 of weight three. Hence there are \(15120+2(6720)+3(120)=28920\) edges with multiplicity, and every vertex has weighted degree 241. The graph is connected.

This is a graph defined by divisor intersection numbers. It is not asserted to be the nodal dual graph of the union of all 240 curves: simultaneous incidence and non-nodal intersections obstruct that interpretation in general.

## Proof

**Root coordinates and Laplacian.** Identify the exceptional class \(E_\alpha\) with the root \(\alpha=E_\alpha+K_S\) in the positive-definite \(E_8\) lattice (using the negative of the surface intersection form). The established geometric intersection formula is
\[
E_\alpha\cdot E_\beta=1-\langle\alpha,\beta\rangle\qquad(\alpha\ne\beta).
\]
The \(E_8\) roots consist of 112 vectors with two coordinates equal to \(\pm1\) and the others zero, together with 128 vectors with eight coordinates \(\pm\tfrac12\) and an even number of negative signs. They all have squared norm two. Put their coordinates in the \(240\)-by-\(8\) matrix \(R\), in any fixed ordering. Directly from the sign symmetries,
\[
\sum_{\alpha\in E_8}\alpha=0,\qquad R^{\mathsf T}R=60I_8.
\]
Writing \(J\) for the \(240\)-by-\(240\) all-ones matrix, the adjacency matrix has off-diagonal entries \(1-\langle\alpha,\beta\rangle\) and zero diagonal. Its Laplacian therefore has the exact expression
\[
L=240I_{240}-J+RR^{\mathsf T}.
\]
Indeed the diagonal is \(240-1+2=241\) and the off-diagonal entries are \(-1+\langle\alpha,\beta\rangle\). The constant vector is a zero eigenvector, the eight columns of \(R\) have eigenvalue 300, and the 231-dimensional common orthogonal complement has eigenvalue 240. These spaces are exhaustive. Hence the graph is connected, the characteristic polynomial above holds, and the matrix-tree theorem gives
\[
\det L_{\widehat v}=\frac{300^8 240^{231}}{240}=300^8 240^{230}
\]
for every principal cofactor obtained by deleting a vertex \(v\).

**Exact integral Smith calculation.** For a rooted \(239\)-by-\(239\) cofactor \(A\), the attached standalone program constructs its entries in two independent ways: from the complete \(E_8\) root list and from the seven explicit degree/multiplicity families of exceptional divisor classes on the blowup of eight general points. It then performs certified elementary row and column operations on \(A\) over \(\mathbb Z/p^k\mathbb Z\). At each step it chooses a remaining entry of least \(p\)-adic valuation, factors off \(p^v\), inverts its unit part, and clears its row and column by invertible operations. These are exact operations, not a floating-point eigenvalue calculation. The full sequences of prime-local Smith valuations, each totaling 239 factors, are:

| Prime | Valuation 0 | Valuation 1 | Valuation 2 | Valuation 3 | Valuation 4 | Valuation 6 |
|---|---:|---:|---:|---:|---:|---:|
| 2 | 9 | 0 | 0 | 0 | 222 | 8 |
| 3 | 9 | 222 | 8 | 0 | 0 | 0 |
| 5 | 9 | 222 | 0 | 8 | 0 | 0 |

The reduction caps are \(2^{24}\), \(3^{16}\), and \(5^{12}\), all well beyond the largest observed valuation. In each case the sum of the recorded valuations equals the exact prime valuation of the cofactor determinant, respectively 936, 238, and 246. This rules out concealed higher prime powers. The spectral determinant has no other prime factors. Thus the nonzero integral Smith factors are nine units, 222 copies of 240, and eight copies of 72000. Since \(240\) divides \(72000\), these are already the invariant factors. Their torsion cokernel is the displayed \(K(\Gamma_S)\).

## Verification

Run `python e8_weighted_component_group_checker.py` with Python 3 and NumPy. The code needs no source data or external files. It rebuilds 240 roots and separately the 240 eight-point-blowup exceptional classes, checks their intersection distributions and Laplacian degrees, and carries out the prime-local Smith operations on three different rooted cofactors from **each** construction. It also checks an auxiliary prime seven, verifies the determinant valuation budget, and checks the matrix-tree order identity. All six rooted reconstructions returned the same Smith data and the final marker `E8_WEIGHTED_ALL_240_EXCEPTIONAL_SMITH_OK`.

No computation over a finite field is substituted for an infinite-dimensional proof: the only computed object is the explicitly finite integer matrix. The root formula and spectral determinant are exact identities for every surface in the stated class.

## Relationship to prior work

The identification of the 240 exceptional curves with the \(E_8\) roots and the intersection formula are classical and explicit in Serganova–Skorobogatov, Section 5 (2010 preprint, 2011 article). Várilly-Alvarado (2008 preprint) gives an earlier explicit exceptional-curve account, including the Bertini involution. Desjardins–Winter (2022 preprint) expressly work with the **weighted** exceptional-curve intersection graph and analyze clique and concurrency configurations, but do not state its integral sandpile decomposition. A separately calculated simple graph retaining only pairs with intersection number one has a different Laplacian and different torsion; its critical group cannot be substituted for the weighted result here. General Smith-form and matrix-tree theory do not furnish the specific invariant factors without an integral calculation.

## Limitations

The conclusion concerns the abstract weighted graph, not the Picard lattice discriminant, the graph obtained by discarding edges of multiplicity two or three, or automatically the Néron component group of a semistable degeneration. The full exceptional divisor need not have only ordinary nodes, so no such geometric smoothing statement is made. A prior exact sandpile table not indexed under these terminology variants could still affect historical priority. Independent mathematical validation has not been performed.

## References

1. A. Várilly-Alvarado, *Weak approximation on del Pezzo surfaces of degree 1*, arXiv:0801.2430, first posted 2008-01-16, https://arxiv.org/abs/0801.2430.
2. V. Serganova and A. Skorobogatov, *Adjoint representation of \(E_8\) and del Pezzo surfaces of degree 1*, arXiv:1005.1272, first posted 2010-05-07; *Ann. Inst. Fourier* 61 (2011), 2337–2360, https://doi.org/10.5802/aif.2676, Section 5, p. 2357.
3. J. Desjardins and R. Winter, *Torsion points and concurrent exceptional curves on del Pezzo surfaces of degree one*, arXiv:2210.11659 (2022), https://arxiv.org/abs/2210.11659; *Canadian Mathematical Bulletin* 68 (2025), 634–652, Section 2.1.
