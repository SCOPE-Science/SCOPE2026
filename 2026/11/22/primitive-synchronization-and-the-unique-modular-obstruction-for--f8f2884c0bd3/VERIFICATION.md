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

The fixed cycle makes any invariant equivalence a subgroup congruence, so only residues mod 3 are proper and nontrivial. If b preserves this partition, rank 7 is too large for the quotient to use only two target blocks, so both letters permute the quotient and no reset exists. For the converse an independent non-enumerative proof replaces the decisive census check. Let r be the least word rank, choose an image C of size r, and let A be any fiber of any rank-r word f. Distinct points of C cannot be merged by a word, or r would drop; the same is true of every rotation C+t. Hence |(C+t)∩A|≤1. Summing over rotations gives r|A|≤9, and all r fibers together have size 9, so all have size 9/r. Since 1<r≤7 in the nonsynchronizing case, r=3. Writing w(x)=|b⁻¹(x)|, each translated fiber A+t has b-preimage size 3: apply b, rotate by −t, then apply f; the result still has rank 3 and uniformly sized fibers. Multiply Σ_{x∈A+t}w(x)=3 by ζ^t and sum over t for a primitive ninth root ζ. The result is (Σ_x w(x)ζ^x)(Σ_{a∈A}ζ^(−a))=0. A rational polynomial of degree at most 8 vanishing at ζ or ζ⁻¹ is divisible by Φ₉(z)=1+z³+z⁶ with quotient of degree at most 2; its coefficient vector is therefore constant on residues mod 3. The first factor cannot vanish because w has support 7, not a multiple of 3. Each A must thus be a full residue class. Apply this to f and f∘b, both rank 3: b takes each mod-3 class into a single mod-3 class. This proves the exact converse for both kernel shapes without relying on running the supplied census. Independently, there are 84+378 partitions with the two kernel shapes and 9!/2! image assignments per partition, yielding 83,825,280. A quotient permutation has six choices, and each class has 3,18,6 maps of local rank 1,2,3, respectively, allowing profiles (1,3,3) and (2,2,3) and their permutations. This gives 1,944+34,992=36,936 obstructions and 83,788,344 synchronizing maps. No nonidentity rotation can stabilize an image of size 7 because its orbit lengths are divisible by 3; division by 9 gives 9,313,920 total classes and 4,104 nonsynchronizing classes. Both C++ census programs and COUNTS.txt were inspected, not executed. The base-nine code exhausts transition tables and closes the four nonzero distance classes, whose rotations parametrize all pairs; the other generates kernel partitions with each ordered image injection once and closes backwards from direct collisions on all 36 pairs. The subset script's full checks at orders 4–6 and sampled checks at order 9 are supplementary and not the converse.

## originality

PASS

The supported distinction is the classification and exact census for every defect-two letter at cyclic degree nine, especially the double-pair kernel not covered by the inspected sufficient conditions. The one-triple-kernel primitive synchronization implication is previously covered, as are the generic minimum-rank kernel-graph facts, and neither is claimed as new. The distinct same-day eight-state census is a genuine method and scope analogue, but does not establish the nine-state congruence criterion or counts.

## value

PASS

Degree nine is the first odd composite cyclic degree and has exactly one potential proper congruence. Defect two is the first defect where two nontrivial kernel fibers can occur and the broad one-exceptional-fiber criterion no longer suffices. Pinning down the complete modular obstruction and both exact kernel-shape populations gives a motivated boundary case and reproducible benchmark for circular synchronization, not a randomly selected number of states or mere reset-length tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
