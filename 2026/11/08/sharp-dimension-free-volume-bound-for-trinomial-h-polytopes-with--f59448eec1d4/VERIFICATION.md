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

Run `python3 verify.py` with Python 3.9 or newer (no external dependencies). All inequalities are checked using exact `fractions.Fraction` arithmetic. The script enumerates invariant-factor groups \(C_m\times C_n\), all allowable distinct upper-height pairs, all nontrivial complex characters, and all automorphisms needed for the remaining orbits.

The local replay returned:

```
certified excluded group 2 8 automorphisms 16 orbit size 16
certified excluded group 4 4 automorphisms 96 orbit size 48
certified excluded group 3 6 automorphisms 48 orbit size 24
EXACT_VERIFICATION_PASS; candidate_pairs_above_12= 46223 spectral_exclusions= 46135 dual_exclusions= 88
```

The spectral test uses an explicit rational cosine lower bound relying on classical \(223/71<\pi<22/7\). The dual tests are exact rational matrix inequalities for every group character; no floating-point feasibility solver is used. The infinite theorem also relies on the group reduction and equality examples established in Tsuchiya, Proposition 4.3 and Example 4.5. This is self-review, not independent validation.
