# First fractional-packing gap and rebound for adjacent-swap codes on Fibonacci words

## Finding

Consider linear binary strings of length \(n\) avoiding adjacent ones, with a communication channel allowing **at most one adjacent transposition of two neighboring unequal bits**, including no error. Only transmitted strings must avoid `11`; the received string is unrestricted. Let \(M_n\) be the greatest cardinality of an error-correcting code whose distinct source words have disjoint complete sets of possible outputs. Let \(P_n\) be the optimum of the natural fractional *output-shadow packing* linear program, and let \(N_n\) count all labeled optimum codebooks, without quotienting by reversal.

**Theorem (complete initial profile).** For each integer \(1\le n\le 10\), these invariants are as follows. All values are exact:

| \(n\) | \(M_n\) | \(P_n\) | \(N_n\) |
|---:|---:|---:|---:|
| 1 | 2 | 2 | 1 |
| 2 | 2 | 2 | 2 |
| 3 | 3 | 3 | 3 |
| 4 | 4 | 4 | 3 |
| 5 | 6 | 6 | 9 |
| 6 | 8 | 8 | 24 |
| 7 | 12 | \(61/5\) | 56 |
| 8 | 18 | 18 | 24 |
| 9 | 25 | \(126/5\) | 1260 |
| 10 | 38 | \(115/3\) | 480 |

The *first strict fractional gap* is at \(n=7\), where \(P_7-M_7=1/5\). Equality returns at \(n=8\), and strict gaps occur again at \(n=9\) and \(n=10\). All ten cases satisfy \(M_n=\lfloor P_n\rfloor\); **there is no assertion of an integer-rounding failure**. At \(n=7\), precisely four of the 56 maximum codebooks are invariant under word reversal, giving 30 reversal classes. At \(n=8\), none of the 24 maximum codebooks is reversal-invariant, giving 12 reversal classes.

## Assumptions and scope

All words are linear and coordinate positions are labeled. Define
\[
\mathcal F_{n,k}=\{w\in\{0,1\}^n:\ |w|_1=k,\ \text{no adjacent coordinates both equal }1\},\quad
\mathcal F_n=\bigcup_{k=0}^{\lceil n/2\rceil}\mathcal F_{n,k}.
\]
For every \(w\in\mathcal F_n\), define its complete radius-one adjacent-swap output set
\[
B(w)=\{w\}\cup\{w_1\cdots w_{i-1}w_{i+1}w_iw_{i+2}\cdots w_n:
1\le i<n,\ w_i\ne w_{i+1}\}.
\]
**Outputs may contain `11`.** No circular wraparound swap is allowed, and neither deletions nor substitutions are permitted. A code \(C\subseteq\mathcal F_n\) corrects this channel if \(B(u)\cap B(v)=\varnothing\) for every two distinct \(u,v\in C\). The fractional packing program is
\[
P_n=\max\left\{\sum_{w\in\mathcal F_n}x_w:
 x_w\ge0,\ \sum_{w:\,z\in B(w)}x_w\le1\text{ for all }z\in\bigcup_{w\in\mathcal F_n}B(w)\right\}.
\]
Here a labeled codebook is an unordered *set of distinct codewords*. Its reversal is obtained by reversing every word; codebooks are not identified by reversal when computing \(N_n\). The theorem makes no assertion for \(n>10\).

## Proof

**1. Exact weight decomposition.** An adjacent swap preserves the number of ones. Hence output sets from distinct weights are disjoint, and both optimization problems split into independent fixed-weight problems. If \(M_{n,k}\), \(P_{n,k}\), and \(N_{n,k}\) denote the corresponding quantities for sources in \(\mathcal F_{n,k}\), then
\[
M_n=\sum_k M_{n,k},\qquad P_n=\sum_k P_{n,k},\qquad N_n=\prod_k N_{n,k}.
\]
The same product rule applies to the number of reversal-fixed optimal codebooks because reversal also preserves weight. Every allowed source is enumerated exactly once as a binary word of length \(n\) with the stated weight and forbidden factor.

