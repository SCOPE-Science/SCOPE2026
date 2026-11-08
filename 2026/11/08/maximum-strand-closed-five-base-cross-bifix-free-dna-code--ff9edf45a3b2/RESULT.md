# Maximum strand-closed five-base cross-bifix-free DNA code

## Finding

Let \(\Sigma=\{A,C,G,T\}\) with Watson--Crick complementation \(\bar A=T\), \(\bar C=G\). For a word \(w=w_1\cdots w_5\), let \(\rho(w)=\bar w_5\cdots\bar w_1\). A code \(C\subseteq\Sigma^5\) is *strand-closed* if \(\rho(C)=C\), and *non-overlapping* (cross-bifix-free) if the prefix of length \(k\) of \(u\) differs from the suffix of length \(k\) of \(v\), for every \(u,v\in C\) (including \(u=v\)) and \(k\in\{1,2,3,4\}\).

**Theorem.** The exact maximum size of such a code is
\[
\max\{|C|: C\subseteq\Sigma^5,\ \rho(C)=C,\ C\text{ non-overlapping}\}=36.
\]
An explicit optimal code is in `witness.txt`. Its \(36\) words split into \(18\) reverse-complement pairs. The upper bound is witnessed by a partition of \(56\) admissible reverse-complement orbits into \(18\) overlap-conflict cliques; the partition is recorded below and in `certificate.json`.

## Assumptions and scope

Words are linear, of fixed length five, over the exactly four specified DNA letters. Both orientations of a word must be included as separate codewords whenever they differ. Overlaps are forbidden even between a word and itself. Only proper lengths \(1\) through \(4\) count; no Hamming-distance, GC-content, melting-temperature or other biochemical constraint is imposed.

## Proof

**1. Canonical endpoint reduction.** Suppose \(C\) is nonempty and write \(P\) and \(Q\) for its sets of first and last letters. Strand closure forces \(Q=\bar P\). The length-one cross-bifix condition gives \(P\cap\bar P=\varnothing\). Since the complement consists of exactly two two-element pairs, \(P\) is contained in a two-letter transversal of those pairs. Complement-preserving permutations of the alphabet map any such transversal to \(\{A,C\}\). Hence, without altering cardinality or constraints, all codewords lie in
\[
W=\{A,C\}\,\Sigma^3\,\{G,T\},\qquad |W|=256.
\]
The empty code trivially satisfies the claimed upper bound.

**2. Involutive quotient.** Reverse complement preserves \(W\). No five-letter DNA word equals its own reverse complement: its middle letter would have to equal its Watson--Crick complement, which is impossible. Thus all reverse-complement orbits in \(W\) have size two. A code can contain an orbit only if the two members are mutually non-overlapping and separately unbordered. Applying these elementary conditions to all \(128\) orbits of \(W\) leaves exactly \(56\) admissible orbits, numbered from \(0\) to \(55\) in the canonical lexicographic order below. Their overlap-conflict graph has \(412\) edges. Two distinct orbit vertices are joined precisely when any proper prefix of any word in one orbit equals a corresponding-length suffix of a word in the other, in either direction. A strand-closed non-overlapping code in \(W\) is therefore equivalent to an independent set of this graph, contributing exactly two DNA words per selected vertex.

**3. Explicit finite upper-bound certificate.** The following \(18\) blocks partition all \(56\) vertices. Every block is a clique: for each pair of indices within a block there is at least one conflicting ordered word-pair and overlap length among \(1,2,3,4\). These pairwise checks, together with the orbit classification, are exhaustively reproducible by `verify_exact.py`, using only the definitions above.

| Clique | Orbit indices |
|---:|:---|
| 1 | 0, 2, 6, 12 |
| 2 | 4, 17 |
| 3 | 5, 20, 23, 48 |
| 4 | 7, 28 |
| 5 | 1, 8, 22, 30 |
| 6 | 14, 36 |
| 7 | 16, 43 |
| 8 | 11, 18, 37, 42 |
| 9 | 19, 21, 44, 46 |
| 10 | 24, 45 |
| 11 | 25, 38, 51, 52 |
| 12 | 26, 29, 32 |
| 13 | 9, 31, 40, 50 |
| 14 | 3, 13, 39, 41 |
| 15 | 15, 47, 55 |
| 16 | 27, 49 |
| 17 | 33, 35, 53 |
| 18 | 10, 34, 54 |

Every independent set meets each displayed clique in at most one vertex, hence has at most \(18\) vertices and yields at most \(36\) DNA codewords. The certificate is a fully finite list of explicit strings, cliques, and comparisons; it does not assume a numerical solver's optimality assertion.

**4. Matching construction.** The \(18\) orbit indices

`4, 6, 7, 8, 9, 15, 19, 23, 27, 32, 34, 35, 36, 37, 38, 39, 43, 45`

form an independent set of the conflict graph; their \(36\) distinct DNA words, listed in `witness.txt`, are closed under reverse complement. Directly checking all ordered word pairs and all four proper overlap lengths gives no overlap. Therefore \(|C|=36\), meeting the upper bound.

The following is the complete indexed orbit table, which fixes the interpretation of the clique and witness indices. Each entry lists the two codewords in one reverse-complement orbit:

