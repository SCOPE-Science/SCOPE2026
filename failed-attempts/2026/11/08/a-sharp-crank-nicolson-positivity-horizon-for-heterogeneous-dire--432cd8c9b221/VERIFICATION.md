---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For positive rates on an n>=3 one-way cycle, s=h/2, the resolvent R=(I-sQ)^-1 has R_ii=1/[(1+sr_i)(1-Pi(s))], Pi=prod_j sr_j/(1+sr_j), and positive offdiagonals. C=2R-I. The minimum diagonal is at maximum-rate M. Multiplying 2R_pp-1 by the positive common denominator gives H_p(s)=sum_k(a_k-Ma_{k-1})s^k, whose coefficients change sign once by Newton-log-concavity of elementary-symmetric ratios and whose final nonzero term is negative. Descartes and endpoint signs force exactly one simple positive crossing, so positivity holds precisely h<=2s*. Raising any other rate raises return probability and the threshold; the homogeneous equal-M vector attains the sharp upper envelope, and one rate tending zero approaches lower infimum 2/M. Independently expanded the prior published threshold F(s) and submitted H(s) for (1,2,4,7), obtaining identical -90s³-35s²+1; this is direct scientific coverage evidence.

## originality

FAIL

A complete earlier published Resultary result dated November 2, A fastest-exit positivity frontier for Crank–Nicolson on directed cycles, treats the identical one-way heterogeneous-rate Markov generator and proves the exact full-matrix positivity interval, strictly positive offdiagonals, max-departure-rate bottleneck, a unique positive root and independence of ordering. Its polynomial F(s)=(1-Ms)product_{j ne p}(1+sr_j)+s^n product_j r_j is algebraically exactly the submitted H_p(s), after cancellation of the degree-n terms; its general monotone-return proof is stronger. The uniform threshold equation and n=3 golden-ratio boundary are also expressly covered. The submitted rate envelope is a short monotonicity corollary of that same explicit resolvent, not a new main classification. Hence title wording differs but the principal claim is not original.

## value

FAIL

The exact nonreversible directed-cycle positivity boundary is a motivated meaningful theorem, but was already established in the prior publication with the same hypotheses and stronger return monotonicity. The extra upper and lower bounds follow by substituting maximal rates or sending one rate to zero in the already known explicit expression, a routine parameter extremization rather than an independent new structural invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
