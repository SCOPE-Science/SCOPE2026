---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The exact raw sum has sign convention I_Q−I_P: expanding both cardinalities leaves quotient avoidance minus product avoidance. The permutations Q_g(x)=gx and P_g(x)=x⁻¹g give independent-set counts on their cycles, including L₁=1 for a forbidden loop. For a rotation g=a^j, the stated gcds and parity give exactly the rotation summands. For g=a^j b, Q_g has n four-cycles. P_g swaps cosets: a^i maps to a^(j−i)b and a^i b maps to a^(i−j), so P_g² fixes rotation exponents 0,n and nonrotation exponents j,j+n. This corrects the frozen proof's local labeling of the four fixed elements, without changing the claimed count of two 2-cycles and n−1 4-cycles or the resulting −4n·7^(n−1). The Lucas bound L_k≤7^(k/4) for k≥3 follows from its two bases and 7^(1/2)>7^(1/4)+1. This gives the displayed B(n) by retaining the order-two quotient term and bounding the remaining product terms. At n=41 the exact bound is positive and the three normalized subtracted terms strictly decrease thereafter, so the finite sweep suffices. Independent replay: python -B /workspace/review_replay.py 5 constructs the graphs from ordered group products and right quotients for n=2–40 and counts independent sets by path/cycle recursion. It reproduces all finite signs, both boundary values, and the exact value of 3B(41). This does not assert any count comparison for product- versus quotient-dominant subsets.

## originality

FAIL

A distinct indexed result gives the identical dicyclic first-moment formula and exhaustive 29/30 sign boundary. This is verified statement-level coverage. The different proof bounds and the later displayed catalogue path do not establish historical priority in either direction.

## value

FAIL

The exact cutoff is a naturally motivated invariant of a family singled out by prior work, but the identified distinct catalogue result already supplies the same invariant and expression. The frozen proof saves a finite range of checks using a sharper sufficient estimate; neither that proof economy nor the local proof correction gives a separate mathematical finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
