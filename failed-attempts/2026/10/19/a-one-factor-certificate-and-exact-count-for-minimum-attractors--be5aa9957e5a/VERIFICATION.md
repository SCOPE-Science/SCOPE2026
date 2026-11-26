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

FAIL

The minimum size, forbidden tuples, sufficiency of the stated certificate, and enumeration are correct. Each length-one factor forces one selected copy; the start residue of any longer factor is fixed. Nonwrapping short factors cover every copy of their last letter. For a wrapping short factor, missing it requires the right wrap to exceed the suffix length, forcing the three forbidden restrictions from the copies in its occurrence intervals. For length at least q, the occurrence intervals touch or overlap, leaving initial and final gaps each shorter than q; a missing factor must leave the last a_{q-1} in the final gap and the first a_r in the initial gap. The other restricted letters can only be chosen in the first block or the final suffix. The displayed certificate has exactly these restrictions and the count follows by independent choices. But the Finding also calls it the unique distinguishing factor without qualification. For q=2,k=3,r=0, in ababab both ba and baba have the same union of occurrence spans, positions 1 through 4 in zero-based indexing. Either is a sufficient single-factor test, and only neither is hit by the bad selection {0,5}. The frozen finite script checks the displayed test and count, not the claimed uniqueness; its reported run is not an independent replay.

## originality

FAIL

A distinct Resultary record states the full classification and count, with the same one-factor certificate and all truncated-prefix cases. The mathematical coverage is exact, irrespective of historical priority. Removing the uniqueness overstatement would not recover a distinct result.

## value

FAIL

The classification would be a useful structural result on its own, but here the certificate and truncated count reproduce an existing indexed theorem; the extra uniqueness wording is false. No independent mathematical gain survives in the frozen contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