**2. Exact finite integer upper and lower bounds.** For a fixed \(n,k\), list all sources \(w_0,\ldots,w_{r-1}\) in lexicographic order and calculate their output sets \(B(w_i)\). Form the *confusability graph* with edge \(ij\) precisely when \(i\ne j\) and \(B(w_i)\cap B(w_j)\ne\varnothing\). Correcting codebooks are exactly its independent sets. For any subset \(S\) of vertices, let \(\alpha(S)\) be its independence number, and \(c(S)\) the number of independent sets with exactly \(\alpha(S)\) vertices. Initialize \(\alpha(\varnothing)=0\), \(c(\varnothing)=1\). For any chosen vertex \(v\in S\), put
\[
a=\alpha(S\setminus\{v\}),\qquad
b=1+\alpha(S\setminus(\{v\}\cup N(v))).
\]
Then \(\alpha(S)=\max(a,b)\). For its number of maximizers, use the count of the exclusion branch if \(a>b\), the count of the inclusion branch if \(b>a\), or the sum of both counts if \(a=b\). These branches partition **all** independent sets according to whether they contain \(v\); there is no heuristic or search-timeout step. The supplied `verify.py` executes this recurrence exactly with arbitrary-precision integer bitmasks and memoization for all 40 nonempty pairs \((n,k)\) with \(1\le n\le10\). The supplied `certificate.json` includes an explicit independent-set witness for every pair. Its checker verifies every word and every pair of output balls, establishing attainability separately from the exhaustive upper bound and optimizer census.

**3. Exact fractional upper and lower bounds.** For each fixed-weight instance, the certificate supplies two **nonnegative rational** vectors, \(x\) indexed by sources and \(y\) indexed by possible outputs. These satisfy
\[
\sum_{w:z\in B(w)}x_w\le1\quad\text{for every output }z,\qquad
\sum_{z\in B(w)}y_z\ge1\quad\text{for every source }w,
\]
and \(\sum_w x_w=\sum_z y_z=P_{n,k}\). The first vector is a feasible primal packing; the second is a feasible dual covering. Weak LP duality proves that their common sum is *exactly* \(P_{n,k}\). All numeric entries are stored as integer or reduced fraction strings, and the standard-library checker recomputes every inequality and equality with exact rational arithmetic. Summing these values by weight yields the stated \(P_n\), with no numerical LP tolerance in the proof.

**4. Reversal census.** For \(n=7,8\), the checker enumerates every maximizing independent set at each weight using the same exhaustive inclusion/exclusion recurrence; it tests equality under the coordinate-reversal permutation of the source list. Multiplying the numbers of choices and of fixed choices across weights gives 56 total / 4 fixed at order seven, and 24 total / 0 fixed at order eight. Burnside's lemma for the two-element reversal group gives respectively \((56+4)/2=30\) and \(24/2=12\) orbits.

Every loop covers a finite, explicitly enumerated source/output set; these steps prove the full table for the **specified range**, not merely sample-based evidence. At the first gap, the sole nonintegral contribution comes from weight two: \(M_{7,2}=4\) versus \(P_{7,2}=21/5\). At \(n=8\), all weight contributions coincide. At \(n=9\), the nonintegral contribution comes from weight four, while at \(n=10\) it comes from weight two.

## Verification

Place `verify.py` and `certificate.json` in the same folder and run `python3 verify.py` with Python 3 and only the standard library. The verifier re-creates all \(\mathcal F_{n,k}\) and all output balls without relying on stored incidence matrices, checks the explicitly listed maximizing codebooks, exhaustively computes the exact integer optima and optimizer counts, and verifies each rational primal/dual certificate. It also enumerates the reversal-fixed optima at orders seven and eight. The expected terminal marker is `VERIFY_OK`, followed by the ten rows and the reversal counts. The code was executed against the actual packaged certificate and passed. In a separate implementation, each weight's integer optimum was independently reconstructed through mixed-integer output-incidence constraints, agreeing across all 40 weight instances; this auxiliary check is not required for the standalone proof.

