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

The linear-first Gram recursion gives the coefficient convolution M_1 F_f=M_f with the conjugated atom coordinates. Clearing denominators gives Q=(1-a)+a(z-1)^2, a=(1+2 cos ε)/3. Both simple poles are outside the closed unit disk throughout the claimed interval. Evaluating the residues using h=z−1=±iε/√3+O(ε³) gives leading numerator coefficients (2/3, −1/3∓1/√3, −1/3±1/√3) times ε²/3. The two rows are orthogonal with Euclidean squared norm 4/3. In the stated weighted domain norm the leading residue map has norm ε/√3, with an operator-norm error O(ε²). The reciprocal poles have modulus r=1−ε²/6+O(ε⁴) and phases ±θ with θ=ε/√3+O(ε³). In the squared geometric-weight mean the relative cross term is bounded by (1−r)/|1−r exp(2iθ)|=O(ε). Cauchy–Schwarz then gives the uniform upper bound; a unit input parallel to either leading residue row kills the other row at leading order and attains the bound by the reverse triangle inequality. Multiplication by r/(1−r) gives 2√3 after scaling by ε; the zeroth coefficient is bounded independently of ε. For fixed separation the absolutely convergent series evaluates to f at each atom, since the common simple singularity of M_f and M_1 has ratio f at that atom. This verifies both the optimum constant and absolute reconstruction.

## originality

PASS

Fixed-separation finiteness is covered by the finite-atomic absolute-convergence theorem and finite dimensionality. The distinct supported claim is the sharp uniform collision law for the infinite coefficient ℓ¹ norm; neither the strongest adjacent quantitative statements nor the general transform and convergence results inspected supply that sharp limit. This is a bounded comparison, not a claim of absolute priority.

## value

PASS

Finite-support absolute convergence is qualitative and does not distinguish well-separated from nearly coincident samples. This minimal symmetric example beyond the planar case quantifies precisely the loss of uniformity and separates the effects of pole damping, oscillatory cancellation and residue geometry. The constant is a benchmark for coefficient estimates, not just another demonstration of convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
