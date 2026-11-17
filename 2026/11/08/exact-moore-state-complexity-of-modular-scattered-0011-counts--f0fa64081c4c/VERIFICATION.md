---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

Parsed actual frozen RESULT.md and checker.py. Prefix statistics (a,b,c,d) for 0,00,001,0011 obey T0=(a+1,b+a,c,d), T1=(a,b,c+b,d+c) modulo m. After t zeros (a,b)=(t,C(t,2)), giving m first-two pairs for odd m and 2m for even m. The words U=1 and W=1^(m-1)0010^(2m-2) independently generate all (c,d) on the zero-phase fiber, and 0^t reaches each phase; suffixes epsilon,1,11,011 recover d,c,b,a exactly. The argument proves upper, reachability and lower bounds for all m>=2, not by finite extrapolation. An independent BFS over complete transitions verified m^3*gcd(m,2) reachable and four-suffix distinguishable states for all 2<=m<=19.

## originality

PASS

Prior Parikh-matrix studies provide the general subsequence-counting framework and investigate universality/probability, but do not in inspected material give this exact Moore-output complexity. Earlier Resultary modular 010 and modular 0^d1 state counts have structurally different counter chains and cannot directly entail the 0011 count. Best-of-knowledge PASS qualified by missing complete primary manuscripts and possible broader unseen binomial-complexity formulations.

## value

PASS

The first balanced two-run binary scattered pattern is a natural automata test beyond unary/alternating cases. Exact minimal memory for arbitrary composite modulus and the even/odd doubling provide a useful sharp classification; explicit witnesses and four-suffix Nerode certificate have mathematical content beyond merely simulating finite machines.

The dated certificate retains the supplied scientific assessment, sources and limitations.
