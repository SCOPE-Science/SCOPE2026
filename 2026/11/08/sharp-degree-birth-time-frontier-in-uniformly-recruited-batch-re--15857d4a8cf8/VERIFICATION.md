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

Use deterministic labels within each batch. The independently uniform recruiter at each time has probability 1/[1+m(t−1)] of selecting a specified eligible label. Summing its log-mgf over times after birth at i comparable to n^u gives (1−u)(exp(theta)−1)log(n)/m+O(1); the squared-probability error is summable. For x>(1−u)/m, Chernoff and a tilt to mean (x+epsilon)log n, with O(log n) tilted variance, give the stated rate uniformly within a cohort of fixed multiplicative width. At each time conditioning on one label being selected suppresses selection of a second; conditioning on the first label's full selection vector leaves the second's selections independent by time. The product-measure monotonicity inequality then gives nonpositive upper-tail covariance, and a cohort with expected exceedance count at least n^c has probability at most n^(-c) of no exceedance. The strict concavity of u−I_u(x) gives the saddle x*=1/log(m+1), u*=1−mx*/(m+1). For a<u*, the boundary equation at u=a has a root between 1/m and x*: u−I_u(1/m) increases from zero up to u*, while a−I_a(x*) is negative. This root has positive u-derivative throughout [0,a]; for a>=u* the saddle is accessible. The displayed u_m in the definition line and nu_m in subsequent lines are the same constant, as is fixed unambiguously by the saddle and example. For x just above or below the frontier it suffices to use upper bounds over a finite exponent mesh and a single positive-exponent cohort for the tilted lower bound. In the bin near u=1 fix a tilt with theta x>2 and then shrink the bin so its log-mgf contribution is below (1/2)log n. The resulting power-error bounds are summable on geometric times; monotonicity fills gaps. At a=0 a finite number of fixed labels gives the separate 1/m limit by the same Chernoff argument. The unique global saddle leaves a strict rate gap outside every fixed birth-exponent neighborhood, including the last bin; this yields the stated convergence in probability for the earliest maximizer, in fact by excluding every outside maximizer with probability tending to one. Inspected frozen verify_max_degree.py and VERIFICATION.md without execution. The exact finite joint checks there use distinct birth steps, not pairs in a single batch; the product-measure argument applies to either. The finite diagnostic is not an asymptotic proof.

## originality

PASS

The model and the batch contraction are known, and much stronger global extreme-degree and birth-label theory is known for the ordinary recursive tree. The supported distinct contribution is the full almost-sure age-restricted recruiter frontier for fixed m>=2 with its saturation threshold and location consequence. Neither known result transfers through the contraction without analyzing individually marked incident edges, and the primary comparisons examined do not provide that marked age-constrained extremum.

## value

PASS

The curve separates the benefit of extra recruitment time from the greater number of contenders at later birth ages. It supplies an exact transition from an active age constraint to saturation, and its unique saddle explains which birth scale produces the global maximum. The full constrained curve is more informative than merely scaling a marginal mean or restating a maximum-degree constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
