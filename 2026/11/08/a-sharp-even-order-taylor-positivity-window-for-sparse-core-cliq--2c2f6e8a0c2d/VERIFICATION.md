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

# Exact-arithmetic verification

Run `python3 verify.py` using only the Python standard library. The verifier builds the full unweighted join Laplacian for every tested graph, computes the completed Taylor polynomial with exact `fractions.Fraction` arithmetic, and independently checks the join projector formulas, all row sums, and matrix-entry signs before and after a rational bracket containing the unique positive root.

Actual run: `VERIFIED 222 graph/order cases and 231840 exact entry comparisons`, followed by `All beta brackets, block identities, row sums, and signs passed.` Tested orders: 2, 4, 6, 8, 10; clique sizes 1 through 4; connected and disconnected residual graphs with degree bounds satisfying the theorem. Every outside test checks a strictly negative clique-to-core entry.

The exact polynomial proof establishes the infinitely many parameters and graphs; these finite tests cannot certify an infinite family, publication novelty, or independent validation. Other graph structures and odd Taylor orders are outside the claim.
