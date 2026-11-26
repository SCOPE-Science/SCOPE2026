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

Gaussian regression and integration of min(t,x)^2 give E[Q|W_x]=1/2+x(1-2x/3)(Z^2-1), and the Gaussian fourth-moment formula gives Var(Q)=1/3. Any independent-randomized binary kernel induces r(y)=P(B=1|Z^2=y); at fixed nontrivial bit mass and with the positive covariance convention, moving any mass below the upper-tail cutoff to above it strictly improves the objective unless the kernel already equals the tail indicator almost surely. Thus randomized encoding cannot improve the optimum. The time factor is positive for x>0 with unique maximum 3/8 at 3/4; x=0 transmits no information. For chi-square-one Y and cutoff c, differentiating centroid distortion gives the sign of 2c-mu_--mu_+. The lower-cell scaled centroid strictly decreases by the exponential tilt on (0,1). The upper-cell scaled survival ratio decreases strictly since z h(z) strictly increases for positive z (h is the normal hazard, with h'=h(h-z)>0 by Mills' inequality). Hence the sum of scaled means decreases from infinity to one, proving the unique interior global cutoff. Normal integration by parts gives the stated equation, conditional means and risk. A separate 60-digit solution gave a=1.48207243570106119220381297475, F=1.30448970814641475910340001849, risk=0.14988946812524375783441770573, and the two decoder values 1.5690062644358755 and 0.3283977640627816. The supplied script and stored output were inspected, not executed; sampled monotonicity in that evidence is not used as proof.

## originality

PASS

The full-value one-time location and Lloyd–Max stationarity are not credited as new. The supported distinct result is the sharp Brownian one-bit design: uniqueness over kernels, the explicit chi-square-one cutoff, and the exact loss for the path energy. The inspected sources do not determine that claim.

## value

PASS

For a natural Brownian path functional, the result specifies what one bit should measure and exactly what information it retains. A sign observation is useless, the best magnitude bit retains about 55% of prior variance, and a full snapshot retains about 84%. The globally unique magnitude design over arbitrary kernels, with a sharp quantitative benchmark, is more than a numerical Lloyd iteration or a rederivation of the full-value time.

The dated certificate retains the supplied scientific assessment, sources and limitations.
