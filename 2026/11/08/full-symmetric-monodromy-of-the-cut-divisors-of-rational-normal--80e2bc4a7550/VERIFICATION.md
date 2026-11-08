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

## Reproduction

Run `python verify.py` with SymPy (tested with the installed version). The expected output is one line beginning `VERIFY_OK`. It checks exact polynomial and matrix identities: disjoint squarefree diagonal witnesses for five sets of block degrees; interpolation at two independent parameters for a \(3\)-by-\(3\) matrix; discriminant multiplicity one at a simple double-root collision for three degrees; and equality \(\det(AQA^{\mathsf T})=\det(AB)^2/\det(B^{\mathsf T}B)\) in an explicit degree-\((2,3)\) frame.

## Verification limits

This is exact finite arithmetic support for the displayed examples and critical identities, not a finite certification of the infinite theorem. The written proof establishes global irreducibility of the ordered-pair incidence by explicit two-point evaluation and the transposition by analytic continuation, then passes from frames to the Grassmannian. No external independent audit has been performed.
