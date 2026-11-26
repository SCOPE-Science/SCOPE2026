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

The difference transforms as d/b or bd minus an integer, so membership in Z[1/b] is invariant and the least integralizing exponent increments or decrements until absorption. This also covers composite b and branch discontinuities. Reflection with the final downward step fixed gives binom(n-1,D-1) minus binom(n-1,D), where D=(n+k)/2, yielding the stated k/n factor. The first-step transform solves r=z(p+qr²), uses the smaller root for z<1, and extends to z=1 by monotone convergence. A successful word reweights by the constant (p/q)^k when the biases are exchanged, giving the stated conditional moments by differentiating the one-level transform. At balance, reflection gives a window containing exactly k lattice points of the allowed parity and hence the stated critical tail. Rationalizing the root to r=2pz/(1+sqrt(1-4pqz²)) yields both near-critical limits by taking k-fold logarithms; the conditional transform is continuous at zero and identifies the stated Brownian law. Countability justifies simultaneous meeting for a fixed reference point. The read-only exact-trajectory script is a finite diagnostic, not a proof of any infinite or scaling assertion.

## originality

FAIL

The paper does not state the frozen package verbatim, but its proof of Theorem 3.14 gives a stronger pathwise normal form for exactly these common-noise pairs. Specializing that normal form to equal bases already reduces pair equality to the first passage of the expansion-minus-contraction walk. The ballot distribution, defect, bias reversal and conditioned diffusive first-passage law are then standard walk calculations, not an additional model-specific phenomenon. Coverage is by concrete implication, not by the paper's asymptotic synchronization theorem or by a keyword hit.

## value

FAIL

The distinction between asymptotic synchronization and exact meeting is useful, and the presentation makes a practical probabilistic corollary easy to use. As a standalone finding, however, the meeting event is already determined pathwise by the existing pair coding; the remaining statistics and crossover are routine first-passage evaluations of the resulting ordinary walk. No distinct quantitative bound, regime, or mechanism remains that would justify accepting this as a separate finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
