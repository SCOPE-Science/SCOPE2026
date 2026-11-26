---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For any two class sums the product coefficient at cell (i,j) is the left class's row count at i times the right class's column count at j. Equality within each target class for every pair of factors implies equality of each complete profile, by separately summing over the factors and cancelling 2 or m in characteristic zero. Conversely equal profiles suffice. Unequal row profiles force all classes into single rows; any two columns sharing one class must share the corresponding class in the other row, giving a common column partition. If all classes are row-balanced, a class name fixes the unordered pair of class names on any column it meets, and a two-name component is balanced exactly when each orientation occurs on half its columns. These descriptions are unique. Row and column classes are intrinsic as principal right and left ideals, so the automorphisms are precisely the independent row and column permutations. For balanced components a single row swap combined with matching half-swaps, together with independent column permutations within the prescribed pieces, gives exactly the prescribed orbits. The labelled assembly weight is 1 plus half the central binomial coefficient on even components, and 1 on odd components, giving the stated EGF with the formal constant 2.

## originality

FAIL

Two distinct earlier Resultary records already give the all-m classification, automorphic completeness, and the labelled count. The October 26 record also gives the identical characteristic-zero scope. The extra numerical evaluations do not supply a distinct theorem.

## value

FAIL

A complete structural classification of this natural family is useful, but the submitted record adds neither new Schur families nor a stronger orbit result to the existing all-m classification. Printing three more terms by the known EGF does not constitute a new useful invariant or computation with its own motivation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
