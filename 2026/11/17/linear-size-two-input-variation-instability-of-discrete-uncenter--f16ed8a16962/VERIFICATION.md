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

# Verification and scope

The exact-rational script `verification/check_bv_instability.py` reconstructs the interval maximal operator, the alternating-tail data and the complete output difference for the specified small witness values. It checks every odd response is zero, every even response is at least half the perturbation, and the total-variation ratio exceeds the analytic lower bound. It also checks the strict prefix threshold and low-vertex witness inequalities for a larger symbolic integer range.

The proof for every integer \(n\ge24\) is an analytic combinatorial interval argument and a zero-padding reduction. The failure of local Lipschitz continuity on \(BV(\mathbb Z)\) follows from the same inequalities, two variation jumps, and positive homogeneity. Finite computations alone cannot establish the infinite-dimensional statement. The results have received a self-review, not an independent audit.
