# Sharp first-covering depths and unique last residue in eleven dyadic Stern-pair graphs

## Finding

For Stern's diatomic sequence defined by \(s(0)=0\), \(s(1)=1\), \(s(2n)=s(n)\) and \(s(2n+1)=s(n)+s(n+1)\), put
\[
\mathcal P_k=\{(a,b)\pmod{2^k}:a\text{ or }b\text{ is odd}\},\qquad
R_k=\min\{r\ge0:\{(s(n),s(n+1))\pmod{2^k}:0\le n<2^r\}=\mathcal P_k\}.
\]
The following table gives the **exact** minimum covering depth for every integer \(1\le k\le11\). The final column gives the smallest index attaining the unique residue pair absent one depth earlier.

| \(k\) | Modulus \(2^k\) | Primitive pairs | Exact \(R_k\) | Least index of last pair |
|---:|---:|---:|---:|---:|
| 1 | 2 | 3 | 2 | 2 |
| 2 | 4 | 12 | 5 | 19 |
| 3 | 8 | 48 | 8 | 184 |
| 4 | 16 | 192 | 11 | 1,291 |
| 5 | 32 | 768 | 14 | 10,708 |
| 6 | 64 | 3,072 | 18 | 140,455 |
| 7 | 128 | 12,288 | 20 | 676,171 |
| 8 | 256 | 49,152 | 23 | 5,416,267 |
| 9 | 512 | 196,608 | 26 | 43,348,660 |
| 10 | 1024 | 786,432 | 30 | 575,329,636 |
| 11 | 2048 | 3,145,728 | 33 | 4,920,978,067 |

For \(k=1\), the unique pair absent at depth \(R_k-1\) is \((1,0)\pmod2\). For **every** \(2\le k\le11\), it is exactly
\[
(-1,-1)\pmod{2^k}.
\]
Every other primitive pair already occurs among \(0\le n<2^{R_k-1}\), and the last pair first appears at the index tabulated above. Hence none of the displayed covering depths can be reduced. In particular, modulo \(2048\), exactly one of the \(3\,145\,728\) primitive pairs is missing below \(2^{32}\), and every one occurs below \(2^{33}\). The increments of the depths are not constant: the jumps at \(k=6\) and \(k=10\) are both four.

## Assumptions and scope

The theorem concerns the complete initial range of dyadic precisions \(1\le k\le11\), nonnegative ordinary integer indices, and the simultaneous ordered pair of consecutive Stern values. A covering depth \(r\) means the exact half-open interval \(0\le n<2^r\), including \(n=0\), not the single Calkin–Wilf level or an arbitrary cutoff. A pair is *primitive modulo* \(2^k\) precisely when its two coordinates are not both even. No claim is made for \(k\ge12\), for odd moduli, or for a general formula for the radii.

## Proof

**1. The exact finite graph.** Fix \(k\) in the stated range, write \(m=2^k\), and encode \((a,b)\in(\mathbb Z/m\mathbb Z)^2\) by \(a m+b\) using representatives in \(\{0,\ldots,m-1\}\). The recurrence gives the *exact* transitions
\[
L(a,b)=(a,a+b),\qquad R(a,b)=(a+b,b)\pmod m,
\]
starting at \(S(0)=(0,1)\). By induction on the binary word for \(n\), every word of length \(r\) in \(L,R\), with zero digits first and leading zeros allowed, yields exactly \(S(n)=(s(n),s(n+1))\) for a unique index \(0\le n<2^r\). The map \(L\) fixes \((0,1)\), so the set attained through depth \(r\) is the set of graph vertices within directed distance at most \(r\). The maps preserve primitivity because adding one coordinate to the other preserves their gcd with \(m\). There are exactly \(3m^2/4\) primitive states.

