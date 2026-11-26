# Rigorous higher-tortoise stabilization thresholds for the regular paperfolding word

## Finding

Let \(\mathbf f=f_1f_2\cdots\) be the regular paperfolding word, with \(f_j=0\) when the odd part of \(j\) is \(1\pmod4\) and \(f_j=1\) when it is \(3\pmod4\). For a finite binary word \(w\), let \(\tau(w)\) delete its first \(1\) and append that \(1\) at the right end; an all-zero word is unchanged. Define \(F_n\) as the set of length-\(n\) contiguous factors of \(\mathbf f\) and

\[
\rho_k(n)=|\{\tau^k(w):w\in F_n\}|.
\]

For \(k\in\{2,3,4,5\}\), let \(s(k)\) be the least integer \(N\ge1\) for which \(\rho_k(n)=|F_n|\) holds for **every** \(n\ge N\). Then all four thresholds exist and are exactly

\[
\boxed{(s(2),s(3),s(4),s(5))=(13,14,25,26).}
\]

Since \(|F_n|=4n\) for \(n\ge7\), these give the sharp onset of \(\rho_k(n)=4n\). The four values were previously reported as computational expectations; the result here supplies finite, complete certificates together with an all-length lifting proof.

## Assumptions and scope

Indices in \(\mathbf f\) begin at \(1\); the alphabet is \(\{0,1\}\). The operation \(\tau\) is the binary specialization of the tortoise map introduced for arbitrary ordered alphabets by Defant and Kravitz. There are no restrictions on where a finite factor starts. The result covers **all** finite lengths above each threshold, not just checked prefixes. It asserts no formula for \(s(k)\) when \(k\ge6\).

## Proof

**Lemma 1 (finite-prefix lifting).** Let \(X\) be any infinite binary word, \(k\ge1\), and \(N\ge1\). Suppose every length-\(N\) factor of \(X\) contains at least \(k+1\) ones. If \(\tau^k\) is injective on length-\(N\) factors, then it is injective on length-\(n\) factors for every \(n\ge N\).

To prove this, write any word \(w\) containing at least \(k+1\) ones uniquely as \(u_0 1 u_1 1\cdots u_k1v\), where each \(u_i\) consists only of zeros and \(v\) is the suffix after the \((k+1)\)-st one. Repeatedly removing the first one yields

\[
\tau^k(w)=0^{|u_0|+\cdots+|u_k|}\,1\,v\,1^k.
\]

Hence, if two length-\(n\) words have equal images, the position of their \((k+1)\)-st one is the same, and their suffixes following that position are identical. The first \(N\) positions of each word include at least \(k+1\) ones; truncating at \(N\) therefore gives length-\(N\) words with equal images. Injectivity at length \(N\) forces these prefixes equal. Their tails from the common \((k+1)\)-st one onward were already equal, so the entire words are equal. This proves the lemma.

**Lemma 2 (complete two-adic factor templates).** Fix \(r\ge1\) and \(1\le n\le2^r\). For each start residue \(a\in\{1,\ldots,2^{r+1}\}\), take positions \(a,\ldots,a+n-1\). At a position not divisible by \(2^r\), use its exact paperfolding bit. If there is a position divisible by \(2^r\), replace that bit by a wildcard, independently taking values \(0\) and \(1\). The union of all resulting words, after duplicate removal, equals **exactly** \(F_n\).

Indeed, every interval of \(n\le2^r\) consecutive indices contains at most one multiple of \(2^r\). At other indices \(j\), the \(2\)-adic valuation is less than \(r\), and the odd part of \(j\) modulo four is determined by \(j\pmod{2^{r+1}}\). Thus the indicated residue templates include all possible factors. Conversely, fix a residue \(a\) and its possible exceptional index \(j=2^rq\). Shifting the start by \(2^{r+1}t\) replaces \(q\) with \(q+2t\). Because \(f_{2^rq}=f_q\), both possible exceptional bits occur: for odd \(q\), its residues modulo four alternate between one and three; for even \(q\), the indices \((q+2t)/2\) range over consecutive positive integers and include odd parts of both residue types. Hence every template variant really occurs in \(\mathbf f\). This proves equality, not merely containment.

