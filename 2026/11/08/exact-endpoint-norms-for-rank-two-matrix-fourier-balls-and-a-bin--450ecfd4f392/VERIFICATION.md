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

Subspace-incidence Möbius identity decomposes the indicator of rank<=2 matrices as Σ_{dim U=2}1_{im A⊂U}-q[m-2 choose1]_q Σ_{dim U=1}1_{im A⊂U}+q^3[m-1 choose2]_q 1_{A=0}. Fourier character annihilators count U≤ker X^T and give integer F_k=q^(2n)[k choose2]_q-q^(n+1)[m-2 choose1]_q[k choose1]_q+q^3[m-1 choose2]_q, k=m-rank(X). F_0>0, F_1<0; for k>=3 the first two summands are strictly positive by q^(n-1)[k-1]_q/((q+1)[m-2]_q)>1, while F_2>0 except q=2,n=m, where z=2^(m-2) gives F_2=(8/3)(-z²+6z+1), negative iff m>=5. Thus strict nonzero signs are exhaustive. Counting rank-s matrices N_{m,n}(s) and Σ_X F=q^(mn) yields the exact L1 and L-infinity convolution norms through negative mass, including all prime powers. Independent tests passed 189 (q,m,n) parameter tuples covering 1512 rank sectors, every required orbit/zero-mass sum, and all 512 Walsh Fourier coefficients on the entire binary 3x3 matrix space; binary 5x5 sign transition follows by the exact inequality, not brute-force inference.

## originality

PASS

Delsarte 1978 Appendix Theorem A2 determines the generalized q-Krawtchouk rank-scheme Fourier eigenmatrix, an explicit prior input. The published 2026-11-08 rank-exactly-two convolution singular-value theorem computes the least absolute eigenvalue and a binary-square least-stable sector for the rank TWO shell, not the rank-at-most-two ball projector or its L1 endpoint absolute Fourier-mass sum. Neither provides the complete sign classification of the rank<=2 transform and exact dual-rank negative-mass weighting as a stated conclusion. Full primary Delsarte pages 1-16 and exact-rank theorem were materially read; best-of-knowledge originality is therefore qualified, not absolute.

## value

PASS

Exact Fourier-projection endpoint stability of the natural radius-two rank-metric ball is a motivated finite-field harmonic-analysis invariant, and the additional binary-square negative rank shell at size five is a precise structural phase transition. The strict sign classification and orbit-weighted endpoint norm have meaningful conditioning/aggregation consequences, even though the q-Krawtchouk eigenmatrix itself is classical.

The dated certificate retains the supplied scientific assessment, sources and limitations.
