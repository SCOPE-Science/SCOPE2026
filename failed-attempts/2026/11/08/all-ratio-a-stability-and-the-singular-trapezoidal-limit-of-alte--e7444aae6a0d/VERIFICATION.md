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

Actual pinned two-step companion matrices give W μ²−P μ+r=0. Independently recomputing (|W|²−r²)^2−|P conj(W)−r conj(P)|² gives (r+1)^4 A B with A>0 for any nonzero z in Re(z)>=0, B>0, and |W|>r, proving strict Schur-Cohn. At z=0 factors (μ−1)([(2r+1)(r+2)]μ−r). Fixed total q and r→∞ yield ((2−q)/(2+q),0), whereas stiff q→∞ at fixed r sends both eigenvalues to zero; noncommuting iterated spectral-radius limits follow. Independent exact SymPy factorization replay completed; finite sample roots are secondary.

## originality

FAIL

A complete earlier published 2026-11-02 RESULT.md proves exactly this claim on the identical standard two-periodic variable-step BDF2 scalar equation. Its normalized monodromy polynomial matches algebraically W/r and P/r; its zero-mode and trapezoidal/stiff limits are identical. Therefore the new final result is covered, independently of correctness.

## value

FAIL

The mathematical subject is important, but the submitted final result is an exact rederivation of an already published theorem, with no new independent invariant, strict improvement or substantive boundary; a second certificate is not an independently valuable finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
