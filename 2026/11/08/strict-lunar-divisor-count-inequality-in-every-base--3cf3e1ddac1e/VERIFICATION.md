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

Proof independently checked by digitwise multiplication: any lunar factorization has product length len(u)+len(v)-1, so every lunar divisor has length at most len(n). All divisors are distinct positive integers at most sigma, giving d<=sigma. For n=1 the one-digit divisors are exactly 1..b-1 and equality holds; for 2<=n<=b-1 the divisor list n..b-1 is shorter than sigma=b-1. For n>=b, both n and the lunar unit b-1 divide n, so sigma has units digit b-1 and dominates the higher digits of n. If n has units digit r>0, w=n-r has zero units; if r=0, w=n+1 has unit 1. In either case w is positive, same length, <=sigma but cannot divide n since its partner would be one digit and its product units digit would be 0 or 1 instead of r. Thus w is a missing integer and d<=sigma-1 for n>1. This proves all bases without extrapolating 1019 finite tests.

## originality

PASS

Directly answers the explicit strict lunar divisor inequality conjectured in Applegate–LeBrun–Sloane (2011) for decimal arithmetic, with a valid extension to all bases. Gross 2020 studies maximally numerous lunar divisors, not d versus sigma. No stronger already-proved statement was identified by Resultary or inspected primary paper; a later uncatalogued solution remains a historical risk.

## value

PASS

Settles a concrete longstanding natural arithmetic conjecture and strengthens it uniformly across bases with an elegant universal missing-integer witness. Its elementary proof does not detract from value; it resolves a stated open comparison rather than merely reprinting an integer table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
