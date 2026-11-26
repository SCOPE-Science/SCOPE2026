---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The reset generator is L0 + r(rho0 Tr − I); evolution forgets the initial state because the no-reset fraction decays as exp(−r t). In the stationary trace-one system, if n is the double-excitation population, u,w are the single-excitation populations and h is the Bell coherence, then 0=r/2−(r+S)n, 0=gamma1 n−(r+gamma2)u, 0=gamma2 n−(r+gamma1)w, and 0=r/2−(r+S/2)h. These equations recover the announced density; all other coherences vanish and the normalized reset mixture is positive. The correlation diagonal (t,−t,v) gives B by the Horodecki criterion for binary qubit measurements with both outcomes, and the X-state spin-flip expression yields C>0 and strict decrease with Q, including the Q=0 endpoint. The numerator of v−t is an affine increasing function of Q with sole root Qc; Qc/S² grows from 0 to 1/4 as r/S reaches 1, and v increases in Q. On 0<r≤S the equal-loss envelope satisfies 1−t²−v_bal²>0, since S³+S²r−r³≥S³>0; also 2t²<1 there. Above S the transverse branch decides the equality and violation threshold. Thus the full invariance for r≥S, the low-rate flat/strictly increasing branches, and the exact examples all hold. Independent symbolic replay: `python /workspace/review-evidence/reproduce.py 2` derives the stationary system and checks the witness numerator, envelope and four examples. The continuum conclusions are analytic; the bundled numerical checker was inspected, not run.

## originality

PASS

The equal-loss boundary and two-branch CHSH expression are prior coverage. The supported distinct contribution is the complete fixed-total-loss comparison across unequal and one-sided damping: the invariant violation boundary, full high-reset invariance, loss-product witness switch and opposing concurrence/Bell ordering on the longitudinal branch. Actual inspected reset methods and the equal-loss theorem do not give that cross-allocation classification.

## value

PASS

At fixed total decay, each diagnostic answers a different question about a physically meaningful loss imbalance. The exact switch explains when an optimized Bell test is blind even as entanglement changes, and when the two diagnostics rank loss allocations oppositely. This is a structural, all-parameter distinction, not simply a stationary matrix computation or a repetition of the equal-loss threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
