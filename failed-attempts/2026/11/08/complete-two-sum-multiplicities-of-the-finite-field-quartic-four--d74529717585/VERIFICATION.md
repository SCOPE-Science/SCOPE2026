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

Set u=x-y; 8(x^4+y^4)=u^4+6s^2u^2+s^4, reduce to z=u^2 and square roots 1+chi(z). The s=0 slice has one singleton and (q-1)/g fibers of g; each s!=0 has one odd fiber of 2+chi(-6). Independent collision count 3q-3-chi(-1)-2chi(-3) plus total q solves the A,B positive-multiplicity counts; summing yields all moments and |C+C|. Independent exact enumeration for prime fields q=5,7,11,13,17,19,23,29,31,37 verified every fiber and frequency; the proof handles arbitrary prime powers char>3.

## originality

FAIL

Earlier November 2, 2026 even-quartic graph theorem covers all C_a=(x,x^4+a x^2) for every field and characteristic and gives complete A_j histograms. Specializing a=0, B_s=6s^2 and lambda=chi(-6)=eta, tau=chi(2), tau*eta=chi(-3)=delta yields H_2=(q+epsilon+2delta)/4 and H_4=(q-4-epsilon-2delta-2eta)/8 exactly. Z=1 and D_j give zero slice; other moments are immediate histogram sums.

## value

FAIL

FAIL: exact quartic multiplicities are natural, but the purported new profile and its higher moments are already implicit explicitly in a more general earlier complete spectrum. The submitted proof does not isolate a non-implied mathematical fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
