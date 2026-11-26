---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

With y=x² and A=(y+1+q)²−4y, the density after dropping the positive scale factor is w/(y+q)+2(y+1+q)/A. Its negative y-derivative has numerator wA²+2(y+q)²[(y+1+q)²−4(q+1)] over (y+q)²A², recovering the displayed quartic; the x-derivative contributes 2x. Independent rational reconstruction verifies the primitive quartics and the sign values at (0,1/10,1), (0,1), and (0,1/20,1/5); Descartes bounds 2,1,2 are attained by distinct roots, and the all-positive fourth quartic has none. The center is simple since its quartic constant is nonzero. Parity and derivative signs give exactly 3,2,3,1 strict maxima across the entire line. Rational masses yield a 249-observation equal-weight KDE after positive normalization. Small perturbations preserve the counts at all four heights: in disjoint neighborhoods of the simple zeros, the second derivative stays nonzero and the derivative retains opposite signs at the ends; on the remaining compact set its modulus is bounded below, and outside the hull of all perturbed observations every individual kernel derivative has the same outward sign. No radius or intervening bifurcation diagram is certified. Read the supporting evidence; the uploaded script was inspected but not executed. Replay the independent rational check with python3 /workspace/branches/a2e15b43-97d4-4238-a498-12de4cbe5b6a/reproduce_exact.py.

## originality

PASS

Best-of-knowledge pass for the exact positive rational, reentrant four-height witness only. Cauchy mode creation in positive-data KDEs is already stated in the literature; it is not a new general phenomenon.

## value

PASS

This is a motivated exact counterexample rather than an arbitrary density census. It certifies disappearance, reappearance, and final disappearance in a single three-location positive family, and the signs are enough to distinguish genuine modes from degenerate numerical peaks. The equal-weight and distinct-site realizations transfer the witness to ordinary data KDEs. No value is assigned to rediscovering the qualitative possibility, or to unasserted minimality or a full phase diagram.

The dated certificate retains the supplied scientific assessment, sources and limitations.
