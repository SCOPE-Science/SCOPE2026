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

# Reproduction and limitations

With Python 3 and SymPy installed, execute `python verify.py` in a directory containing `verify.py`. The script performs exact Gröbner-basis elimination, a finite monomial semigroup check, explicit polynomial inverse/jet tests for permitted and forbidden plane automorphisms, and orbit witnesses. Expected final line: `ALL_EXACT_CHECKS_PASS`.

The elimination check compares the ideal of the parametrization \((u,uv,v^2,v^3)\) with all four claimed binomial generators. The semigroup enumeration stops at coordinate degree 16; the complete unbounded one-hole assertion follows from the monomial argument in `RESULT.md`. Individual polynomial maps are checked symbolically, but their number is finite; no finite collection of tests can prove a statement about the entire automorphism group. The unrestricted full-group theorem follows from functorial normalization and the exact subring equality. The connectedness claim follows from an explicit algebraic contraction with polynomially extending inverses, not a topological numerical experiment.

The theorem has not undergone an independent mathematical audit.
