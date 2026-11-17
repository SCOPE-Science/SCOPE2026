---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For every fixed 0<=b<1 at a=4(1+b)/(1-b), direct substitution gives a symmetric prime two-cycle and F=T^2 multipliers 1,b^2. With R=-T, the local center map q -> -q+c2 q^2+c3 q^3+O(q^4) has c2=(1+b)/(1-b) and c3=(1+b)(1-3b)/(1-b)^2; the second iterate is q -> q-[4(1+b)/(1-b)]q^3+O(q^4). The strictly attracting parabolic normal form and transverse b^2 contraction yield local asymptotic stability, strong-stable exceptional curve and n^(1/2) coordinate displacement coefficient sqrt((1-b)/(8(1+b))) outside that curve. The b=0 degenerate transverse collapse is allowed. Independently rederived symbolic coefficients; finite trajectories in the supplied code corroborate but do not establish the universal statement.

## originality

PASS

Full arXiv HTML of Itin 2026 Theorem 1 and Appendix A Proposition 8 directly gives the symmetric orbit, nonhyperbolic unit multiplier at A=4, and asymmetric branches for A>4. It does not give nonlinear center attraction or a discrete-time n^-1/2 coefficient at A=4. Existing general center-manifold/flip theory permits such an analysis but does not determine this map-specific coefficient. Resultary semantic searches found no other covering theorem; closely related scalar Soft Muon and momentum oscillators are different maps and equilibria. Best-knowledge PASS with explicit historical risk.

## value

PASS

At the precise parameter equality where Floquet linear stability cannot decide the orbit fate, the claim determines attraction versus repulsion, an actual physical-coordinate critical relaxation constant for every fixed momentum b, and the codimension-one faster stable exception. The sharp critical-boundary analysis is a natural, nonroutine quantitative bifurcation result even though the orbit and its linear criterion were previously known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
