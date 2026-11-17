---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The bright/dark Hilbert split follows from loss supported on the weight-one shell and Hermitian invariant cyclic span. Radial constants R_k and first-harmonic centered coordinate functions W_k yield the projector; the frame identity sum_{|x|=k}v_xv_x^*=binom(d,k)k(d-k)/(d(d-1)) I yields explicit entries, and the even middle Krawtchouk vector contributes the rank-one correction. An independent Walsh eigenspace SVD compared 5,456 projector matrix entries for d=2..6 (max discrepancy <5e-9), and checked idempotence. All d proof is algebraic, not finite extrapolation.

## originality

FAIL

The 12 October published SCOPE theorem for the SAME all-weight-one absorber model already identifies the FULL bright space as E=direct sum of affine functions on each Hamming layer, with P_B=P_E for odd d and P_B=P_E-|q><q| for even d. This determines the entire operator P_B uniquely, including all offdiagonal entries, before any new arithmetic. The submitted formula is a frame-matrix evaluation of that already-characterized projector; the corner phase law is an immediate expectation value of the known central radial vector. Statement-level implication is decisive despite different prose and missing explicit matrix table.

## value

FAIL

Coherent initial-state effects are physically motivated, but this specific exact projector and corner interference follow by routine linear algebra from the earlier complete subspace/projection characterization. No independently new invariant or structural fact remains after prior coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