## Relationship to prior work

Sloane's publicly indexed adjacent-transposition code sequence OEIS A057608 (entry originally dated October 9, 2000) gives unrestricted binary code sizes, not the optimum obtained after forbidding `11` at the source. Gómez Soto, Leaños, Ríos-Castro and Rivera (2017 preprint, 2018 publication) solve the weight-two problem on *all* binary words, equivalent to a two-token path-graph packing; it does not determine the weight-two problem on the restricted independent-position language, let alone the other weights or fractional profiles. Kovačević (2018 preprint) studies bit-shift correction with \((d,k)\) run constraints; its main bounds are asymptotic and its precise finite source convention has prescribed endpoint markers, so neither its inequalities nor constructions yield this exact unguarded finite table. Kovačević, Kiah and Goyal (2025 preprint, subsequent revision) study unrestricted-alphabet adjacent transpositions, with general and asymptotic results, not these finite restricted LP and equality data.

Castro, Klavžar, Mollard and Rho's 2010–2011 2-packing study counts Fibonacci-cube packings under **single-bit Hamming adjacency**, a different graph from the weight-preserving adjacent-swap channel here. Kulkarni and Kiyavash's 2012 fractional-shadow framework addresses **deletions**, a different output length, although its packing methodology motivates the natural relaxation here. Other published results on constrained-source deletion codes and directed weight-two shifts have different errors, and their exact statements do not imply the displayed values. The present contribution is the finite constrained-source exact profile, its first fractional gap and return to equality, and the labeled/reversal optimizer census—not the definition of shift correction, the general packing method, or unrestricted finite-code calculations.

## Limitations

No asymptotic capacity, general formula for all lengths, integer-rounding failure, or independent external mathematical audit is claimed. The values depend on exactly the stated source constraint, bidirectional single adjacent-swap channel, unmarked endpoints and output-alphabet convention. Although relevant primary full texts, public databases and closely related published results were compared, older or unindexed equivalent finite data may still exist; independent historical-priority review remains warranted.

## References

1. N. J. A. Sloane, OEIS A057608, *Maximal size of binary code of length n that corrects one transposition*, entry dated 2000-10-09, https://oeis.org/A057608.
2. J. M. Gómez Soto, J. Leaños, L. M. Ríos-Castro, L. M. Rivera, *The packing number of the double vertex graph of the path graph*, arXiv:1711.03682 (2017), https://arxiv.org/abs/1711.03682; author-hosted full text: https://matematicas.reduaz.mx/~jmgomez/jmgomezweb/Publications_files/7-PackingGraph2018.pdf.
3. M. Kovačević, *Runlength-Limited Sequences and Shift-Correcting Codes: Asymptotic Analysis*, arXiv:1803.06117 (2018), https://arxiv.org/abs/1803.06117.
4. M. Kovačević, H. M. Kiah, K. Goyal, *Bounds on Codes Correcting Adjacent Transpositions*, arXiv:2509.06692 (first posted 2025), https://arxiv.org/abs/2509.06692.
5. A. Castro, S. Klavžar, M. Mollard, Y. Rho, *On the domination number and the 2-packing number of Fibonacci cubes and Lucas cubes*, Computers & Mathematics with Applications 61 (2011), https://doi.org/10.1016/j.camwa.2011.03.012.
6. A. A. Kulkarni and N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, arXiv:1211.3128 (2012), https://arxiv.org/abs/1211.3128.
7. S. Wang, V. K. Vu, V. Y. F. Tan, *Codes for Correcting Asymmetric Adjacent Transpositions and Deletions*, arXiv:2301.11680 (2023), https://arxiv.org/abs/2301.11680.
