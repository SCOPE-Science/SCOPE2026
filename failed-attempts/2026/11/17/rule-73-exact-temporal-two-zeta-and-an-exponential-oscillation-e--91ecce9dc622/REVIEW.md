# Independent mathematical audit

## correctness

PASS

Rule73 truth table has ones exactly on neighborhoods 000,011,110. A 4-state de Bruijn graph tests one-update fixed windows and a 16-state graph tests the five-symbol double update; cyclic closed walks correspond exactly to indexed states, even for rings n=1,2 with wrapped repeated positions. Complete finite elementary-directed-cycle determinant expansion yields det1=1-z³-z⁴, det2=(1-z)^2(1+z²)^2(1-2z²-z³+z⁴); independent graph/determinant implementation matches exactly. Formal −log det=Σ tr(M^n) z^n/n proves both rational functions for all n. Primitive SCC Perron arguments and rational root sign isolations give spectral radii α>β, so c_n=(t_n-s_n)/2~α^n/2. Independent direct source checker is finite confirmation, not all-n argument. Crucially the exact expanded det2 was also independently compared to published all-rule table row73 and agrees coefficient by coefficient.

## originality

FAIL

Decisive published same-model dominating coverage: the separately published 256-rule exact first/second-iterate zeta classification supplies BOTH denominator polynomials for EVERY elementary rule in its downloadable 256-row rule_table.csv, including row 73 exactly. The submitted Rule73 rational zeta identities are a parameter-specialization of that all-rule theorem. The advertised exponential gap follows mechanically from its known Rule73 polynomials by elementary Perron/root comparisons; the formula is not a distinct original theorem despite a different emphasis or title. Both related records have 2026-11-17 dates; historical within-day precedence is not inferred.

## value

FAIL

As an unchanged standalone final claim this is a known exact table recomputation plus routine spectral consequences; the finite exact result would otherwise be interesting, but is already available as an explicit row of a natural complete classification. Correctness, reproducibility, and a simpler factorization do not provide a fresh mathematically motivated independent contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
