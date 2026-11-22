# Self-review

## Correctness — PASS
The proof reduces four-periodic points to full graph-wide phase rotors and then to a fully explicit rim-transfer pair matrix with a forbidden-hub correction. The exact 16-state and 9-state characteristic polynomials are reproduced using integer Faddeev–LeVerrier and final Cayley–Hamilton identities. A separate complete small-wheel simulation agrees through rim length eight; the all-size conclusion rests on the transfer proof, not extrapolation. The dominant-root asymptotics follow from primitive companion polynomials and rational sign brackets.

## Originality — PASS (with risk)
The most relevant same-graph published result is *Two spectral scales in three-state excitation on wheel graphs*; it already gives the three-state cubic comparator, which is credited. The new formula applies to **four** states and has a different exact characteristic polynomial and a tribonacci subtraction. Four-state complete multipartite results and threshold-two wheel results do not cover these premises. Full classical 1978 source text was not accessible, so unpublished or unindexed historical equivalences cannot be fully excluded; this does not displace a known stronger result from the inspected material.

## Value — PASS
An all-circumference count of the actual shortest nontrivial four-state temporal waves on wheels is a natural dynamical invariant. The quintic census produces a specific new palette-sensitivity phenomenon: more absolute temporal orbits but a smaller probability that random initial states are already on one. The claim is intentionally limited to immediate periodic states, not eventual basins or other temporal periods.

## Reproducibility and scientific limitations
Run `python3 checks/verify_transfer.py` and `python3 checks/verify_direct.py` from the unpacked package directory. Both are standard-library Python programs with finite exact calculations. The second tests all labelled wheels through eight rim sites, while the first's integer matrix computation and analytic proof apply at arbitrary length. Full external independent audit and historical-priority confirmation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
