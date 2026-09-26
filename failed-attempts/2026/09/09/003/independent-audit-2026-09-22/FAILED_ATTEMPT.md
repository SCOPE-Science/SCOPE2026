# Failed attempt — 2026/09/09/003

**Disposition:** failed on independent audit, 2026-09-26 UTC. The complete accepted package is preserved here with its original blob contents. `ORIGINAL_VERIFICATION.md` preserves the prior verification entry; `VERIFICATION.md` records the failed independent audit and retains the other channels.

## Decisive counterexample

The claimed 41 circle-pair contacts are selected with a tolerance of \(2\times10^{-12}\) on squared distance. Parsing the committed 12-decimal centers and radius as exact rationals shows that 39 of these pairs have strictly positive clearance. Only pairs (2,3) and (8,14) exactly attain distance \(2r\); all 14 listed wall contacts are exact. Therefore the 55-row matrix and its positive stress constrain many pairs that are not active constraints of the stated packing.

More directly, let \(\varepsilon=10^{-15}\) and raise the radius to \(r+\varepsilon\). For each listed wall contact, move the center inward by \(\varepsilon\) normal to that wall. In addition, move center 2 left and center 3 right by \(\varepsilon\), and move center 8 down and center 14 up by \(\varepsilon\). Leave all other coordinate components unchanged. Exact rational evaluation of every one of the 465 pairwise squared-distance inequalities and 124 wall inequalities finds no violation. The minimum pair squared gap and minimum wall gap are both zero, attained by constraints that remain contacts. This is a feasible packing at a strictly larger radius, contradicting the claimed first-order maximality for the exact committed coordinates.

The rank and stress calculations may be correct for the tolerance-selected graph, but they do not prove jamming for the actual active set. A corrected claim would require a truly exact feasible contact configuration or a rigorous interval argument with quantified perturbation and active constraints. The prior Packomania coordinates and counts are cited in the package; their live text was inaccessible during this audit, so no assertion of independently reading that file is made.

## Axes and evidence

See `INDEPENDENT_AUDIT_2026-09-22.md` and `.json` for the separate correctness, originality, and scientific-value decisions. The original `RESULT.md`, `AUDIT.json`, metadata, slogan, verifier, and verifier output remain in this archive as evidence of the attempt.
