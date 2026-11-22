---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

A primitive word of length m corresponds uniquely to a least-period-m doubling orbit and the minimum point to its Lyndon rotation, so the open-hole endpoint survives at equality. Two-zero primitive necklaces are indexed exactly by shorter cyclic gap 1≤d≤⌊(m−1)/2⌋; equal gaps are excluded as nonprimitive. Their b_m,d increase geometrically in index. For three zero gaps, maximizing the shortest gap and resolving repeated minima gives primitive lexicographic maximizers (q−1,q+1,q),(q,q,q+1),(q,q+1,q+1) by congruence. The published Kong–Pu Lemma 3.3 gives monotonicity of fixed-weight maxima, excluding all ≥4-zero words above this first three-zero word. The strict interleaving b_(e−1)<η_m<b_e and count formula follow. Fresh exact primitive-necklace enumeration m=4..15 verified every leading word, not used as an infinite proof.

## originality

PASS

PASS for the *complete ordered cross-weight initial staircase* with linearly many exact first-entry thresholds. Kong–Pu Theorem 3.1 determines only fixed-weight extremal Lyndon representatives and Lemma 3.3 orders their maxima; the current linear block and geometric cross-weight enumeration are consequences that require additional comparison, but prior input is explicitly credited. This is a potentially modest incremental theorem, with publication-priority risk retained.

## value

PASS

Survival of primitive periodic orbits under a growing interval hole is a standard dynamical invariant. Knowing every threshold in an initial block of length m/6+O(1), exactly and for all m, is a structurally meaningful partial census and can support escape/periodic-orbit calculations even without a complete lower staircase; not an arbitrary hand-picked finite list.

The dated certificate retains the supplied scientific assessment, sources and limitations.
