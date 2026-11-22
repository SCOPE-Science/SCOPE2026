---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For any q-grid separation δk, the two-cluster invariant submanifold with one oscillator separated from N−1 gives δdot=−gN H(δ). Full exponential attraction of all grid states forces H′(2πk/q)>0 for every k including synchronized k=0. For odd real trigonometric H of degree d<q, sum over q roots of unity of the derivative equals zero, contradiction. H(s)=sin(qs) is sharp: every grid Jacobian has relative eigenvalues −gNq and one global phase-zero eigenvalue. On the q-cover the flow reduces to first-harmonic attractive Kuramoto gradient ascent, whose nonzero-order-parameter mixed antipodal equilibria are unstable; zero-order-parameter equilibria are minima, and almost-all trajectories converge to synchrony, yielding exactly q^(N−1) lifts. The deck group permutes basins so each Haar share is q^(1−N). Independent exact root-sum numerical residuals <2.2e−13 for q≤15. Pure-harmonic covering/basin facts are prior work, not new.

## originality

PASS

Delabays 2019 FULL original PDF establishes q-fold covering, fixed-point stability and basin rescaling of pure higher harmonics. This entire sufficiency/census portion is not independently original. The separate sharp necessity lower bound d≥q for *all* labelled grid states under any odd trigonometric interaction uses root-of-unity orthogonality and is not in the inspected Delabays results; related 2025 and 2026 works motivate but do not imply it. Novelty is restricted to the lower bound.

## value

PASS

A network-size-independent sharp Fourier degree barrier answers a natural simultaneous multistability design question for all phase colorings. Unlike merely observing multicluster dynamics for a chosen harmonic, the obstruction proves a lower bound for arbitrary mixtures, is attained, and sharply identifies its domain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
