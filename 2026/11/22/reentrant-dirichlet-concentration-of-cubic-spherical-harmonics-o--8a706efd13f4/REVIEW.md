# Scientific review: reentrant cubic Dirichlet cap concentration

## Correctness — PASS

The theorem fixes the exact-degree-three harmonic space and Dirichlet-energy normalization. Four transverse harmonic types exhaust the space, and the latitude-gradient formula gives the four listed energy polynomials. Beta moments supply exact normalizations. Each displayed spectral-gap polynomial is proved by differentiation with a shared endpoint normalization; the five sign relations and a finite integer discriminant subcase establish the complete all-dimensional ordering. The sharp thin-cap ratio follows from the leading endpoint densities. Replaying `checker.py` returned 234 checks, independently including numerical cap quadrature. The checker does not replace the proof. Boundaries \(a=0,1\) are excluded and correctly discussed.

## Originality — PASS, with historical-priority risk

The original 2013 Plattner–Simons vector-field Slepian paper treats tangential gradients and general cap spectral matrices on the two-sphere; the 2021 Michel–Plattner–Seibert paper treats general spherical vector and tensor Slepian formulations. Material from their full accessible texts, including vector definitions, cap block matrices, and constructions, was inspected. These sources provide general background but not an explicit all-dimensional pure-cubic double-cap Dirichlet order/reentrance theorem.

The published 2026 scalar pure-cubic double-cap theorem (finding `45d96c049f3f`, full `RESULT.md` inspected) concerns *scalar value energy*, with top-sector sequence \(2\to1\to0\) and cutoffs \(1/(d+2),3/(d+2)\); it does not imply this gradient sequence \(1\to0\to1\) or the new second cutoff. The comparable 2026 indexed cubic scalar summary `c0fecc278359` likewise concerns scalar values. A previously published pure quadratic tangential-gradient theorem concerns a different harmonic degree. Several specialized unindexed works may nevertheless contain an equivalent calculation; no global priority is certified.

## Mathematical value — PASS

A local energy observable changes which pure cubic spherical harmonics are most identifiable. The explicit universal top-sector reentrance, sharp second threshold, complete spectrum, equality eigenspaces, and thin-cap stability law directly address exact vector-field observation from two polar patches; these are not straightforward rewordings of the scalar cap theorem. The fact can inform the placement and conditioning of gradient-based measurements without claiming a general multi-degree Slepian method.

## Scientific limitations

Exact degree three, intrinsic gradient energy, symmetric antipodal caps, and integer \(d\ge3\) only. External independent verification is absent. Priority risk persists in unindexed specialized harmonic-analysis literature.

Self-review: passed. Independent audit: not yet performed.