| Orbit ID | DNA words |
|---:|:---|
| 0 | `AAAAG` / `CTTTT` |
| 1 | `AAACT` / `AGTTT` |
| 2 | `AAAGG` / `CCTTT` |
| 3 | `AAAGT` / `ACTTT` |
| 4 | `AAATG` / `CATTT` |
| 5 | `AACAG` / `CTGTT` |
| 6 | `AACCT` / `AGGTT` |
| 7 | `AACGG` / `CCGTT` |
| 8 | `AACTG` / `CAGTT` |
| 9 | `AACTT` / `AAGTT` |
| 10 | `AAGAG` / `CTCTT` |
| 11 | `AAGGG` / `CCCTT` |
| 12 | `AAGGT` / `ACCTT` |
| 13 | `AAGTG` / `CACTT` |
| 14 | `AATAG` / `CTATT` |
| 15 | `AATCT` / `AGATT` |
| 16 | `AATGG` / `CCATT` |
| 17 | `AATGT` / `ACATT` |
| 18 | `ACAAG` / `CTTGT` |
| 19 | `ACACT` / `AGTGT` |
| 20 | `ACAGG` / `CCTGT` |
| 21 | `ACAGT` / `ACTGT` |
| 22 | `ACCAG` / `CTGGT` |
| 23 | `ACCCT` / `AGGGT` |
| 24 | `ACCGT` / `ACGGT` |
| 25 | `ACCTG` / `CAGGT` |
| 26 | `ACGAG` / `CTCGT` |
| 27 | `ACGCT` / `AGCGT` |
| 28 | `ACGGG` / `CCCGT` |
| 29 | `ACTCT` / `AGAGT` |
| 30 | `ACTGG` / `CCAGT` |
| 31 | `ACTTG` / `CAAGT` |
| 32 | `AGACT` / `AGTCT` |
| 33 | `AGAGG` / `CCTCT` |
| 34 | `AGATG` / `CATCT` |
| 35 | `AGCCT` / `AGGCT` |
| 36 | `AGCGG` / `CCGCT` |
| 37 | `AGGGG` / `CCCCT` |
| 38 | `AGGTG` / `CACCT` |
| 39 | `AGTGG` / `CCACT` |
| 40 | `AGTTG` / `CAACT` |
| 41 | `CAAAG` / `CTTTG` |
| 42 | `CAAGG` / `CCTTG` |
| 43 | `CAATG` / `CATTG` |
| 44 | `CACAG` / `CTGTG` |
| 45 | `CACGG` / `CCGTG` |
| 46 | `CACTG` / `CAGTG` |
| 47 | `CAGAG` / `CTCTG` |
| 48 | `CAGGG` / `CCCTG` |
| 49 | `CATAG` / `CTATG` |
| 50 | `CCAAG` / `CTTGG` |
| 51 | `CCAGG` / `CCTGG` |
| 52 | `CCCAG` / `CTGGG` |
| 53 | `CCGAG` / `CTCGG` |
| 54 | `CTAAG` / `CTTAG` |
| 55 | `CTCAG` / `CTGAG` |

## Verification

From the directory containing `certificate.json`, run `python3 verify_exact.py` and `python3 verify_independent.py`. Both use only the Python standard library. The first derives the canonical \(256\) words and the admissible \(56\) orbits, checks all \(412\) conflicts, verifies each of the \(18\) upper-bound cliques, and checks the optimal \(36\)-word witness. The second implements the same conditions by a separate integer-encoded representation, rederiving the graph and all certificate inequalities. Its calculations are independent cross-checks of the elementary finite proof, not a substitute for the canonical-endpoint reduction.

## Relationship to prior work

Non-overlapping codes are also known as cross-bifix-free or mutually uncorrelated codes. Chee, Kiah, Purkayastha and Wang (2012) provide asymptotic constructions and bounds; Blackburn (2013) develops general constructions and short-length results. Stanovnik, Moškon and Mraz (2024) classify maximal codes using prefix/suffix structures and determine unrestricted optima. Table 1 of Stanovnik, Moškon and Mraz (2024) records maximum unrestricted length-five quaternary cardinality \(81\), but an unrestricted optimal code need not be closed under Watson--Crick reverse complement. The value \(36\) is a different constrained optimum and is not an immediate consequence of \(81\).

A separate adjacent-length analysis reports a four-base strand-closed maximum of \(17\); it is not independently reassessed here and is not used in the proof. Its \(20\)-vertex length-four graph cannot imply the \(56\)-vertex length-five graph or the new \(18\)-clique certificate. A separately recorded five-base construction with additional GC-count restrictions reports a \(24\)-word optimum under those stronger hypotheses. That narrower claim cannot bound the full strand-closed family: the present \(36\)-word theorem both removes the GC restriction and supplies a distinct unrestricted-under-GC sharp upper certificate. The earlier finding is used only for statement-level comparison, not as a lemma in the proof.

Reverse-complement-closed orientation-invariant framing, rather than simply a larger unconstrained length, motivates the length-five case: it is the first odd length beyond three, and the absence of fixed reverse-complement orbits is a structural change. The exact value concerns a standard alphabet and a natural fixed-blocklength synchronization invariant, not a general theorem for longer lengths.

## Limitations

The result covers only five-symbol DNA words and exact noiseless overlap avoidance. No inference is made for lengths six and above, for distance-correcting codes, or for the laboratory suitability of individual DNA sequences. Searches of available literature and published research records did not locate this exact constrained cardinality, but non-indexed historical work and potentially inaccessible treatments remain priority risks; no independent historical-priority audit has been performed.

## References

1. Y. M. Chee, H. M. Kiah, P. Purkayastha, C. Wang, *Cross-Bifix-Free Codes Within a Constant Factor of Optimality*, arXiv:1209.0236, public version dated 2012-09-03. https://arxiv.org/abs/1209.0236
2. S. R. Blackburn, *Non-overlapping codes*, arXiv:1303.1026 (2013). https://arxiv.org/abs/1303.1026
3. L. Stanovnik, M. Moškon, M. Mraz, *In search of maximum non-overlapping codes*, Designs, Codes and Cryptography 92 (2024), 1299–1326. https://doi.org/10.1007/s10623-023-01344-z
