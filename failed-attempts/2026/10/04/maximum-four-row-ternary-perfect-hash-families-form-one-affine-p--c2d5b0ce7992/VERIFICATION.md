---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The finite classification in the package is correct. Normalizing any pair by row/symbol symmetry leaves four Hamming-distance cases. The inspected exhaustive backtracking certificate proves a size-nine family containing the pair exists only at distance three. Thus every pair in any maximum has distance three, making every two-coordinate projection injective and giving the upper bound nine. The displayed affine-plane family has nine columns and separates every triple. At equality, projection to two coordinates is bijective and the remaining two coordinate functions form an ordered orthogonal pair of Latin squares of order three. There are twelve Latin squares and seventy-two ordered orthogonal pairs; the full row/symbol orbit of the displayed family also has size seventy-two, yielding one orbit and stabilizer 31104/72=432. A fresh independent replay earlier in this run reproduced all four normalized pair-search outcomes and the Latin/orthogonal-pair counts. These computations are exhaustive for the stated finite parameter set.

## originality

FAIL

Originality fails decisively. A ternary strength-three perfect-hash family with four rows is exactly a trifferent code of length four when columns are viewed as codewords. Kurz's 2023 complete classification uses the same equivalence operations: permutations of columns, rows, and symbols. It explicitly tabulates one equivalence class at length four/cardinality nine and states in the appendix that there is, up to equivalence, a unique length-four trifferent code of maximum cardinality T(4)=9. Thus both the sharp maximum and the one-equivalence-class extremizer theorem are already published. The audited exact labeled count 72 and stabilizer 432 are secondary orbit bookkeeping for this known unique maximum and do not restore originality of the final claim.

## value

FAIL

The package gives a clean independent proof and useful labeled orbit statistics, but the scientifically central finite boundary and classification are already known: maximum nine and a unique equivalence class at length four are explicitly published in Kurz's complete small-length census. Once that class and representative are known, the additional labeled-count and stabilizer calculation is secondary group-action bookkeeping and is not enough to make the unchanged final claim a distinct worthwhile finding under the required value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
