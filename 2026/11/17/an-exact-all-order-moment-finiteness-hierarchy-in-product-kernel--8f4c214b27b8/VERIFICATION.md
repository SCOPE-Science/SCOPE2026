---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

PASS. For the stipulated mass-conserving non-gelling λ>4 stationary branch, M2(t) increases to aλ=(λ-sqrt(λ(λ-4)))/2. Binomial expansion of product coagulation, retaining the two endpoint terms, gives dM_p/dt=(pM2(t)-λ)M_p+λ+(1/2)∑_{j=2}^{p-2}C(p,j)M_{j+1}M_{p-j+1}. Finite-time truncation/induction and Grönwall justify each order. For λ>p²/(p-1), algebra gives c=λ-p aλ>0, and all lower moments are bounded by induction, so M_p is bounded and converges to its explicit stationary recurrence. For 4<λ≤p²/(p-1), if stationary M_p were finite, all lower moments would be finite, allowing a stationary balance with LHS (λ-paλ)M_p≤0 and strictly positive RHS λ+..., a contradiction, including equality. Independent exact root comparisons p=3,4,5,8 verify the threshold algebra. No finite cutoff used to infer divergence.

## originality

PASS

PASS best of knowledge. Matveev (Nov 6 2026) establishes the stationary recurrence, mass-one non-gelling branch and second moment, and an earlier Resultary theorem proves ONLY p=3 threshold 9/2. The all-integer complete sequence λ_p=p²/(p-1), its sharp equality divergence and exact triangular recursion are not obtained by that single p=3 statement alone. The new result is a natural uniform moment-order classification derived from the known model by a nontrivial induction; unindexed older moment-hierarchy treatments remain a risk.

## value

PASS

PASS. Exact finiteness of every natural integer cluster-size moment is a meaningful stationary phase diagram of a physical coagulation–shattering process: distinct thresholds at every p, including equality, distinguish degrees of tail heaviness after gelation suppression. It is a complete infinite hierarchy rather than a two- or three-moment toy calculation, even though the underlying recursion is a standard tool.

The dated certificate retains the supplied scientific assessment, sources and limitations.
