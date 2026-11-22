# Three consecutive homology degrees first occur at eight letters in fixed-point-free-involution word complexes

## Finding
For each even \(n\ge 2\), let \(I_n\subseteq\mathfrak S_n\) denote the permutations consisting of \(n/2\) disjoint transpositions. Let \(X_n\) be the semisimplicial complex whose top cells are the one-line injective words for all members of \(I_n\), with all ordered subsequences as faces. Distinct orders of the same vertex set define distinct cells.

The following is the **complete reduced \(\mathbb F_2\)-homology classification for \(n\in\{2,4,6,8\}\)**. Unlisted groups vanish.

| \(n\) | Nonzero reduced homology over \(\mathbb F_2\) |
|---|---|
| \(2\) | None |
| \(4\) | \(\widetilde H_1\cong\mathbb F_2\), \(\widetilde H_2\cong\mathbb F_2\) |
| \(6\) | \(\widetilde H_2\cong(\mathbb F_2)^3\), \(\widetilde H_3\cong(\mathbb F_2)^{19}\) |
| \(8\) | \(\widetilde H_3\cong(\mathbb F_2)^8\), \(\widetilde H_4\cong(\mathbb F_2)^{294}\), \(\widetilde H_5\cong(\mathbb F_2)^9\) |

In particular, eight is the **first even alphabet size** at which these complexes exhibit nonzero mod-two reduced homology in three distinct degrees, and those degrees are consecutive.

## Assumptions and scope
The ground alphabet has exactly \(n\) distinct letters, with \(n\in\{2,4,6,8\}\). A fixed-point-free involution is a permutation \(\sigma\) satisfying \(\sigma^2=\mathrm{id}\) and \(\sigma(i)\neq i\) for every letter. We identify \(\sigma\) with its one-line word \(\sigma(1)\cdots\sigma(n)\). A \(k\)-cell is an injective word of length \(k+1\) obtainable by deleting positions from some such full word. The semisimplicial realization, or equivalently its barycentric subdivision as a simplicial complex, is intended. We compute reduced *cellular* homology with coefficients in \(\mathbb F_2\), not the ordinary abstract simplicial complex formed by forgetting letter order.

## Proof
The finite classification is established by an exhaustive exact arithmetic certificate with source code in `verification/verify.py` and fully reproduced output in `verification/expected_output.txt`. Here are the complete enumerative specifications and the correctness argument for the certificate.

**1. All generators.** To enumerate \(I_n\), choose the least letter not paired yet and pair it, in turn, with every other unpaired letter; recurse on the remaining letters. Each complete matching is reached once, because its partner of the least available letter is unique. Conversely every recursion leaf is a fixed-point-free involution. Hence the program enumerates exactly \((n-1)!!\) full words, yielding generator counts \(1,3,15,105\), respectively.

**2. All cells.** For each enumerated full word and each length \(1\le k\le n\), enumerate all increasing \(k\)-subsets of positions and retain the resulting word. Set union removes only duplicate *identical ordered words*. Every cell is, by definition, a subsequence of a generator and so is reached; every generated word lies in the complex. This establishes the exact cellular bases. Their sizes by degree \(0,1,\ldots,n-1\) are:

| \(n\) | Cellular dimensions \((c_0,c_1,\ldots,c_{n-1})\) |
|---|---|
| 2 | \((2,1)\) |
| 4 | \((4,12,12,3)\) |
| 6 | \((6,30,120,186,90,15)\) |
| 8 | \((8,56,336,1680,3612,2677,840,105)\) |

**3. Exact boundary ranks.** For every word \(w=(w_0,\ldots,w_k)\), use \(\partial_k w=\sum_{i=0}^{k}(w_0,\ldots,\widehat w_i,\ldots,w_k)\) over \(\mathbb F_2\), and the augmentation \(\partial_0(w_i)=1\) into the unique degree-minus-one generator. Each column is stored as an exact integer bit vector indexed by the complete preceding cellular basis. Integer exclusive-or is addition over \(\mathbb F_2\). The elimination algorithm processes columns in a fixed order and eliminates an occupied pivot by exclusive-or; a new pivot adds an independent vector. Induction on processed columns proves that the pivot set is a basis for their span, so its size is the exact matrix rank, without floating point or sampling. The program checks this independently with highest-set-bit and lowest-set-bit pivot conventions. It verifies every relation \(\partial^2=0\) explicitly by deleting two letters in both orders. The exact augmented differential ranks by degree are:

| \(n\) | \((\operatorname{rank}\partial_0,\operatorname{rank}\partial_1,\ldots)\) |
|---|---|
| 2 | \((1,1)\) |
| 4 | \((1,3,8,3)\) |
| 6 | \((1,5,25,92,75,15)\) |
| 8 | \((1,7,49,287,1385,1933,735,105)\) |

**4. Rank-nullity and cutoff.** Write \(r_k=\operatorname{rank}\partial_k\), set \(r_n=0\), and let \(c_k\) be the listed cellular count. Since the complex is augmented and \(\partial^2=0\), for every \(0\le k<n\) we have \(\dim_{\mathbb F_2}\widetilde H_k(X_n;\mathbb F_2)=c_k-r_k-r_{k+1}\). Substituting the two exact arrays yields the full Betti vectors \((0,0)\), \((0,1,1,0)\), \((0,0,3,19,0,0)\), and \((0,0,0,8,294,9,0,0)\). Euler characteristic identities are independently checked. The four possible even values through eight have respectively \(0,2,2,3\) nonzero degrees, proving the asserted first occurrence without any inference about larger alphabets.

## Verification
Run `python3 verification/verify.py` with Python 3.9 or newer from the directory containing this document. It uses only the standard library, builds every cellular boundary column, verifies both rank algorithms, tests boundary-square zero and Euler identities, and compares all computed arrays with the tables above. `verification/expected_output.txt` is the exact successful output from the packaged source. These tests are exhaustive **only for the stated four sizes**; no random tests or numerical ranks substitute for proof.

## Relationship to prior work
The general notion of a permutation complex and its injective-word chain complex comes from Chachólski, Levi and Meshulam (2019). Govc (8 November 2026) proves that the fundamental group of every permutation complex is free, a complementary degree-one statement not determining these higher-dimensional homology ranks. Elizalde, Hanlon and Hersh (5 October 2026) determine homology in several pattern-avoiding families, where the generators satisfy a pattern condition rather than belonging to the fixed-point-free involution conjugacy class. None of these results supplies the listed ranks by direct implication. The full injective-word complex, and complexes generated by all derangements, are likewise different families: an inclusion of cellular complexes does not determine the induced homology of this proper subcomplex.

## Limitations
The claim is exact but finite, restricted to even \(n\le8\) and coefficients \(\mathbb F_2\). It does not assert homology formulas for larger even \(n\), integral torsion, connectivity beyond that forced by the listed homology, shellability, wedge-of-spheres homotopy types, or equivariant representations. Existence of an unindexed duplicate computation is a residual publication-priority uncertainty. Independent validation has not been performed.

## References
- W. Chachólski, R. Levi, R. Meshulam, *On the topology of complexes of injective words*, first public 9 August 2019, https://arxiv.org/abs/1908.03394.
- D. Govc, *Fundamental Groups of Permutation Complexes*, first public 8 November 2026, https://arxiv.org/abs/2611.11362.
- S. Elizalde, P. Hanlon, P. Hersh, *Complexes of pattern-avoiding injective words*, first public 5 October 2026, https://arxiv.org/abs/2610.07303.
