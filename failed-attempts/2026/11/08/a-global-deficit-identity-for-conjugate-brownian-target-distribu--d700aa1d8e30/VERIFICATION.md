---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The renewal quotient T_mu=g_mu/f_mu follows from one-attempt success; the backward heat equation and half-line boundary give g_mu(x)=(1/D)∫min(x,y)f_mu(y)dy. Symmetric nonnegative Green kernel makes averaging h(y)/h(x) with its reciprocal yield the exact squared-ratio gap. Finite reference first moment controls normalization and reference risk. Equality forces h constant and f_mu=f_mu0 via x↓0, and Brownian characteristic function E e^(−Dk²τ) identifies reset-time law by Laplace uniqueness. Tonelli handles infinite competitor risk. Code inspected; not used as a substitute proof.

## originality

FAIL

An earlier stronger mathematically implying Green-kernel identity was read in full. Mathematical implication is explicit and dominates the new squared-ratio theorem. Unique law under free Brownian uses its elementary exponential Fourier–Laplace mixture, not an independent hard global optimization result; prior result published November 2 versus assigned November 8.

## value

FAIL

The underlying global optimization is mathematically worthwhile, but the central squared-ratio Green-kernel regret identity and its global-minimization consequence were already published in stronger diffusion generality Nov 2, 2026. The unbounded half-line and Brownian law-injectivity specialization do not isolate a separately motivated unsolved invariant or hard theorem. Repackaging as a special case with extra numerical certificates would not restore value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
