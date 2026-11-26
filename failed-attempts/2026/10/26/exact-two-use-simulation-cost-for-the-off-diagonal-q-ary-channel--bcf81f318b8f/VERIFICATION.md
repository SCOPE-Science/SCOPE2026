---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Conditioning on the common seed gives a deterministic image of size at most M. Exact support on each of finitely many input rows forces this image to meet every allowed output row for almost every seed simultaneously. Two outputs y,z cannot suffice: choose x=(y_1,z_2), which excludes them both; the written Hamming-distance intersection count additionally gives the sharp maximum two-output cover q^2-2. Three distinct diagonal symbols give a support cover when q>=3, and independent coordinate permutations followed by the equivariant tie-break give invariant probabilities over the whole allowed row, because the stabilizer of that input acts transitively there. For q=2 the target is a deterministic bijection, so almost every seed (not literally every seed on an arbitrary null set) needs all four outputs; four messages work. An independently written exact check, /workspace/review_evidence/5_exact_counts.py, verifies the maximum two-output cover for q=2..6, the binary bijection, and integer-weight uniformity of the proposed simulator for all input rows at q=3,4 and two representative rows at q=5,6. The group argument, not those finite checks, establishes exactness for all q.

## originality

FAIL

The exact numbers are a mechanical specialization of the known shared-randomness simulation support/covariance method to a graph minimum already covered by distinct indexed work. No claim about publication order between same-day records is made; earlier primary work identifies the exact off-diagonal NOT channel and uses the same support and twirling argument for it, and the graph computation adds only the elementary row-column obstruction and three-cell matching.

## value

FAIL

The exact finite-block simulation quantity is natural, but this instance adds only a symmetrization already used for the same one-use channel and an elementary, independently covered support minimum. No additional meaningful threshold or novel simulation phenomenon survives that reduction. No substantive repair of this finding is supported.

The dated certificate retains the supplied scientific assessment, sources and limitations.
