# Complete Walsh spectrum and sharp projection norm for spanning trees of \(K_{4,4}\)

## Finding

Let \(G=(\mathbb F_2)^{16}\), whose coordinates are the edges \(e_{ij}\) of the complete bipartite graph \(K_{4,4}\), with \(0\le i,j<4\) and bit position \(4i+j\). Write \(\mathcal T\subset G\) for the incidence vectors of its labelled spanning trees, \(f=\mathbf1_{\mathcal T}\), and \(Tg=f*g\) for **unnormalized** counting convolution on \(G\). With \(\chi_s(x)=(-1)^{\sum_{i,j}s_{ij}x_{ij}}\), set

\[
W(s)=\sum_{x\in\mathcal T}\chi_s(x).
\]

There are exactly \(4096\) spanning trees. The **complete** signed Fourier-multiplier distribution is as follows; the two signs in each nonzero row have the displayed multiplicity *each*.

| Fourier multiplier | Multiplicity for each sign |
|---|---:|
| \(\pm4096\) | 1 |
| \(\pm640\) | 32 |
| \(\pm512\) | 72 |
| \(\pm288\) | 144 |
| \(\pm256\) | 96 |
| \(\pm224\) | 16 |
| \(\pm128\) | 3504 |
| \(\pm64\) | 448 |
| \(\pm32\) | 7008 |
| \(0\) | 42894 (total) |

It follows that

\[
\operatorname{rank}(T)=22642,\qquad
\min_{W(s)\ne0}|W(s)|=32,\qquad
\|T^\dagger\|_{\ell^2\to\ell^2}=\frac1{32},
\]

and the positive-spectrum condition number is \(128\). If \(P\) denotes the orthogonal projection in \(\ell^2(G)\) onto the range of \(T\), then its **sharp endpoint norms** are

\[
\boxed{\|P\|_{\ell^1\to\ell^1}=\|P\|_{\ell^\infty\to\ell^\infty}=\frac{737515}{16384}.}
\]

The exact Walsh spectrum is constant on precisely \(192\) orbits of edge-sign patterns under arbitrary permutations of the four vertices on each shore and interchange of the two shores. The complete orbit-representative certificate is supplied in `orbits.csv`.

## Assumptions and scope

All graph vertices and edges are labelled; every edge is included or excluded once. Character frequencies \(s\) range over **all** \(2^{16}=65536\) binary edge sign assignments. The tree family consists of all connected acyclic spanning edge sets with seven edges. There is no probability normalization: the Fourier transform and convolution are counting conventions. The result is a complete finite classification for this graph only, not an assertion about arbitrary \(K_{m,n}\).

## Proof

**Signed matrix-tree reduction.** For a frequency \(s\) set \(w_{ij}=(-1)^{s_{ij}}\) and form the eight-by-eight weighted graph Laplacian with off-diagonal entry \(-w_{ij}\) at an edge and diagonal weighted-degree sums. Kirchhoff's weighted matrix-tree identity is polynomial in the edge weights, so it remains valid at negative integral weights. Deleting the final row and column gives a seven-by-seven integer matrix \(L_s^*\) with

\[
W(s)=\det L_s^*.
\]

The bipartite tree formula gives \(|\mathcal T|=4^3\cdot4^3=4096\), also independently checked by exact enumeration.

**Exhaustive but symmetry-reduced signed determinant certificate.** Permuting the four row vertices, permuting the four column vertices, and interchanging shores preserve the spanning-tree indicator, hence preserve \(W(s)\). The seven adjacent row/column swaps and transpose generate these permutations. A breadth-first orbit traversal of the complete 16-bit mask range yields exactly \(192\) disjoint orbits, whose sizes sum to \(65536\). The complete `orbits.csv` records, for each orbit, its smallest integer representative, exact size and signed determinant. The program `orbit_check.py` constructs the orbits afresh; evaluates the corresponding seven-by-seven determinants by integer fraction-free elimination, including zero-pivot row swaps; and checks the supplied certificate row by row. Summing the orbit sizes by determinant yields the table in the Finding. In particular, no nonzero value has magnitude below \(32\), and the zero orbits have total size \(42894\).

