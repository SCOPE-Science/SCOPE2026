# Independent Audit — 2026/09/12/069

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `067bf3d295f531d0f5938e9e15d3950796f3a9b2`  
**Disposition:** **FAILED**

## Correctness
Within the stated symmetric normalization, the collision algebra is correct. Factoring the difference V(s1)-V(s2) and substituting the normalized moments gives the integral G(s1,s2)=∫_1^3 E(E^2-s1)(E^2-s2)w(E)dE. For the three pairs among 9,1,d^2 the integrand has a strict constant sign on (1,3), so no collision occurs. Also b=-J3/J1 is minus a weighted mean of E^2 in (1,9), placing b in (-9,-1) and keeping all three denominators nonzero. Thus the reduced speeds are real, finite, and distinct for 0<d<1.

## Originality
Grava–Minakov’s mKdV Whitham analysis states that the mKdV characteristic speeds are obtained from the KdV speeds by W_j(beta1,beta2,beta3)=V_j(beta1^2,beta2^2,beta3^2), and cites strict hyperbolicity V3>V2>V1 for ordered positive squared invariants. Taking beta1=d, beta2=1, beta3=3 directly covers the submitted symmetric family for every 0<d<1. The no-collision conclusion is therefore a specialization/rederivation of an established general result.

## Scientific value
The one-signed integral proof is a clean alternative derivation, but it proves only a fixed-parameter subfamily already contained in the known positive-mKdV strict-hyperbolicity theorem. Without a new regime, sharper theorem, or genuinely new invariant, the calculation is not a standalone research contribution.

## Literature
- https://arxiv.org/abs/1907.11859 — Grava–Minakov’s mKdV Whitham analysis gives the squared-invariant reduction to KdV speeds and strict hyperbolicity for ordered positive invariants, directly covering d<1<3.
- https://doi.org/10.1137/19M1279964 — peer-reviewed version of the same work.

## Independent checks
I re-derived the collision numerator factorization, the beta-cancellation, the moment integral G, its signs for all three pairs, and the denominator bounds. These confirm the finite family calculation but also make clear that it sits inside the published general strict-hyperbolicity statement. Current main blobs match the assignment snapshot and compare shows no path changes. No GitHub writes were made.
