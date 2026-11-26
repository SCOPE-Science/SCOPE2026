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

Two indexed positions produce the same deletion output exactly when the interval between them is constant. A run-delete class fails the receiver filter exactly for an interior singleton with like-letter neighbors, at least one doubled. On each run-pair transfer the appended letter has one repeat choice and q−2 other choices; the transfer scores the finalized interior run while the two endpoint scores remain fixed, and a single run is counted separately. For k double runs, b valid singletons, and e double endpoints, the invalid-singleton count is at most 2k−e and b>=2−e for at least two runs. Hence n<=4d−(3b+e)<=4d−2. A single run also obeys the bound. Alternating run colors make all designated interior singleton deletions invalid in the four constructions: use double endpoints and two singleton runs per gap at n=4h−2, shrink the final gap to one singleton at n=4h−3, or truncate to a singleton endpoint at the other two lengths. Equality at maximal span uses every double-neighbor incidence once with no valid singles, forcing exactly two singletons between successive doubles and one color choice per gap. The upper bound is the number of runs, with equality at n only for all-singleton runs. The independent bounded replay explicitly deduplicated and filtered outputs and matched local degrees and transfer histograms for 35,880 legal words: q=2 through n=14, q=3 through n=9, q=4 through n=7. It confirmed both extrema, maximum counts and all maximal-span census/equality cases in those ranges.

## originality

PASS

The supported distinct contribution is the receive-filtered distribution, sharp minimum, and rigid maximal-span census. The unrestricted class-per-run law and the general transfer-matrix method are not being credited as new, and the comparison does not establish historical priority.

## value

PASS

The same admissibility test on transmitted and retained words gives a natural repair/filter combinatorics problem, distinct from unrestricted deletion and from code-size optimization. The degree distribution supplies the full invariant; the q-independent sharp lower bound and its rigidity quantify the worst loss of admissible outputs and identify exactly when overlapping local losses can be maximized. This is more than the ordinary endpoint count or a finite histogram.

The dated certificate retains the supplied scientific assessment, sources and limitations.
