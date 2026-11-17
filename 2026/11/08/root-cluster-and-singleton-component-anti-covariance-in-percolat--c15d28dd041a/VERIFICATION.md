---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

In the sequential uniformly random parent and independent retention model, delta C=A 1{parent in root component}, delta I=1-A-A 1{parent isolated}. Their conditional product is -p J_t/t where J_t is the event that the root is isolated; the C_t I_t terms cancel exactly. The resulting m_{t+1}=m_t+(1-p)a_t-p u_t/t and product recurrences yield the stated closed mixed moment and covariance for every n>=2 and p in [0,1]. The elementary inequalities prove strict negativity for 0<p<1. Gamma ratios and reflection give the n^p main term, constant correction and both p->1 windows. Root C variance from (1+2p/t), and singleton variance recursion, give the stated positive correlation-limit coefficient. Independently reconstructed the rational first-step recurrences at p=2/5 for n=2..12. Finite checking is supporting evidence only; infinite claims follow from the recurrences and asymptotic estimates.

## originality

PASS

The exact mixed moment for bond-percolated root-component size versus the total count of retained-isolated vertices is not stated by the inspected prior Resultary root-degree, leaf and site-percolation theorems. Primary Kürsten and Baur abstracts confirm the separate cluster and first-generation quantities but do not resolve whether their full text contains an implicit equivalent formula. At best of current knowledge, the cross-generation singleton mixed moment and two distinct p-upscaling windows survive. Access restriction is recorded, not used as a failed novelty proof.

## value

PASS

The sign and exact strength of dependence between the ancestral cluster and all isolated components is a natural joint statistic not determined by the separately published marginals. The exact all-n covariance, critical correlation decay, and finite versus n/log n high-retention limits quantify a genuine percolation dependence structure, beyond a routine normalization or small-n calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
