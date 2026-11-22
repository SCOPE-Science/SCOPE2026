# Sharp first five-bit synchronization payload under one-sided binary run limitation

## Finding

Let \(\mathcal F_n=\{w\in\{0,1\}^n: \text{the factor `11' does not occur in }w\}\). A code \(C\subseteq\mathcal F_n\) is **non-overlapping** (cross-bifix-free) if for all \(u,v\in C\), including \(u=v\), and every integer \(1\le j<n\), the length-\(j\) prefix of \(u\) differs from the length-\(j\) suffix of \(v\).

The largest size \(M_n\) of such a code, for \(1\le n\le16\), is exactly

\[
(M_1,\ldots,M_{16})=(2,1,1,1,1,1,2,2,3,5,7,9,14,20,30,42).
\]

Consequently, **16 is the shortest fixed blocklength allowing 32 distinguishable codewords** (a five-bit payload) under both conditions: at length 15 only 30 codewords are possible, while a certified family of 42 is available at length 16. Among the standard binary fixed-zero-marker families of Chee--Levenshtein form intersected with \(\mathcal F_{16}\), the largest has 24 codewords. The constrained optimum therefore carries one additional whole payload bit compared with those marker families at this blocklength.

## Assumptions and scope

Words are ordered binary strings, not necklaces. All proper overlap lengths are forbidden, in both orientations and even within a single word. The constraint `11` applies to each word internally; it is not imposed across successive transmitted codewords. Codeword length is an integer from 1 through 16. This is a noiseless frame-synchronization problem, not a substitution- or deletion-correcting code problem.

## Proof

Define \(V_n\) to be the unbordered words in \(\mathcal F_n\), i.e., the words whose proper prefixes are different from their corresponding-length suffixes. Construct a simple graph \(G_n\) on \(V_n\): two different vertices are adjacent precisely when neither has a proper prefix equal to a suffix of the other. By definition, every admissible code consists of vertices of \(G_n\) and is a clique, and conversely every clique is an admissible code. Hence \(M_n=\omega(G_n)\).

The accompanying `verify.py` is a terminating, exact-integer exhaustive algorithm for \(\omega(G_n)\). It first constructs **all** words avoiding `11` by appending a bit in every permitted way, deletes precisely those with self-overlaps, and tests all vertex pairs for all overlap lengths. A second implementation using integer shifts rechecks every resulting edge independently of the string-slicing tests. For small orders, a third language generator using Cartesian products is compared with the recursive one.

For the clique upper bound the algorithm uses a branch-and-bound procedure. Each recursive call holds a clique \(Q\) and a set \(P\) of vertices adjacent to all vertices of \(Q\). It greedily colors the induced graph on \(P\) with proper color classes and orders its vertices by increasing color index. A clique among the first \(i\) vertices has at most as many members as the highest color index on that prefix. Processing these vertices from last to first, the algorithm branches on taking a vertex \(v\), replacing \((Q,P)\) by \((Q\cup\{v\},P\cap N(v))\), and then removes \(v\) from the remaining parent candidates. Thus every clique is either examined in a branch or excluded only when its possible size is at most the incumbent. This is a complete finite proof of the matching upper bounds, not an inference from the samples of codewords.

The same program retains one largest clique for every length and independently checks all codeword pairs and every proper overlap. Its output table is reproduced below. The file `certificates.json` contains the complete codebooks and deterministic visited-node counts; no external solvers or external files are required.

| \(n\) | \(|\mathcal F_n|\) | \(|V_n|\) | \(M_n\) | search nodes |
|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 3 |
| 2 | 3 | 2 | 1 | 2 |
| 3 | 5 | 2 | 1 | 2 |
| 4 | 8 | 2 | 1 | 2 |
| 5 | 13 | 4 | 1 | 2 |
| 6 | 21 | 4 | 1 | 2 |
| 7 | 34 | 8 | 2 | 3 |
| 8 | 55 | 10 | 2 | 3 |
| 9 | 89 | 18 | 3 | 4 |
| 10 | 144 | 24 | 5 | 6 |
| 11 | 233 | 42 | 7 | 19 |
| 12 | 377 | 62 | 9 | 24 |
| 13 | 610 | 104 | 14 | 44 |
| 14 | 987 | 158 | 20 | 473 |
| 15 | 1597 | 262 | 30 | 3944 |
| 16 | 2584 | 410 | 42 | 308053 |

For comparison with the classical marker construction, reverse the Chee--Levenshtein family to words starting with `1`, ending with \(k\) zeros preceded by `1`, and with no \(k\) consecutive zeros before that suffix; intersect with the words avoiding `11`. The program enumerates every integer \(2\le k\le n-2\), checks non-overlap, and finds maximum size 24 at \(n=16\), attained at \(k=5\). These are restricted marker constructions; the comparison does not assert optimality among other proposed constructions.

## Verification

Place `verify.py` and `certificates.json` together and run `python3 verify.py` with Python 3.10 or later. The checker recomputes all source words, independently compares graph edges through binary-mask arithmetic, recomputes every maximum clique, checks the published codebooks and marker-family comparison, and finishes with `VERIFY_OK`. Every computation uses exact integer operations. The length-16 search considers 410 unbordered eligible vertices and visits 308,053 branch-and-bound nodes. This is a finite exhaustive proof, not a randomized trial or extrapolation.

## Relationship to prior work

Chee, Kiah, Purkayastha and Wang introduced general cross-bifix-free constructions and optimal small unrestricted binary instances [1]. Blackburn developed size bounds and constructions for unrestricted non-overlapping codes [2]. Stanovnik, Moškon and Mraz characterized the unrestricted maximum-code problem and presented unrestricted exact tables [3], then developed general methods for run-limited and balanced non-overlapping codes [4]. The length-16 finite calculation here imposes the **asymmetric** restriction `11` on every codeword and determines its exact capacity and the resulting first five-bit threshold. It is not an unrestricted or symmetric maximum-run-length calculation. The general methods in [4] motivate the question and could in principle be specialized, but the inspected statements and tables do not specify the capacity sequence above.

## Limitations

All asserted capacity values are confined to \(1\le n\le16\). The 16-bit conclusion is not an asymptotic rate theorem, and the exact finite algorithm is not a closed-form capacity formula. The codewords are not certified against noise, substitutions, insertions or deletions. This self-review is not independent mathematical validation. Unindexed equivalent finite tables or earlier implicit computations could affect historical priority.

## References

1. Y. M. Chee, H. M. Kiah, P. Purkayastha and C. Wang, *Cross-Bifix-Free Codes Within a Constant Factor of Optimality*, arXiv:1209.0236 (first public version, 2012-09-03), https://arxiv.org/abs/1209.0236.
2. S. R. Blackburn, *Non-overlapping codes*, arXiv:1303.1026 (first public version, 2013-03-05), https://arxiv.org/abs/1303.1026.
3. L. Stanovnik, M. Moškon and M. Mraz, *In search of maximum non-overlapping codes*, Designs, Codes and Cryptography 92 (2024), https://doi.org/10.1007/s10623-023-01344-z.
4. L. Stanovnik, M. Moškon and M. Mraz, *On maximal almost balanced non-overlapping codes and non-overlapping codes with restricted run-lengths*, Computational and Applied Mathematics (2025), https://doi.org/10.1007/s40314-024-03055-0.
