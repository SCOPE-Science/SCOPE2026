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

Independently filtered all permutations through order eight by the equation pi(pi(i))=i, computed the direct Walsh character sums and inverse support sums, and checked the order-seven spectrum against spectrum_n7.tsv. The ranks are 1,1,1,4,8,16,28,64; the extra even zeros are 43,45,53,63, and the least nonzero magnitude is 8. The integer projection kernel numerator has absolute sum 144 on 64 points at order seven, and absolute sum equal to group order in every other claimed case. Averaging conjugates of an arbitrary projection over translations preserves the range, fixes it pointwise, and cannot increase either endpoint norm. The averaged projection is the unique Fourier indicator of the range. Its endpoint norms are its absolute kernel sum (max absolute row/column sums), also over the reals. Orthogonal Walsh diagonalization independently gives pseudoinverse norm 1/8 with the stated unnormalized convolution. Recovery at eight is contractivity on the rank-64 range, not invertibility on 128 coordinates. The Python 3.9 minimum in the notes is too low for int.bit_count(); this does not affect the integer certificate. Independent replay recipe: /workspace/branches/independent-math.md, section 2.

## originality

PASS

Chow's prescribed-descent-set formulas give the entire input, so neither descent enumeration nor the Walsh-odd vanishing is new. The supported distinction is the first departure from norm-one endpoint projection, the exceptional spectral geometry and exact optimum 9/4, followed by contractive recovery at eight. The closest distinct same-day entries concern a different weighting or a different feature of involutions. Available evidence does not establish earlier equivalent coverage of the combined obstruction and sharp optimum.

## value

PASS

A motivated finite boundary for stable projection onto a combinatorially defined range: the usual contractive even-frequency projection actually breaks at seven, with least possible amplification 9/4, and returns at eight. The sharp cost among all projections, not just a preselected convolution projection or a recomputation of published descent counts, is the useful invariant. The result is finite and does not support an eventual pattern.

The dated certificate retains the supplied scientific assessment, sources and limitations.
