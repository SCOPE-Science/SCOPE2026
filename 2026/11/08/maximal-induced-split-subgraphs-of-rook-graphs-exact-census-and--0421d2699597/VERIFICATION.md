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

# Reproducibility

The file `verify_rook_split.py` is standalone Python 3 with no external dependencies. It constructs the \(m\)-by-\(n\) rook graph directly from cell-coordinate adjacency, enumerates forbidden induced \(2K_2\), \(C_4\), and \(C_5\) patterns, checks every candidate selected vertex subset, and tests inclusion-maximality by adjoining every omitted vertex. The expected polynomial is independently computed from the theorem's falling-factorial formulas. The exact command is `python3 verify_rook_split.py`.

The completed check was `VERIFY_OK instances=14 candidate_subsets=1763152 forbidden_induced_tests=2K2_C4_C5`. Checked sizes include \((2,n)\) for \(2\le n\le9\), \((3,n)\) for \(3\le n\le6\), \((4,4)\), and \((4,5)\). All coefficients matched. In particular the small exceptional square and equal-exponent rectangular boundary were tested. No proof for infinite parameter families is inferred from the enumeration; the proof is in `RESULT.md`.

Independent mathematical audit: not performed.
