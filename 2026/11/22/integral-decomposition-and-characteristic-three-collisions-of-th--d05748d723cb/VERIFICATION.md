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

# Verification record

The proof determines the local rings in all characteristics from the five quartics and uses a finite-flat comparison to identify the global arithmetic scheme. The four rank-nine components are copies of the explicitly defined finite flat group scheme \(\mu_3\times\mu_3\); this is stronger than matching point sets. The local characteristic-three length is obtained by the nine monomials \(s^it^j\) with \(0\le i,j\le2\), giving Hilbert function \((1,2,3,2,1)\).

`check.py` is a Python-3, no-dependencies finite-field consistency checker. It enumerates all projective rational points in characteristics \(2,3,5,7,11,13,17,19\), and tests monomial lengths. Its successful execution corroborates examples, but does not establish the infinite-characteristic theorem or priority. The written mathematical proof handles every prime. No machine formalization or independent audit is claimed.