**Exact finite certificate.** Apply Lemma 2 with \(r=4\) for lengths \(12,13,14\) and \(r=5\) for lengths \(24,25,26\). For each factor compute its image by literally removing the first \(1\) and appending it, repeated \(k\) times. The complete template tables yield:

| \(k\) | Last colliding length \(N-1\) | Factors / images at \(N-1\) | First injective length \(N\) | Factors / images at \(N\) | Minimum ones in an \(N\)-factor |
|---:|---:|---:|---:|---:|---:|
| 2 | 12 | 48 / 46 | 13 | 52 / 52 | 5 |
| 3 | 13 | 52 / 49 | 14 | 56 / 56 | 5 |
| 4 | 24 | 96 / 94 | 25 | 100 / 100 | 10 |
| 5 | 25 | 100 / 98 | 26 | 104 / 104 | 11 |

For transparency, the following colliding factor pairs occur at the four preceding lengths; each pair has an identical image under the specified iterate:

- \(k=2\), length 12: `000110110001` and `100100110001` (one-based starts 8 and 96).
- \(k=3\), length 13: `0010011100110` and `1011000100110` (starts 17 and 28).
- \(k=4\), length 24: `000100111001101100010011` and `100100110001101100010011` (starts 16 and 192).
- \(k=5\), length 25: `1000100111001101100010011` and `1100100110001101100010011` (starts 15 and 191).

The check is finite and exhaustive by Lemma 2, using at most \(2^{r+2}\) template variants in each case; the standalone `verify.py` and `certificate.json` reproduce the complete tables and collisions. As the final column is at least \(k+1\) in every row, Lemma 1 proves injectivity at **every** length at or above the displayed \(N\). The listed collisions exclude any smaller eventual threshold. Thus the four claimed values of \(s(k)\) are exact.

## Verification

Run `python verify.py` in the directory containing `certificate.json` (Python standard library only). The verifier reconstructs the two-adic templates, checks their distinct-image counts and minimum one-counts, verifies the explicit collisions, and compares the exact outputs with `certificate.json`. A separate finite cross-check independently enumerates factors of a 16,384-bit paperfolding prefix; this cross-check is supplementary and is **not** used to justify the all-length statement. `verification_output.txt` records the checker output. The infinite conclusion depends on the proved completeness of the templates and Lemma 1, not on extrapolation from the prefix.

## Relationship to prior work

Campbell and Rampersad introduce tortoise complexity for automatic sequences. Their Theorem 3 proves the \(k=1\) paperfolding stabilization at length eight; immediately afterward they report the numerical predictions \(13,14,25,26\) for \(k=2,3,4,5\) as computations that *appear* to hold, without proving those four infinite-length assertions (arXiv:2604.25811v2, Section 5). The numerical values are therefore not claimed as newly discovered data. The new contribution is their complete proof, using a general prefix-lifting lemma and an explicit two-adic enumeration of **all**, not merely sampled, critical factors. Defant and Kravitz introduced the underlying tortoise map, but did not analyze these paperfolding factor-complexity thresholds. Allouche's factor-count formula \(|F_n|=4n\), \(n\ge7\), supplies the standard conversion from injectivity to the complexity values.

## Limitations

The argument is specific to the regular paperfolding word and the four stated iterate counts. It provides a reproducible finite exact certificate whose completeness rests on the elementary two-adic factor rule. It does not determine a general recurrence or growth law for \(s(k)\) at larger \(k\). Historical priority under different terminology remains possible; independent validation has not been performed.

## References

1. J. M. Campbell and N. Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811v2 (2026), Sections 2, 3 and 5; original submission 2026-04-28. https://arxiv.org/abs/2604.25811
2. C. Defant and N. Kravitz, *Stack-sorting for words*, Australasian Journal of Combinatorics 77(1) (2020), 51–68, Definition 1.1. https://ajc.maths.uq.edu.au/pdf/77/ajc_v77_p051.pdf
3. J.-P. Allouche, *The number of factors in a paperfolding sequence*, Bulletin of the Australian Mathematical Society 46(1) (1992), 23–32. Cited and used in Reference 1, Section 5.
