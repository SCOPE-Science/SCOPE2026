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

The cycle mean is a+b/v; the radial return reward density is S/v, where S(z)=P(W>z). For the diffusion reward, applying the heat equation to (x-z)_+, doubling by symmetry and stopping at the independent alarm gives H/D with H(z)=E[(W-z)_+]. Integrating H and S yields Da and b, so the density is normalized. Its tail has the displayed A and C because integrating H again gives E[(W-z)_+^2]/2. The Gamma transform factors the Brownian endpoint into a signed difference of two iid Gamma(k,sqrt(r/D)) variables. When k>1 their convolution and positive-ray survival are log-concave by log-concave marginalization. The integral in RESULT.md gives analyticity for z>0 (dominated locally even on the complex right half-plane), and factoring z^(k-1) out of that integral gives its nonconstant polynomial prefactor at infinity by dominated convergence. Thus log S has no affine interval, making each positive-lag ratio S(z+t)/S(z) strictly decreasing. At 0<k<1 the inverse-power Laplace integral gives the density, and after integration also the survival, as positive exponential mixtures with nondegenerate rates; strict log-convexity reverses all those ratio inequalities. Integrating gives strict monotonicity of H/S. The normalized v-mixture ratio at v2>v1 increases strictly as a function of H/S, hence it is strictly ordered in z in the stated directions. Positive densities and equal total mass force the unique crossing, so every positive threshold has a strict tail difference. At k=1 H=S/sqrt(r/D) and both phase laws are the same exponential. At other shapes the strictly monotone fractional-linear tail has unequal endpoints C/b and A/a; the displayed inverse is valid only on the open probability interval and assumes D,r,k known. The written proof is decisive. Independently replay `python3 /workspace/review_checks.py 1` (SciPy): nine direct physical-time reward cases at D=1.7,r=0.8, including k=0.35, test the two phase rewards, an exponential anchor, two-speed signs and inverse recovery. This bounded quadrature is not a certificate of monotonicity outside the sample. The frozen checker was inspected but not executed.

## originality

PASS

The same Gamma/constant-speed model, stationary density framework and exponential-clock invariance are not credited as new. The supported distinction is the strict likelihood-ratio (and thus every-threshold) comparative statics as speed varies across both nonexponential shape ranges. Single-threshold injectivity follows from this strictness; the inversion algebra alone is routine. Closest full-text access limitations keep this a qualified best-of-knowledge judgment.

## value

PASS

The stronger all-radius law answers whether changing a physical speed parameter makes the stationary displacement smaller or larger, not just at asymptotic or chosen thresholds. The reversal and loss of identifiability at the exponential clock mark a sharp model boundary. An exact positive-threshold observation calibrates the speed on either side given the other parameters, without claiming finite-sample inference.

The dated certificate retains the supplied scientific assessment, sources and limitations.