**Independent full Boolean-transform computation.** The program `tree_walsh_check.py` visits all 16-bit edge masks, selects exactly those with seven edges and no cycle by a disjoint-set union test, and independently applies the integer radix-two Walsh-Hadamard transform. It obtains the same signed multiplier histogram and checks the sum-of-squares identity

\[
\sum_{s\in G}W(s)^2=2^{16}\,|\mathcal T|=2^{16}\cdot4096.
\]

The program `cross_check.py` further compares both independently computed 65,536-term transforms **pointwise**, not merely as histograms. Since every spanning tree has seven edges, the complement of all sixteen signs gives \(W(s+\mathbf1)=-W(s)\), explaining the paired sign multiplicities.

**Endpoint projection norm.** Character diagonalization of the counting convolution gives the rank and sharp pseudoinverse bound from the multiplier table. The range projection has Fourier multiplier \(\mathbf1_{W\ne0}\), so its convolution kernel is

\[
p(x)=2^{-16}\sum_{s:W(s)\ne0}(-1)^{s\cdot x}.
\]

Exact Walsh inversion of this binary multiplier array yields

\[
\sum_{x\in G}|2^{16}p(x)|=2950060.
\]

For convolution on a finite group, the sharp \(\ell^1\) and \(\ell^\infty\) operator norms equal the total absolute mass of its kernel. Dividing by \(65536\) gives \(2950060/65536=737515/16384\), as claimed. Both independent programs recompute the endpoint quantity with integer arithmetic.

## Verification

Use Python 3 without external packages from the directory containing the supplied files:

```sh
python3 orbit_check.py
python3 tree_walsh_check.py
python3 cross_check.py
```

Expected success markers are `CERTIFIED_SYMMETRY_ORBIT_DETERMINANTS_PASS`, `TREE_ENUMERATION_WALSH_PASS`, and `ALL_65536_FOURIER_MULTIPLIERS_AGREE_PASS`. The 192-row certificate is supplied as `orbits.csv`; no network fetches or external datasets are required. Integer computations are exhaustive over the stated finite domain, not extrapolations to larger graphs. Exact run outputs include \(22642\) nonzero multipliers, \(42894\) zeros, and the endpoint numerator \(2950060\).

## Relationship to prior work

Classical matrix-tree enumeration and its weighted extensions are assumed. Martin and Reiner (2003) study factorizations of weighted spanning-tree enumerators for threshold graphs and Cartesian products of complete graphs. Aalipour, Duval, Kook, Lee and Martin (2015) treat weighted enumeration of complete colorful complexes; its section on complete multipartite graphs specializes to vertex-degree weights, and does not present the full independent edge-sign Fourier-multiplier distribution of \(K_{4,4}\). Dong and Ge (2021) determine inclusion counts of spanning trees containing specified forests; combined with inclusion–exclusion, their formula could in principle be used to compute the present moments, but the inspected theorem does not state the 19-level histogram, 192 sign orbits, convolution rank or sharp range-projection norm. Published Fourier analyses for \(K_{2,n}\) or \(K_{3,n}\) have different bipartition sizes and do not determine the \(4\)-by-\(4\) invariants without new calculation.

Thus the claim is the exact *evaluated finite Fourier and endpoint classification*, not discovery of the weighted matrix-tree theorem or a universal new formula for tree enumeration.

## Limitations

The result is a finite exact classification; it does not give a closed formula for general bipartition sizes, singular frequencies of other graphs, or an optimal convolution inverse at the endpoint norms. Full historical-priority certification and independent mathematical audit are not claimed. The known general weighted counting identities make this classification computationally accessible, so novelty should be understood as a specific fully evaluated invariant and not as a new foundational method.

## References

1. J. L. Martin and V. Reiner, *Factorizations of some weighted spanning tree enumerators*, arXiv:math/0302213, first posted 2003-02-18. https://arxiv.org/abs/math/0302213
2. G. Aalipour, A. M. Duval, W. Kook, K.-J. Lee and J. L. Martin, *A weighted cellular matrix-tree theorem, with applications to complete colorful and cubical complexes*, arXiv:1510.00033, first posted 2015-09-30. https://arxiv.org/abs/1510.00033
3. F. Dong and J. Ge, *Counting spanning trees in a complete bipartite graph which contain a given spanning forest*, arXiv:2103.05294, first posted 2021-03-09. https://arxiv.org/abs/2103.05294
