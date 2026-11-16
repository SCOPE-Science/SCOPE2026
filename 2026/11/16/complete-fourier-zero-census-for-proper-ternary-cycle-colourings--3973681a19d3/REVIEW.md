# Review of the Fourier zero census for ternary cycle colourings

## Correctness — PASS

The endpoint conditions are distinct vertices on a simple \(n\)-cycle, \(n\ge3\), with unnormalized additive characters. The increment parametrization, closed-sum root-of-unity filter, and three signed powers of two prove the exact transform. A minimal-exponent parity argument completely classifies zero triples, and an alphabet-symmetric multinomial count gives exact multiplicities. Fourier diagonalization then proves the rank. Exact replay of `checker.py` checks 88,560 coefficients, but finite checks are not substituted for the proof.

## Originality — PASS under bounded comparison

The closest published work includes Chang--Shrock's uniform-field Potts transfer matrices (arXiv:0907.0925), Shrock--Xu's subset-weighted chromatic partition functions (arXiv:1009.1182), the general weighted-colouring generating functions of Beck--Braun--Cornejo (arXiv:2509.22946), and a published first-degree Fourier Gram theorem for proper cycle colourings (research record 8dc8f90856db). The first two do not encode independent character weights at all sites; the general weighted chromatic generating function does encode their values as specializations but does not state the closed zero census; the published Gram theorem is limited to first-coordinate characters. No inspected stronger theorem implies the all-frequency cancellation criterion and multinomial rank. A prior equivalent specialization under different terminology remains possible.

## Mathematical value — PASS

Global colour shifts explain only a forced family of Fourier zeros. A precise additional nullspace appears for exactly one residue class of cycle lengths; the theorem quantifies it and gives the entire Fourier transform. This is a motivated natural invariant of the chromatic constraint operator rather than an arbitrary enumeration or a routine normalization consequence.

## Limitations

This is an all-length theorem only for three colours on simple cycles. It does not determine nonzero multiplier distributions or sharp inverse norms for every length. No independent mathematical audit or exhaustive historical-priority verification has been carried out.

Self-review: passed. Independent audit: not yet performed.
