---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For each designated r-subset forming one whole functional component, every other image must remain in its complement; conditional on this event the complementary restriction is an independent uniform mapping. This proves E[K X_r]=E[X_r](1+mu_{n-r}); counting cycles proves mu_n. The rooted-forest/cycle decomposition yields c_r=(r-1)! sum_{q=0}^{r-1}r^q/q!, including r=n with 0^0=1. The function 1+mu_{n-r}-mu_n strictly decreases with r, has positive first and negative final term. The analytic Gaussian-product expansion mu_m=S_m+A/sqrt(m)+O(m^-1), A=sqrt(pi/2)/3, and the smooth Riemann-sum difference S_n-S_m=(1/2)log(n/m)+O(1/n), uniform for m/n in compact subsets (0,1), give the claimed cutoff shift. Independent enumeration of maps for n=2..5 and larger-n cutoff checks corroborated these identities; they do not prove the asymptotic.

## originality

PASS

PASS on best-knowledge priority: precise order-sqrt(n) location of the component-size/total-component-count covariance sign change was not found in inspected earlier mapping frequency-spectrum statements. Earlier machinery could encode mixed moments, but no inspected accessible theorem implies this explicit second-order sign boundary. Lack of older full text is a residual risk, not automatic failure.

## value

PASS

PASS: a natural covariance statistic of uniform random mappings has a rigorously unique sign cutoff at a macroscopic fraction 1-e^-2 and a positive order-sqrt(n) shift. The coefficient makes quantitatively different finite-size predictions and is not an arbitrary numerical slice or merely a known marginal distribution. Its value is the exact dependence transition, with residual historical priority risk acknowledged.

The dated certificate retains the supplied scientific assessment, sources and limitations.
