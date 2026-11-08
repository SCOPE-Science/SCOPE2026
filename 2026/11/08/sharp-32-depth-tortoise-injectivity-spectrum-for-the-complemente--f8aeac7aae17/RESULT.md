# Sharp 32-depth tortoise-injectivity spectrum for the complemented period-doubling word

## Finding

Let \(\mu(1)=10\), \(\mu(0)=11\), and let \(\mathbf d=\mu^\omega(1)\) be its right-infinite fixed point, with the ordered binary alphabet \(0<1\). On a finite binary word define \(T(w)\) by deleting the first \(1\) and appending \(1\); if no \(1\) occurs, leave the word unchanged. Let \(\mathcal F_n\) be the distinct length-\(n\) factors of \(\mathbf d\), and put

\[
 s(k)=\min\{N\ge1: T^k\text{ is injective on }\mathcal F_n\text{ for every }n\ge N\}.
\]

For **every** integer \(1\le k\le32\), this minimum exists and has the following exact values. Each length immediately preceding the displayed threshold has exactly **one** nontrivial \(T^k\)-fiber, of size two. At the threshold and every greater length there are no collisions.

| \(k\) | \(s(k)\) | \(|\mathcal F_{s(k)}|\) | \(k\) | \(s(k)\) | \(|\mathcal F_{s(k)}|\) |
|---:|---:|---:|---:|---:|---:|
| 1 | 5 | 8 | 17 | 75 | 118 |
| 2 | 9 | 14 | 18 | 76 | 120 |
| 3 | 17 | 26 | 19 | 77 | 122 |
| 4 | 19 | 30 | 20 | 79 | 126 |
| 5 | 20 | 32 | 21 | 80 | 128 |
| 6 | 33 | 50 | 22 | 129 | 194 |
| 7 | 35 | 54 | 23 | 131 | 198 |
| 8 | 36 | 56 | 24 | 132 | 200 |
| 9 | 37 | 58 | 25 | 133 | 202 |
| 10 | 39 | 62 | 26 | 135 | 206 |
| 11 | 65 | 98 | 27 | 137 | 210 |
| 12 | 67 | 102 | 28 | 139 | 214 |
| 13 | 68 | 104 | 29 | 140 | 216 |
| 14 | 69 | 106 | 30 | 141 | 218 |
| 15 | 71 | 110 | 31 | 143 | 222 |
| 16 | 73 | 114 | 32 | 144 | 224 |

In particular the first large jumps are \(s(2)=9\), \(s(3)=17\), \(s(6)=33\), \(s(11)=65\), and \(s(22)=129\). This exact finite-depth spectrum does not imply any asserted recurrence or asymptotic law for uncomputed depths.

## Assumptions and scope

The language is the factor language of the **complemented** period-doubling word \(\mu^\omega(1)\); complementing letters is not an invariant operation for \(T\), since it changes which symbol is removed. All factors are contiguous and distinct, and indices refer to nonnegative word positions. Iteration depth ranges from \(1\) through \(32\), while the word length ranges over **all positive integers**, including arbitrarily large lengths. The table gives sharp eventual injectivity thresholds, not the entire tortoise-complexity sequence below them.

## Proof

**1. An exact finite factor-language certificate.** The substitution is uniform of length two. Its length-two language is precisely \(\{01,10,11\}\). For a given \(n\ge1\), take \(q=\lceil\log_2 n\rceil\) and define \(B_c=\mu^q(c)\) for \(c\in\{0,1\}\). Since \(n\le2^q\), every factor of length \(n\) lies in two consecutive blocks of the canonical \(q\)-block decomposition. Conversely, every allowed adjacent letter pair actually appears in \(\mathbf d\). Thus, with \(\operatorname{Fact}_n\) denoting distinct length-\(n\) substrings,

\[
 \mathcal F_n=\bigcup_{ab\in\{01,10,11\}}\operatorname{Fact}_n(B_aB_b).
\]

