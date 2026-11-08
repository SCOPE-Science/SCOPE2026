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

# Verification

The analytic proof covers every finite nonempty poset, without a size cutoff; it relies on precisely stated hypotheses for Stanley's transfer map, the continuous FKG theorem, Holley's stochastic monotonicity criterion and a strict scalar covariance lemma.

The included `check_order_chain_inertia.py` script uses Python 3's standard library, with `fractions.Fraction` for exact arithmetic and a deterministic seed for supplemental cases. It independently enumerates all 5230 transitively closed, naturally labeled posets on two through six vertices; for each poset it enumerates linear extensions, computes first and second moments of the order and chain coordinates, computes the exact boundary covariance, and verifies every identity and the strictness classification. It also checks 250 generated seven-vertex posets and the three-chain gap \(1/80\). Expected terminal marker: `ORDER_CHAIN_INERTIA_FKG_CHECKS_PASSED 5230 3708 1522 250`.

Finite enumeration does not establish the universal inequalities. Proof of association and strictness is analytic, not computational. No independent mathematical audit has been performed.
