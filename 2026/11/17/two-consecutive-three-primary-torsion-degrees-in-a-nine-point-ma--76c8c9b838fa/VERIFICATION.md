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

# Verification

The complete cellular quotient model is reconstructed without external packages by `verify_matching9.py`, using all matchings and all strict inclusion flags. The action is first made without inversions by barycentric subdivision. The verifier checks all face orbits, integer signs and \(\partial^2=0\), and calculates integral Smith forms with unimodular pivot elimination followed by exact rank-one and gcd-of-entries residual tests. Its independent direct fixed-matching enumeration finds nine fixed three-matchings under a three-step rotation and no matching fixed by the generator.

Execute:

```text
python3 verify_matching9.py
```

The recorded actual output is in `verification_output.txt`. No floating-point estimates or partial enumerations are used. Finite exact matrices establish the claimed nine-point homology; Armstrong's theorem and known connectivity give the fundamental group. The full homotopy type, cup products, any higher-parameter pattern and independent external validation are not established.
