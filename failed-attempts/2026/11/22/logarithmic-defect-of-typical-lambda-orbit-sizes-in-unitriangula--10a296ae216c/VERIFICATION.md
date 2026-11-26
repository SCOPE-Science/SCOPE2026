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

The entire group acts by (I+a)B, so the orbit is B+A_nB. The free coefficients in different rows of a are independent; hence the dimension of A_nB is the sum of ranks of rows strictly below each row, omitting the zero last row. Expose suffixes of m=0,…,N potentially nonzero rows from bottom to top. The next row has m+1 coordinates and there are q^(m−d) choices in the existing span for defect d. Defect therefore either stays d or increases to d+1; summing the new defect after each step gives both transfer entries and M−∑D_m for the exponent. The first row is unrestricted. Dividing point counts by q^ℓ gives disjoint orbit counts. Zero exponent forces the suffix to be zero; maximal exponent requires independence at every step, giving q(q−1)^(n−2) maximal orbits, including n=2. For uniform points the defect birth probability is q^(−d−1). The holding time before increment k is geometric with parameter q^(−k). For h=⌊log_q m⌋, completing the holding time for k=h+u by m has probability at most m q^(−h−u)≤q^(1−u); failure to reach k=h−u+1 by m is bounded by E[T_k]/m≤q^(2−u)/(q−1) for k≥1. Summable tails give E|D_m−h|=O_q(1), and the floor-log sum differs from N log_q N by O_q(N). Independence between different suffix ranks is not needed. These arguments work over all prime-power fields. The frozen finite enumeration and output were inspected, not rerun; the q=4 check is transfer-only, not an enumeration over the extension field.

## originality

FAIL

The claimed point-sampled L¹ law is a direct consequence of an already published, stronger finite-dimensional law: the first-column projection of the Borodin transition as stated in Van Peski, Proposition 3.8, gives precisely the whole suffix-defect birth process. The prior exact process, the established left-action row operations, and geometric waiting-time estimates give the stated integrated error, not just the leading quadratic exponent. The failure is based on that explicit implication, not on title similarity with terminal-rank work, the date of another catalogue record, or a claim that the exact displayed inequality was printed before.

## value

PASS

The observable is a natural group-action invariant with genuinely different typical sizes for equal-point and equal-orbit sampling. The explicit n log n deficit and a linear mean absolute error distinguish typical point-sampled orbits from maximal ones much more finely than a leading quadratic law. This is a useful quantitative interpretation, although the earlier exact growth process prevents accepting it as an original theorem on this evidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
