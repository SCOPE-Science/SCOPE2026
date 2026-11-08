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

The symbolic proof and exhaustive finite checks are separate evidence types. The verifier `artifacts/verify.py` depends only on Python's standard library. Run `python3 artifacts/verify.py` to check that, for every integer \(3\le n\le12\), independent ternary-word enumeration finds the stated global Roman minimum weight and the precise numbers of labelled and dihedral minima. The verifier additionally constructs the stated cyclic-gap templates for every \(6\le n\le80\), checks the two defining adjacency requirements directly, and compares both enumeration formulas. A successful run ends in `VERIFY_OK`.

The proof uses all positive integer lengths through explicit inequalities and gap classification. Numerical checks alone cannot establish assertions for unbounded \(n\), and they are not presented as an independent mathematical audit. Inaccessible earlier literature remains a bibliographic risk.
