---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-20.md",
      "INDEPENDENT_AUDIT_2026-11-20.json"
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

Reconstructed from full-sphere quadratic-harmonic normalization 2 tr(A²)/[d(d+2)], the conditional fourth moments of x=t v+sqrt(1-t²)y, and the simplex tight-frame identity Σ_i v_i v_i^T=((d+1)/d)I. The trace-free vertex projectors B_i=v_iv_i^T-I/d have Gram spectrum (d²−1)/d² (mult d) and 0 (mult 1), giving exactly d and (d+1)(d−2)/2 concentration sectors. Differentiating the quartic zonal primitive yields b_d(a)=c_d(d+4)a(1−a²)^((d−1)/2)(a²−3/(d+4))/((d−1)(d+1)); trace via the degree-two addition theorem fixes the common scalar, giving exactly the two stated eigenvalues. Comparing 3/(d+4) with (d−1)/(2d) proves d3 unique interior coincidence, d4 cap-touching endpoint only, d≥5 none. Analyticity and positive-measure complement show 0<λ<1. Funk–Hecke yields the cubic xyz moment 8/(147√3). Independent separate moment-integration code (not repository check.py) diagonalized 15 full matrices for d=3,4,5,6,8 at distinct legal thresholds with absolute errors ≤3.0e−12, including boundary; an exact symbolic primitive identity and cubic moment were also checked. These finite tests corroborate, not replace, the all-d analytic argument.

## originality

PASS

Best-of-knowledge original as a November 8 full-family result: reviewed earlier general Slepian theory, primary cap/design literature, earlier same-center geometric records, and later exact tetrahedral special-case theorem. The later November 16 tetrahedral classification is algebraically the same d=3 case but postdates the candidate and leaves the dimension-uniform d≥4 two-branch formulas and sharp d=4/d≥5 coalescence boundary outside its hypotheses. No identified pre-November-8 source states or directly implies the complete claim. This is qualified historical originality, not a uniqueness certification.

## value

PASS

The union of equal simplex-centered caps is a canonical nonaxisymmetric spherical observation mask and the exact smallest/largest pure H2 concentration eigenvalues determine sharp measurement conditioning in each dimension. The complete two-sector spectrum, strict positivity, and exact first/only interior isotropic tetrahedral aperture are natural exact invariants, not an arbitrary isolated numerical slice. The sharp d=4 touching transition and permanent d≥5 noncoalescence answer a coherent dimension-family question; the nonzero cubic moment demonstrates the nontrivial restriction to degree two. The needed fourth-moment tensor and simplex rank argument go beyond a textbook one-polar-cap substitution, although their tools are classical. The work is valuable as an independent closed-form spectral classification without requiring an unrelated downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
