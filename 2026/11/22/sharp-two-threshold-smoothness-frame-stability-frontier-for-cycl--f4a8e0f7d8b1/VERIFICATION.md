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

Parseval reduces the squared excess budget to ||T||²≤β for the missing block T. The fixed m−1 observed edges give trace 2(m−1); the missing arc gives 2+Tr(T*AT)−2 Re Tr(B*T), A positive definite. The feasible ball is compact convex and the objective strictly convex; deleting interior observed columns weakly decreases norm and strictly decreases energy unless they are already zero. Reflection and conjugation preserve the problem, so the unique solution is real and maps endpoint parity into orthogonal missing parity. Hence the operator-norm constraint separates into two Euclidean ball constraints. Their resolvent solutions have strictly decreasing squared norms in the multiplier and harmonic norms q/2 and q(q−1)/(6(q+1)), obtained from affine interpolation and the centered square sum. This proves the thresholds including equality cases. The sine endpoint coefficients select odd/even modes, and substitution A v=b−λv gives each energy 1−G−λF. A surviving interior zero column gives the lower sharp frame bound 1. The small-budget unit-direction expansion gives −2√β+β⟨b,Ab⟩ per channel before adding constants, and the two quadratic coefficients sum to 4; q=2 uses eigenvalues 1 and 3. As an independent corroboration, 20 tests use the full matrix multiplier S≥0 for T*T≤βI, checking AT+TS=B, complementarity, the frame eigenvalues, harmonic energy and q=2 formula, in /workspace/branches/independent_replay.py (cycle). These finite certificates verify their instances only.

## originality

PASS

The all-completions constrained frontier and its independent release of the antisymmetric mode before the symmetric mode are supported as distinct. The harmonic endpoint is established prior, and both numeric harmonic feasibility values are already encoded in the prior isometric minimal-cycle harmonic spectrum on q=m−2. Those old values are not credited as separate discoveries; they do not solve the positive-multiplier modes or the exact active-budget trace curve.

## value

PASS

The exact optimum over all linear completions is a natural graph interpolation benchmark: the full Parseval coefficient energy is a worst-input amplification budget, while trace graph roughness is isotropic mean squared roughness. Endpoint locality, sequential parity release, exact frontiers across the budget continuum and limiting threshold ratio show what is gained by departing from either zero padding or unrestricted harmonic continuation. The benchmark does not rely on the already known harmonic endpoint as its new invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
