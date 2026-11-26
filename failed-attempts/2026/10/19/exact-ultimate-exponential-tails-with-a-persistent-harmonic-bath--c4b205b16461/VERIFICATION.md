---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The semigroup is the common-mode projection plus an exponentially decaying part, so both conditional innovation variances are 2D_c t+O(1). At reset events the bath evolves by an affine recursion with coefficient β(T) in (0,1) almost surely. Its backwards innovation series has finite conditional variance almost surely since Eβ²<1 and EV_y(T)<∞. Products of coefficients vanish almost surely (infinitely many intervals exceed a fixed positive duration), giving uniqueness beyond finite-moment initial laws. The independent stationary Poisson backward age and earlier spacings construct the invariant joint law. For the conditional-variance recursion, the normalized one-step exponential drift tends to zero by domination below r/(2D_c); iteration bounds the requisite bath transform. In the tracer age integral the bath multiplier is uniformly bounded below the cutoff and at least one by symmetry, proving divergence also at equality. Chernoff gives the tail upper bound; bounded initial bath and age in [uz,uz+1] cost ru+1/(4D_c u) per unit displacement, minimized at √(r/D_c), giving the matching lower bound on each side by symmetry. The dimensionless specialization is correct. An independent generator calculation reproduced Var X=3/2 and Var Y=9/4 at unit parameters (/workspace/independent_checks.py); second moments do not certify tails. No density asymptotic or singular-parameter uniformity is established.

## originality

FAIL

Resultary 6d27e15f4a50 directly covers the dimensionless tracer result and also proves the bath marginal result. For arbitrary positive diffusivities at the same drift, there is an exact comparison to that reference theorem: choose D_x^0=ad, D_y^0=bd with d=D_c(a+b)/(ab), which preserves D_c. Rescaling time by a and both coordinates by √d reduces the reference model to that theorem with γ=a/b and rate r/a. On common Poisson spacings both models have the same coefficients β(t), α(t). The difference of their free bath innovation variances is O(t) near zero and O(1) at infinity by the shared leading slope, so its absolute value is bounded by C(1−β(t)^2). The conditional stationary bath variance difference is then bounded by C by telescoping the product-weighted series. The conditional tracer variances likewise differ by a uniform constant. This transfers the entire open MGF interval including endpoint divergence by multiplying the conditional MGF by bounded factors for each θ. Adding an independent Gaussian of variance equal to the bound to either tracer gives absolute-tail stochastic domination of the other (conditional Gaussian variance ordering); the Gaussian noise is superexponentially small at any fixed fraction of large displacement. A triangle-inequality tail comparison, then taking that fraction to zero, transfers the exact logarithmic tail. Thus the extra diffusivity ratio does not introduce a scientific remainder not already implied by the matching theorem. Indexed coverage is established; relative provenance and priority are not inferred from directory dates.

## value

FAIL

The fixed-memory exponent and exact moment boundary are useful for distinguishing a limiting Gaussian profile from ultimate tails. However, both facts are supplied by the indexed theorem, and the extra independent diffusion ratio is a bounded conditional-variance perturbation absorbed by matching D_c. The reviewed claim provides neither an additional invariant nor a new tail prefactor, regime or limit-order estimate. It lacks incremental value as a distinct finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
