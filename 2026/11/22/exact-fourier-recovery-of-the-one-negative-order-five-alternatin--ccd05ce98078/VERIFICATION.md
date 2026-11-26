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

The 0/1 running-sum tests ending at one are equivalent to the alternating-sign rules. The support determines all signs, because each row alternates starting positive. Independently, for the unique negative at interior (i,j) in zero-based indices, choose one occupied cell above and below it in column j, and one to its left and right in row i. The two leftover rows and columns are joined by a bijection; this gives exactly 2(3+4+3)^2=200 labeled matrices, each with seven occupied cells. The separately written exact replay /workspace/branches/0aa39191-e263-48a4-a4e1-6f69c0af413a/independent.py and logs full.log, smoke.log and occupancy_check.log reproduce all 429 order-five matrices, the 200 supports, zeros 4194816, rank 29359616, gap 4 and maximum 200 over the full 2^25 characters. The direct low-weight census reproduced the listed twelve pairs, both dihedral orbit sizes 4 and 8, and the zero counts 0,12,200. The maximum is attained at the trivial character, so the ratio on the recoverable Hilbert range is 50. The integer transform of the nonzero-frequency mask gives absolute sum 2222212096, and Fourier inversion divides by 2^25, giving 2170129/32768. Entrywise absolute row and column sums of the translation-invariant projection give both endpoint norms. Averaging any projection onto the invariant range leaves its restriction to the range equal to the identity and its image within the range. The average commutes with translations and hence is diagonal on Walsh characters with the required 0/1 multipliers. This proves the optimality assertion over either scalar field, without assuming that other minimizers must be invariant. No general-order, full-ASM, or ternary-encoding assertion follows.

## originality

PASS

The closest earlier analogue is the full order-four occupied-cell spectrum, and the closest same-object work is Lalonde's one-negative enumeration. Neither supplies the signed occupied-cell spectrum for the 200 order-five matrices, its low-weight zero geometry or the optimal endpoint constant. The counting family, Walsh transform and projection averaging are not credited as new methods.

## value

PASS

The one-negative stratum is a natural first departure from permutation matrices, with its own established enumerative theory. The order-five result identifies precisely the leading failure of recovery from occupied-cell characters by two distinct geometric orbits, then quantifies the surviving recovery space and the unavoidable endpoint projection cost. These exact facts are useful for comparing support data with ternary or negative-site tomography of the same matrix order; they do not follow from the known stratum cardinality or the generic projection theorem. The claim is an exact finite invariant, not a claimed general ASM spectral law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
