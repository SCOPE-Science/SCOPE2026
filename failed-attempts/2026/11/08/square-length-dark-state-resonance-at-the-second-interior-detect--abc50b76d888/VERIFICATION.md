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

The complete assigned RESULT.md has exact simple Krawtchouk eigenvectors with eigenvalue J(d-2k), and K_1=d-2k, K_2=((d-2k)^2-d)/2. Strict positivity of independent loss rates makes undamped eigenspaces precisely eigenlines zero on all sinks; a reducing-subspace argument gives all-density-matrix eventual capture. K_2 has exactly two integral roots for square d>=4 and none otherwise; K_1 has one only when d even; their roots never coincide. The endpoint survival for d=s^2 is 2*binom(d,(d-s)/2)/2^d, equal to 21/64 at d=9. The e^{-1/2} local-binomial factor follows from one-standard-deviation local CLT. Independent direct integer Krawtchouk sums checked d=3..42 and nonintersection, not substituted for the proof. No statement extends to finite-time capture, other hopping, or collective sinks.

## originality

FAIL

The identical perfect-square Hamming-shell absorption law and exact endpoint survival were already published for the hypercube. The hypercube symmetric shell basis reduces its adjacency exactly to the assigned weighted path, with shell-2 local absorption preserving the dark-eigenvector criterion. The extra first-detector parity and two-detector zero-dark projector follow immediately by intersecting known K_1/K_2 zero sets and the established general target-absorption principle. This is a correct context-specific synthesis but not sufficiently independent from covered and elementary existing results.

## value

FAIL

Perfect-transfer dark-state control is a motivated physical problem. Nevertheless the striking perfect-square dichotomy and quantitative survival are exactly equivalent to a published shell-detection result under the standard equitable quotient; the residual one/two-detector checks are elementary low-degree root intersections of the existing spectral principle, not a distinct structural advance requiring an independent result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
