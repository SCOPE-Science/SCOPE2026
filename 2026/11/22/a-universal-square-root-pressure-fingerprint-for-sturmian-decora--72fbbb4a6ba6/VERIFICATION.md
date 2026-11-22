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

The analytical proof in `RESULT.md` establishes uniqueness of equilibrium and the universal limits. Its critical inputs are (i) the induced-return entropy inequality including the marker-free component; (ii) exact Sturmian factor complexity and the heavy-factor distribution of *distinct* words under irrational-rotation partitions; (iii) Abelian asymptotics of weighted renewal series and their derivatives. These prove the theorem for all irrational slopes and each fixed real color field.

The standalone `verify.py` (Python 3 standard library only) was executed from the package directory. The program reconstructed Sturmian factor languages at lengths one through twelve and compared their heavy-factor multiplicities with an independently built partition profile. It also solved truncated weighted renewal equations at three real color fields and two positive activities, comparing pressure, marker density, color density, and the exact zero-field identities. All twelve direct factor comparisons and six pressure/composition cases passed. These checks involve finite truncation and floating-point arithmetic and do not prove the infinite assertions.

The originality assessment compared the main theorem to Ramirez–Somers (2025), Fici–Mignosi–Shallit (2017) for the heavy/light partition, the 2026 binary renewal-type pressure paper, a relevant full public decorated-gap zeta theorem, the searchable result index, and the accessible existing claim ledger. This is a self-review with residual priority risk, not independent certification. No external expert or independent audit was performed.
