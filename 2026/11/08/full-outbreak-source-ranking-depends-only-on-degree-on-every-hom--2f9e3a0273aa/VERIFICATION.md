---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The theorem's decisive steps are: (1) on a tree all vertices are infected iff every parent sends at least one contact to each child before removal; (2) each parent's simultaneous child-transmission probability is \(m_j=\mathbb E[(1-e^{-\lambda T})^j]\), independently across parents; (3) rooting changes the outgoing-child count from \(d_v-1\) to \(d_v\) at exactly the source; (4) Cauchy–Schwarz gives strict monotonicity of moment ratios for positive nonconstant infectiousness; (5) beta-integral evaluation yields the exponential-recovery specialization.

`CHECKER.py` is self-contained and can be run with `python CHECKER.py`. It reconstructs finite-state continuous-time SIR absorption probabilities exactly with rational transition rates, then performs independent latent-infectiousness and directed-transmission enumeration. It makes 120 exact comparisons, including all sources on six tree structures. Two nonisomorphic six-vertex examples share degree multiset \((3,2,2,1,1,1)\) and have the same exact full-outbreak probabilities per source degree when \(\lambda=\mu=1\): degree one \(1/24\), degree two \(1/18\), and degree three \(1/16\).

Finite testing cannot certify every finite tree or every infectious-period distribution; the complete quantification follows from the analytic proof. Independent scientific audit has not been performed. The model excludes cyclic contact routes, heterogeneous contact rates, and reinfection.
