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

For a three-run word 0^a1^b0^c, direct string counting gives S=n+b min(a,c). For four runs 0^a1^b0^c1^d, the only nonconstant palindromic subsequences have three runs and S=n+b min(a,c)+c min(b,d). Four exhaustive parameter-order cases yield 2[b min(a,c)+c min(b,d)]≤(a+c)(b+d)≤n²/4, and integer witnesses (1,t,n−2t−1,t) with t maximizing t(n−2t) attain floor(n²/8) for every n≥4; n≥3 for three runs. Independent short-word exhaustive enumerations corroborate, not replace, the proof. The removed odd-run asymptotic is also mathematically correct but already published in greater generality.

## originality

PASS

Only the sharp, unexpectedly equal all-length three-/four-run maxima remain original and independently useful as a boundary between neighboring combinatorial complexity classes.

## value

PASS

The repaired exact equality M3(n)=M4(n)=n+floor(n²/8) for every admissible n provides a sharp non-obvious structural plateau in the natural number-of-runs hierarchy of distinct palindromic subsequences. The earlier general asymptotic is not counted as this contribution. Not a random small numeric slice: it resolves all lengths across the first genuinely alternating even-run case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
