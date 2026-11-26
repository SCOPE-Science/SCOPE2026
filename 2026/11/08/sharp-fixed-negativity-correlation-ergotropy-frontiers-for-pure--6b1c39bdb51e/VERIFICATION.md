---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Partial-transpose eigenvalues for a pure Schmidt state are p_i and ±sqrt(p_i p_j), giving N=2 ln s. In the ergotropy difference the original energy cancels; global passivation has ground energy zero, and each marginal's passive energy is ω(p1+2p2). For z=sqrt(p1), write d=sqrt(2-s²+2sz−3z²), so q0,2=(s−z±d)/2. Ordered nonnegative roots require d≥|s−3z| and d≤s−z. The first inequality gives the (2s±D)/6 bounds, and q2≥0 retains only z≤(s−sqrt(2−s²))/2 when s<sqrt(2); the other quadratic branch lies above (2s+D)/6. Thus the exact section is a single closed interval. B=(s−z)d has derivative with sign of 3z²−3sz+s²−1; opposite endpoint signs show its sole in-section zero is the strict interior maximum. For the minimum, above sqrt(2) the endpoint spreads differ by D²/6, favoring the two largest equal; below sqrt(2), comparing the two endpoints reduces to 8(1+t²)−(s+3t)²=6(1−st)>0, t=sqrt(2−s²), favoring rank two. At sqrt(2) the minimizing-spread triple is (1/sqrt(2),1/sqrt(2),0), and the left spread slope diverges while the right is finite. At s=1 and sqrt(3) the sections are singletons. By continuity every intermediate work value is realized with a Schmidt-diagonal ket. Independent circle parametrization and angular optimization at six sections confirmed the two formulas (private replay: python3 /workspace/branches/independent_checks.py, qutrit_check). No uploaded checker executed; the continuum proof is analytic.

## originality

PASS

Best-of-knowledge pass for the exact fixed-log-negativity extremal range and spectra. The negativity formula and work at an individual spectrum are already established. The closest full-text comparisons do not perform the constrained simplex-section optimization or classify the rank transition.

## value

PASS

At fixed entanglement as measured by log negativity, correlation-locked work varies even for pure states. The result quantifies that variation exactly and shows why a rank-two ansatz fails on the lower-work frontier and above the upper-work threshold. It provides state benchmarks independent of a charging trajectory, not merely a replot of the known work identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
