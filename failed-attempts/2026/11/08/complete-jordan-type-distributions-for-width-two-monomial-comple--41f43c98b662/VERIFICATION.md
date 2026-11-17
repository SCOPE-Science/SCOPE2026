---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

As R=k[y]/y^m module, multiplication by f=a+xb is [[a,0],[b,a]]. The exact t-th power is [[a^t,0],[t a^{t-1}b,a^t]]. Smith exponents over k[[y]] are d=min(tu,(t-1)u+v if p∤t) and 2tu-d, hence rank sum of max(m-exponent,0). The finite second difference gives Jordan-block multiplicities and independent y-valuation weights enumerate each finite-field multiplier; q^{2m-1} total nilpotent elements. Direct matrix multiplication and modular rank elimination passed 52,045 bounded assertions, p=2,3,5 and m=2,3,4; characteristic-zero formal Smith proof is clear.

## originality

FAIL

Resultary 2026-11-02 full published RESULT.md proves precisely the same complete Jordan distribution on k[x,y]/(x²,y^n) for every positive characteristic and includes arbitrary scalar eigenvalue. Set lambda=0 to recover all submitted finite-field nilpotent histogram; its valuation rank formula and block second differences are algebraically identical, including all nonlinear multipliers and modular cases. The new characteristic-zero extension follows routinely by letting no t vanish; no independent finite-field distribution remains.

## value

FAIL

The same complete field-positive nilpotent Jordan census was already established in the identical algebra; the characteristic-zero specialization adds only the standard no-modular-vanishing choice in the same Smith normal form proof. Neither a reformatted enumerator nor a routine all-characteristic packaging supplies a separately valuable new exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
