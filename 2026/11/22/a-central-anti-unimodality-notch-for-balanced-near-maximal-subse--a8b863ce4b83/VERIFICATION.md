---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The greedy terminal letters followed by a missing suffix letter give the obstruction when the number of arches is too small. Exact balance then forces one surplus of each letter when there are k arches; a length-four arch or a length-two monochromatic rest cannot occur. Thus the disjoint cases are k+1 ordinary arches, one length-three arch plus the opposite surplus letter in the rest, and two length-three arches with opposite repetitions. In the last two cases direct cross-pair accounting gives shifts j−1 and 2k−j+3, or k−d+1 and k+d+2, respectively, over the baseline binomial(k,2); k−d position pairs realize gap d. This yields the three polynomials without multiple counting. Reversal gives reciprocity, and the low, middle and reflected high blocks cover the stated integer support. Taking adjacent coefficient differences reduces the ordinary block to one binomial difference, the flat shifted block to its boundary binomials, and the gap-weighted block to a telescoping boundary term and unweighted binomial sums. Independent symbolic reduction confirms the resulting parity-specific deficits; both are positive on the stated range and reciprocity forces a later rise. Independently authored finite checks compared full arch histograms through k=8, checked direct subsequence universality on all 4,704 balanced words through k=6, and verified each component gap through k=100. These do not replace the unrestricted symbolic argument. Frozen scripts were read as evidence, not run.

## originality

PASS

Best-of-knowledge contribution is the all-order weighted histogram and central nonunimodality at exact balance (k+1,k+1), k≥4. The arch criterion, the coefficient support as an existence statement, the aggregate count and fixed k=3 information are prior or already implied by prior work.

## value

PASS

The first balanced relaxation that allows surplus on both symbols is a natural boundary beyond saturated-letter formulas. Its exact joint count resolves how universal words populate fixed pair-count fibers; the strict central drop at every k≥4 is a structural change from the unimodal one-surplus setting. Neither that shape change nor the exact fiber sizes can be inferred from the previously known support or total.

The dated certificate retains the supplied scientific assessment, sources and limitations.
