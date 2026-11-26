---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For the frozen Erlang reversal model, the two-run affine map preserves [0,2], maps it into (0,2), and couples starts by a product of independent factors BC with negative mean logarithm. Equilibrium sampling of either sign has probability 1/2 and biases the current duration only, not the entrance deficit. Checked the critical moment: the bound (U+V)^(-p) ≤ U^(-(p−q))V^(-q), with U=2(1−B) and V=BCZ′, has finite B factor at small durations if p−q<m, and finite B and C factors at large durations if q<β. Starting with any p<m and taking steps of size at most min(m/2,β/2) reaches β with only strictly subcritical intermediate q. Integrating the ordinary Erlang survivor and dividing by m/λ gives the leading equilibrium-age term e^(−λt)(λt)^(m−1)/(m(m−1)!), hence the stated factor β^(m−1)/(2m(m−1)!). The normalized positive-age integral is dominated by a constant times Z^(−β) since Z≤2, and Pr(Z≤ε)=o(ε^β). The ordinary-run survivor gives the analogous end-of-positive-run small-ball asymptotic; negative runs contribute only when their independent equilibrium age is O(ε) and their starting deficit is at most 2ε. Symmetry and the distinct powers m/(κτ) give the left edge and fixed-mean ordering. Audited frozen RESULT.md, metadata, audit/review, verification and checker source; the reported finite checks were not rerun and are not a limit certificate.

## originality

PASS

The renewal framework and even the exact occupancy transform predate this result. In the inspected work neither supplies the critical inverse entrance moment or the sharp light-tailed prefactor and fixed-mean shape comparison. This is a qualified comparison, not a claim of absolute priority.

## value

PASS

Rare occupancy of the propulsion-supported edge is a natural stationary observable. The exact leading coefficient and logarithmic multiplicity distinguish Erlang phase counts at identical mean times, where a mean-based approximation loses the ordering. Proving critical entrance-gap integrability is substantive, not a substitution of an exponential rate into the known beta distribution. The theorem does not claim uniformity over shapes or thermal robustness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
