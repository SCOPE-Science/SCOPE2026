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

The claimed identities were reviewed by exact symbolic reconstruction of the finite graph and a separate direct enumeration. They have not been independently mathematically audited.

Execute `python verify_transfer.py` after installing SymPy, and `python verify_direct.py` with a standard Python 3 installation. The first program derives the edge set from the square-avoidance predicate; it checks recurrent components, complement symmetry, both degree-six determinants, the count recurrence, Möbius counts and the Perron root. The second builds cyclic binary tuples independently and directly checks their windows for all lengths up to \(16\), then verifies explicit primitive constructions for lengths \(13\) through \(150\).

The proof of the all-length zeta uses the exact signed-adjacency matrices specified in RESULT.md, not the finite experimental range. The proof of the unbounded primitive-period spectrum uses a return-loop construction; the finite construction test is not a substitute for that argument. All roots, counts and normalizations refer to indexed periodic words, except the explicitly defined primitive rotation classes.
