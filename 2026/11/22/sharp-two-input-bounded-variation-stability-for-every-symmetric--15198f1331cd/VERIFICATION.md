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

For w=2r+1, k=w−2q, compare adjacent windows as labeled multisets, counting clamped copies separately. The shared observations with shared ranks q+1 through w−q−1 necessarily survive either insertion. Thus a step direction changes the retained binary-tag count by at most one across an edge. For a cut just before j, only edge indices j−r−1 through j+r−1 can contribute, intersected with the path. Step decomposition and segment integration over ordering chambers, with continuity at ties, give min(w,n−1)/k. For n=w+1, use the even values followed by odd values and perturb the right half positively by ε<1. At left center i the rank of 2j−1 is r+2j−i. The admissible j are the intersection of [1,i] with the integer interval [ceil((i+2−t)/2),floor((i+t)/2)], t=r−q+1. This gives the reported counts and unit successive changes. Reflected counts are k minus the original counts and the two central counts differ by one since the middle k consecutive integers have odd count (k±1)/2. Appending the last value and its step tag preserves the original outputs and denominator. This proves attainment and strict inequality on shorter paths including the mean and median endpoints.

## originality

PASS

Pass for the exact symmetric-trim family and sharp clamped-path onset, not for the classical filter, the already separately covered median endpoint, or the elementary linear mean case. The strongest available comparisons address a single rank or a cyclic special case, not joint selection of the middle k ranks and the shared sharp clamped extremizer. This is a bounded statement-level assessment, not a priority finding.

## value

PASS

Gives the exact perturbation amplification uniformly across the standard robustness continuum from moving mean to median. The overlap lemma explains why averaging adjacent ranks is much better than adding rank-filter norms, while the parity construction and first attainable length identify when the worst amplification is physically possible on a finite path.

The dated certificate retains the supplied scientific assessment, sources and limitations.
