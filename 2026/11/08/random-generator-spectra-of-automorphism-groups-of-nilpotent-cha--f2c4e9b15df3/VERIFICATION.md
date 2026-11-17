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

For n>=2 and prime power q=p^f, multiplication enforces T(e1)=a e1+b en, a!=0, and T(e_i)=a^(2^(i-1)) e_i. With x=b/a this is F_q^+ semidirect F_q^* via scalar a^(2^(n-1)-1). The kernel has order d=gcd(2^(n-1)-1,q-1), image H order h. For h>1, F_p[H]=F_{p^e}, e=ord_h(p), hence additive module rank r=f/e. Nielsen reduction of generating cyclic quotient tuples leaves s-1 independent uniform translations, and a faithful H-generator has no fixed nonzero scalar, giving Phi_s(q-1) product_(i=0)^(r-1)(1-p^{e(i-s+1)}). For h=1 the direct product gives Phi_s(q-1) product_(i=0)^(f-1)(1-p^{i-s}); zero factors, empty products and s=1 handled. Commutator equation (a^L-1)y=(c^L-1)x gives k=q-1+d² classes. Characteristic-two gcd(2^f-1,2^(n-1)-1) and proper-subfield bound give f vs 2 generator jump, including q=2. Independent full group closure for prime q=2,3,5,7 and n=3,4 verified 2-generator counts and commuting classes; finite tests supplement the all-parameter proof.

## originality

PASS

The earlier general chain-endomorphism theorem already implies the triangular automorphism normal form, and finite-group semidirect-module rank arguments are standard. The assessed residual is the simultaneous exact indexed all-s random-generator probability, finite-extension-degree resonance in this algebra family, and q-1+d² commuting-class count. Neither the inspected original characteristic-zero automorphism theorem nor the complete prior all-field endomorphism theorem gives those statistics. Possible general scalar-affine-group generation laws remain a real priority risk.

## value

PASS

These exact group-generation probabilities and sharp characteristic-dependent generator ranks are natural, reusable invariants of a standard family of nilpotent nonassociative algebras; resonance distinguishes extension degrees from dimensions. This is a motivated complete calculation across all q,n,s, not only an automorphism-normal-form restatement or small-table computation. No general-group novelty or downstream theorem is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
