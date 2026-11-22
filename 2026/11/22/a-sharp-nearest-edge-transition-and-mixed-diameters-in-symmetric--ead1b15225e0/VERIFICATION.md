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

# Verification of the symmetric Monge simplex metric extrema

Execute `python verify.py` from this directory with Python 3; it requires only the standard library. The program builds the complete normalized vertex matrices from the block and star formulas, checks their adjacent Monge inequalities and sum-one conditions, then computes every unordered pair distance using actual matrix coordinates and exact rational arithmetic.

The independent coordinate computations are compared with the three symbolic Gram formulas. The program then verifies the minimum and diameter values **and complete sets of attaining vertex pairs** for all orders \(2\le n\le12\), testing 3, 15, 45, 105, 210, 378, 630, 990, 1,485, 2,145 and 3,003 unordered pairs in the respective dimensions. The concluding observed output is `SYMMETRIC_MONGE_EUCLIDEAN_EXTREMA_EXACT_PASS`.

The finite checks do not prove the statements for unrestricted \(n\). The proof in `RESULT.md` supplies the all-dimensional crossing-support bound, nested-one-step reduction, mixed-pair monotonicity and exact cubic maximizer; those are the critical mathematical arguments. Historical novelty remains subject to independent literature verification; this is not an independent mathematical audit.
