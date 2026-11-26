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

Projection into the m-dimensional span and extension there to a hyperplane cannot increase the maximum error. For its unit normal w, the coordinates y=B* w satisfy ||w||²=y^T G^{-1}y and the error is ||y||∞. Homogeneity gives the reciprocal of the maximum inverse-Gram quadratic on the real cube for the squared width. Every maximizer is a corner by strict convexity in each coordinate. Multiplication verifies G^{-1}=A(I−γ11^T)A; positivity follows from 0<mγ<1. This yields the stated discrepancy formula and all optimal planes within the span, with opposite signs giving the same plane. At δ=1, normalization gives pairwise cosine 1/2 and the threshold holds exactly for a balanced sign assignment. The rational instance map has polynomial bit length, the certificate is a sign vector, and the usual subset-sum dynamic program is pseudopolynomial. The frozen CHECK.py (inspected, not run) supplies only finite rational diagnostics; the general claim follows from the proof.

## originality

FAIL

The earlier weighted-simplex zonotope result already determines the entire δ>0 terminal-width formula, optimizer sign patterns and threshold via the elementary inverse-Gram duality acknowledged by the frozen result. This is a demonstrated implication on strictly positive weights, not an inference from a keyword hit, an inaccessible source, or a one-zero-weight limit.

## value

FAIL

A fixed-angle threshold is a meaningful way to limit a width problem, and the reciprocal-radius correspondence can be useful exposition. Here the core invariant and full optimizer/threshold information are mechanically transported from the earlier positive-weight zonotope computation, using a constant shift and rescaling on the cube. The frozen finding supplies no distinct nonroutine consequence beyond that transport.

The dated certificate retains the supplied scientific assessment, sources and limitations.
