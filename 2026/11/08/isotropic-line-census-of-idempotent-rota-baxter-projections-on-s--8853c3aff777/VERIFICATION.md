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

# Reproduction and limits

Run `python3 check_short_local_rb.py` with Python 3 and no additional packages. The script implements the stated multiplication in the basis \((1,e_1,e_2,z)\), including \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\). It enumerates all radical subspaces, checks subalgebra closure, constructs both projection orientations for every complement, verifies the Rota–Baxter identity on basis pairs, counts ranks and checks the proposed polynomial.

For each of three nonzero bilinear forms over \(\mathbb F_2\), the separate `brute_all_binary` routine exhaustively checks all \(2^{16}=65536\) linear operators \(A\to A\) directly for idempotence and weight-minus-one Rota–Baxter identity and compares their exact rank counts. This avoids assuming the splitting parameterization in the exhaustive check. The records for \(q=3,4,5\) use independent subspace enumeration rather than enumerating all \(q^{16}\) linear operators.

The saved observed output is `check_results.txt`, ending in `ALL_SHORT_LOCAL_RB_COUNTS_PASS`. Counts from a finite number of fields are corroborating tests, not proofs of the formula over all fields or of originality. The general statements follow from the explicit six-step proof in `RESULT.md`; no external proof assistant or independent mathematician has reviewed this package.
