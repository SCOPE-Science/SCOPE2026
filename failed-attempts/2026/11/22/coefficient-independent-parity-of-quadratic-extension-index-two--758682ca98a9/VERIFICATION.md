---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The claim is conditional on bijectivity, with a nonzero coefficient and odd prime-power q. On the fibers of x↦x^D, D=d(q−1), injectivity forces gcd(r,2(q−1))=1. On the induced permutation of μ_{(q+1)/2}, multiplying the images gives B^D=1 for B=a^{(q+1)/2}−(−1)^{(q+1)/2}≠0. Both B and w=a^{(q+1)/2} belong to μ_{2(q−1)}. If w^q=−w, then B^q=−w−(−1)^{(q+1)/2} equals neither B nor −B, a contradiction in odd characteristic. Thus B lies in the base field. The q+1 cosets of F_q^× have even size, and the common power map occurs an even number of times; only the internal translations contribute signs. Their product in F_q^× is δ^{q(r−1)/2}B², where δ generates F_q^×; the quadratic character gives the stated sign. Zero is fixed. An independent replay using quadratic towers and inversion parity tested 16,064 parameters, with 1,142 even and 990 odd permutations; the per-field totals were 16, 288, 288, 480 and 1,060 for q=3,5,7,11,9, respectively.

## originality

FAIL

Distinct indexed records state exactly this parity law on the entire nonzero admissible domain. The third same-day result 008dae091151 covers zero as well and also states a coefficient-square restriction. This is verified equivalent/broader coverage, not an inference about which same-day result came first.

## value

FAIL

The alternating character is a useful exact invariant beyond a permutation-existence criterion, but this frozen scope duplicates an indexed theorem and adds no uncovered structural case, parameter regime, or new use. Repeating the same finite checks or excluding zero does not leave a scientifically valuable remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
