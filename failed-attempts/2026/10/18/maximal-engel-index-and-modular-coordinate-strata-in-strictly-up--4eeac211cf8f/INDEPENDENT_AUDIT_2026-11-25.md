# Independent mathematical audit

## correctness

PASS

Checked RESULT.md lines 5–37. The degree filtration makes ad_X raise superdiagonal degree by at least one, so its (n−1)st power vanishes and its (n−2)nd power has image in kE_{1n}, killing degrees ≥2. Expand the latter power using the commuting left and right multiplication operators. To move E_{i,i+1} to the terminal coordinate in n−2 steps the left path has i−1 unit steps and the right path n−i−1 unit steps, giving coefficient (−1)^{n−i−1} binom(n−2,i−1) times the product of all a_j except a_i. Thus the index criterion holds in every characteristic and the top power's rank is the block multiplicity. Counting the disjoint all-nonzero and eligible-single-zero assignments leaves N−n+1 arbitrary coordinates. Lucas's digit test gives K; all smaller integers satisfy the digitwise bound iff the digits below the leading digit of n−2 are all p−1. Adding one gives n−1=c p^t, including the carry case c=1 and t increased by one. The inclusion-minimal vanishing patterns are precisely an ineligible singleton and an eligible pair; their incomparable coordinate flats are the components, with a pair always available because both endpoint binomials equal one. A separate finite verification (python3 /workspace/review_checks.py 4) computed ordinary matrix commutators on the full matrix-unit basis in eight small (q,n) cases across fields of orders 2,3,4,5, checked both terminal powers, and obtained the predicted totals, including 320 at (2,5), 540 at (3,4) and 2880 at (4,4). The frozen checker was inspected, not run; finite checks are corroboration only.

## originality

FAIL

The distinct indexed result b59c81367d35 states the same all-n, all-prime-power maximal-adjoint-block criterion, block multiplicity, count and component stratification, via the same terminal-power formula. It proves a stronger scheme statement for the full zero scheme over fields of characteristic p. The frozen statement is contained entirely in it. The narrower indexed n=5 result gives further overlap but would not itself cover the general theorem. This verdict concerns equivalent indexed coverage, not chronological priority or provenance; the comparators have later displayed catalogue paths.

## value

PASS

The elementwise extremal adjoint Jordan behavior is a natural statistic of the type-A nilradical. The terminal-power computation yields both a uniform finite-field census and a characteristic-dependent geometric jump between divisorial and codimension-two exceptional loci. Those are mathematically meaningful conclusions rather than a routine application of nilpotence alone. This evaluates the content of the general theorem and does not identify a distinct result beyond the comparator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
