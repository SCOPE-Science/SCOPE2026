# Independent audit — 2026/09/09/078

Date: 2026-09-26. Disposition: archive failed attempt.

## Correctness — FAIL

The exact full-virial identity in Holmer–Roudenko, arXiv:math/0703235, eq. (1.4), is V″=24E−4K. Multiplying by M and using K_Q=3M_Q and E_Q=M_Q/2, for x=MK/(M_QK_Q)=G² and y=ME/(M_QE_Q), gives

    M V″ = 12 M_Q² (y−x).

Consequently **every** H¹ datum with ME>M_QE_Q and G<1 has V″>0, anywhere in phase space. This exactly rules out the record's negative-full-virial target and its near-Q “quadratic gap” without computing an unstable mode, second-order correction, or finite-difference coefficients. The RESULT.md sentence “to first order G<1 ⟺ V″<0” has the wrong sign: its own dV″=4K_Q dF with F=1−G² gives G<1 on the positive-virial side. For the concrete direction u=(1+a)Q with a<0 small, G=(1+a)²<1 and V″=24M_Q[(1+a)²−(1+a)⁴]>0. The numerical experiments may be internally reproducible, but the stated first-order equivalence and suggested far-from-Q full-virial escape are incorrect. A localized cutoff can differ, but a single negative localized second derivative is not by itself a uniform-in-time Glassey bound.

## Originality — FAIL

The decisive obstruction is an elementary algebraic consequence of the cited 2007 full virial identity and ground-state Pohozaev relations. A numerical 36-point scan and fitted +0.968 coefficient are unnecessary for the asserted incompatibility and cannot be promoted to a new rigorous near-Q theorem.

## Scientific value — FAIL

The computed mode may be exploratory data, but the record frames a globally exact no-go as numerical local evidence and leaves a false impression that a negative full-virial route might work far from Q. It supplies neither the admitted blowup datum nor a new obstruction beyond the known identity.

Sources: https://arxiv.org/pdf/math/0703235 ; https://arxiv.org/pdf/0806.1752 . Matching full preprints were open access.
