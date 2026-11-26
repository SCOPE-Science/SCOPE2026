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

The synchronous edge phase update is an exact coboundary: if the old oriented edge difference is +1, the head cannot advance more than the tail; reversal and the zero case finish the check. Thus extinction forces zero cycle circulation. Conversely the integral lift is monotone and bounded by the first multiple of three above its initial maximum: a site at that bound cannot have an excited neighbor. Stationarity then forces all phases to be resting. The open-ladder squares form an integral basis (face boundaries generate, or eliminate successive rail edges). Independently count extensions in the lift by setting the old rung increment to s in {0, +/-1}: new rail increments u,v each lie in {-1,0,1}, and the next rung increment is s+v-u in that same set. The counts of zero/nonzero next increments are (3,4) for s=0 and (2,4) for either nonzero s. Initial multiplicities are 3 and 6, so the trace and determinant of the reduced transfer are 7 and 4, with counts 9 and 57. These give the stated numerator, roots, and leading constant with the stated normalization by 9^n. A fresh reverse-reachability calculation on the full finite state graphs yielded 9, 57, 363, 2313, 14739 for n=1 through 5 (python3 /workspace/review_checks.py). The supplied verifier and recorded output were inspected, not executed. The finite check is not the infinite proof.

## originality

FAIL

A distinct indexed result gives exactly the extinction count as the zero-rate member of its three-rate population census for the same labeled open ladders and the same deterministic GHM rule. Its catalogue date is later than the frozen record's; the decision is equivalent coverage in the inspected corpus, not a finding of earlier publication or an allegation about provenance. The generic graph criteria and the same-day circular-ladder result do not by themselves establish this overlap.

## value

FAIL

The initial-condition extinction probability is a natural statistic, and its exact boundary transfer would be meaningful in isolation. As a distinct finding against the available corpus, however, this is entirely the zero-rate slice of the broader exact population census; the prefactor is a routine consequence of its already supplied recurrence. No new boundary case, invariant, or independently useful uncovered conclusion survives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
