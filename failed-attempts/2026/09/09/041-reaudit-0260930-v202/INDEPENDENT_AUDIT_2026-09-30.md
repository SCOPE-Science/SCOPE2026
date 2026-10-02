# Independent audit — SCOPE-20260909-041

Audited at: 2026-09-30T22:49:30Z

Final disposition: **failed**.

## Correctness

**PASS** — Fresh independent segmented-sieve recomputation over every integer in [1030000000,1050000000] reproduced exactly 61,310 twin lower members, first 1030000259 and last 1049999957, 61,309 interarrival gaps, unique maximum 3870 at index 19459 between lower members 1036385639 and 1036389509, gap sum 19,999,698, median 228, mean 326.2114534570781, 2,571 gaps >=1000, and the first cousin lower member 1030000567. All gaps are multiples of 6. The two committed independent sieve implementations and deterministic primality checks are therefore corroborated.

## Originality

**PASS** — No checked source or published SCOPE record contained this exact 20-million-wide twin-interarrival table or maximum. Standard twin-prime databases give cumulative counts or global data, not this interval-specific gap log.

### Equivalent formulations

Searches checked: published-record search: twin prime interarrival gap 1030000000 1050000000 3870; web exact endpoint and gap searches.

Evidence: The exact semantic match was the present record; no independent exact-window publication was located.

Reasoning: No equivalent table or endpoint statement was found.

### Broader coverage

Searches checked: OEIS A007508 twin counts below powers of ten; MathWorld Twin Primes; Prime Gap List Project.

Evidence: These sources cover cumulative twin counts, general theory, or consecutive-prime record gaps rather than all twin interarrivals in this window.

Reasoning: Global/cumulative resources do not imply the unique local maximum without a finite scan.

### Exact database or table

Searches checked: OEIS A007508; Nicely/Sebah twin counts; prime-gap databases twin interarrival.

Evidence: A007508 lists pi_2(\(\(10^n\)\)); no checked database supplied the 61,310-member window list or the 3870 maximum.

Reasoning: The exact finite table appears absent from the checked standard resources.

### Claim versus prior implication

Searches checked: Hardy-Littlewood twin-prime approximation; Brun theorem; bounded prime gaps.

Evidence: Asymptotic/conjectural twin-prime distribution and bounded-gap theorems do not determine an exact local census.

Reasoning: The window result is computational, not a corollary of general theory.

### Source inspections

- **OEIS A007508: Number of twin prime pairs below \(\(10^n\)\)** (https://oeis.org/A007508): NOT_COVERING. Material read: complete sequence page with values, comments, references and formulas. Provides cumulative counts only at powers of ten, not interval interarrival gaps.
- **Twin Primes** (https://mathworld.wolfram.com/TwinPrimes.html): NOT_COVERING. Material read: definition and general distribution/theorem material. No exact [1.03e9,1.05e9] interarrival table or maximum.

Checked sources: published SCOPE findings search; OEIS A007508; MathWorld Twin Primes; Prime Gap List Project.

Residual risks: A specialized unpublished or nonindexed twin-prime dataset could contain the same window; no such source was located.

## Scientific value

**FAIL** — The interval [1030000000,1050000000] is not tied to an intrinsic arithmetic threshold, extremal transition, or externally motivated exact boundary. The result is a routine sieve census of one chosen 20,000,001-integer slice; the stated Hardy-Littlewood calibration motivation does not establish a need for this precise slice, and neighboring windows would serve similarly. Correctness, reproducibility and apparent novelty therefore do not meet the required value bar.

## Scientific rejection

The computation is preserved, but a finding is accepted only when correctness, originality and value all pass. The failed value assessment above therefore prevents validation.
