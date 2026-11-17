---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For the cited Grange symmetric piecewise-motility continuum model, stationary flux F=R/v0=h Pr(|X|>x) on each half-line with h=M chi/2 and chi=sqrt(r(r+alpha))/v0; common profiles coexist for m>4 and 1<h<m/4. Gas density is u_m(F)=m(1-sqrt(1-4F/m))/2; droplet density mF for F>1. Since dx/dF=-1/(chi rho(F)), inverse-tail-quantile difference is chi^-1∫_{max(1,hq)}^h[1/u_m(F)-1/(mF)]dF, strictly positive and CONSTANT for q<=1/h. The quantile monotone coupling therefore gives exact W∞=Delta and W1= [B(u_h)-B(u_*)-(h-1)/m]/(h chi), B(u)=u-3u²/(2m)+2u³/(3m²). Concavity f_m''<0 shows unique interior contrast maximum iff endpoint h f'-f<0; its boundary function G(s) strictly decreases from 1/4 to -infinity and yields unique m*=7.322227068..., with h*(m)→e and max gap→M/(2e). Independently computed m*=7.322227068378924 and m=8,h=1.5,M=2 transport pair W1=.1510528565, W∞=.1846733847; all-parameter conclusions rest on analytic inequality not numerical sampling.

## originality

PASS

PASS QUALIFIED: Grange already derives both branch steady profiles, coexistence interval and droplet radius/nonmonotone half-width, so those inputs are prior. The exact stochastic order between the entire coexisting radial laws, sharp W∞/W1, constant far-tail shift and new contrast optimizer m*=7.322... are different model-specific statements not established by a stationary profile alone or by classical one-dimensional transport theory. Priority remains qualified by direct availability of source inverse profiles.

## value

PASS

Both coexisting radial laws are physically natural at identical parameters, and their sharp Wasserstein separation captures complete-spatial-profile disagreement. Uniform stochastic ordering has consequences for every increasing radial observable, and a model-specific crowding transition distinguishes interior from boundary maximal phase contrast. The exact constant extreme-tail shift is a motivated structural invariant and not just another raw profile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
