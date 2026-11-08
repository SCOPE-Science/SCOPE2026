---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and verification

`check.py` requires only Python 3 standard libraries. Execute `python3 check.py` in a directory containing this document and the embedded checker.

The script enumerates exactly all nonzero degree-at-most-two Boolean evaluation words for dimensions \(m=3,4,5\), using a Gray-code accumulator with a generator matrix constructed independently of the theorem's filtration description. For every integer pair-radius from zero to the block length, it calculates the rank of the span of all words up to that radius and compares against the announced formula. The exhaustive counts are \(127+2047+65535=67709\) nonzero words. It also evaluates the explicit generators from the proof for \(3\le m\le8\), checks their cyclic pair weights and verifies each layer has the predicted full rank. These checks passed in the recorded same-model replay.

For manual proof validation, separately check the Walsh radical identity, the affine codimension-two characterization at weight \(n/4\), the at-most-two-block run bound for a least essential bit, the rank-seven eight-cycle edge span, and independence of the quotient classes supplied by the two quadratic generator types. The last item makes the result infinite rather than merely enumerative.

The checker does not enumerate all words for dimensions beyond five; its construction tests beyond five are finite. Neither this document nor the checker constitutes independent validation, historical priority certification, or a claim for different evaluation orders.
