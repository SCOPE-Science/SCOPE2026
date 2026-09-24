# Independent audit — 2026-09-22 campaign

**Record:** `2026/09/08/039`  
**Audit date (UTC):** 2026-09-24  
**Audited public head:** `47f38581ee43f67fa9ed5470f5640a60e68ef11a`  
**Audited source-tree SHA:** `2c2b6e88133d0bddf9fde08b818b41ee1019ada3`  
**RESULT.md blob:** `39275103e6c3648d83b529bb49c6dca3f7915cb6`  
**Reviewer:** separate AI independent audit for the SCOPE three-axis campaign.

## Scope and claim extracted

The record asserts an exhaustive finite census of longest-increasing-subsequence (LIS) lengths for all 231-avoiding permutations at `n=9` and `n=10`. It gives the rows

- `n=9`: `1,36,336,1176,1764,1176,336,36,1`;
- `n=10`: `1,45,540,2520,5292,5292,2520,540,45,1`;

and observes that both equal the Narayana values
`N(n,k)=(1/n) binom(n,k) binom(n,k-1)`. It also gives a recursive Dyck-path map and claims, for every generated object through `n=10`, that LIS equals the number of peaks. The stated scientific novelty is not a new general theorem: it is the finite LIS-keyed census/replay certificate at these two sizes.

## Correctness — PASS

I independently reconstructed the finite computation rather than relying on the historical `AUDIT.json`/`REVIEW` material.

A clean-room generator used the standard Catalan decomposition at the maximum: for every left size `l=0,...,n-1`, recursively generate a 231-avoiding left permutation on `1,...,l`, place `n`, and append an independently generated right permutation shifted onto `l+1,...,n-1`. For each object I computed LIS by patience sorting (`lower_bound` piles). I independently implemented the record's recursive map
`D(pi)=U D(R_std) D D(L)`, checked Dyck balance, counted adjacent `UD` peaks, and checked injectivity by storing all images.

The resulting checks for every `1 <= n <= 10` were:

- number generated = Catalan number;
- every image is a balanced Dyck word;
- all images are distinct;
- `LIS(pi) = peaks(D(pi))` object-by-object;
- the LIS histogram equals `(1/n) binom(n,k) binom(n,k-1)` for every `k`.

At `n=9` the recomputed histogram is exactly
`[1,36,336,1176,1764,1176,336,36,1]` over 4862 objects.  
At `n=10` it is exactly
`[1,45,540,2520,5292,5292,2520,540,45,1]` over 16796 objects.

Thus the finite mathematical statements highlighted in the result are correct within the stated window.

## Originality — FAIL

The central novelty premise is contradicted by an older full-text source. In Section 2 of:

Emeric Deutsch, A. J. Hildebrand, Herbert S. Wilf, **“Longest increasing subsequences in pattern-restricted permutations”**, arXiv:math/0304126 (submitted 2003),

the authors explicitly state, citing Reifegerste, that the number of 231-avoiding permutations of `n` letters whose LIS has length exactly `k` is

`e(n,k) = (1/n) binom(n,k) binom(n,k-1)`,

their equation (2.1). This is the Narayana number and is stated for arbitrary `n`, not merely asymptotically or for a restricted finite window.

Direct mapping to this record is exact: substituting `n=9` and `n=10` into the 2003 formula gives every entry of the two claimed census rows. Therefore the headline finite distributions are already completely determined by a published all-`n` result. The current RESULT.md itself cites Deutsch–Hildebrand–Wilf but describes it only as “limiting laws”; that description omits the exact formula in Section 2 and materially overstates novelty.

Search/falsification queries included:
- `"231 avoiding" longest increasing subsequence exact distribution Narayana`;
- `"Longest increasing subsequences in pattern-restricted permutations" 231 k`;
- `Reifegerste 231 LIS binomial`.

The closest and decisive result was the 2003 arXiv full text above, Section 2, equation (2.1). No publisher-access fallback was needed because the relevant full text is openly available on arXiv.

The record's replayable code may independently verify the known formula, and its particular finite table formatting may be new as a repository artifact, but that is not a new mathematical census once the exact general formula is known.

## Scientific value — FAIL

After subtracting the known all-`n` exact formula, the main claimed contribution at `n=9,10` is a routine specialization and exhaustive re-verification of a classical enumeration. Those finite rows do not expose a new regime, improve a theorem, supply a new algorithm with a demonstrated advantage, or establish a structural phenomenon not already implied by the prior result.

The object-level replay certificate has reproducibility/educational utility, but under this campaign's scientific-value criterion that does not make the mathematical finding independently worthwhile. In particular, evaluating the known Narayana formula at two values of `n` is exactly the kind of routine substitution that the audit standard says is insufficient by itself.

## Bounded repair attempt

I considered narrowing the claim to “a replayable finite certificate at `n=9,10`.” That wording would be accurate, but it would not rescue scientific value: the mathematical content remains a finite verification of an exact formula known for all `n`. Broadening to the general Narayana formula would not help either, because that theorem is already in the 2003 source (via Reifegerste). No bounded correction preserving this record's identity yields a contribution that passes all three axes.

## Final disposition

- **Correctness:** passed.
- **Originality:** failed.
- **Scientific value:** failed.
- **Disposition:** **failed / withdraw from accepted findings**.

This is a scientific rejection for prior coverage and lack of residual value, not an operational failure and not a claim that the computations are wrong. The original package and historical audit material should be preserved in the failed-attempt archive by the authorized publisher.
