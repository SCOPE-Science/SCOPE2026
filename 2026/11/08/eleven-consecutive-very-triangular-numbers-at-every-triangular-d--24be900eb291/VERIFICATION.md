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

Let T(n)=n(n+1)/2 and s₂ count binary 1s. Independently checked that all eleven T(36,853,059+j) (j=0..10) exactly match the submitted hexadecimal integers and each has Hamming weight 26. For every triangular H=t(t+1)/2 with t≥13, set L=(H−26)/2 and q=2^L−1 for even H, or L=(H−27)/2 and q=3(2^L−1) for odd H. Repunit complementary-block arithmetic proves s₂(A(2^L−1))=L for 1≤A<2^L and s₂([3(2^L−1)]²)=L+1. When K≥L+30, the exact expansion T(q2^K+r)=q²2^{2K−1}+q(2r+1)2^{K−1}+T(r) has three disjoint binary supports, hence weight 26+2L or 27+2L=H uniformly for all 11 r. Infinite strictly increasing K gives infinitely many blocks. Independently checked t=13..49, 11 positions each, at K=L+30 with arbitrary-precision integers; the algebra proves all t and K, not these tests.

## originality

PASS

Best-of-knowledge PASS. Baumheckel–Forgács 2021/2023 original work defines very triangular numbers and proves infinitely many isolated prescribed-triangular-weight examples and six consecutive terms, with a digit-weight preservation technique. The submitted result constructs eleven CONSECUTIVE indices at each specified triangular weight H≥91, a stronger joint fixed-weight/length assertion not mathematically forced by the earlier six-term result. Resultary searches and external query found no equivalent stronger eleven-term theorem. The exact new seed and parity-resolved repunit lift are additional mathematics, not title substitution.

## value

PASS

A constructive long fixed-digit-weight block phenomenon sharpens a published six-consecutive theorem in a natural binary-arithmetic sequence and fills a motivated gap between isolated examples and uniformly long runs. The precise simultaneous prescribed-H and eleven-index nature is a reusable exact combinatorial fact; no claim of maximal length or best H threshold is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
