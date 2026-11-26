# Independent mathematical audit

## correctness

PASS

For insertions at distinct gaps to produce the same parent, the inserted bits and every intervening symbol must agree; hence the only duplicate histories are the extensions of one existing run, accounting for exactly m redundancies among 2(m+1) histories. The compliant receiver loses one extension per saturated run and always retains at least two parents. In a noncompliant receiver only an interior opposite-bit split can repair a long run, and only one; the allowed split positions range from s-h to h. This proves the list formula, including the zero and singleton cases and the alternating-word maximum. For the generating function, weight an ordinary run by its length minus its saturation indicator, with a global t^2, or place the unique long run between two ordered ordinary-run compositions. At t=1 the ordinary term has a simple pole, while the term for each long size s has leading coefficient 2 rho^s (m+1) rho^(-m)/(rho A'_h(rho))^2. Equality in the triangle inequality for the powers z and z^2 rules out other singularities on the dominant circle for h>=2. Normalizing the double-pole terms gives the asserted masses and h=2 specialization. For h=1 there are two alternating outputs and 2(m-1) singleton outputs. A separate forward-deletion enumeration, deduplicated within each source, checked the formula and spectrum for h=1..6, m=1..12 (49,140 receiver/cap cases). Replay: python3 /workspace/reproductions/frozen_checks.py 1; output in /workspace/reproductions/frozen-check-1.txt.

## originality

PASS

The prior unrestricted insertion counting ingredient is standard. The checked primary papers and related indexed results do not give or mechanically imply the all-cap inverse-fiber spectrum and its geometric limit under uniform feasible-output sampling. The strongest related inverse-fiber results use genuinely different source constraints, not merely different notation.

## value

PASS

The full feasible-output inverse-degree law for a standard run constraint answers a natural ambiguity question that cannot be read off from code size or source growth. In particular, the class visibly violating the run cap, not the compliant class, dominates the distinct feasible outputs; the exact unique-parent fraction and limiting distribution make that effect quantitative for each cap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
