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

Run `python3 verify.py` using Python 3.9 or newer and the standard library only. The program creates the triangular-graph adjacency masks directly from the edges of a labeled complete graph. It checks total domination by open neighborhoods and checks inclusion-minimality by testing every single deletion. Separately, a labeled-component recurrence evaluates the two generating functions and compares coefficients.

Observed output ended with:

`VERIFY_OK full_graph_orders=3..7 restricted_order=8 tested_subsets=2630165 minimal_sets=36943 all_and_minimal_polynomials=PASS arithmetic_orders=4..30`

Every one of the \(2^{\binom n2}\) selected-edge subsets was tested for each \(3\le n\le7\). For \(n=8\), the search covered precisely all subsets with sizes between two and the proved maximal possible inclusion-minimal size \(n-2=6\), rather than every subset of \(E(K_8)\). The pure integer recurrences checked the exact spectrum and upper-coefficient expression for \(4\le n\le30\). Enumeration over finitely many values does not certify the general theorem, which follows from the structural proof in `RESULT.md`.
