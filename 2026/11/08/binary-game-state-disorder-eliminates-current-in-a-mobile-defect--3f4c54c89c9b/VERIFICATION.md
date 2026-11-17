---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Starting with one cyclic cooperative block of at least two and at least one defector, payoff P_i=-s_i+[r_(i-1)(s_(i-1)+s_i)+r_i(s_i+s_(i+1))]/2 gives boundary-defector-to-cooperator incentive r_(interior cooperative edge)-1>0 for defector runs of length >=2. The strict interval 1<r_L<r_H<1+r_L/2 guarantees an isolated defector cannot disappear and all rates a_j^+,a_j^-,b_j^+,b_j^- displayed in RESULT.md are positive. States S_j (one defector) and E_j (adjacent pair) make one irreducible 2n-state ring. Kolmogorov cycle-product ratio equals product_j [1+r_(j-1)/2-r_(j+1)]/[1+r_(j+1)/2-r_(j-1)]; on each step-two parity orbit every L-to-H change is balanced by H-to-L, so binary-product exactly one. Detailed-balance recurrence produces stationary probability and mean; homogeneous weights yield 2/r. Verified every binary environment on n=4..10 (2032 patterns) with exact rational factors at r_L=6/5,r_H=7/5. The ternary ring (11/10,11/10,6/5,11/10,13/10) yields exactly 77/75, so reversibility fails. The proof covers all n>=4 and binary arrangements; finite arithmetic checks alone are not the proof. Above-bound extinction is an existence example, not universal extinction.

## originality

PASS

Wei et al. analyze an active, randomly changing hypergraph public-goods model; Cooper et al. use different imitation/updating and homogeneous games on cycles. Detailed balance is standard, but payoff-specific two-type cancellation under every frozen edge arrangement and the third-type obstruction are not established in these works. Related published aspiration dynamics have a different Markov kernel.

## value

PASS

Frozen binary environmental heterogeneity is the first natural nonhomogeneous extension of the cycle imitation model. The exact cancellation of every binary label pattern, sharp dynamical trapping, explicit stationary defect number, and 77/75 three-level current distinguish reversible versus circulating stochastic dynamics; these are substantive structural invariants, not a cheap small instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
