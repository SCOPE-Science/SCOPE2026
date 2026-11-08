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

# Verification record
The standalone standard-library script `distributed_knowledge_verifier.py` directly evaluates \(D_Gp\) by quantifying over all worlds matching the distinguished point in every coordinate of \(G\). It exhaustively checks every valuation on the eight parameter tuples \((2,2)\), \((2,3)\), \((3,3)\), \((2,4)\), \((2,2,2)\), \((2,2,3)\), \((2,3,2)\), and \((2,2,2,2)\). Total: 74,832 valuations. Every semantic profile agrees with the downset characterization; every nonzero profile-fiber size agrees with the formula; the restricted nonempty-coalition profile count is correct; the explicit grand-only fiber agrees with the closed formula. The script prints `ALL CHECKS PASSED` on success.

The general all-size assertions follow from the five-step proof in `RESULT.md`, including an independent derivation of each factor in the counting formula. The Bernoulli probability law follows from disjoint signature-cell independence, and the asymptotic sharp scale follows from the logarithmic expansion of \(1-x\). Exhausting finitely many examples cannot prove the all-size theorem. No independent human or external correctness or priority certification has been performed.
