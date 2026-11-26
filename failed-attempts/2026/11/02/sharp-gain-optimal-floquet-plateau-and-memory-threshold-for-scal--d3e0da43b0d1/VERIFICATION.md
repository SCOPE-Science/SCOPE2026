---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For a primitive two-cycle the positions must be nonzero and of opposite sign: at zero the memory alone contracts, and the two displacements must cancel. With a=λ|x₁|, b=λ|x₂| and memory square roots u,w, cancellation gives a(u+ε)=b(w+ε), whereas the memory equations give (1+β)(a²u²−b²w²)=β(a⁴−b⁴). Unequal a,b give opposite signs, so the cycle is antipodal, with memory λ²r² and r=h/2−ε/λ>0. At the positive phase the Jacobian entries are −1+4(1−β)r/h, 2β/(hλ²), 2(1−β)λ²r, β in row order. Position reflection R gives the return derivative (RJ₊)². The trace and determinant of RJ₊ are t=1+β−4(1−β)r/h and β. The degree-two Schur inequalities reduce to 1−β>0 and 1+β±t>0, both strict for every supercritical gain, giving local exponential attraction at the smooth nonzero states. The two-step spectral radius equals its lower bound β precisely for |t|≤2√β. The trace decreases from 1+β to −1+3β, and 1−3β−2√β=(1−3√β)(1+√β), so the finite exit exists exactly below β=1/9 and at equality only the infinite-gain limit reaches that edge. At a finite edge the nonzero off-diagonal makes the repeated nonzero root defective, and squaring preserves the Jordan defect. Substitution verifies [3,8] in the exact example. The uploaded checker was inspected, not executed.

## originality

FAIL

No inspected source states the exact 1/9 split verbatim. However, the same-map earlier general Floquet formula, combined with its reduced cycle equation, specializes directly to the scalar polynomial for every admissible gain. Both stability and the claimed optimal interval are mechanical consequences of the trace range and quadratic discriminant; this is coverage by implication, not an exact catalogue duplicate or a historical priority judgment.

## value

FAIL

The gain interval is a useful tuning readout and the Jordan caveat is accurate, but for the frozen scalar map both are direct quadratic-spectrum calculations from the earlier exact formula. The record does not resolve an independent dynamical gap such as basin size, nonlinear endpoint rates, or a setting not already covered by the formula. The failure is for the mechanically implied result as a standalone contribution, not for studying gain tuning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
