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

The lexicographically first rotation starts a longest zero block and is preceded by 1; tied full rotations share their last character. Thus the transform, with k ones, starts in 1 and has at most k runs of each symbol. For certified gaps the rows are grouped by decreasing initial zero length t, with exactly one 1 in a level for each distinct full gap and no 1s in intervening unmarked levels. Each intermediate level exists because a longer gap also contributes a suffix row there. The one-starting rows contribute only 0s when all gaps are positive, proving exactly 2k linear runs. Sorting and subtracting 2i−1 yields a weakly increasing k-tuple of nonnegative entries summing to n−k(k+1). For indexed counting, every rooted gap vector and any of the n locations of the marked 1 produce one rooted word; erasing the mark divides by k. Thus k!p rooted vectors give n(k−1)!p indexed words; distinct gaps preclude a proper cyclic period, so dividing by n counts the necklaces. This handles k=1 directly as well. Under the uniform rooted law, a specified gap is zero with probability (k−1)/(n−1); for k≥3 a close pair has at most two choices per composition of the remaining k−2 coordinates of total at most n−k, i.e. at most 2 binom(n−2,k−2) vectors. For k=2 there are at most two bad vectors directly; for k=1 there is no pair. The union bound yields the truncated lower bound and tends to one for k=o(n^(1/3)); it does not locate a sharp probability threshold or give exact counts of all maximizers. An independent full-rotation enumeration checked 32,738 mixed words through n=14 and the exact certified counts for 91 pairs. The supplied checks were inspected but not executed; check_gaps.py lines 42–49 only checks nonnegativity of its partition outputs, not an independent count, whereas the supplied exhaustive checker actually compares counts on its finite range. None of these finite checks is used for an all-length inference.

## originality

PASS

The identified polynomial increasing-gap construction is a direct antecedent for one subclass, and the exact indexed or necklace spectra are stronger at weights three and four. The distinct contribution is a permutation-independent sufficient structure, its exact certified enumeration and a joint n,k high-probability law. No inspected prior result entails all these assertions with k growing.

## value

PASS

The structural certificate delivers extremizers at every feasible length for the separated-gap family, an exact count, and a probability estimate uniform over growing weights. It gives information between isolated constructions and fixed-weight exact spectra. The interpretation is deliberately limited to a sufficient asymptotic regime, not a true critical window or the full run spectrum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
