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

On the residue ring the invariant weight is τ_i/S: each oriented edge flux is p/S or q/S. This gives V=n(p−q)/S for the lifted displacement. The centered Poisson equation has periodic slope d_i with sum zero and p d_i−q d_{i−1}=(p−q)(nτ_i/S−1). The corrected displacement is a martingale with jump increments 1+d_i and −1−d_{i−1}. Its time-averaged bracket gives (p+q)(n+Σd_i²)/S; a bounded corrector changes the variance only by O(√t)+O(1), and the finite residue chain gives the bracket-rate limit from each initial residue. Iterating the slope recurrence gives the geometric convolution divided by 1−r^n. For a shift s, splitting its cyclic autocorrelation at s gives (1−r^n)(r^s+r^(n−s))/(1−r²). Expand Σd_i², cancel diagonal and centering terms, and count each unordered pair twice to obtain the claimed positive prefactor and variance difference. For each m the k m-step spans sum to mn, so strict integer convex smoothing gives equality exactly when they differ by at most one. Floor positions simultaneously realize these spans. On the real gap simplex the m=1 sum provides strict convexity; only vertices can maximize, they are feasible integer gaps and all represent one contiguous block up to rotation. At p=q the corrector is constant, and at q=0, 1+d_i=nτ_i/S, giving the stated placement-independent rates. The argument assumes fixed multiplicities and strict bias for the comparison, not general site-dependent biases. Inspected VERIFICATION.md and checks/check_transport.py: the independent tilted-generator calculation and finite exact rational placements are support, not the universal proof; the frozen code was not run.

## originality

PASS

The standalone minimization of a strictly convex repulsive energy by most-homogeneous positions is established and should not be presented as new. General periodic drift/diffusion formulas are also established. The supported distinct theorem connects unwrapped displacement variance in this common-bias two-clock walk to an exact positive cyclic interaction, and uses it for the full two-sided placement and equality laws at unchanged drift. No inspected comparator states or directly gives this transport conclusion without the specialized variance reduction.

## value

PASS

A general formula predicts the variance for a specified period; it does not settle how to design that period at unchanged transport speed. The theorem isolates the full arrangement-sensitive term, turns multiplicity-preserving rate design into a known geometric problem, and identifies both optimal and worst layouts with strict equality cases and the bias endpoints where all layout differences disappear. Its value is in this transport conclusion, not in repeating the classical lattice-gas minimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
