---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For the symmetric three-site generator, the simple real spectrum makes the abundance difference G a sum of at most three distinct real exponentials. G(0)=0 and G'(0)=Delta>0. Rolle induction bounds its real zeros counted with multiplicity by two, leaving at most one positive zero, necessarily simple. With s=1+Delta/m the critical matrix has positive eigenvector (1,1,s) with eigenvalue r1, hence this is the Perron root. The first row gives v11-v12=(r1-lambda1)v11/m, and lambda1 increases strictly in r3 by the positive square of the third coordinate of the normalized Perron vector. This gives the asserted eventual signs off threshold and uniquely decides the crossing because of the zero bound. At equality the leading coefficient vanishes and G=H(exp(lambda2* t)-exp(lambda3* t))>0. The two-site version with positive initial derivative is a positive multiple of a difference of two exponentials and never crosses. With a unit Perron vector, the derivative of the leading coefficient at threshold is -[s^2/(2+s^2)](2+s)/[m(2+s^2)]=-K. At any fixed positive horizon G stays positive as epsilon tends to zero, so the crossing tends to infinity; division by its second exponential gives |a1| exp((lambda1-lambda2)t*)=H+o(1). In particular t*=O(log(1/epsilon)), making the error from replacing its gap by the critical gap o(1), including in the additive remainder. Inspected RESULT.md lines 23–69 and CHECK.py: the latter's exact Taylor sign bracket is subsidiary, not the general proof. No uploaded script was executed.

## originality

PASS

The matrix-exponential observable and its short-/long-parameter limiting rankings are established. The checked record instead gives a parameter-explicit iff for a unique finite-time crossing (including the zero leading-coefficient boundary), the two-site exclusion, and a critical-time expansion with the log constant. The closest catalogue reversal concerns survival as migration varies, not total abundance as the observation time varies. No inspected result gives or dominates the conjunction being credited.

## value

PASS

The comparison isolates how choice of measurement horizon changes a natural release-site decision in the smallest corridor admitting a reversal. The sharp threshold, single-crossing guarantee, and quantitative divergence distinguish a genuine but practically late reversal from no reversal. This is more informative than endpoint signs and useful as an exact test case for linear growth–dispersal models. It is not a claim about survival probability, nonlinear recovery, or an uncertain-parameter field policy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
