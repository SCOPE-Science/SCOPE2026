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

The Vandermonde conditions give the Lagrange weights at zero. For x_j=N_j^{-2}, the ratio of successive absolute per-node coefficients is bounded below by 2 times the product of (1-4^{-q}) over earlier levels, hence is strictly greater than one (the first ratio is at least two). Two grids in an integer-divisibility chain are nested if their quotient is odd and disjoint if it is even. Each actual node receives an alternating tail entirely within one block, with the strict sign of the terminal coefficient, so there are no zero weights. The nonfinal terminal level just before an even refinement at i is i-1; its sign is negative exactly when i and d have the same parity. Summing over disjoint negative blocks recovers the negative coefficient sums, and the sharp absolute perturbation bound is attained by sign-aligned node errors. For the strict maximum, tails in any earlier block have magnitude at most b_t<b_d, including singleton tails newly introduced at that block's last grid; in the final block only singleton tails reach b_d. This clarifies an overstatement in the prose of the maximum proof without changing the conclusion. The midpoint Euler–Maclaurin expansion terminates at the claimed degree and the moment conditions cancel all remaining even powers.

## originality

PASS

The supported distinct contribution is the midpoint-specific necessary and sufficient parity classification and negative-block formula for all integer-divisibility chains. Evaluation by Lagrange weights, alternating growth techniques, polynomial exactness, the general norm identity, and the form of the final-grid peak are established or analogous to prior work, not independent novelty claims. No inspected prior statement covers the midpoint classification.

## value

PASS

For standard midpoint quadrature with an arbitrary admissible refinement chain, the classification decides directly whether high-order extrapolation retains norm one under bounded sample errors. The positions, not just the presence, of even refinements distinguish stable positive mixed chains from genuinely negative ones. Quantifying the defect gives a usable exact error bound on nonpositive chains. The contribution is the structural classification and its consequence for chain choice, not merely two small computed examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
