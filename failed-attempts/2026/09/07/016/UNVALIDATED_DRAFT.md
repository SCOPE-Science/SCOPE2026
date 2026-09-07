# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified census and first-occurrence closure for diameter-16 prime sextuplets in [10¹², 10¹²+10⁹]

## 1. Claim (theorem + computed record)

**Pattern.** `S(p) = (p, p+4, p+6, p+10, p+12, p+16)`, diameter 16, the smallest admissible prime 6-tuple.

**Interval.** `I = [1000000000000, 1001000000000]` (closed, length 10⁹).

**Theorem (unconditional, machine-checked).** There are exactly **N(I) = 42** integers `p ∈ I` with all six entries of `S(p)` prime, namely (ordered):

```
1000033407547, 1000045512997, 1000053943237, 1000063630327, 1000095799597,
1000118854447, 1000127146297, 1000141335367, 1000181001217, 1000200344317,
1000201901047, 1000234290607, 1000311410377, 1000372389547, 1000390436317,
1000394570167, 1000462080967, 1000480771387, 1000528640467, 1000557640207,
1000579013167, 1000610394517, 1000675045957, 1000678450687, 1000693576777,
1000702589977, 1000710807907, 1000761318367, 1000778926237, 1000803064897,
1000808468827, 1000810514437, 1000852200697, 1000861384417, 1000862900617,
1000865098687, 1000908281827, 1000924914877, 1000953377647, 1000970819197,
1000973858317, 1000987944487
```

In particular the least such `p` in `I` is

```
p* = 1000033407547
S(p*) = (1000033407547, 1000033407551, 1000033407553,
         1000033407557, 1000033407559, 1000033407563)
```

all 13-digit, each certified prime by deterministic Miller–Rabin **and** a full Pratt certificate verifiable by modular exponentiation alone (252 certificates total, all pass; per-tuple check <1 ms).

**Completeness.** Two independently coded segmented sieves agree byte-identically (`N=42`, identical ordered list, `SHA-256(census.json)=39af0f34…cedd4ce75`).

**Table novelty (conditional, honestly qualified).** All 42 lie at/above 10¹², above the dense OEIS A022008 b-file coverage (offline triage knowledge: dense coverage stops far below 10¹²; embedded head `[7,97,16057,19417]` verified here has zero overlap) and in a different regime from Wikipedia/t5k largest-known size records (hundreds of digits). Hence `p*` is the least tuple in `I` overall and, conditional on that truncation claim, the least absent from public dense tables. Live b-file diff was impossible (HTTPS transport errors for both OEIS and Wikipedia on 2026-09-07); `diff_tables.py --bfile` upgrades this to a line-by-line diff when a local b-file is supplied. We do **not** claim a maximal-digit record and do **not** change the classical pattern.

## 2. Why this is not textbook / parameter substitution

- Admissibility (`p≡7 mod 30` for `p>5`) is classical and only used as a filter; the contribution is **closure of a stated 10⁹ gap** at a new decade with **completeness proof + machine-checkable primality proofs**, not another term.
- Public sources give definitions, small examples (`7,11,13,17,19,23`, …), a b-file truncated far below dense 10¹² coverage without Miller–Rabin transcripts or Pratt certificates, and sporadic largest-known size records. None publishes a Pratt-certified complete list for this window with double-sieve agreement, 5-of-6/4-of-6 miss analysis, and Hardy–Littlewood comparison. The fallback census alone (had `N` been 0) would still close the gap as a reproducible benchmark; here `N=42`.

## 3. Method (reproducible)

**Reduction.** For `p>5`: mod 2 forces `p` odd; offsets mod 3 are `{0,1,0,1,0,1}` (miss 2) so `p≡1 (3)`; offsets mod 5 are `{0,4,1,0,2,1}` (miss 3) so `p≡2 (5)`. CRT gives a unique class `p≡7 (30)`. For any prime `q>5` the six offsets are pairwise distinct mod `q` (pairwise differences `{2,4,6,8,10,12,16}` contain no multiple of 7, 11, 13 and are `<q` for `q≥17`), hence exactly 6 forbidden residue classes per `q>5`. There are `33,333,333` candidates `≡7 (30)` in `I` (closed-form check passes).

**Sieve A (primary, odd-only).** Base primes to `⌊√(HI+16)⌋+1 = 1000500` (78,537 primes) by simple sieve. Segments of 5,000,000 over `[LO, HI+16]` with odd-only `bytearray`; for each odd `q`, mark odd multiples from `max(q², ⌈L/q⌉·q)` with stride `2q`; scan `p≡7 (30)` (overhang `p+16≥R` by trial division — at most 16/segment). Time 0.74 s. Source `sieve_census.c`, log `sieve_census.log`.

**Sieve B (independent recount, wheel-30).** Same base primes, segments of 5,000,000 over candidates `p≡7 (30)`; for each `q>5` and each offset `o`, forbid `p≡−o (q)` (first solution by scan, then stride `q·30` since `gcd(q,30)=1`), then confirm each surviving candidate's six values by trial division. Time 1.84 s. Source `sieve_recount.c`, log `sieve_recount.log`. Different array, different marking arithmetic, different confirmation path from Sieve A.

**Validation of sieve code.** Both logics prototyped in Python and checked against `sympy.isprime` brute force on `[7,20000]` (primary exact) and `[10⁶,1.1·10⁶]` (both exact). The only small-range discrepancy (recount marks `p+o==q` as composite) provably cannot occur in `I` since members `≥10¹² ≫ 10⁶ ≥ q`.

