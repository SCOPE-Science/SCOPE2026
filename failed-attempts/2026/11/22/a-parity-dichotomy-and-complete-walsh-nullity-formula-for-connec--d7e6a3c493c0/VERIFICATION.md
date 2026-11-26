---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

A nonempty induced vertex set is connected iff it is a singleton or hits multiple parts. Subtract the empty set and, disjointly, nonsingleton subsets of each part from the full Boolean cube. For a frequency S the sum over the subsets of part i factors as a product of 1+(-1)^{1_{v in S}}, so it is 2^{n_i} for a missed part and zero otherwise. Subtracting the singleton and empty contributions gives the claimed multiplier, with the full cube term 2^N only at S=0. Orthonormal Walsh characters diagonalize the operator after unit normalization; eigenvalue magnitudes are singular values. Their common parity is N+r-1 mod 2. If N+r is odd, an all-parts-hit frequency of weight (N+r-1)/2 is feasible in [r,N] and has multiplier zero. If N+r is even, an all-parts-hit frequency of weight (N+r)/2 in [r,N] has multiplier -1, also in the complete graph edge case N=r. The zero-frequency cardinality is maximal by the triangle inequality. Each proper missed-part set defines a disjoint class, counted by the stated coefficient, and the empty character has positive multiplier. Comparing nullity with the relevant binomial layer costs at most twice the union bound sum_i 2^{N-n_i}; Stirling at a bounded offset from N/2 gives the stated relative O_r(1/N) error. Finite independent replay used graph search on each induced subset then direct integer character sums; 479 assertions for 136 nondecreasing shapes (2<=r<=6, each size <=6, N<=11) corroborated parity and the minimum invertible singular value. For (2,2), (2,3), (3,4), respectively, (nullity, maximum absolute eigenvalue) equals (0,13), (12,26), (34,112). Replay details: /workspace/reviews/evidence/5-walsh-replay.md. The frozen verifier was inspected, not executed.

## originality

FAIL

The separately indexed same-date record 9d3a9242b352 covers the same operator, every multiplier, the equivalent parity, the exact same coefficient formula and more spectral information. Its proof already gives the quantitative error bound for all part sizes; the apparent broader asymptotic is obtained from that displayed inequality by inserting the different part-size bound and applying the standard Stirling estimate. This is direct corpus overlap, not a claim as to which authors or same-date records have historical priority.

## value

FAIL

The parity transition and exact convolution kernel would be meaningful as a standalone result, but here they duplicate the same operator's published spectrum/nullity. The only apparent extra range for the asymptotic is a routine substitution into the companion's explicit error bound; no independently useful new invariant or nonmechanical remainder is demonstrated. No repaired claim is proposed as accepted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