**2. Complete exhaustive certificate.** The bundled `check.py` implements breadth-first search from \((0,1)\) on precisely these explicitly defined transitions. For each discovered state it records its exact first distance; repeated states are skipped. Its queue exhausts all vertices reachable in this finite graph. The checker then separately visits *every* one of the \(m^2\) possible states and asserts that it was reached if and only if at least one coordinate is odd. This proves that the visited graph is the entire \(3m^2/4\)-element permitted state space rather than a sampled subset. The shortest-path histogram at each level is computed from first-visit distances and saved in `census.json`. All eleven histograms have a final layer consisting of exactly one state, with the target residue asserted against the stated pair. Their largest nonempty layer indices are exactly the tabulated depths. This is finite exhaustive proof for the stated eleven moduli, not extrapolation from partial enumeration.

**3. The least indices.** In the breadth-first queue, children are visited in the binary order zero then one. Consequently the first word discovered at any state is the lexicographically least among shortest words reaching it. Because shorter binary words, padded with leading zeros, were already considered at earlier levels, its integer value is the *smallest nonnegative index* with that residue pair. The `first` array in `check.py` records this word exactly with unsigned 64-bit integers; every index here is below \(2^{33}\). Independently, the program recomputes the integer Stern recurrence for all indices up to the target for \(1\le k\le6\) and performs separate set-frontier searches for \(1\le k\le7\). The full graph check and these independent finite cross-checks agree.

## Verification

Use Python 3.9 or later, standard library only. From the directory containing the two included artifacts, run `python3 check.py`; successful execution ends with `EXACT_CENSUS_AND_INDEPENDENT_CROSSCHECKS_PASSED`. The program checks all \(3\,145\,728\) primitive states modulo \(2048\), and for each smaller modulus checks the full primitive state space. It regenerates `census.json` with every shortest-distance histogram, unique final pair, and least arrival index. It also performs independent layer checks for the seven smallest moduli and direct full-index checks for the six smallest moduli. No external computational package or third-party data is needed. A nonterminating computation would not be evidence of impossibility; here the entire finite queue terminates and every allowed vertex is accounted for.

## Relationship to prior work

Reznick's *Regularity properties of the Stern enumeration of the rationals* establishes surjectivity and equidistribution for the same adjacent Stern-pair state graph modulo arbitrary fixed integers. Its Section 4 describes the two graph moves and proves eventual positivity of sufficiently large transfer powers, but supplies no least first-covering depth, exhaustive dyadic power-of-two diameter table, or unique penultimate missing pair. Published follow-up work proves joint modular/digit-weight equidistribution and the dyadic discrepancy exponent of a pair modulo nine; these are asymptotic and do not imply the exact finite first-coverage statements. A separate exact modulo-eight *single-coordinate* histogram does not recover full ordered-pair covering at each precision. Thus the finite cutoffs are additional data beyond the known general existence results.

## Limitations

The uniform last-pair pattern is **proved only for the eleven listed exponents**; the theorem neither claims nor suggests that it must persist indefinitely. It is an exact computation-assisted finite theorem, not an infinite asymptotic bound and not a classification of all moduli. The complete exhaustive algorithm is short and independently replayable; its full finite search is essential to the proof. An earlier unpublished or unindexed first-coverage table, or an implicit specialization of an exact general graph-diameter theorem, remains a historical originality risk. No independent mathematical audit is asserted.

## References

1. B. Reznick, *Regularity properties of the Stern enumeration of the rationals*, first public arXiv posting 19 October 2006, https://arxiv.org/abs/math/0610601 ; Section 4.
2. *Binary-digit-weight independence for Stern diatomic residues* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-binary-digit-weight-independence-for-stern-diatomic-residues--9c2ceec9f9d1 .
3. *Sharp non-square-root dyadic discrepancy for a Stern residue pair modulo nine* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-non-square-root-dyadic-discrepancy-for-a-stern-residue-pai--57068b08083f .
4. *Complete modulo-eight residue spectra of Stern's diatomic sequence on dyadic blocks* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-complete-modulo-eight-residue-spectra-of-stern-s-diatomic-sequen--67fcd3f4bd6d .
