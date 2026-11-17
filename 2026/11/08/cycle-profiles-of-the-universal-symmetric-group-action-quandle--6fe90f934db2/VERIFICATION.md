---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For n>=1 and every positive power k, direct induction gives R_h^k(x,g)=(x^{g^{-k}h^k},h^{-k}gh^k). A fixed point requires g to centralize q=h^k and g^k(x)=q(x). In C_{S_n}(q)=product_d(C_d wr S_{m_d}), the containing block has orbit length uniformly distributed in 1..m_d; the net d-rotation is uniform, hence the fixed-point probability is 1/d exactly when ell|k and gcd(d,k/ell)=1. This proves F_h(k)=z(q)B_k(q). Mobius inversion reconstructs all cycles. For n>=3 the trivial center forces h^k=1 if R_h^k=1; letting g range over all S_n forces lcm(1,..,n)|k. The small n=1,2 formulas are individually valid. Direct, independently written permutation enumeration rechecked every h and k=1..12 for n=1..4 and the actual translation cycle profiles.

## originality

PASS

The full k-th right-translation fixed-point formula and induced all-cycle profile for arbitrary h,n,k are not established by the inspected Kai/Nelson sources or by the earlier ordinary quandle-polynomial result. However, the special k=1 fixed-point formula and partition fixed-pair probability are exactly known from the October 26 universal-Cayley-quandle theorem, and are NOT novel here. The surviving k>1 wreath-cycle coprimality and common exact order are distinct.

## value

PASS

The complete power-fixed-point data determines every right-translation cycle multiplicity for a natural universal quandle, a useful general invariant beyond first-iterate quandle-polynomial counts; the n>=3 uniform order bound is an exact structural consequence. The already published fixing-pair probability supplies no independent value by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
