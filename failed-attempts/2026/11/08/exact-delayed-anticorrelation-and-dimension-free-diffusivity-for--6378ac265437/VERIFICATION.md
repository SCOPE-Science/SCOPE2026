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

The specified two-branch twisted baker map preserves normalized Lebesgue measure. Its Perron–Frobenius operator preserves the span of centered affine coordinates, with A_11=1/4,A_12=1/2, middle diagonal/superdiagonal 1/2, final A_M1=-1/4,A_MM=1/2. This gives C_M(n)=(A^n)11/3 and exactly the stated cofactor rational generating function. The shortest negative closed walk from vertex 1 through the cycle has length M with weight -2^{-(M+1)}, so C(n)=4^-n/3 for n<M and C(M)=(4^-M-2^{-(M+1)})/3<0. Spectral contraction makes the correlation sum valid; z=1 yields total 1/3 and zero positive-lag sum. The explicitly branchwise bounded d=f+H-H∘F with Pd=0 is a reverse martingale difference and supports the fixed-dimension CLT with variance 1/3. Independently rebuilt exact rational transfer matrices for 2≤M≤8 and checked the resolvent at z=1 and all first-negative coefficients. These tests corroborate, but do not prove, the all-dimension argument.

## originality

FAIL

Decisive published prior coverage: Resultary 2026/11/2 paper "Oscillatory coordinate memory and dimension-free variance in the twisted baker map" has the IDENTICAL map, normalized Lebesgue first-coordinate observable, IDENTICAL rational autocovariance generating function, same coordinate transfer matrix, strictly nonreal poles, cancellation Σ_{n≥1}C_n=0, and EXACT same martingale-coboundary identity and CLT N(0,1/3). Its complete RESULT.md and proofs were read. The submitted first-negative-lag n=M is just the first nontrivial coefficient in that earlier exact generating function, equivalently the first negative signed cycle through the already displayed transfer matrix. Additional novelty in a readily calculated first sign is not enough to make the unchanged broader theorem original. The originating Saiki/Takahasi/Yorke map is also prior; the submitted literature comparison overlooked the direct November 2 same-map result.

## value

FAIL

The central mathematical contribution—exact covariance transform, cancellation and dimension-free diffusivity—is already available in stronger published form on the same observable and every dimension. Isolating its coefficient at n=M gives an elementary and expected finite-lag corollary requiring only one step of the previously published matrix-walk expansion, not a motivated independent structural boundary beyond the already known oscillatory sign theorem. The tiny refinement cannot sustain an original, independently valuable finding, notwithstanding correctness and reproducibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
