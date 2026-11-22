# Exact weight-three two-read deletion capacities through length 32

## Finding

For every integer \(3\le n\le32\), let \(M_3(n)\) be the largest size of a length-\(n\), binary Hamming-weight-three code that permits unambiguous source reconstruction from any **two distinct one-deletion outputs**. The exact finite-blocklength capacities are

\[
M_3(3)=1,\qquad
M_3(2m)=\frac{2m^3-6m^2+13m-12}{3}\quad(2\le m\le16),
\]
\[
M_3(2m+1)=\frac{(m-1)(2m^2-m+12)}{3}\quad(2\le m\le15).
\]

The corresponding maximum sizes at every proved length are:

| Length \(n\) | Maximum code size \(M_3(n)\) |
|---:|---:|
| 3 | 1 |
| 4 | 2 |
| 5 | 6 |
| 6 | 9 |
| 7 | 18 |
| 8 | 24 |
| 9 | 40 |
| 10 | 51 |
| 11 | 76 |
| 12 | 94 |
| 13 | 130 |
| 14 | 157 |
| 15 | 206 |
| 16 | 244 |
| 17 | 308 |
| 18 | 359 |
| 19 | 440 |
| 20 | 506 |
| 21 | 606 |
| 22 | 689 |
| 23 | 810 |
| 24 | 912 |
| 25 | 1056 |
| 26 | 1179 |
| 27 | 1348 |
| 28 | 1494 |
| 29 | 1690 |
| 30 | 1861 |
| 31 | 2086 |
| 32 | 2284 |

For example, \(M_3(16)=244\) and \(M_3(32)=2284\). These are finite results, not an extrapolated all-length theorem.

## Assumptions and scope

An indexed binary word is a vector in \(\{0,1\}^n\), with positions \(0,1,\ldots,n-1\). The set \(W_n\) contains every such vector with precisely three ones, hence \(|W_n|=\binom n3\). For \(w\in W_n\), define \(D(w)\) to be the **set of distinct**, length-\(n-1\) binary words obtained by deleting exactly one coordinate. Multiple deletion coordinates producing the same output contribute only one element. Two distinct words \(u,v\) are confusable exactly when \(|D(u)\cap D(v)|\ge2\). A valid two-read code is a subset \(C\subseteq W_n\) whose distinct members are never confusable.

The data and proofs cover every integer \(n\) from \(3\) through \(32\), inclusive, with no restriction on the locations of the three ones. The claim does not cover unindexed necklaces, noisy substitutions, multiple deletions, or larger Hamming weights.

## Proof

Let \(G_n\) be the simple graph with vertex set \(W_n\), adjoining distinct vertices \(u,v\) precisely when \(|D(u)\cap D(v)|\ge2\). By definition, \(M_3(n)=\alpha(G_n)\).

For each \(n\in\{3,\ldots,32\}\), the accompanying `certificates.json` contains two objects indexed in the **lexicographic list of increasing triples of one-positions**:

* `independent_indices` specifies a collection \(I_n\) of exactly the tabulated number of vertices. For every two distinct indices in this collection, the corresponding deletion sets have intersection cardinality at most one. Thus \(\alpha(G_n)\ge |I_n|\).
* `clique_partition` partitions every one of the \(\binom n3\) vertices, each exactly once, into exactly the same number of classes. Every pair of vertices in a class has deletion-set intersection cardinality at least two, so each class is a clique. Therefore every independent set uses at most one vertex from each class, and \(\alpha(G_n)\le |I_n|\).

These lower and upper bounds coincide for each included \(n\), proving each exact capacity. The verifier `verify_direct.py` independently constructs the complete one-deletion descendant set for every word and checks **all** pairwise requirements within every listed clique, **all** pairs of independent vertices sharing a descendant, exhaustive partition coverage, uniqueness of indices, and the claimed sizes. It uses elementary bit encoding of deletion outputs and requires only Python's standard library. Consequently, the finite proof is not contingent on an optimization solver's optimality flags. The displayed cubic formulas are then checked against the exact capacities at **every integer in their stated ranges**, so no polynomial extrapolation beyond those ranges is being used as proof.

## Verification

Place `certificates.json`, `verify_direct.py`, and `verify_structural.py` in one directory and run:

```sh
python3 verify_direct.py
python3 verify_structural.py
```

Both programs were executed on the included bytes successfully. `verify_direct.py` verifies all thirty integer lengths from \(3\) to \(32\), including the largest certificate with \(\binom{32}{3}=4960\) vertices and \(2284\) clique classes. `verify_structural.py` separately constructs tuple-coded deletion descendants and cross-checks an alternating-interval graph characterization exhaustively for lengths \(3\) through \(12\); it also checks independent-code membership through a distinct interval-toggle construction at selected larger lengths. The direct certificate verifier alone proves the entire stated finite range.

## Relationship to prior work

Multi-read reconstruction from synchronization errors was established as a coding-theoretic question by Sala, Gabrys, Schoeny, and Dolecek (2016). Chrisnata, Kiah, and Yaakobi (2020) treat general two-read single-deletion reconstruction and redundancy, not this complete fixed-Hamming-weight-three finite capacity census. Existing exact weight-two two-read results apply to a different vertex layer, while known weight-three one-read deletion-correcting capacities impose a strictly stronger separation rule. Neither supplies the \(3\)-weight two-read exact sequence above. Published related triangle, edge, and degree enumerations for the unrestricted two-read graph do not determine its weight-three induced subgraph's independence number.

## Limitations

The result is an exact **finite classification through length \(32\)**, not a symbolic all-length identity; the piecewise cubic formulas may fail at longer lengths. The certificates are reproducible finite combinatorial proofs, not independent external review. Related unindexed work or inaccessible full texts could contain equivalent earlier computations. No assertion about asymptotic coding rate, larger weights, or optimal single-read deletion correction is made.

## References

- F. Sala, R. Gabrys, C. Schoeny, and L. Dolecek, *Exact Reconstruction from Insertions in Synchronization Codes*, first public arXiv submission 2016-04-11, https://arxiv.org/abs/1604.03000 .
- J. Chrisnata, H. M. Kiah, and E. Yaakobi, *Optimal Reconstruction Codes for Deletion Channels*, first public arXiv submission 2020-04-13, https://arxiv.org/abs/2004.06032 .
- Related indexed scientific records: https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-two-read-single-deletion-capacity-in-the-binary-weight-two--7d25cc21af64 and https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-two-sharp-constant-weight-single-deletion-code-sizes-at-lengths--31b98d1c763d . These records are used solely for scientific comparison, not as proof of the finite capacities above.
