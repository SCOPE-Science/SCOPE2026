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

Choosing equality partitions and ordering their blocks by least label gives a bijection between original matrices and clarified matrices with their two partitions. Row and column duplication preserves rank: the two duplication maps each have a left inverse obtained by selecting representatives. In a full-rank factorization H=UV, the maps sending a row of U or a column of V to the corresponding row or column of H are injective. Thus pairwise distinct spanning tuples are the correct factors and each H is represented by one free GL(d,q) orbit. Subspace Möbius inversion gives (2), and the basis-extension construction realizes precisely d≤a,b≤q^d for d>0; rank zero requires a=b=1. The Stirling EGF and rank normalization follow by summing the partition bijection. Independent direct enumeration used field elimination and distinct row/column vectors for every binary matrix of sizes 2×2, 3×3, 4×4 and every ternary 2×2 matrix. All profiles matched (1); the clarified binary vectors by rank were (96,168) and (96,13608,20160) for 3×3 and 4×4. These tests are bounded; the proof, not those counts, establishes the field-general claim. The frozen verify.py was inspected, not run; the direct replay is to enumerate the q^(rm) entry arrays, bucket by row and column set sizes and elimination rank, and compare each bucket to (1).

## originality

PASS

The retrieved sources do not state or subsume the explicit finite-field factorization, exact support and generating-function package as a result on the joint profile. This is a qualified assessment of statement-level distinctness, not a claim of priority or that the underlying census is independently hard or mathematically novel. The census itself is mechanically determined by established results, as shown in the prior-implication and value assessments.

## value

FAIL

The parameters are natural, but the proposed exact census is a mechanical application of the established unranked double Stirling inversion with q^(ij) replaced by the standard rank-d count of an i×j quotient. This works because copying rows and columns preserves rank, with no additional counting problem on a specified partition. The EGF is then the ordinary Stirling substitution and the support is the elementary dimension/cardinality bound with a basis padded by distinct vectors. The alternative factorization is a convenient expression of the determined census, but does not establish a separate substantive result that rescues this frozen finding. The failure is for scientific value as a distinct exact finding, not for false formulas or inaccessible literature.

The dated certificate retains the supplied scientific assessment, sources and limitations.
