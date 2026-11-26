---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For a label j≥3, the depth-two indicator depends only on attachment choices through j, and the survival-as-leaf indicator only on later choices. The latter has mean (j−1)/(n−1). The covariance with an earlier root attachment is its Bernoulli variance divided by n−1; the attachment at j is incompatible with depth two and gives the negative term −H_{j−2}/[(j−1)(n−1)]; a later root attachment precludes that arrival choosing j and gives H_{j−2}/[(n−1)(i−1)(i−2)]. The latter terms telescope. Summing over j yields H_m−H_m^(2)−m²/(m+1)² for m=n−2. The forward difference is (m²+m−1)/[(m+1)(m+2)²]>0, with exact values −13/144 at n=5 and 71/3600 at n=6. Standard harmonic asymptotics give the stated constant and growth. The independent attachment-history replay (`python -B /workspace/branches/replay_records_1_3_4_5.py`, section 5) agrees at n=3,…,8, including −1/4 at n=3 and −7/36 at n=4; it is supplemental to the unrestricted proof.

## originality

FAIL

The wider exact Hoppe-tree depth law mechanically supplies this covariance by an exponential tilt in root degree and the independent no-child survival product. There is also a direct reduction to the prior ordinary level covariance and labeled leaf covariance using independence before and after each vertex's birth. No compared source was found to print this exact sign cutoff, but the exact invariant governing it is covered by these implications, not merely suggested by a title or unavailable source.

## value

FAIL

The contrast between a bounded total-leaf covariance and logarithmic depth-two terminal covariance is a natural observation. Here the exact depth-two fact is a direct coefficient, survival factor and derivative of a known finite root-weighted depth law, and the sixth-vertex switch is an elementary evaluation of the resulting harmonic expression. It does not supply a distinct nonroutine invariant as submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
