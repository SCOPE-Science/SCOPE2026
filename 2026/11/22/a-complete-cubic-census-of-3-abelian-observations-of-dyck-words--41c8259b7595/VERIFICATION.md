---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Reconstructed the full profile map. In a run of length a, 111 contributes max(0,a−2), giving m−2p+u across the up-runs; 110 counts nonsingleton up-runs, 011 excludes the first up-run, and 010 counts all singleton up-runs except the first. Interchanging 0 and 1 and reversing gives the remaining triple formulas. The 10 bigram gives p even at m=1, where all triple counts are zero. The profile and parameter tuple therefore determine each other at a fixed m (which the one-letter counts already give). If p=m there is only alternation. Otherwise each side has at least one nonsingleton, and the totals imply u,v≥2p−m. An initial single up-step forces a complete initial 10; a final single down-step forces a terminal 10, since the preceding up-run starts at nonnegative height and must reach height 1 before that down-step. These singletons are disjoint except for the one-peak alternating case, already separated. Conversely removing t=α+β boundary peaks leaves M=m−t>r=p−t≥1 and prescribed singleton counts u−t,v−t in [0,r−1] with M≥2r−(u−t),2r−(v−t). Thus both compositions exist with a nonsingleton; decreasing up lengths and increasing down lengths give completed-peak heights nonnegative by comparison with jM/r. The first up-run and last down-run of the core are nonsingletons, so adjoining boundary peaks realizes the flags exactly. Counting for fixed t, substitute r=p−t: the number of options for each singleton count is min(r,m−t−r) for r≥1. Writing F_n=Σ_{r=1}^{n−1}min(r,n−r)^2, total P_m=1+F_m+2F_{m−1}+F_{m−2} (empty sums zero). Since a square of a minimum contributes 2k−1 for every k≤r,n−r, Σ F_n z^n = Σ_{k≥1}(2k−1)z^{2k}/(1−z)^2. Multiplication by (1+z)^2 and addition of z/(1−z) give z(1−2z+3z²)/(1−z)^4 and extraction gives exactly the cubic. One word per attained profile is both an upper bound and achievable code size. Independent replay `python3 /workspace/reviews/5-check.py` uses a prefix DP on counts of up/down steps, suffix up to length two and the accumulated full 14-count vector. All possible legal extensions update the vector locally and merge only identical states. At semilengths 1–18 the attainable parameter sets and profile cardinalities were exactly as stated (1650 for 18). This check is bounded, not a replacement for the construction or summation. Frozen scripts were inspected, not executed.

## originality

PASS

Best of knowledge, originality is the necessary-and-sufficient Dyck profile support and explicit realization, not the cubic polynomial or generating function as numerical invariants. The known 3-Abelian equivalence and Dyck pattern enumerations do not provide the simultaneous support in the inspected statements.

## value

PASS

This is an all-length exact classification of the possible outputs of a natural short-factor readout on a globally constrained language. It gives an explicit inverse representative for every feasible output, not just a known cubic with a changed name, and determines the exact largest code distinguishable by that readout. The richness is in the support theorem; the same enumerative formula elsewhere does not undermine its usefulness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
