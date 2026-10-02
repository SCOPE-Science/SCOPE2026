# Independent mathematical audit — 2026-09-30

## Outcome

**FAILED** for the final finding as stated.

## Correctness — PASS

The inner Rouché argument was independently replayed in exact rational arithmetic: the certified products T_upper(r,n)*exp_upper(r) for n=10,...,14 are approximately 0.11885, 0.12652, 0.13496, 0.14422 and 0.15435, all strictly below 1. The outer certificate was independently replayed: all five homotopy checks pass, exact polygon windings are 10,11,12,13,14, and the worst required-radius/center-lower-bound ratios are about 0.0669 to 0.1326. Thus the annulus claim is correct subject to the explicitly documented IEEE-754/libm error assumptions of the outer certificate.

## Originality — FAIL

A stronger published SCOPE record, SCOPE-20260908-076, certifies an isolating Rouché disk of radius 0.01 for every zero of s_n for all 1<=n<=16. Its committed centers imply for n=10..14 radial ranges [3.6305,6.5707], [3.8955,7.2992], [4.1977,8.0381], [4.4654,8.7862], and [4.7643,9.5427] after the radius-0.01 allowance, all strictly inside the claimed [0.30n,0.75n] annuli. Therefore the audited annulus is a direct corollary of stronger current published coverage. The stronger record was published later on the same UTC date, so this finding concerns current coverage and does not by itself negate historical priority at 07:25 UTC.

### equivalent_formulations

Searches: exponential partial sums zeros finite n annulus 0.30n 0.75n; Szego partial sum zeros certified disks n<=16

Evidence: The assigned annulus record and the stronger SCOPE-20260908-076 zero-disk census are both exact semantic matches in the current published corpus.

Reasoning: A per-zero certified disk table is a stronger formulation than a coarse common annulus when every disk lies inside that annulus.

### broader_coverage

Searches: certified Rouche disks exponential sections n<=16; SCOPE-20260908-076

Evidence: SCOPE-20260908-076 certifies every zero of every s_n for n<=16 in an isolating radius-0.01 disk.

Reasoning: For n=10..14, direct calculation from its committed rational centers plus radius 0.01 gives bounds strictly stronger than both sides of the audited annulus.

### exact_database_or_table

Searches: exponential partial sums zero tables n<=16; certified disks.json exponential sections

Evidence: The stronger record's committed disks.json provides all rational centers; the derived radial extremes remain well inside 0.30n and 0.75n.

Reasoning: The exact table directly contains enough certified information to imply the entire audited theorem.

### claim_vs_prior_implication

Searches: Walker 2003 zeros partial sums exponential series; Newman Rivlin 1972 exponential partial sums zeros; SCOPE-20260908-076 implication

Evidence: Classical sources provide asymptotic/finite zero information; the decisive current-coverage comparison is the later stronger certified disk census.

Reasoning: Current published stronger coverage implies the claim as a corollary, even though the stronger SCOPE record postdates the original annulus publication and therefore does not establish earlier priority.

### source_inspections


- **Certified Rouché-disk zero table for exponential sections s_n, n<=16** (https://github.com/Resultary/2026/tree/main/2026/9/8/SCOPE076): trigger=Highly relevant stronger published SCOPE result.; material read=Complete RESULT.md, METADATA.json, and complete committed disks.json.; method=Full record/file inspection and direct radius calculation from rational centers.; assessment=DECISIVE CURRENT COVERAGE: the per-zero radius-0.01 enclosures imply the audited annulus for every n=10..14.; evidence=Derived certified radial ranges are strictly contained in [0.30n,0.75n] for all five degrees; SCOPE076 published_at is 2026-09-08T21:38:59Z, later than the audited record.

- **Assigned inner_cert.py and outer_cert.py** (2026/09/08/005/artifacts/): trigger=Critical correctness certificates.; material read=Complete source of both certificate scripts.; method=Source inspection and independent replay.; assessment=Supports correctness but not originality.; evidence=All inner exact inequalities and outer homotopy/winding checks pass.

- **The Zeros of the Partial Sums of the Exponential Series** (https://doi.org/10.1080/00029890.2003.11919971): trigger=Classical finite-n zero literature cited by the record.; material read=Accessible bibliographic/abstract material.; method=Primary-source metadata/abstract inspection.; assessment=Relevant background; not needed for the decisive coverage finding.; evidence=Classical study of zeros of exponential partial sums.

### checked_sources

- SCOPE-20260908-076 full published record and disks.json
- doi:10.1080/00029890.2003.11919971
- doi:10.1016/0021-9045(72)90007-X
- assigned RESULT.md, inner_cert.py, outer_cert.py

### residual_risks

- Because the stronger SCOPE record postdates this record by roughly 14 hours, a separate historical-priority question would need chronology-sensitive treatment; the present audit applies the required current published-coverage bar.

## Scientific value — PASS

A certified finite-degree annulus with explicit margins and a reproducible argument-principle certificate is a motivated numerical/complex-analytic benchmark and would be independently useful if not already subsumed by stronger certified zero locations.

## Limitations

- Outer correctness remains conditional on the documented floating-point/libm assumptions.
- The originality failure is due to current stronger published coverage; it is not a claim that the later record preceded the original publication.
- No repaired narrower claim was proposed because the existing stronger disk census already dominates the annular statement.
