---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The integer identity 2(P_s(x)-P_s(y))=(x-y)((s-2)(x+y)-(s-4)) is valid for all x,y. If s=2 mod4 the difference has an odd multiplier and is injective mod 2^k. If s=0 mod4, completing a square with odd coefficient gives the standard square-root multiplicities; the zero/odd valuation and k=1,2 edge cases have been checked. For odd s, same-parity collision impossible, while opposite parity collision forces x+y=2m+1-2r, where r=(s-2)^(-1) mod m; disjoint pairs count d=min(r-1,m+1-r), yielding d holes/d doubles. Independent enumeration tested s=3..80,k=1..8, corroborating the proof, not exhausting parameters.

## originality

PASS

Classical quadratic-congruence solvers cover each individual target, and Ulness already proves the s=3 triangular case. The assigned uniform s-dependent law on precisely n=0..2^k-1, particularly odd s where P_s has a potentially longer natural period, requires half-period cross-parity pairing/counting not supplied by the inspected individual-root solver. The new contribution is the closed histogram and extreme criteria, not square-root arithmetic alone.

## value

PASS

Residue multiplicity and permutation behavior of polygonal number maps are natural finite-ring arithmetic properties; the global all-order dyadic spectrum, in particular the odd half-period reflection-pair law, gives an unknown exact classification not just a single worked polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
