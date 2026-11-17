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

For the odd prime-power inverse hyperbola, fixing the first unit and writing the other inputs as t,r,1+t-r reduces the two equalities exactly to (1+t)(r-1)(r-t)=0 mod p^k with all four inputs units. The t classes t ≠ ±1, t=-1, t=1 mod p yield valuation sums B=3p^{k-1}(k(p-1)-1); multiplying by φ(p^k) gives E=3φ(p^k)^2(k-1/(p-1)), with CRT for odd composites and character orthogonality for fourth Kloosterman moment. Direct independent energy tests at odd moduli including 3,5,9,25,49,81,125 and odd composites support the unrestricted proof.

## originality

FAIL

FAIL — decisive prior coverage. The published same-date stronger theorem Complete pair-sum spectrum and fourth Kloosterman moments of odd modular hyperbolas (Resultary 2026/11/8, ac77d61c23da) gives the entire ordered r_q(s,t) histogram for the identical inverse hyperbola for odd prime powers and CRT composites, and explicitly derives E=φ(p^k)^2(3k-3/(p-1)). This is identically the submitted 3φ²(k-1/(p-1)) and includes the identical two-frequency Fourier fourth moment. Full mathematical source text was inspected; the submitted energy is a strict corollary of its stronger classification.

## value

FAIL

FAIL because the submitted entire claimed invariant and its Fourier/CRT equivalents are already a proved consequence of the earlier full pair-sum histogram. A different normalized collision proof does not give a new exact mathematical fact, although the computation itself is natural and correct.

The dated certificate retains the supplied scientific assessment, sources and limitations.
