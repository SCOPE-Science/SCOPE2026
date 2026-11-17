# Integral homology of the first five symmetric quotients of cycle-free chessboard complexes

## Finding

For every integer \(3\le n\le 7\), let \(\Omega_n\) be the cycle-free chessboard complex, with vertices the directed arcs \(i\to j\) for distinct labels \(i,j\in\{1,\ldots,n\}\). Its faces are arc sets consisting of vertex-disjoint directed paths and isolated vertices. Let \(S_n\) relabel endpoints simultaneously, and set \(Q_n=|\Omega_n|/S_n\), the **ordinary geometric orbit space**. Then all \(Q_n\) here are connected, and their complete positive-degree integral homology is:

| \(n\) | Nonzero positive-degree groups of \(Q_n\) |
|---|---|
| 3 | \(H_1=\mathbb Z\) |
| 4 | \(H_1=\mathbb Z/2\mathbb Z\) |
| 5 | \(H_2=\mathbb Z,\ H_3=\mathbb Z\) |
| 6 | \(H_3=\mathbb Z\oplus\mathbb Z/2\mathbb Z\) |
| 7 | \(H_3=\mathbb Z/2\mathbb Z,\ H_4=\mathbb Z,\ H_5=\mathbb Z\) |

All other positive-degree integral homology groups vanish in these five cases. In particular, genuine order-two torsion occurs at sizes 4, 6, and 7, but not 3 or 5.

## Assumptions and scope

The complexes are the standard \(\Omega_n\) of Vrećica and Živaljević (first public version, 27 October 2007). The action is simultaneous conjugation/relabeling by the **entire** symmetric group, not independent row and column permutation, and not a quotient of a free action. No result for \(n\ge8\) is claimed. All chains use integral coefficients.

## Proof

**Orbit cells.** The first barycentric subdivision of \(\Omega_n\) has a simplex for each strict chain of nonempty path-forest faces \(F_1\subsetneq\cdots\subsetneq F_r\). Every symmetry preserving such a simplex setwise preserves each face individually because their edge counts are distinct. Hence the orbit of the barycentric subdivision is a genuine \(\Delta\)-complex with one \((r-1)\)-cell for each orbit of face chains and the usual alternating boundary.

Record each directed path component of the largest forest by the word of arc-birth indices: an arc has color \(j\) if first present in \(F_j\). Unused labels are isolated vertices. The quotient-cell invariant is the **unordered multiset** of these path words, subject to the sum of their path-vertex costs being at most \(n\) and every color \(1,\ldots,r\) occurring. This is a bijection: directed paths have no nontrivial orientation-preserving automorphisms, and any two forests with the same colored component words are related by relabeling. A word of length \(a\) uses \(a+1\) vertices.

**Boundary.** Deleting the last face drops all last-color arcs and splits surviving paths at those gaps. Deleting an earlier face merges its birth color with the next color and shifts subsequent indices down by one. Each deletion contributes sign \((-1)^{j-1}\); because the chain is ordered by inclusion, no further orientation sign occurs. These rules form exact integral matrices for \(\partial_{r-1}\). Their composition vanishes, as checked directly.

**Integer reduction.** Every nonzero \(\pm1\) matrix entry permits an integral cancellation of one adjacent pair of cellular generators. In a boundary matrix \(\partial_k\), eliminate that row from the other columns by subtracting integral multiples of the pivot column; remove the chosen column and row, the corresponding row from \(\partial_{k+1}\), and the corresponding column from \(\partial_{k-1}\). The chain identity guarantees these operations give a chain-homotopy equivalent integral chain complex. Repeat until no unit entry survives. The resulting exact counts are:

| \(n\) | Initial cell counts in degrees \(0,1,\ldots\) | Remaining cell counts in degrees \(0,1,\ldots\) | Remaining nonzero differential |
|---|---|---|---|
| 3 | 2, 2 | 1, 1 | none |
| 4 | 4, 9, 6 | 1, 1, 1 | \(\partial_2\): one entry of absolute value 2 |
| 5 | 6, 29, 48, 24 | 1, 0, 1, 1 | none |
| 6 | 10, 83, 253, 300, 120 | 1, 0, 0, 2, 1 | \(\partial_4\): a two-by-one column, entries of absolute value 2 |
| 7 | 14, 215, 1114, 2352, 2160, 720 | 1, 0, 0, 1, 2, 1 | \(\partial_4\): a one-by-two row, entries of absolute values 2 and 4 |

The Smith invariant of every surviving nonzero matrix is precisely 2 (the greatest common divisor of its entries), and each has rank one. Reading kernels modulo images yields the homology table stated above. In particular, the degree-three group at \(n=6\) has both a free summand and a two-torsion summand; it is not purely torsion.

## Verification

Execute `python3 verify.py` from this package. It reconstructs all orbit cells and signed differentials for \(3\le n\le7\), checks \(\partial^2=0\), performs every unit cancellation using arbitrary-precision integers, checks the final chain identities, and calculates homology from the reduced complexes. It independently enumerates labeled barycentric flag orbits for sizes 4 and 5. Recorded output is in `verification_run.txt`. The exact intermediate count of unit cancellations is 1; 3,5; 5,24,23; 9,74,179,119; and 13,202,912,1439,719, respectively.

## Relationship to prior work

Vrećica and Živaljević introduced and studied the connectivity of the *unquotiented* cycle-free chessboard complexes. Ault's dissertation identifies their suspensions with algebraic chain complexes and analyzes symmetric-group homology representations. The published record entitled *Hamiltonian-cycle basis and symmetric-group top homology of cycle-free chessboard complexes* determines an integral top-homology lattice and the rational invariant at top degree. Those results do not determine the present finite list of integral homology groups of the **geometric orbit spaces**, particularly the order-two torsion in lower degrees. Rational invariant homology of a cover cannot detect integral torsion of its nonfree quotient.

## Limitations

The result is a finite exact classification for five specified sizes, not a theorem for arbitrarily large sizes. The chain contractions are algebraic and establish homology; they do not by themselves prove a homotopy wedge decomposition or classify attaching maps. The complete full-text comparison to a relevant published mathematical record was unavailable, so equivalent literature not indexed by searches remains a priority risk. No independent mathematical review has been performed.

## References

1. S. T. Vrećica and R. T. Živaljević, *Cycle-free chessboard complexes and symmetric homology of algebras*, arXiv:0710.5252, first public 27 October 2007, https://arxiv.org/html/0710.5252v3 .
2. S. Ault, *On the Symmetric Homology of Algebras*, arXiv:0807.4521, first public 28 July 2008, https://arxiv.org/html/0807.4521v1 .
3. *Hamiltonian-cycle basis and symmetric-group top homology of cycle-free chessboard complexes*, published mathematical record, 2026 (record summary examined, full text not accessible in this run).
