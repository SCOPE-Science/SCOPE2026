---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The 90 labelled row/column-sum-two binary 4x4 matrices were independently enumerated from all four-row pairs. For degrees r=0..4 independent evaluation of all <=r parity characters yielded numerical ranks (1,10,39,75,90); the quadratic 90x90 matrix H2H2^T had eigenvalues (160^9,256^9,320^4,384^12,512^4,650^1) and 51 zeros, matching the exact source characteristic polynomial. The supplied verify_krawtchouk.py and independently constructed verify_direct.py were read and implement exact integer characteristic polynomials and independent prime-modular rank lower bounds. The Krawtchouk kernel 137-34d+2d^2 follows by counting character intersections; the invertible triangular character-to-squarefree-monomial map proves Hilbert increments (1,9,29,36,15), sharp degree four and normalization/condition numbers. This is a finite exact theorem with reproducible complete enumeration, not an infinite extrapolation.

## originality

PASS

Best-of-knowledge novelty assessment from actual statement-versus-implication comparisons and the indicated primary source reading, with stated residual risks.

## value

PASS

The binary two-regular 4x4 fiber is a natural first nontrivial square case explicitly singled out by the open binary contingency-table orbit-harmonics question (Oh–Rhoades Problem 7.4). The complete graded rank law and quadratic spectrum are unknown exact natural invariants of this fiber, independently useful as a benchmark and not a known-table recomputation on inspected evidence; no general theorem is required for this small but motivated classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
