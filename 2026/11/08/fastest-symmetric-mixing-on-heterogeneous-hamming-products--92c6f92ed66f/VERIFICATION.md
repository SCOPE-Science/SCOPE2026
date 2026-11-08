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

# Reproducible checks and their logical limits

Run `python3 verify.py` with Python 3.9 or newer. The script requires only the Python standard library. It constructs each finite transition matrix with exact rational entries, checks every row sum, and applies that matrix to a full tensor basis consisting of one constant vector and \(q_i-1\) independent zero-sum contrast vectors in each coordinate. It also compares the exact candidate SLEM with rational-grid feasible designs and rechecks the all-\(Q\) benchmark on a finite range.

The tested tuples are \((2,3)\), \((2,9)\), \((3,4)\), \((2,3,4)\), \((2,2,3)\), \((3,3,4)\), and \((2,3,3,2)\). The expected output is `VERIFY_OK 7 tensor basis families, 144 exact basis vectors, 1458 rational-grid designs, 17 comparison examples`.

Crucially, neither the finite tensor checks nor the rational-grid enumeration proves the theorem for every parameter or every feasible stochastic matrix. The universal proof is the operator-norm symmetrization, tensor eigenbasis, elementary capacity bound and one-dimensional minimax in `RESULT.md`. The finite checks are consistency/reproducibility evidence only. Publicly available literature comparisons do not independently certify novelty.
