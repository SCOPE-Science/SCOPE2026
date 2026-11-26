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

The resolvent of the actual two-compartment loss matrix gives (qs+h)/(s(s+r_-)(s+r_+)), with strictly separated positive relaxation rates by positive trace, determinant and uv. Thus D_j=qF_j+hF_(j+1), where F_j=I^j B and B=(e^(−r_- t)−e^(−r_+ t))/(r_+−r_-). B is strictly log-concave. For each of these positive smooth f with f(0)=0, G=If has G²(log G)''=f'(t)G−f(t)²=f(t)∫_0^t f(s)[(log f)'(t)−(log f)'(s)]ds<0. Consequently F_j/F_(j+1) strictly decreases from infinity to zero: at zero use B∼t; at infinity apply the integral kernels to the integrable positive B by dominated convergence. Positivity gives no crossing if qh≥0, including either one-zero case, and D_j≡0 if q=h=0; otherwise the ratio gives a simple sign crossing from q to h. The phrase 'opposite steady-state loss-weighted source difference' in the introductory prose should be read via the explicit qh<0 and h=bS1−aS2, not as inserting a second minus sign. Integrating before the first zero forces the next zero to be later, and F_(j+1)≤(t/j)F_j implies t_j≥j|q/h|. For u=v=k in the crossing regime, a≠b and both r_-(k) and the rate gap increase. For 0<s<t the quotient B_k(s)/B_k(t) increases strictly, so the inverse kernel-integral ratio falls strictly with k, as does its crossing time. Its fixed-t limit is r/(e^(rt)−1), r=(a+b)/2, by dominated convergence of the kernel quotient; bracketing its strictly decreasing root gives the exact positive limit. Independently evaluated the example exponential zeros, 0.48562329495372988614 and 0.92165190130663244676, and the stated limiting time 0.32437208648653150558. The frozen checker was inspected, not executed; its reported finite checks do not certify all j or arbitrary mixing.

## originality

PASS

On inspected evidence the distinct claim is the comparison of early and equilibrium zonal order for two constant simultaneous sources, with exact all-integral horizons and strict symmetric-mixing dependence and limit for the instantaneous zero. The multizone step-response framework, spectral modes and log-concavity/convolution tools are prior knowledge; no general novelty for those tools or for a single zero of a two-mode transient is asserted.

## value

PASS

The problem distinguishes fast sensor ordering, cumulative exposure ordering, and equilibrium ordering in a motivated compartment model. The exact criterion separates the existence of a reversal from its time, shows why repeated integration postpones the reversal without bound, and establishes a nonzero lower time even for arbitrarily strong symmetric exchange. These give a model benchmark and a limitation on naive extrapolation from early sensor readings, not an empirical building-design prescription or a claim for nonzero initial data or asymmetric mixing changes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
