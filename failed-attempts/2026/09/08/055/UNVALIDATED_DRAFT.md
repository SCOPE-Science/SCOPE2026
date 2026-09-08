# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified census: small automatic/morphic binary words that are 7/3-power-free are all overlap-free; plus a strict-7/3-free finite word with exact factor counts

## 1. Objects and definitions

- Alphabet `{0,1}`. A *k-power* with exponent `e = n/p >= 7/3` means a factor of length
  `n = ceil(7p/3)` with period `p`. A word is *7/3-power-free* if it has no factor of
  exponent `>= 7/3`; it is *overlap-free* if it has no factor of exponent `>= 2+`
  (length `2p+1`, period `p`). A 7/3-free word containing an overlap is *strict*.
- `p(n)` = number of distinct factors of length `n`.
- Families searched (prefix length `N`, then 7/3-test restricted to the prefix):
  - (U) all binary `m`-uniform morphisms `h(0),h(1)` with `m = 2..8`, `h(0)` starting
    with `0`: 43,688 morphisms; fixed point from `0`, 12 iterations capped at 6000 letters;
  - (NU) all binary (possibly non-uniform) morphisms with `|h(0)|,|h(1)| in 1..6`:
    7,812 morphisms, 15 iterations capped at 6000;
  - (D2), (D3): all binary DFAOs (MSB-first) with 2 states (32) and 3 states (2,916),
    output of state 0 normalized to `0`, evaluated at `n = 0..3999`.
  - 7/3-freeness tested on the full generated prefix (vectorized period test);
    overlap-freeness tested for periods `<= 400` (DFAO: `<= 300`).
- Strict-word construction: lexicographic depth-first search with backtracking under
  the 7/3 constraint (periods `<= 3000`), seeded with a shortest strict word.

## 2. Results

**(R1) Census: every 7/3-power-free word found in (U), (NU), (D2), (D3) is overlap-free.**
Kept 7/3-free counts: (U) 3 of 43,688; (NU) 2 of 7,812; (D2) 2 of 32; (D3) 116 of 2,916;
number strict in each family: 0. The kept words fall into two factor-complexity
classes, `p(40)/40 = 3.1` (Thue-Morse-like) and `3.3` (twisted-like); none exceeds the
overlap-free ceiling. In particular no strict 7/3-free automatic word exists with
`<= 3` DFAO states, and no strict morphic fixed point exists for the morphism bounds
above. Full kept lists are in
`census_uniform.json`, `census_nonunif6.json`, `census_dfao2.json`, `census_dfao3.json`.

**(R2) Shortest strict words.** Exhaustion over all `2^L` binary words for `L <= 12`
proves: no binary word of length `<= 8` is simultaneously overlap-containing and
7/3-free; at `L = 9` there are exactly 4, namely `001100110, 011001100, 100110011,`
`110011001` (all period-4 overlaps `axaxa`, `|a| = 4`, exponent `9/4 = 2.25 < 7/3`).
Counts `L = 9..12`: `4, 4, 8, 4`. See `shortest_strict.json`.

**(R3) Certified strict 7/3-power-free word of length 1500 with exact factor table.**
`strict_001100110.txt` holds the DFS-built word `w`, `|w| = 1500`, beginning
`001100110`. Verified by an independent vectorized scan: no factor of exponent
`>= 7/3`; earliest overlap witness at position 0, period 4 (`001100110`).
Exact distinct-factor counts (suffix-array + LCP accumulator, cross-checked against
naive `set` enumeration at `n = 9, 25, 50, 60, 100, 200` — all equal) in `strict_p.json`
give finite ratios above the Thue-Morse constant `10/3 = 3.333`, e.g.

| n   | 22 | 23 | 24 | 25 | 26 | 48 | 49 | 50 | 97 | 100 | 193 | 200 |
|-----|----|----|----|----|----|----|----|----|----|-----|-----|-----|
| p(n)| 74 | 78 | 82 | 86 | 88 |162 |166 |168 |326 | 332 | 646 | 663 |
|p(n)/n|3.364|3.391|3.417|3.440|3.385|3.375|3.388|3.360|3.361|3.320|3.347|3.310|

## 3. Honest scope (what is NOT claimed)

- (R1) is a *bounded-slice census*, not a theorem about all automatic words; it does
  not bound `C(7/3)`, the infinite-class supremum. The 4-state DFAO space was only
  randomly sampled (72/3000 7/3-free kept, all overlap-free) and is cited as computed
  evidence only, not a certificate.
- (R3) is a *finite* word: its ratios `p(n)/n` are exact finite-word facts, not a
  certified `limsup p(n)/n` of an infinite word, so it does not by itself raise the
  lower bound on `C(7/3)` past `7/2` (main target) or certify an infinite-word growth
  constant above `10/3` (fallback (b)). It is the first strict-7/3-free object in this
  lane with complexity ratios above `10/3` at finitely many `n`, with a replayable
  generator (seed + DFS rule) and exact counts.
- No Walnut certificate was produced (no network/toolchain); 7/3-freeness claims rest
  on the archived prefix plus the replay script `utils.py`.

## 4. Replay

- `python3` with `numpy` only. Power test: `has_power_at_least(s,7,3)` in `utils.py`
  (period loop with `cumsum` mismatch scan). Factor counts: `sam_via_sa(s,nmax)`
  (suffix-array doubling + `distinct(m) = #{suffixes with length >= m} - #{LCP >= m}`).
- Rerun the census tallies from the JSON kept-lists; regenerate `w` by DFS from seed
  `001100110` (lexicographic `0 < 1`, backtracking) and re-run the power scan and
  `sam_via_sa` counts.
