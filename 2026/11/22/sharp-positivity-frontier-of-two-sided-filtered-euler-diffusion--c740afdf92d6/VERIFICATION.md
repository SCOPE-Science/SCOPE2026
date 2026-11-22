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

Run `python3 verify.py` with Python 3 standard library. The expected output is `VERIFY_OK 3586 exact_rational_checks`.

The script directly constructs and inverts three-by-three rational resolvents for 512 conductance/time combinations, compares three exact analytic transition formulas, checks row sums, symmetry, positive diagonal bounds and sign criteria, and independently evaluates the rational Gauss--Legendre comparison. The arbitrary-conductance-and-time theorem is established by the displayed algebraic proof; finite checks do not establish its universal quantifiers. The rational threshold formula, nonreentrance and relationship with Crank--Nicolson are proved symbolically in RESULT.md. No independent mathematical audit has been performed.
