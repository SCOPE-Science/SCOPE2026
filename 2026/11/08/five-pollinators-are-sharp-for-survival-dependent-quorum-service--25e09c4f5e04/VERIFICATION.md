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

`python3 verifier.py` completed without third-party dependencies. It exhaustively checked all 341 eligible nontrivial neighborhood multisets through five pollinators, including 1,284 independently recalculated action coefficient vectors. It established coefficientwise universal winners for the 13 three-pollinator and 77 four-pollinator classes, and 245 of 251 five-pollinator classes; the remaining six form one plant-symmetry orbit. The canonical two winning action vectors are `(0,0,1,3,3,1)` and `(0,0,0,4,5,1)`, yielding the exact difference `p^2*(1-p)*(1-3*p)`. Test cases with `Fraction` additionally verify the factorization. The mathematical proof is finite: the code loops over the entire set of incidence classes and permitted link types. No exhaustive or asymptotic result beyond five pollinators is tested.
