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

# Exact arithmetic reproduction

Execute `python3 verify_cayley.py` with standard Python 3. No packages beyond the standard library are required. The script checks the four integral coefficient equations after substituting the explicit dual-number-pair family, computes the Jacobian determinants at each of the three diagonal lines, and verifies the top Chern coefficient \([\alpha^3\beta^2]\bigl((\alpha-\beta)c_4(\operatorname{Sym}^3\mathcal S^\vee)\bigr)=27\) as an exact integer. It exhaustively enumerates \(35\), \(130\), and \(806\) projective lines on \(\mathbb P^3\) over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\), finding exactly nine in the Cayley cubic in each case. The recorded output `verification_output.txt` ends with `ALL_CHECKS_PASSED`.

The proof for all characteristics additionally relies on the classification by projection from a node and a smooth conic, regularity of the Grassmannian zero scheme in each zero-dimensional fiber, the top-Chern length, and proper/quasi-finite plus Nakayama descent. The script's finite tests do not alone establish these infinite statements. Independent audit is not performed; a specialist literature search could reveal an equivalent older calculation.
