---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Independent kernel derivation: put N=n+1 and extend a path vector oddly across 0 and N to the 2N-cycle. The two unit cyclic shifts U and U^{-1} preserve the odd subspace in their sum; their half-sum restricts to the half-adjacency. The Chebyshev recurrence on the cycle gives 2T_m=(U^m+U^{-m}), whose restriction counts the forward difference and the two odd reflections, yielding (1). At a<b only d=b−a and h=min(a+b,2N−a−b) can contribute, with opposite signs unless h=N (outside the window). At fixed m the d-count is n−m and the h-count is twice floor((m−1)/2); at distinct equal-parity j<k each of a+b=k and a+b=2N−k gives exactly one feasible pair of difference j, and opposite parities give none. The centered scores are 2 times the sum of off-diagonal entries times z_a z_b; distinct unordered pairs are orthonormal in sign space, so all covariance constants follow. Each parity block is scalar minus twice the all-ones matrix: the parity of n has eigenvalue zero on constants and the other parity eigenvalue one, with the stated scalar eigenvalues on orthogonal contrasts. The finite sine sum for U_n(x) gives twice the sum of the parity-n Chebyshev terms plus I for even n; U_n(A_n)=0 on the sine eigenangles. This covers n=2, where the even block is identically zero and has no off-diagonal correlation claim. Independent replay gave 216224 kernel entries, 9454 Gram entries, 9454 null-polynomial entries and 203 exact raw full-sign-space covariance entries.

## originality

PASS

Best-of-knowledge pass for the explicit off-diagonal Gram/covariance law and its benchmark interpretation. The reflected kernel is a specialization of known Dirichlet spectral matrix-function structure, and the null polynomial is a classical Chebyshev characteristic identity. Neither is credited as independently new. The older Toeplitz–Hankel framework is closer to the proof than the trace-estimation papers and should be credited.

## value

PASS

For a standard Dirichlet test matrix this gives the exact stochastic risk of every degree≤n polynomial in one shared sample, with systematic variance cancellation absent from independently sampled degrees. A researcher comparing sampling and polynomial designs can use the signed covariance, exact spectrum and deterministic null contrast as a complete finite-size benchmark. The result makes no speedup claim and derives meaningful all-size constants, not just sample covariances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
