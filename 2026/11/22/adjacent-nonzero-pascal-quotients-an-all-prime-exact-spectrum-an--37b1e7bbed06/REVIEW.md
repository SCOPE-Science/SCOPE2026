# Scientific review

## Correctness — PASS
The theorem has explicit quantifiers over all primes, depths, and eligible horizontal pairs. Lucas's congruence reduces an eligible pair to a unique first nonterminal digit. Lower digits contribute units equal to one, upper digit factors cancel in the quotient, and a finite-field reflection counts the exceptional \(-1\) quotient exactly. Summation over the position yields the all-depth law; character orthogonality and an exact signed-digit decomposition yield the four-cell sign law. Direct enumeration of complete finite levels, together with independent integer-binomial checks, passed 57,254 assertions (`checker.py`). The program is not treated as an infinite proof. No claim is made for ratios where either coefficient is divisible by the prime.

## Originality — PASS, with identified risk
Garfield--Wilf's full 1992 article gives one-entry row residue generating functions and a rowwise quadratic-character criterion, not nearest-neighbor quotient fibers. Lane's accessible 2023 manuscript also concerns distributions of individual entries. The closest published-finding corpus entries address lengths of nondivisibility runs, counts of nonzero coefficients, and unrelated binomial valuation correlations; their statements do not determine the quotient values of adjacent nonzero entries. Broad digital-distribution work of Barat--Grabner (2001) and Wilson (1998) was located, but full text access was unavailable; their abstract-level descriptions are not used to declare noncoverage. An earlier implicit exact quotient enumeration remains the main priority risk. Search absence alone was not regarded as proof of novelty.

## Mathematical value — PASS
Single-entry residue statistics do not determine the local transitions of a Pascal row. The exact doubled \(-1\) class is uniform across all primes and all block depths, identifying a complete natural nearest-neighbor invariant of the prime-modular Pascal gasket rather than an arbitrary coefficient slice. The character consequence proves nonvanishing two-point dependence even when individual signs balance, supplying meaningful information beyond established one-point frequencies.

## Verification and limits
The quotient law includes \(p=2\); the quadratic-character law requires odd primes. The proved domain is complete blocks of \(p^r\) rows modulo \(p\), not prime powers as residue moduli or arbitrary cutoffs. A complete prior-art classification has not been independently established.

Self-review: passed. Independent audit: not yet performed.
