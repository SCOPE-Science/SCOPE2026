---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The inspected RESULT.md and checker.py use the canonical full-Laplacian Euclidean simplex in 1^⊥, not lattice-equivalent coordinates. Verified the known vertex-transitive metric lemma: facet normals are L⁺ e_i, equal squared lengths tr((L⁺)²)/(2m), so R=√12 and r=(2m tr((L⁺)²))^(−1/2). The prism Laplacian spectrum is common cyclic band 2−2cos(2πj/m) (j=1..m−1) plus periodic 4−2cos(2πj/m); the Möbius ladder has the same first band and antiperiodic 4−2cos((2j+1)π/m). Their reciprocal-square traces are A_m and B_m from the theorem. The common band contributes (m²−1)(m²+11)/720. Sampling the absolutely summable cosine Fourier series of (4−2cos θ)^−2 gives the exact positive difference (m q^m/3)[2/(√3(1−q^(2m)))+m(1+q^(2m))/(1−q^(2m))²]. Independent exact rational matrix inversions for m=3,4,5,6 yielded trace gaps 2/25, 125/3528, 5570/393129, 179/33800 respectively and agreed with the displayed expression. Asymptotics A_m,B_m~m⁴/720 and A−B~m²q^m/3 yield relative gap 120q^m/m² and absolute gap 720√10 q^m m^(−9/2). Infinite m follows analytically; finite inversions only corroborate.

## originality

PASS

PASS on best-of-knowledge priority for the precise two-family metric comparison. The known general vertex-transitive simplex theorem already supplies inradius in terms of tr((L⁺)²), and Azimi–Farrokhi supply exact pseudoinverse entries for circular and Möbius ladders. These establish ingredients from which the new traces can be computed, but their inspected formulas/results do not assert this squared-trace difference, its strict sign and sharp exponentially small inradius comparison. The nontrivial periodic/antiperiodic Fourier-aliasing identity provides the new comparison. An earlier unlocated closed-form biharmonic-index comparison remains a meaningful risk.

## value

PASS

A natural pair of cubic vertex-transitive graphs with the same order and Euclidean circumradius provides a motivated test of whether a global spectral inradius detects a boundary twist. The strict all-m order and exponentially small sharp gap are an independently useful quantitative distinction not supplied by the general metric lemma, Kirchhoff indices or tree-count identities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
