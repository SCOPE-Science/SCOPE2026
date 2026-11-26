---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For real L1 of an arbitrary probability space, f≥0 and a positive contractive T of rank ≤r, the Riesz–Kantorovich modulus gives an order obstruction on the diffuse part: Lyapunov bisects the finite vector of coordinate functionals evaluated on f restricted to D, yielding |h|=1_D f and Th=0. For the atomic compression C, a finite-rank expansion C=∑u_k⊗φ_k on ℓ1 makes ∑_i(Ce_i)_i absolutely convergent (bounded by ∑_k||u_k||_1||φ_k||∞) and equal to ∑_k φ_k(u_k), the trace on the range. The eigenvalues there have modulus ≤1, so the nonnegative diagonal entries d_i lie in [0,1] with sum ≤r. On each atom the output modulus contributes at least a_i(1−d_i), while on D it contributes at least 1_D f, so the disjoint-band sum and the sorted-mass inequality give the asserted lower bound. Projection onto up to r largest atoms attains it, including r=0, no atoms, and tied or zero masses. Independently replayed `python /workspace/independent_replay.py 2`: 1,000 rational contractive matrices, 5,000 exact rank/modulus/mass comparisons; this checks the finite atomic part only. No formal verification claimed.

## originality

PASS

The exact fixed-f rank-budget optimum in regular-operator modulus is distinct from the known qualitative SPAP characterization and from sharp operator-norm approximation numbers of other operators; the independent later-version comparison narrows the contribution accordingly.

## value

PASS

Finite rank is a natural quantitative constraint in the existing SPAP problem. The exact rank needed to reach a prescribed error, or the irreducible error on a mixed space, is read from an all-rank formula valid for arbitrary positive signals, not just finite supports. The proof quantifies both the diffuse obstruction and atomic allocation and identifies an attaining operator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
