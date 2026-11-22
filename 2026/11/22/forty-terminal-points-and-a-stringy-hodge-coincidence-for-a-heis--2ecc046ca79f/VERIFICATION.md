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
# Verification and reproducibility

The exact checker `CHECK.py` enumerates all vectors of a four-dimensional vector space over three elements, their 40 one-dimensional subgroups, and each subgroup's 27 cosets. It reproduces 1080 nonfree-point labels and verifies that each nonidentity element fixes exactly 27 labels while independent subgroup generators fix no common labels. It also checks the Euler and Hodge arithmetic.

Run `python3 CHECK.py` alongside this document. All four printed `PASS` messages are finite algebraic consequences of the geometric fixed-point theorem and cohomology input, **not** an independent construction of the hyperkähler family. The full argument for all smooth members uses source theorems, transfer, Hodge theory, symplectic linearization and the orbifold formula in RESULT.md. There has been no independent audit of this mathematical result.
