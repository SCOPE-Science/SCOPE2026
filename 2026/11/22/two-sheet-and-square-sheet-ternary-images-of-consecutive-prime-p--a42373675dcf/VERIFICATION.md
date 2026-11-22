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

The proof is symbolic and covers every positive exponent parameter \(s\) and every modulus depth \(n\). The critical checks are the binomial coefficient valuation \(\nu_3\binom{3^s}{j}\ge s-\nu_3(j)\), the two residue-branch isometries, and the square-conjugacy at the symmetric critical point.

Run `python3 check.py` with standard Python 3. The program exhaustively compares the complete residue-to-preimage-count maps for \(s=1,2\) through depth \(9\), and for \(s=3,4\) through depth \(8\), totaling 34 finite rings. Its expected counts are derived from square-root multiplicities independently of direct polynomial enumeration.

Finite tests alone do not prove the all-depth result. The asserted bibliographic distinction relies on mathematical implication comparisons; unindexed equivalents remain possible. Independent audit has not been performed.
