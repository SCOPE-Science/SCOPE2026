---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The marked-cycle identity, expectation, covariance formula, uniqueness of the sign threshold, and macroscopic limit were reconstructed independently. Direct exact enumeration of every permutation through order six for Ewens parameters \(1/2\), \(1\), and \(2\) reproduced the package expectation and covariance identities for every cycle length. Analytically, deleting a marked \(r\)-cycle leaves the Ewens law on \(n-r\), the Chinese-restaurant Bernoulli representation gives the mean total-cycle count, the tail sum is strictly increasing in \(r\), and the stated threshold and scaled covariance follow from harmonic/Riemann-sum and gamma-ratio limits.

## originality

FAIL

The final claim is implication-covered by classical Ewens partition structure. The exact joint sampling formula already yields the package Palm identity by multiplying by the \(r\)-cycle count and reindexing, and classical size-biased deletion is the same structural statement in equivalent form. Once that identity is in hand, the covariance sign switch and macroscopic threshold use only the standard total-cycle mean, monotonicity of a contiguous harmonic tail, and a routine logarithmic limit. This is stronger coverage, not a failed-search novelty judgment.

## value

PASS

The sign reversal between a global Ewens statistic and macroscopic frequency counts is mathematically natural and interpretable, and an exact threshold/profile would be useful if it were not already a routine consequence of the classical exact law. The rejection is therefore originality-based rather than a claim that the probabilistic question is intrinsically unmotivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
