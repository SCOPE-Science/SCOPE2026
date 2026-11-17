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

Kummer establishes that a central binomial coefficient is divisible by 3 iff its half-index contains ternary digit 2; Lucas gives (-1)^k otherwise. Parity fixes nonzero residue for even b. Choosing L with 3^L=1 mod b, K_m=sum_{j=1}^m3^{Lj} covers nonzero signs while adding a single separated digit two gives zero, and high-digit shifts preserve congruence and yield infinitely many n. Independent direct binomial/Lucas checks for k<100 and modular witnesses support finite cases but not the all-b proof.

## originality

PASS

Guo–Krattenthaler Conjecture 7.1 genuinely asserts all r in F_p for a>b with gcd(a,p)=1, hence a=2b, p=3 is an eligible subfamily. Vsemirnov 2014 disproved it at p=5, but the searched prior results do not present the complete p=3 central-line progression spectrum; parity is elementary but digit construction proves precise infinite attainment.

## value

PASS

Motivated by an explicit historically published residue-attainment conjecture; produces an infinite p=3 counterexample family and a complete positive/negative spectrum for every admissible progression, beyond merely exhibiting one exceptional coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
