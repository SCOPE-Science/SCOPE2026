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

At clean state, only an all-outlier batch changes the state, with p_t=beta^k_t; at outlier state only an all-clean batch changes, q_t=alpha^k_t. Fresh-batch independence yields exact conditional no-switch tail products. For P=sum p_t<infty,Q=sum q_t=infty, first Borel–Cantelli makes entries to outlier finite while every outlier state eventually escapes a.s.; thus eventual clean. P=infty implies Q=infty (alpha>beta), both absorbing-tail products zero and finite switches impossible, hence infinite switches a.s. Q<infty gives finite expected number of changes and positive-probability no-exit/first-entry paths for either eventual label. If k_t->infty and Q=infty, recursion u_t=(1-p_t-q_t)u_(t-1)+p_t and r_t=p_t/(p_t+q_t)->0 forces u_t->0. For logarithmic batch, z^ceil(c log(t+1)) comparable up to factor z with t^(-c log(1/z)), giving both exact endpoints (harmonic divergence). Constant k stationary p/(p+q) and eigenvalue 1-p-q are exact.

## originality

PASS

Best-of-knowledge novel exact result after checked primary source scope comparisons. The closest inspected primary results differ by parameter regime, sample law, or strictly weaker quantitative conclusion; inaccessible full texts and independent historical priority remain explicit risks.

## value

PASS

The screening batch size is a motivated knob of the actual minimum-loss robust SGD algorithm. The theorem makes a precise, counterintuitive design prediction: less screening gives infinitely many bad steps despite convergence in probability, intermediate logarithmic growth recovers a.s., and excessive growth can lock into corruption forever. It is a meaningful exact phase classification of a minimal natural stochastic model, not a purely unmotivated toy enumeration; no general SGD guarantee is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
