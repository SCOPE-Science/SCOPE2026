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

Run `python3 verify.py` with Python 3 and no external packages. The checker enumerates all 269 ordered part-size tuples with two to four parts, sizes one through four, total vertices at most eleven; an integer Walsh–Hadamard transform from the graph's connected-set indicator is compared coefficient-by-coefficient with the derived exact multiplier formula. The same run computes all zero coefficients from the separate generating-polynomial expression and checks sharp positive singular gaps and invertibility in every case. No random sampling is used. The script confirms representative ranks and nullities as printed by the command.

The unrestricted theorem is established by symbolic character orthogonality, parity and finite combinatorial counting in RESULT.md; the finite checker does not extend its tested range or establish historical priority. Independent external validation has not been performed.
