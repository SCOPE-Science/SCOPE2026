# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Complete h*-vector census with extremal witness for hollow and once-punctured lattice tetrahedra of normalized volume 20
- **Round:** 2026-09-07-first-light-01
- **Lane:** 24
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Convex Geometry
- **Method:** Hermite-normal-form classification with Barvinok-style lattice-point enumeration and Ehrhart-series rational-function verification

## Problem

Close the normalized-volume-20 stratum for lattice tetrahedra (3-simplices) with at most one interior lattice point: enumerate up to unimodular equivalence all such tetrahedra of normalized volume 20, compute the exact complete set of Ehrhart h*-vectors (1,h1,h2,h3) with h3 in {0,1}, and certify an extremal lattice-width (and maximum-h1) witness, via exhaustive Hermite-normal-form generation with dual lattice-point counts and Ehrhart-series rational-function consistency checks with replayable logs.

## Attempted claim

At normalized volume 20, the set of h*-vectors over lattice tetrahedra with interior points h3 in {0,1} is exactly the certified enumeration (pilot scan of all 1085 HNF types predicts 24 distinct vectors: (1,0,19,0), (1,1,18,0), (1,2,17,0), (1,3,16,0), (1,4,15,0), (1,5,14,0), (1,6,13,0), (1,7,12,0), (1,9,10,0), (1,10,9,0), (1,11,8,0), (1,12,7,0), (1,13,6,0), (1,14,5,0), (1,15,4,0), (1,19,0,0) with h3=0 and (1,1,17,1), (1,3,15,1), (1,4,14,1), (1,5,13,1), (1,6,12,1), (1,7,11,1), (1,8,10,1), (1,9,9,1) with h3=1), each realized by an explicit HNF tetrahedron with dual-count (L1,L2,L3) certificate satisfying sum h_i = 20 and h3 = interior count, together with the certified stratum-maximum lattice width W and maximum-h1 witness tetrahedra with attaining data.

## Research outcome

Closed volume-20 hollow/once-punctured stratum: 24 h* vectors with HNF representatives, dual lattice-point certificates, Ehrhart consistency, White empty consistency, and certified stratum maxima (max-h1 19, max-width 2) with replayable verifier.

## Why this attempt failed

Failed axes: value.

value: Even though correct and narrowly new, the result as stated is not independently worth finding later: it is a mere parameter substitution and unexplained single-volume enumeration. Decisive evidence: (1) Same textbook HNF-plus-brute-force pipeline yields analogous censuses at neighboring divisor-rich volumes with no new ideas — auditor recomputed V=12 (455 HNF -> 17 total, 13 h01: 10 hollow+3 once-punctured) and V=18 (910 HNF -> 29 total, 20 h01) in seconds using identical code, and V=30 has 2821 HNF. V=20 (1085 HNF -> 39 total, 24 h01) is one arbitrary instance among infinite volumes; choosing 20 has no principled threshold. Draft's 'smallest divisor-rich volume beyond textbook examples where all diagonal types interact' is factually false: V=12=2^2*3 has identical divisor structure (6 divisors, 18 ordered diagonal types) and is smaller, also has both i=0 and i=1 strata populated and L1 up to 15 (beyond 6-point Blanco-Santos range). Richness merely grows with V. (2) Claimed extremal witnesses are trivial or single-volume computations without general insight: max-h1=19 is immediate from sum hi=V, h0=1, hi>=0 => h1<=V-1, attained by obvious infinite long-edge family conv{0,(1,0,0),(0,1,0),(0,0,V)} giving h*=(1,V-1,0,0) for any V — no search needed. Max-width 2 over h01 at V=20 is a finite check (318/597 attain) with no theorem explaining pattern, and gaps (hollow missing h1=8,16,17,18 / L1=12,20,21,22; once-punctured missing h1=0,2) are logged without explanation. Certificates (HNF reps, L-triples, reciprocity, Hibi h1>=h3) verify correctness but do not explain why those 24 occur. Width-3-outside example shows non-triviality of the bound at this V only, not a structural result. (3) Motivation (toric-code/Fano benchmarks, reusable pipeline) is generic: no recognized open problem asks for V=20 specifically; GRDB/Fano interest is in reflexive/canonical families, not a single hollow-inclusive volume slice; pipeline is standard HNF generation + tiny-box enumeration (stdlib, <2min), not a new scalable method. Citability as anchor table is low since any CAS can recompute in ~1min and the next volume would need a new table. This matches SCOPE value-reject precedents for fixed-parameter exhaustive enumerations (e.g. RT(30,K4,6), SmallGroup(96) extrema) even when correct and certified. Therefore fails the 'independently worth finding later' bar; it is an unexplained enumeration / parameter instance, not a substantive closure.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Relies on cited left-HNF existence/uniqueness (Cohen Alg 2.4.5/2.4.8) for column convention; implementation correctness mitigated by dual-route agreement but not machine-proved; Python integer arithmetic assumed; h3>=2 vectors (15 logged) share pipeline but not part of claimed stratum; representatives are h*-witnesses only (not unimodular uniqueness); no claim over White/multi-width/point-count theories beyond stated delta.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
