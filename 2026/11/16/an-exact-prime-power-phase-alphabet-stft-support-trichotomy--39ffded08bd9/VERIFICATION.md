---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For p prime, q=ell^r with ell != p, the p-term zero-frequency row sum of qth roots cannot vanish by the prime-power cyclotomic coefficient obstruction: a sum of p nonnegative integer multiplicities cannot have size divisible by ell. For k != 0, Q(zeta_q) and Q(zeta_p) are linearly disjoint; the only length-p kernel of evaluation at zeta_p^k is the scalar all-ones vector, so vanishing implies that translated pointwise product row is constant. Two constant rows of distinct translations force both f and g constant up to global phase. Thus either every row is constant (support p), exactly one row is constant (p²-p+1), or none (p²). The p choices of the unique constant row yield p(q^{p-1}-1) phase-normalized pairs; all remaining q^{2p-2} pairs fill support p². Critical algebra is all-parameter; five bounded direct-DFT enumerations (p,q)=(2,3),(3,2),(3,4),(5,2),(5,4) only corroborate it.

## originality

PASS

No identified prior text implies the all-prime, coprime-prime-power three-stratum classification together with exact zero-row geometry and normalized pair counts; standard cyclotomic and minimal-support theorems are credited, with residual priority risk.

## value

PASS

A natural exact support/inverse rigidity problem for finite-alphabet phase windows, relevant to ambiguity-function zeros and constant-modulus coding. The sharp forbidden support gap, full exceptional shift geometry, and closed multiplicities for all coprime prime-power alphabets add information beyond universal p-support inequalities. Finite tests are not the contribution; the symbolic family and classification are.

The dated certificate retains the supplied scientific assessment, sources and limitations.
