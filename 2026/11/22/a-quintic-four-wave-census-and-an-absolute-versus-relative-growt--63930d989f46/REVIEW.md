# Scientific assessment with corrections

## Correctness — PASS
The proof reduces four-periodic points to full graph-wide phase rotors and then to a fully explicit rim-transfer pair matrix with a forbidden-hub correction. The exact 16-state and 9-state characteristic polynomials are reproduced using integer Faddeev–LeVerrier and final Cayley–Hamilton identities. A separate complete small-wheel simulation agrees through rim length eight; the all-size conclusion rests on the transfer proof, not extrapolation. The corrected root argument uses rational sign brackets and a coefficient-ratio bound on the deflated quintic to establish that all of its nonleading roots have modulus smaller than the tribonacci root, as required for the stated error term.

## Originality — PASS (with risk)
The most relevant all-length same-graph published result is *Two spectral scales in three-state excitation on wheel graphs*; it gives the three-state cubic comparator, which is credited. The four-state formula has a different characteristic polynomial and a tribonacci subtraction. Prior complete tripartite work does cover \(W_4=K_{1,2,2}\) and its count of 20 orbits; the overlap is explicitly excluded from the contribution. It does not give a census for all rim lengths. Threshold-two wheel results change the update rule. Full classical 1978 source text was not accessible, so unindexed or inaccessible historical equivalents cannot be ruled out.

## Value — PASS
An all-circumference count of the actual shortest nontrivial four-state temporal waves on wheels is a natural dynamical invariant. The quintic census produces a specific new palette-sensitivity phenomenon: more absolute temporal orbits but a smaller probability that random initial states are already on one. The claim is intentionally limited to immediate periodic states, not eventual basins or other temporal periods.

## Reproducibility and scientific limitations
Run `python3 checks/verify_transfer.py` and `python3 checks/verify_direct.py` from the unpacked package directory. Both are standard-library Python programs with finite exact calculations. The second tests all labelled wheels through eight rim sites, while the first's integer matrix computation and analytic proof apply at arbitrary length. Full external independent audit and historical-priority confirmation remain outstanding.

This account incorporates the corrections to the proof and prior-work comparison. It is not a claim of formal verification or external attestation.
