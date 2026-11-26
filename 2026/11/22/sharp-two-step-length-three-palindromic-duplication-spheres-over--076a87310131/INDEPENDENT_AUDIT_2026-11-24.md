# Independent mathematical audit

## correctness

PASS

The forced pairs (a,b+3) and (b,a), with b−a≥3, form a matching on the (n−2)(n+1) histories, so subtracting exactly one per pair gives a valid universal upper bound even when other collisions exist. I independently reconstructed the signature table: if the two differences within the second source triple are α,β and its outgoing difference is γ, the insertion replaces γ by (0,−β,−α,α+β+γ) mod 3. Applying this rule to the first defect 0--0 gives all six local signatures and the two generic gaps −d−1 and d−4 in RESULT.md:41–50. The finite output extends by an unchanged periodic tail, and the initial symbol is fixed, so signature equality is exactly word equality. Different histories have the same signature only across the generic families, at a common gap h≥2 and common first defect, giving exactly the commuting pair (a,b+3),(b,a) with b−a=h+1; within either family the history is uniquely determined. This handles legality, end insertions and n=3 (four outputs) as well as general n. The archived checker and output are supplementary, read but not rerun.

## originality

PASS

The numerical bound and its attainment over sufficiently large alphabets are prior. The supported distinct result is that the period-three source attains that bound with only three letters for arbitrary n, with exactly the commuting collisions. The strongest located prior requires distinct source symbols (q≥n) and the cited even-block construction does not furnish a PAL3 source.

## value

PASS

The fixed-alphabet regime matters for palindromic-duplication channel sphere counts: an unbounded distinct-symbol source does not model arbitrarily long words over a small alphabet. The record gives an explicit extremizer and a complete history-fiber classification even when the second duplication uses newly inserted symbols.

The dated certificate retains the supplied scientific assessment, sources and limitations.