This is an **equality**, not a sampled-prefix approximation. The assertion about the two-letter language follows directly from \(\mu(1)=10\), \(\mu(0)=11\) and the presence of \(10,01,11\) in a finite iterate. In particular no factor contains \(00\), and every length-\(n\) factor contains at least \(\lfloor n/2\rfloor\) ones.

**2. The prefix-inheritance lemma.** Let \(k,N\) be positive with \(N\ge2k\), and assume \(T^k\) is injective on \(\mathcal F_N\). Then it is injective on \(\mathcal F_n\) for all \(n\ge N\). Indeed, the first \(N\) symbols of each such factor contain at least \(k\) ones. Iterating the tortoise map therefore removes precisely those first \(k\) ones and appends \(k\) ones, yielding a core of length \(n-k\) followed by \(1^k\). If two length-\(n\) factors had equal output, their cores would agree; restricting their cores to the first \(N-k\) symbols gives equal tortoise images of their length-\(N\) prefixes. By injectivity these prefixes agree. Their first \(k\) deletion positions are therefore identical, so equality of their undeleted cores also forces the original length-\(n\) factors to agree. This contradicts a collision.

**3. Finite calculations with full coverage.** For every table row, use the exact two-superblock expression in step 1 at lengths \(s(k)-1\) and \(s(k)\). The \(T^k\)-image partition at the earlier length has exactly one size-two fiber and no other non-singleton fibers; the output partition at \(s(k)\) is discrete. The table supplies the cardinality of the latter factor set; the attached `thresholds.csv` supplies the earlier collision witnesses for all 32 depths. Each listed threshold is at least \(2k\), so step 2 extends finite injectivity to **every** greater length. The collision at the immediately preceding length proves that a smaller eventual threshold is impossible, even if other shorter lengths happen to have no collision.

The finite calculations are reproducible, and the accompanying `verify.py` independently builds the word using the valuation formula \(d_i=1-(\nu_2(i+1)\bmod2)\), compares its factor sets against the two-superblock enumeration, checks iterative and direct-delete implementations of \(T^k\), verifies all witnesses, and checks exactly one size-two nontrivial fiber at every penultimate length. The finite enumeration is a complete certificate at those lengths because of step 1; the lemma, not testing of longer lengths, supplies the infinite conclusion.

## Verification

Run `python3 verify.py` in the same directory as `thresholds.csv`. Successful execution prints `PERIOD_DOUBLING_REVERSED_TORTOISE_VERIFY_OK 32`. It uses only the Python standard library. The same factor sets are reconstructed by two different descriptions: adjacent substituted superblocks (exhaustive by proof) and a directly generated valuation prefix (cross-check, not the exhaustiveness argument). The table has 32 rows and explicitly lists each pair whose equal image proves sharpness.

## Relationship to prior work

Campbell and Rampersad (2026) introduced and developed tortoise complexity for automatic sequences, especially the paperfolding and Thue–Morse words, and asked for additional relationships between ordinary and tortoise factor complexity. The present result gives a sharp multidepth completion for a different canonical automatic word. A separate earlier one-step result for the standard, **noncomplemented** period-doubling presentation concerns the operation deleting the first \(1\) there; after complementing, that operation corresponds to deleting the first \(0\) here. It does not imply the values above for the first-\(1\) operator on the complemented word. The distinction demonstrates genuine dependence on the ordered alphabet, rather than invariance under exchanging symbol names.

## Limitations

No theorem for all iteration counts is asserted; the fully checked range is exactly \(1\le k\le32\). The table is not a closed-form rule for future depths and does not enumerate the full complexity below each threshold. The result applies to this specified fixed point and ordered alphabet; it does not automatically extend to arbitrary period-doubling codings or arbitrary automatic words. Independent mathematical audit and definitive literature-priority confirmation have not been performed.

## References

1. J. M. Campbell and N. Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811 (first submitted 2026-04-28). https://arxiv.org/abs/2604.25811
2. C. Defant and N. Kravitz, *Stack-sorting for words* (2020), cited in reference 1.
3. J.-P. Allouche and J. Shallit, *Automatic Sequences*, Cambridge University Press (2003), standard background on uniform morphic words.