**Primality proofs.** (a) Deterministic Miller–Rabin for 64-bit integers with bases `{2,325,9375,28178,450775,9780504,1795265022}` (Jaeschke–Sinclair–Sorenson-Webster), full per-base transcripts in `mr_transcripts.json`, plus independent `sympy.isprime` (v1.12): 252/252 prime, 0 mismatches, 0.14 s. (b) Full Pratt certificates: factor each `q−1` by trial division to 10⁶ (complete as `√q<10⁶⁺`), take smallest witness `g` with `g^(q−1)=1`, `g^((q−1)/r)≠1` for each distinct `r∣q−1`, recurse. Generation 0.2 s; standalone stdlib verifier `pratt_verify.py` (only `pow`) passes 252/252 in 0.032 s. Certificates `certs/<q>.json`.

**Hashes/timestamps.** `SHA-256(census.json)=SHA-256(recount.json)=39af0f3429c36116648d85c84fe027e172ee777f006c73f47561a87cedd4ce75`; list-only `dec7de22…cbe9542`; 261-line `SHA256SUMS`. Logs record counts, elapsed times, and full ordered lists.

## 4. Results

**Census.** `N(I)=42` as above; sorted, in-interval, all `≡7 (30)` checked; consecutive gaps min 1,516,200 / max 77,119,770.

**Least record `p*`.** Decimal expansions (string match verified, all 13-digit):
`1000033407547, 1000033407551, 1000033407553, 1000033407557, 1000033407559, 1000033407563`.
Witnesses `g`: e.g. `q=1000033407547 → g=2` (full certs in `certs/`; each `<q` cert checks in microseconds).

**Near misses (fallback table, also delivered).** `miss_census.c` counts `k`-of-6 among the 33,333,333 candidates: `{0:13585316, 1:13504110, 2:5186465, 3:965788, 4:88013, 5:3599, 6:42}` (sums exactly). 5-of-6 by missing offset `{0:580, 4:598, 6:584, 10:624, 12:618, 16:595}` (uniform within noise, as expected) with 8 examples per offset archived in `miss_table.json` (first 5-of-6 at `1000000274587` missing +16; first 4-of-6 at `1000000033147`).

**Hardy–Littlewood check.** `C₆=∏(1−w(p)/p)/(1−1/p)⁶` with `w(p)=|{offsets mod p}|` (`w=6` for `p>16`): product to 2·10⁵ is 17.2987109590, tail `exp(−15/(L log L))≈0.9999939`, so `C₆=17.2986046677` (stable to 5·10⁵: 17.29864919). Predicted `C₆·10⁹/(log 10¹²·⁰⁰⁰⁵)⁶ = 38.8671` (9-pt integral identical); observed 42; ratio 1.081; Poisson `P(N≥42|38.87)=0.328` — agreement well within chance (`<0.6σ`). Details `hl_compare.json`.

**Table diff.** `diff_tables.json`: 0/42 overlap with embedded head; all 13-digit ≥10¹²; verdict as in §1 with explicit limitation and `--bfile` upgrade path.

## 5. Limitations / uncertainty (read before citing novelty)

1. **No live table diff.** Both OEIS and Wikipedia fetches failed with transport errors (logged). First-occurrence novelty is therefore a *range + offline-knowledge* argument, not a line-by-line b-file diff. Anyone with a local `b022008.txt` can run `python3 diff_tables.py --bfile b022008.txt` for an exact diff; we predict 42/42 novel for dense coverage.
2. **No originality claim on pattern/methods.** Sextuplet pattern, segmented sieve, deterministic MR bases, and Pratt certificates are all standard; novelty is only the certified closure of this stated window.
3. **Trust base.** Sieve code is short C (auditable) double-implemented; primality ultimately rests on `pow` modular arithmetic + trial division to 10⁶ (both re-checkable without trusting sieve output). `sympy.isprime` is a second opinion, not part of the proof chain.
4. **Scope.** Completeness is only for the closed `I`; gaps/constellation claims outside `I` are untouched.

## 6. How to reproduce (minutes, deterministic)

```bash
gcc -O2 -o sieve_census sieve_census.c -lm
gcc -O2 -o sieve_recount sieve_recount.c -lm
./sieve_census  output/artifacts/census.json  output/artifacts/sieve_census.log
./sieve_recount output/artifacts/recount.json output/artifacts/sieve_recount.log
diff output/artifacts/census.json output/artifacts/recount.json  # must be identical
python3 mr_verify.py output/artifacts/census.json output/artifacts/mr_transcripts.json
python3 pratt_gen.py output/artifacts/census.json output/artifacts/certs
python3 pratt_verify.py output/artifacts/certs   # 252 PASS
gcc -O2 -o miss_census miss_census.c -lm && ./miss_census output/artifacts/miss_table.json
python3 hl_compare.py
python3 diff_tables.py
sha256sum -c output/artifacts/SHA256SUMS  # selected files (paths as archived)
```

All steps use only `gcc`, Python 3 stdlib (+ `numpy`/`sympy` for the prediction/second opinion), and deterministic integer arithmetic; total runtime under 10 s on a laptop (0.74 s + 1.84 s sieves, 0.14 s MR, 0.2 s Pratt gen, 0.03 s verify, 1.05 s miss census).

## 7. Artifact inventory (under `output/artifacts/`)

`census.json`, `recount.json` (identical, `N=42`), `sieve_census.log`, `sieve_recount.log`, `sieve_census.c`, `sieve_recount.c`, `miss_census.c`, `mr_transcripts.json`, `mr_verify.py`, `pratt_gen.py`, `pratt_verify.py`, `pratt_verify.log`, `certs/` (252 `*.json` + `_summary.json`), `miss_table.json`, `hl_compare.json`, `hl_compare.py`, `diff_tables.json`, `diff_tables.py`, `SHA256SUMS`.
