---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

A row-stochastic matrix preserves constants, so in path-difference coordinates its induced ℓ¹ norm is the maximum variation of a unit cut indicator. At that cut, symmetry identifies the two cross blocks as transposes, and the admissible cross block is exactly the sub-stochastic edge-weight polytope of the cut's bipartite bandwidth graph: all unallocated mass can be put on the diagonal. Integrality and convexity thus give an optimal matching without assuming all symmetric stochastic matrices are mixtures of involutions. For p left hole runs and q right island runs, the two internal transition counts are at most 2p−e_L and 2q−e_R, where e_L,e_R are the adjacent switch indicators. The cut transition is 1 if those indicators agree and 0 otherwise, giving the two bounds used in the proof, even at finite endpoints. At even bandwidth 2k, the only way to exceed 4k−1 is with both adjacent sites unchanged and k runs on each side. That forces every switched depth to be 2,4,…,2k; the depth-2k hole has no permissible partner. At odd bandwidth 2k−1 the run counts alone suffice. Set s=min(n,4k), m=ceil(s/2). The parity target has exactly m ones and the sorted transpositions have constant displacement at most 2ceil(s/4)−1 on every nonempty matching (check s modulo four); if s<n the last alternating entry is zero, so there is no extra endpoint jump. This realizes min(n−1,4k−1), including n=2 or r≥n−1. Symmetry really matters: the bandwidth-two permutation with row images (0,3,1,4,2,5) maps the cut at 3 to (1,0,1,0,1,0), of variation 5 rather than the symmetric maximum 3. An independently written sweep of all banded involutions using an adjacent-edge cut histogram passed for 52 (n,r) pairs, 21,330 involution instances; separate deduplication by cut confirmed the reported 1,373 profiles across the original 30 pairs.

## originality

PASS

The checked distinct claim is the exact uniform symmetric-bandwidth envelope, including even-odd plateaus and finite-size involution attainment. The induced-norm reduction and matching integrality are existing methods; TV nonincrease for a particular filter and fixed-matrix seminorm computations are not this extremal theorem. The decision is best-of-knowledge, not a claim to have ruled out every treatment of banded stochastic matrices.

## value

PASS

For a local conservative filter, the exact worst amplification is a stability bound on arbitrary path data. The tradeoff between locality and oscillation is not captured by stochasticity alone: positivity and symmetry still allow amplification, but symmetry removes two potential transitions at even bandwidth. The parity plateau and the sharp finite-size cutoff tell precisely when enlarging the stencil cannot worsen that bound, and the explicit local swaps show it cannot be made smaller on this class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
