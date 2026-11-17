---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For even k=2m, the exact period gcd G=gcd(F_{k+1}-1,F_{k+2}-1)=U_m follows from standard addition identities; the cubic Cassini congruence and local valuations give D=gcd(F_{k+1}^3−1,F_{k+2}^3−1)=3^{[4|m]}G. The all-shift cube differences share gcd D; the telescoping initial sum S_0 gives gcd(D,S_0)=D/2 exactly when 3|m, otherwise D. This gives the stated infinite-window formula, including C_3(6)=2, C_3(8)=9. Independently computed exact 14-window gcds for 120 even lengths; these only corroborate the proof. Read two earlier full independent mathematical proofs, one for every even Fibonacci AND Lucas cubic window and the other for every positive Fibonacci cubic window.

## originality

FAIL

The exact stated even-length Fibonacci-cube shifted-window GCD formula appeared in two full published November 2 results. One also treats Lucas cubes for every even length; another treats standard Fibonacci cubes for every positive length, with the same factor 3 at 8|k and loss of 2 at 6|k. Explicit substitution k=2m and matching starting-index convention prove that the submitted theorem is a covered special case.

## value

FAIL

The higher-power Fibonacci window GCD is motivated by an explicit prior open question, and the formula is mathematically meaningful, but both Nov 2 primary results already solve this very even-window formula (one also Lucas, one all k). This later duplicate does not supply a novel invariant, family extension, bound or mathematical insight qualifying independently as research value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
