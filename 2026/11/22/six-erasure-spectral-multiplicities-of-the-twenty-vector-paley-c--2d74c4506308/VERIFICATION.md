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

For the exact bordered F19 sign convention, the independent integer replay verified skew-symmetry and all 400 conference-identity entries, and classified all 38,760 unordered six-subsets by four- and six-Pfaffian squares. The six counts in the stated order were 1140, 6840, 13680, 6840, 7980, 2280. The same 1140 masks in the first bin became transitive after switching a designated vertex to a source (remaining outdegrees 0,1,2,3,4). This test is invariant for the switching-transitive class: starting from a transitive order, switching an interior vertex to a source just rotates the two blocks of the other vertices. The largest t for the first cubic is 7+4 sqrt(3); the competing maxima are 6+sqrt(33), a root in (10,11) beyond which its cubic is increasing, 5+2 sqrt(5), 7 and 9. The Parseval normalization and equality of nonzero Gram and erased-vector operator spectra give the claimed sharp positive surviving bound and sharp error. The replay is /workspace/branches/3a261c25-3a71-4d81-8d52-bdf2b142412e/replay_six.py (full_run.txt in the same directory); the supplied trace/Bareiss, matching-Pfaffian and universal-sign scripts were inspected, not executed. No conclusion about optimality among frames is needed.

## originality

PASS

Best of knowledge, the supported distinct result is the joint characteristic-polynomial multiplicity table on labeled six-subsets of this Paley order, including the exact count of worst masks. Credit prior coverage of the construction and the universal list of six possible polynomials. Comparing the roots of that list and converting a principal spectrum into a sharp error are deductions once the maximizing type is known to occur; the originality case is not those deductions in isolation.

## value

PASS

The explicit Paley conference frame is a standard structured benchmark; principal Gram spectra determine robustness under a natural family of erasures. A complete distribution over equally likely six-erasures gives the full discrete loss distribution, the exact frequency of worst cases, and a structural test for them, information not delivered by a worst-case bound or an arbitrary-six-matrix possibility list. This is a useful exact classification of the fixed frame rather than a new universal frame theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
