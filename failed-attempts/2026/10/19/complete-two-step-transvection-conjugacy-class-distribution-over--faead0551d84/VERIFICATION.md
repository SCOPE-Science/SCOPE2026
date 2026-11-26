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

Fix I+aα and write a second transvection as I+bβ using a single representative b for each image line. The product minus identity is N=aα+bβ+α(b)aβ. With s=α(b), t=β(a), c=st≠0, the active span ⟨a,b⟩ has N-matrix [[c,s],[t,0]] and splits off from the fixed space. The active product is nonscalar, thus cyclic even at a repeated root, and has polynomial X²−(2+c)X+1 with value −c at 1. There are q^(n−1) lines with s≠0 and q^(n−2) forms with prescribed t=c/s. At c=0, N³=0 and N²=XY+YX (X=aα, Y=bβ), with exactly one nonzero rank-one summand when exactly one of s,t is nonzero; rank N≤2 then forces one J_3. Each such stratum has q^(2n−3)−q^(n−1) choices. At s=t=0, N is square-zero. For the common image line there is one cancellation and q^(n−1)−2 rank-one choices; for each of the L−1 other lines in ker α the q−1 nonzero multiples of α give rank one and the remaining q^(n−2)−q forms give rank two. This verifies every class count and omission at n=2,3. Counting projective lines times forms gives H, and conjugation gives the ordered-pair and probability normalizations. The source checker was inspected, not executed. An independent bounded check enumerated nonzero square-zero 2×2 matrices over F_2[x]/(x²+x+1) and multiplied I+X on the left by [[1,1],[0,1]]; it found one identity, two nonidentity unipotents and four products for each nonzero trace (trace equals trace shift in characteristic two). The algebraic count, not enumeration, covers all fields and dimensions.

## originality

FAIL

A distinct indexed result supplies the same complete table for every prime power and dimension, with additional prescribed-element counts and limiting masses. The overlap is mathematical (row-by-row identity under the same normalization), not a title match. This finding is already covered by that indexed result. The review does not assert that the indexed result was published first or establish direction of dependence from the catalogue dates.

## value

FAIL

The complete two-step distribution for a natural random walk is a worthwhile target. But the frozen finding contributes only the full table and its class-mass normalization, both of which the distinct indexed convolution already provides. It identifies no further exact invariant or new consequence beyond that coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
