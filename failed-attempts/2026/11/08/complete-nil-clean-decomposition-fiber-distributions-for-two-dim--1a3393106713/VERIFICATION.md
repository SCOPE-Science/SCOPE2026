---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Trace of 2x2 idempotent equals rank, and trace-zero/determinant-zero characterize nilpotents. Rank-one projections indexed by complementary lines give q+1-e(A)+q e_{1-d}(A) for trace-one A. Evaluating its characteristic polynomial at 1-d gives d^2, so correction only at d=0. Standard GL2 centralizer sizes yield every displayed split/irreducible/Jordan stratum; q=2 coincident bins are added. Independently enumerated every idempotent and decomposition over F2,F3,F5 and all matrices, reproducing exact histograms and maximum. Infinite all-prime-power statement comes from projective-line proof and class enumeration.

## originality

FAIL

FAIL decisively: previously published October 13 Resultary theorem Exact nil-clean decomposition multiplicities in 2x2 finite-field matrix rings gives for identical A and all prime powers the EXACT elementwise formula ν(A)=1_{A nilpotent}+1_{A-I nilpotent}+1_{tr A=1}(q+1-e(A)+q1_{det A=0}) and the same finite-field locus, plus a complete trace-one class-by-class table. Combining its stated q^2 nilpotent and I+nilpotent classes with that table gives ALL bins of the submitted histogram, including q=2 collision, with no new combinatorics. This is directly prior mathematical coverage, not merely an overlapping maximum or an alias. No disclaimer or verification can rescue originality of the original full claim.

## value

PASS

The finite-field nil-clean multiplicity distribution is a natural elementwise ring-theoretic invariant: its full decomposition fibers stratify the matrix algebra by eigenline geometry and determine the nil-clean locus and sharp index. Motivated and mathematically useful but already established, so originality fails independently of correctness and value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
