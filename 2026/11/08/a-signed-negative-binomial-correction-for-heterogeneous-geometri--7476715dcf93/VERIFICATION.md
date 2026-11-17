---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

In convolution Banach algebra ℓ1, G_y=(1−y)/(1−yz), A_y=∂_y log G_y and ∥A′_y∥1=2/(1−y)², ∥A″_y∥1=4/(1−y)³. Along y_j=w+t δ_j, Σδ_j=0 cancels the linear response, giving ∥P′_t∥1≤2t S2/a², hence TV≤S2/(2a²). Compare P′_t with t S2 P_0*A′_w, control differences by 2t³S2²/a⁴+2t²S3/a³ and integrate to obtain S3/(3a³)+S2²/(4a⁴). The convolution term is exactly shifted NB(c+2) minus NB(c), with zero mass. Its signed mass changes at k(k−1)=c(c+1)w²/(1−w)², yielding the tail difference and strictly positive local leading constant for nonzero v.

## originality

PASS

Best-of-knowledge originality of the exact final claim (not of elementary starting tools). Search included signed compound-Poisson approximations and negative-binomial Stein perturbations. General signed series can contain second-order terms, but no inspected prior establishes this particular fixed arithmetic-mean NB difference with these uniform nonasymptotic constants. The DeSalvo first-order bound is weaker and does not imply signed cubic residual; general signed approximation papers not read in full cannot be declared noncovering, so any possible implication is explicitly unresolved as a priority risk, not asserted absent.

## value

PASS

A recent named problem asks for a usable second-order signed approximation to heterogeneous geometric sums; the explicit NB-shift correction, uniform-in-number-of-summands constants and exact local TV coefficient are naturally reusable probability tools.

The dated certificate retains the supplied scientific assessment, sources and limitations.
