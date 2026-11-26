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

The generic permutation extension property realizes every ordered pair of insertion gaps, and homogeneity over the named base identifies each pair with one complete nonalgebraic singleton type. Its grade is the Hamming distance between the two corresponding initial sets. Inversion swaps the Boolean chains, and reversal of either order complements one initial set after reindexing the gaps; thus the generators either keep or reverse the coefficient sequence, preserving unimodality with plateaus. An independently written exact census starts with the gap row d(0,j)=j; when first-order position i is added, d(i+1,j)=d(i,j)+1 for j≤π(i) and d(i+1,j)=d(i,j)−1 otherwise. Checking all possible peak positions found no failures at n=1..9 and 32 among the 3,628,800 permutations at n=10 (4,037,913 checked total). Its independent orbit closure checks that the five representatives are lexicographic minima, that the sizes are 8,8,8,4,4, and that the disjoint union is exactly the observed failures. The reproduced witness profile is (3,8,16,20,19,20,15,8,6,4,2). The n=0 sequence is (1). Appending a largest point in both orders leaves the old grid unchanged and adds two strip positions at each grade 1..n+1 and one joint corner at grade zero. This preserves the strict valley at 3,4,5 indefinitely. Replay from /workspace/branches/b96f0ead-5448-426b-b390-6b5ba9188979: python3 independent_census.py --max-n 10 --output full_results.txt.

## originality

PASS

The strongest actual overlaps concern the same coefficient spectrum, but optimize one coefficient at a time or describe particular extremizing fibers. Neither gives the simultaneous unimodality property or its exact finite cutoff and orbit census. The identical catalogue hit is not a distinct predecessor. The bounded checks support only the sharp coefficient-shape finding and persistence, not priority of the homogeneous model or the symmetric-difference interpretation.

## value

PASS

The least failure order for a natural shape property of a whole type spectrum is not fixed by the known total count or grade-by-grade bounds. The exact cutoff, sparse complete orbit classification, and elementary embedding of the obstruction at every greater order give a useful benchmark for generic permutation spectra and Boolean-chain distance enumerators.

The dated certificate retains the supplied scientific assessment, sources and limitations.
