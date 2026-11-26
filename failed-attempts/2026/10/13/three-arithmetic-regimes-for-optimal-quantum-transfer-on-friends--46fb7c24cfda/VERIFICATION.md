---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The input and output pair have opposite projection product −1/2 on the −1 eigenspace, product (m−1)/(2m) on +1, and product 1/(2m) times the outer-state propagator on the remaining 2×2 block. The block with diagonal (0,1) and off-diagonal √(2m) gives exactly cos(Dt/2)+i sin(Dt/2)/D after extracting e^{it/2}. With x=t/2, the base amplitude peaks have modulus 1−1/(2m) at x_j=π/4+jπ/2; the squared loss away from them is 2α sin²(2δ), where α=(m−1)/(2m). In the nonsquare case positive time is dense in the two-torus, so one can independently maximize the fast phase. The projection near any base peak tends to |cos x_j|=1/√2 and the nonnegative base loss gives the matching lower bound on the deficit. In the square case periodicity makes the supremum a maximum; an O(1/m) competitor at x_j and the quadratic base loss force δ=O(1/D). On writing δ=z/D the scaled base loss tends to z²/2 and the cross term tends to cos x_j cos(Dx_j+z), uniformly on bounded z. Localization gives a bounded optimizing sequence, and testing any fixed limit minimizer gives the reverse bound. Reducing D modulo 8 gives the two phase offsets up to z reversal. The two objectives have second derivative at least 1−1/√2, are coercive and have unique minimizers; an independent bisection gave z=−0.318366325403 and −0.704812002001 and constants 0.419296833428176 and 1.305301344446716. The strict ordering also follows analytically from the lower bound on cosine loss and the |z|<1 and |z|≥1 estimates. These are unrestricted squared-fidelity limits, not finite-time or finite-grid maxima.

## originality

FAIL

A distinct Resultary record states all three sharp limits for the identical graph, endpoints and Hamiltonian and adds an exact non-PGST result at each fixed size. Conjugating the time convention leaves the probabilities unchanged, and setting u=2z equates the variational objectives. This establishes exact content overlap, not publication order or chronological priority.

## value

PASS

As a mathematical question the best possible single-edge fidelity is a natural transport invariant, and a sharp arithmetic difference invisible to amplitude perturbation bounds is substantive. This value assessment in isolation does not cure the exact coverage on originality or justify a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
