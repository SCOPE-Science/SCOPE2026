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

# Computational and mathematical verification

The standalone `check.py` performs exact fraction arithmetic with no external dependencies. Execute `python3 check.py` to validate the renewal balance equation, sharp TV inequality, and zero-bias/return equivalence on 771 connected simple graphs of orders two through five, 480 positive rational directed cases, and 46 star/directed-cycle boundary cases; 19,556 test instances completed successfully. It separately solves finite directed invariant laws by exact linear elimination.

The unrestricted statement is proved symbolically in `RESULT.md` by renewal-reward, telescoping, total-variation contraction and the periodic-chain limit theorem. Enumeration of finitely many graphs and random directed examples is supporting evidence only. Timing conventions require stationary equilibrium-renewal sampling, not deterministic-phase convergence. Source novelty comparisons and scientific value are assessed in `REVIEW.md` and `AUDIT.json`, with independent external audit not performed.
