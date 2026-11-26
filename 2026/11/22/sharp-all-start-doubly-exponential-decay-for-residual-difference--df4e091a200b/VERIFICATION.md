---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

With e_k the high/low squared spectral-energy ratio, direct substitution of r_k−r_(k−1)=−alpha_(k−1)Br_(k−1) in the RD quotient gives alpha_k=(a²e_(k−1)+b²)/(a³e_(k−1)+b³). Both mode filters are nonzero for positive finite e and e_(k+1)=e_k/(kappa⁴e_(k−1)²). The first residual Rayleigh step gives e_1=1/e_0. Thus phi=log(kappa²e) obeys phi_(k+1)=phi_k−2phi_(k−1), phi_0=2L+t, phi_1=2L−t. The roots (1±i sqrt(7))/2 give q=sqrt(2), cos(theta)=1/(2q), and phi_j=Cq^j cos(j theta−delta) with cosine coordinate 2L+t and sine coordinate (2L−3t)/sqrt(7). Their squared sum is 4L²+16(t+L/2)²/7, strictly positive, minimized at t=−L/2 (realizable by mixed data). The two negative log filter gains differ by uniformly bounded amounts from [phi_(k−1)]_+ and [−phi_(k−1)]_+, respectively, since log(1+kappa exp(phi))=[phi]_++O_kappa(1). Summing from k=1 to n−1 gives an O(n) log error including the fixed first step; after scaling, set m=n−j, so the first term of U is at m=2. Extending the series to infinity costs O(q^(−n)) and preserves uniform continuity. Opposite spectral phases give U and U shifted by π; comparing the Euclidean norm with the larger orthogonal component changes its log by at most log(sqrt(2)), hence the pointwise minimum H is correct. Four successive phases have gaps <π, so the finite part m=2..5 alone guarantees positive values of both positive-part sums at every phase, and compactness gives min H>0. The frozen irrational-rotation argument is also valid since 2cos(theta)=1/sqrt(2) cannot be an algebraic integer (its field norm is −1/2). This establishes the exact phase law, the double-log exponent and no mixed finite termination or geometric exception. On either nonzero pure mode the first step terminates. The conclusion is all mixed starts at fixed spectrum in exact arithmetic, not a one-step Q-rate or a uniform bound over coalescing eigenvalues.

## originality

PASS

Credit the shared exponent to the common content of the two frozen RD records, not twice. The phase-envelope shape, logarithmic recurrence and weighted conjugacy have known antecedents. The supported distinct claim is the sharp, strictly positive startup-amplitude law along the prescribed residual-SD initial-data curve for unmixed RD, including the minimizing input energy ratio and its specific phase-resolved norm law. The closest prior envelope is for matched BB1, a different curve that contains the geometric zero-amplitude state. The earlier broad weighted-BB theorem gives conjugacy and sharp linear estimates, not this amplitude along this initialization. No global priority or within-day order is claimed.

## value

PASS

The specified first step is a natural startup for an actual short spectral solver. Its exact two-mode oscillatory strength, worst initial spectral-energy ratio for that amplitude, and phase-resolved residual scale are useful for distinguishing robust all-start asymptotics from results that only exclude a null trajectory generically. The strictly positive gap quantifies the startup's margin against the balanced geometric orbit without alternation. The exponent and common envelope shape are not counted as separate value, and the result does not promise improved floating-point behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
