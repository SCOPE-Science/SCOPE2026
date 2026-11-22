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

The proof uses the exact Neumann mean-zero evaluation Green kernel, one antisymmetric Rayleigh certificate, and a positive two-dimensional compression. The minimax lower bound and equality rigidity are analytical for all triples, not grid-dependent.

Running `python verify.py` with Python 3 and SymPy reconstructs the symbolic matrix identities and balancing cubic, integrates the kernel on rational test sites, and gives 1,999 exact algebraic/rational assertions together with the numerical root. The root is isolated by the proof's rational interval and monotonicity argument. The checker does not prove coverage beyond its finite tests; the document proof establishes the infinite-domain statements.

No independent audit or external validation has been performed. The exact optimality classification does not extend by this argument to other sampling cardinalities or statistical reconstruction criteria.
