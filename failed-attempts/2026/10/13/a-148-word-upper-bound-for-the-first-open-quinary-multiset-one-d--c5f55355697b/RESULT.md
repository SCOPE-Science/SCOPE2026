# A 148-word upper bound for the first open quinary multiset one-deletion instance

## Finding
For the multiset model on five labeled symbols, let \(S_5(9,1)\) be the largest family of multiplicity vectors \(x\in\mathbb Z_{\ge0}^5\) with \(\sum_i x_i=9\) such that the sets of one-symbol deletions of distinct vectors are disjoint. Then
\[143\le S_5(9,1)\le148.\]
The upper inequality follows from an explicit rational deletion-shadow fractional covering, and the lower inequality is attained by a residue-class code. This does not determine the exact maximum.

## Assumptions and scope
Coordinates are five distinct alphabet symbols; order within a multiset is irrelevant. A one-deletion shadow contains each distinct vector obtained by removing one occurrence of a present symbol, counted once. The bound applies to arbitrary (not necessarily linear or cyclic) quinary multiset codes of total multiplicity nine. The underlying question and nomenclature follow Kreindel, Essayag, and Zabokritskiy (2026), arXiv:2601.05636; the paper gives exact values through length eight and states the conjectured value 143 for length nine.

## Proof
Write \(V_r=\{x\in\mathbb Z_{\ge0}^5: \sum_i x_i=r\}\). Then \(|V_9|=715\) and \(|V_8|=495\). For \(y\in V_8\), sort its five coordinates in descending order to obtain a partition \(\lambda(y)\). Assign \(w(y)=b_{\lambda(y)}/420\), where the following table gives the complete 18-entry integer price certificate. The multiplicity column counts members of \(V_8\) with each partition, and the last column is \(b\).

| Partition of eight (descending) | Multiplicity | Integer price \(b\) |
|:--|--:|--:|
| `8,0,0,0,0` | 5 | 420 |
| `7,1,0,0,0` | 20 | 200 |
| `6,2,0,0,0` | 20 | 220 |
| `6,1,1,0,0` | 30 | 108 |
| `5,3,0,0,0` | 20 | 200 |
| `5,2,1,0,0` | 60 | 120 |
| `5,1,1,1,0` | 20 | 96 |
| `4,4,0,0,0` | 10 | 220 |
| `4,3,1,0,0` | 60 | 100 |
| `4,2,2,0,0` | 30 | 180 |
| `4,2,1,1,0` | 60 | 84 |
| `4,1,1,1,1` | 5 | 57 |
| `3,3,2,0,0` | 30 | 140 |
| `3,3,1,1,0` | 30 | 136 |
| `3,2,2,1,0` | 60 | 72 |
| `3,2,1,1,1` | 20 | 111 |
| `2,2,2,2,0` | 5 | 204 |
| `2,2,2,1,1` | 10 | 54 |

**Covering inequality.** For every \(x\in V_9\), the quantity \(\sum_{i:x_i>0}b_{\lambda(x-e_i)}\) is at least 420. This is a finite exact statement: sorting \(x\) gives one of precisely 23 partitions of nine into at most five parts, and direct integer substitution of the displayed prices establishes all 23 inequalities. The accompanying standalone verifier independently checks all 715 labeled vectors, avoiding reliance on an optimization solver. Because deletion shadows are disjoint within any one-deletion-correcting code \(C\), the nonnegative prices give
\[
|C|\le \sum_{x\in C}\sum_{y\in\partial x} w(y)
\le \sum_{y\in V_8}w(y)
=\frac{62165}{420}=\frac{12433}{84}<149.
\]
Consequently \(|C|\le148\).

**Lower bound.** Assign the symbols residues \(0,1,2,3,4\) modulo five and choose all \(x\in V_9\) satisfying \(\sum_{i=0}^4 ix_i\equiv0\pmod5\). Distinct length-nine words with a common one-deletion vector must differ by replacing one symbol with another; their syndromes differ by the nonzero difference of those symbol residues. Thus the chosen words have disjoint deletion shadows. Cyclically relabeling the five alphabet symbols changes the syndrome by \(9\equiv4\pmod5\), so the five syndrome classes have equal cardinality. As \(|V_9|=715\), each has \(715/5=143\) members.

## Verification
Run `python3 verify.py` with a standard Python 3 interpreter; no third-party packages are used. The script reconstructs all 18 shadow partition prices, all 495 shadow vectors and 715 received vectors, confirms the 23 input partition orbits, checks each rational covering inequality, reproduces the exact total price, and checks disjoint deletion shadows for all 143 lower-bound codewords. Expected output: `VERIFY_OK`. This is finite exhaustive verification of the stated finite bound, not an unproved extrapolation.

## Relationship to prior work
Kreindel, Essayag, and Zabokritskiy's paper, arXiv:2601.05636, studies multiset deletion codes, provides exact quinary values through length eight, and identifies the conjectured value 143 for subsequent lengths. Here the lower bound agrees with their conjectured value but the exact length-nine optimum remains unresolved. The upper bound 148 comes from a new explicit, 18-variable symmetrized shadow cover and improves on the general single-deletion shadow/support counting estimates for this instance. Related simplicial rook graph independence is an equivalent graph-theoretic viewpoint; neither the inspected original paper's table nor the published ordinary-string coding result for ordinary quinary *string* deletion codes covers this multiset claim.

## Limitations
The bound does not establish whether 143, 144, 145, 146, 147, or 148 is sharp. It concerns only length nine and alphabet size five, and makes no asymptotic assertion. A previously unindexed equivalent fractional cover or improved bound from simplicial rook graph literature remains a novelty risk; an independent audit has not been performed.

## References
1. Kreindel, Essayag, Zabokritskiy, *Multiset Deletion Codes: Cyclic Constructions, Bounds, and Exact Results*, arXiv:2601.05636, publicly available 2026-01-09; https://arxiv.org/abs/2601.05636.
2. *Notes on simplicial rook graphs*, Journal of Algebraic Combinatorics (2015), https://doi.org/10.1007/s10801-015-0633-y (related graph framework, not an asserted prior bound for this parameter).
3. *Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes*, arXiv:2603.18322 (related general deletion-ball bounds).
