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
# Reproducible finite checks

Run `python3 verify.py` with Python 3.9 or newer; no third-party dependencies. The script derives ring operations from explicit finite arithmetic, reconstructs projective points and determinant-zero incidences, and verifies the proposed coefficient formula.

For each of \(\mathbb Z/4\mathbb Z\) and \(\mathbb F_2[t]/(t^2)\), it exhaustively checks every independent subset of nonzero determinant coordinate fibers, weighting an independent subset of size \(k\) by the number \(|R|^k\) of scalar lifts. Both yield exactly 610173 independent sets, independence number 6, and 262144 maximum independent sets on 60 matrix vertices. For \(\mathbb Z/9\mathbb Z\) and \(\mathbb F_3[t]/(t^2)\) it checks projective-line counts, nonprimitive compatibility and closed coefficients but not an exhaustive graph independent-set enumeration. It also exhaustively checks field boundaries for \(\mathbb F_2\), \(\mathbb F_3\) under the separate field formula. A successful run ends with `VERIFY_OK`.

All unbounded cardinalities and the formula for every allowed chain ring follow from the written mathematical proof, not from finite enumeration. This verification is an ordinary computational replay, not an independent audit.
