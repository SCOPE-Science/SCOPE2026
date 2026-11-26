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

On the even sector the spin-flip product for a density matrix with diagonal entries a,b and coherence c has nonzero square-root eigenvalues sqrt(ab)±|c| (using |c|²≤ab), so concurrence is 2|c|. In logical Bloch coordinates this is the length of the averaged xy projection. The x projection after m applications of a rotation about n is n_x²+(1−n_x²)cos(mθ), so its age average is at least min f_w, since min f_w≤1. A y-axis rotation removes the y projection and gives C=|f_w(θ)|; it extends by the identity on the odd space. Uniform convergence for arbitrary probability weights gives continuity and a minimum; if min f_w≤0, f_w(0)=1 ensures a zero. For p∈(0,1), the geometric transform p(1−q x)/(1−2q x+q²), q=1−p, is increasing in x=cosθ, giving p/(2−p) at x=−1, also valid at p=1. Uniform phase with period k≥2 has f_w(2π/k)=0 by the roots-of-unity sum. The matched quantity is the mean inter-reset interval, not the mean age.

## originality

PASS

The inspected primary and Resultary sources establish age mixtures, fixed-model Bell-reset concurrence or complementary optimizations; they do not cover the attained all-gate infimum as a functional of an arbitrary fixed age law. The universal projection bound and attaining rotation are both needed. This is a bounded statement-level decision, not a priority certification.

## value

PASS

This gives an exact robustness criterion for a reset experiment when the evolution is known only to preserve parity. The transform determines whether every permitted gate retains ensemble entanglement and yields a gate attaining the floor. Two clocks with identical mean inter-reset intervals can give strictly different worst-case guarantees, a meaningful distinction not supplied by fixed-gate diagnostics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
