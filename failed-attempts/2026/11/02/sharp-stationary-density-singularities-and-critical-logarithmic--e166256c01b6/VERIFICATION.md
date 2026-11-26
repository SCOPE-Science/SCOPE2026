---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Contraction adds two buffered zeros, and doubling removes one if present or consumes an original binary digit otherwise. Thus the reflected +2/−1 walk has negative drift for p<1/3, is irreducible and aperiodic, and its stationary balance gives the normalized PGF in the finding. The number of original digits removed is at least the excess of expansions over twice the contractions and tends to infinity almost surely. Approximation by dyadic step densities proves total-variation exactness of doubling; conditional scaling preserves total variation, and mixing over the convergent buffer then proves uniqueness within absolutely continuous laws, not among all stationary laws. On annulus N the sum is H_N=Σ_{k≤N}2^kπ_k; the larger root hits 1/2 at p=1/7, with critical coefficient 2/5 and a bounded alternating remainder. Above it, 2^{−(N+1)}H_N^r is asymptotically a positive constant times 2^{N(rα−1)}, including divergence at equality. With ε=1−3p and z=e^{−εt}, the PGF denominator is ε(1+t+o(1)), and εlog₂(1/U) vanishes in probability. The analytic arguments are decisive. The frozen checker was read, not run: it verifies its own coefficient recurrence and annulus positivity and is not an independent annulus or limit certificate. `python3 /workspace/branches/review_reproduction.py 1` separately checked finite forward balance and the exact critical summands.

## originality

FAIL

The principal exact stationary law and regularity/scaling results are covered by the earlier indexed modified Boyarsky–Góra–Islam result after folding the spatial law. This is not just a similarity of two queue denominators: the folded density is exactly the frozen density on every annulus. Uniqueness/attraction throughout the absolutely continuous class is not claimed as an implication of that indexed result.

## value

FAIL

The density singularity and heavy-traffic scale are intrinsically meaningful, but here their exact new-map versions merely reproduce the earlier folded invariant law. The remaining extension from shell invariance to attraction from arbitrary absolutely continuous initial data is the standard dyadic exactness argument once the buffer consumes a positive rate of original digits; no new mixing-rate or non-AC classification is established. There is no independently valuable distinct remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
