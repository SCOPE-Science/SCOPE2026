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

Grouping the scalar unit-row projections by measurement value gives P_ij=n_j exp(-η|v_i-v_j|)/Z_i. The symmetric conductances n_i n_j exp(-η|v_i-v_j|) have degrees n_i Z_i, including the self-loop weight n_i^2; after normalization these give detailed balance and the exact unique invariant law. Taking η→∞ gives squared multiplicities, with sharp corruption bounds because k ≤ sum k_j^2 ≤ k^2, and stationary squared error strictly positive. At a clean start the escape probability is the same on each survival step, with leading coefficient k_*/g from all nearest bad levels; the ordinary geometric law gives the claimed scaling. The ordered exponential kernel is positive definite: a Gaussian Markov recursion with successive correlations exp(-ηd_i) has this kernel and independent innovations of positive variance. For the spectral gap, the two-block Rayleigh test has scaled energy tending to the unique adjacent cross-edge contribution, and its variance tends to M_L M_R(A-B)^2/(M_L+M_R)^2. Conversely centered unit-variance minimizers are uniformly bounded and their scaled energies are bounded by the test; every internal adjacent coefficient tends to infinity after scaling, forcing each subsequential limit to be constant on each side. The one surviving cross-edge gives the matching lower bound n_a n_(a+1)(1/M_L+1/M_R). The two-state recurrence gives the claimed transient and joint limit. Replay python3 -B /workspace/checks/kaczmarz.py: direct rational row-level two-value iterates agree exactly; a separate calculation from the principal minors of I-P gives scaled gaps 0.617647095607356 and 2.450000000000000 at η=18 for two distinct three-level examples, versus limits 21/34 and 2.45. The proof, not the numerical diagnostics, gives the asymptotic.

## originality

PASS

Credit existing generalized residual-weighted sampling, the weighted-degree stationary identity and the standard two-mass bottleneck coefficient structure. The supported contribution is the joint fixed-exponential scalar corruption analysis: squared-multiplicity bias and sharp corruption bounds, nearest-level first-error clock, and matching sharp relaxation law in this concrete dense kernel where other conductances vanish too. This is not a new general reversibility principle or universal weak-link formula.

## value

PASS

The example is a natural stress test of a residual-downweighting method on inconsistent measurements. It gives three distinct, exact diagnostics: the geometry of repeated bad values determines limiting bias, the nearest bad level controls the first corruption, and the longest adjacent gap controls global relaxation. A sharp, fixed-prefactor limit distinguishes relaxation from merely a conductance order estimate, and the two-level transient clarifies why apparently accurate short runs do not disprove persistent stationary error. The claims do not generalize this caution to all weighted Kaczmarz algorithms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
