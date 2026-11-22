---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and limits

The elementary finite weight in Equation (5) agrees with the published classification in Dolinka and East, Proposition 3.1. The independent standalone checker enumerates **all** block maps and all point assignments for \((m,n)=(2,2),(2,3),(3,2),(3,3),(4,2)\), tests \(f^2=f\) by composing explicit maps, groups by induced block map, and compares each multiplicity against the factorial-free integer product count in Equation (5). Totals were respectively 21, 256, 189, 9028 and 2073. The script also evaluates normalized logarithmic rates for \(m=2,3,4\) at \(n=2000\); finite rates converge slowly and are not certificates for the limit.

Proof-critical checks are the exact identity (6), the uniform vanishing of its two correction terms on bounded positive \(t\)-intervals, the globally bounded correction outside those intervals, the unique maximum \(t=s\), and strict convexity of \(s\log s\). The proof supplies these estimates for all fixed \(s\) and consequently all fixed \(m\); the finite checker does not establish infinite limits.

The known finite enumeration is explicitly credited. Limits when \(m\) grows with \(n\), multiplicative constants in rare-event probabilities, and fluctuation theorems for point-image rank remain unproved here. Historical priority against equivalent asymptotic results in uncatalogued literature remains a residual risk.

Run: `python3 verify_fixed_block_retractions.py`. Expected final output: `VERIFY_OK_FIXED_BLOCK_RETRACTIONS`.
