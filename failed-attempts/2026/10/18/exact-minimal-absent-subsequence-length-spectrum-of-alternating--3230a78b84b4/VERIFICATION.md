---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Greedy matching in the infinite alternating word gives P=m+a+E=2m−R+a for target length m, first bit a, equal-adjacency count E and run count R. Direct endpoint checks, including m=2, give deletion cost 0 at the first position just for 01, 0 internally just for 010 or 101, and last-position cost 1 for a change or 2 for equality; all remaining costs are 2. Minimal absence therefore forces P=2k+1 or 2k+2 with exactly the stated run restrictions. Setting m=k+j gives the four run counts 2j−1,2j,2j−2,2j−1 in the printed order. For R>=2, the minimum allocations are respectively 2R−1, 2R−2, 2R and 2R−1 letters, reproducing the common binomial top k+1−j by stars and bars. At j=1 the two constant targets contribute separately and the zero-run case contributes nothing. Pascal twice combines the rows including zero layers. Summing over k, the j=1 term is z(3−2z)/(1−z)^2 and the j>=2 terms are geometric in z^3/(1−z)^2. This yields the displayed OGF, recurrence and initial values. The characteristic cubic is r(r−1)^2−1; it has only one real root, greater than one, since the maximum of r(r−1)^2 on [0,1] is 4/27. The other two roots are conjugate with modulus rho^(−1/2) by the root product, and the numerator does not cancel the positive dominant pole. Independent complete finite subsequence sets reproduced the length histograms through k=10. An independent pair-transfer inversion also gave the same full length enumerator. Neither check replaces the proof.

## originality

FAIL

A distinct indexed record, 47ef0e5dde29, gives the identical full binomial spectrum for the same linear binary hosts after shifting its excess-length index by one. It also states the identical total OGF, recurrence and growth. Another distinct record, 2ef499428033, gives the full bivariate enumerator and the same greedy-endpoint membership test; 7389806d175c covers the totals. These are verified overlaps in available coverage. Their later catalogue dates do not establish historical priority or dependency. The all-alphabet transfer in frozen ordinal 4 also specializes to the complete binary distribution, without requiring any ordering of the two frozen entries.

## value

FAIL

The distinction between shortest and minimal absence in the alternating word is a natural problem and the binomial formula is useful. But the frozen scientific finding, including all layers, extreme lengths, short count and growth, has exact independent catalogue coverage. The run-composition proof of the covered invariant does not by itself establish a distinct result with enough additional mathematical value for a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
