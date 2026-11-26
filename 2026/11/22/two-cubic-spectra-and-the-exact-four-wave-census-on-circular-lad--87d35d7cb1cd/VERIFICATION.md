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

On a four-periodic trajectory any vertex that fires consumes all four steps of its cycle in the forced excursion, so cannot wait at zero. A neighbor that is identically zero would be excited by this vertex, and connectivity propagates this to all vertices. Thus every nonzero four-step return is a global phase advance, has least period four, and is characterized by every vertex having a successor-colored neighbor. At its unique resting time that neighbor provides exactly the required excitation. The 256-state transfer takes overlapping pairs of rungs; a length-n closed walk with an indexed start specifies one labelled word of rungs, even for a spatially repeated word. For n=3 the left and right neighbors are distinct as required. Only temporal translation gives the divisor four. Replay: python /workspace/audit-evidence/frozen1.py independently computes the exact full 256-state characteristic polynomial, checks the SCC sizes and four twisted determinants, and scans all microscopic states at n=3,4,5, finding respectively (1,1,121), (1,1,265), (1,1,2121) fixed by iterates (1,2,4). Subtracting the all-rest state gives the reported short counts. The determinant's nonzero spectrum has multiplicities 8 each at ±1 and ±i, twice the roots of each reciprocal-sign quadratic, and one copy of each cubic. The power sums give the displayed recurrences and the computationally checked values n=3–12. The first cubic has its only real root λ in (4,5) and a conjugate pair of modulus sqrt(4/λ)<1. The second is strictly increasing on the real line and has a real root ρ>1/4 and <1, so its pair has modulus sqrt(4/ρ)<4. Remaining moduli are at most sqrt(2), so λ is simple and strictly dominant and the stated fraction follows. The frozen scripts were inspected, not executed; the finite microscopic scan corroborates the transfer but does not prove the general law. Nothing here counts eventual basins.

## originality

PASS

The distinct supported contribution is the all-n labelled four-cycle census with explicit low-degree spectral terms and exact exponential growth, not the GH rule, successor-phase principle as a general framework, or generic use of a cyclic transfer. The pentagonal-prism computation exactly covers n=5; the order of the two same-day records is unknown. The best inspected related all-length results differ in their graph, dynamics or boundary conditions. Older-source access limits remain.

## value

PASS

The family is a canonical periodic width-two graph, where time-periodic phase waves and the normalization against all states are natural invariants. The exact finite transfer spectrum condenses the infinitely many counts into two cubics and explicit parity corrections, distinguishes absolute from fractional growth, and provides reproducible benchmarks beyond the already counted pentagonal instance. It does not purport to quantify attraction to those waves.

The dated certificate retains the supplied scientific assessment, sources and limitations.
