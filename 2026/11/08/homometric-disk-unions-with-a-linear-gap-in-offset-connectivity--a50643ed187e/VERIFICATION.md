---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and limitations

The complete proof is in `RESULT.md`; no unproved general lemma is needed. Run the standalone arithmetic checker with `python3 checker.py`. It verifies the signed-multiset identity for the explicit base configuration, all positive and negative coefficients, pairwise center separation, and the connectivity gap for 61 values of \(m\) up to \(200\), including rational offset radii with enlarged-disk radius strictly between \(3\) and \(7/2\). Expected terminal output: `HOMOMETRIC_DISK_OFFSET_LINEAR_COMPONENT_GAP_OK 61`.

The statement for all positive integers \(m\) rests on the exact convolution identity; finitely many checks are only regression tests. Continuous covariogram equality follows by indicator convolution, which is valid because the component disks have disjoint interiors. The elementary gap criterion is exact for collinear disk centers. Its strict endpoint limitations are encoded in the statement. A geometric counterexample to reconstruction is not a uniqueness theorem; prior-art comparisons are necessarily finite and subject to historical uncertainty. No independent mathematical audit has been performed.
