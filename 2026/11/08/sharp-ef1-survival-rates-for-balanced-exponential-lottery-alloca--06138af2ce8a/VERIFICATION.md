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

The exact claim is for fixed positive integer \(r\ge2\) and all \(n\ge2\), with iid rate-one exponential agent-item values and a deterministic balanced allocation. The proof uses four necessary steps: agent-wise independence, exponential order-statistic spacings, the distinct-rate hypoexponential tail coefficient, and dominated convergence after a logarithmic substitution. These are given explicitly in `RESULT.md`. The final probability \(P_{n,r}\) is the \(n\)th power of the one-agent event, not merely that event.

Execute `python3 check.py` after extracting this record. The actual checks performed: exact rational values for each \(2\le r\le4\), \(2\le n\le6\) (15 cases), compared with independent numerical quadrature; the independent beta/harmonic identity for each \(2\le n\le6\) when \(r=2\); anchor rational values; and seeded Monte Carlo tests of whole-allocation EF1 events for four small parameter pairs. All checks passed. The seeded simulations are non-certifying sanity checks, and finite tests are not used to infer the limit.

The proof assumes a fixed \(r\) in the asymptotic, not a growing bundle size. No code, appendix, or outside artifact is needed to supply a missing proof lemma. The standalone program uses only Python 3 standard-library modules and does not depend on any unpublished data. All displayed source dates refer to first public versions of the motivating scientific works.
