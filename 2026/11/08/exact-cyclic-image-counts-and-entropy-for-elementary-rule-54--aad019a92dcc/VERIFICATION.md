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

# Reproduction and mathematical boundary

Run the two included standard-library-only scripts from the extracted directory:

```text
python3 verify_relation.py
python3 verify_direct.py
```

The first recreates the four-bit Boolean relation representation, checks all 109 reachable states and their complete transitions, computes the exact seven-term vector relation at the 109 states, and checks the generating-function numerator coefficients. This finite vector identity is closed under subsequent transitions, so it proves the all-length recurrence; it is not merely a guess obtained by extrapolating a sequence.

The second implements \(F_n(x)_i=x_i\oplus(x_{i-1}\lor x_{i+1})\) independently by cyclic bit rotations and exhaustively counts distinct outputs for every ring length \(1\le n\le18\). It checks this against the recurrence derived from the identity. The two programs use different representations, but share the mathematical definition of Rule 54; they are not independent expert validation.

No claims are made about source-code formal verification, infinite brute-force enumeration, multistep images, or independent historical-priority certification.
