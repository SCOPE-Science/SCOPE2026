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

# Reproduction and proof checks

Run `python verify_abelian_c2.py` using Python 3 and its standard library. The program enumerates all finite abelian-group isomorphism types of orders 1 through 128, checks all 351 pairs of distinct types at equal orders, and confirms equivalence precisely when the three theorem invariants agree. It independently normalizes the 27 possible placements of two variables and the identity inside the ternary relation on groups of orders at most 36, then tests larger order examples. The expected terminating marker is `VERIFY_OK`; all output from the completed run is preserved in `verify_abelian_c2.out`.

The proof was separately checked symbolically: counting formulas for the sizes of groups, cubic-torsion sets and 2-power kernels each use only two variable names; the cardinalities of 2-power kernels uniquely recover finite abelian 2-group cyclic factors; the odd-coordinate class partition is equitable for every atomic two-variable pattern because square, inverse and unique square root have exactly the coincidence patterns listed in RESULT.md. This argument is independent of a finite enumeration cutoff.

Limits: Code does not prove the theorem for arbitrarily large groups. The sufficiency induction and group decomposition establish the infinite quantifiers. No external independent audit has been conducted. The publisher's journal version of Gomaa's 2010 work was not fully inspected; its publicly available dissertation counterpart was materially read.
