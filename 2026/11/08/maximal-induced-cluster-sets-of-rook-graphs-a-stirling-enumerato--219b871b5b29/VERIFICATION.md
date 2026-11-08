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

# Verification record

The standalone file `verify_cluster_rook.py` uses only the Python standard library. It identifies the literal forbidden induced \(P_3\) patterns as all three-corner selections of \(2\)-by-\(2\) rectangles and builds the valid-set table by adding individual selected cells. Maximality is checked by testing all missing cells against that table, independently of the star-forest classification. Its separate `formula` function counts component classes via the recurrence for associated Stirling numbers.

Execution: `python3 verify_cluster_rook.py`.

Observed output:

`VERIFY_OK instances=14 examined_subsets=1152910 cluster_sets=9545 maximal_sets=1539 all_coefficients=PASS rectangular_spectra=PASS`

The exhaustive finite range consists of all \(1\le m\le4\), \(m\le n\le5\), and \(mn\le20\), for a total of 14 instances. The exact rectangular spectra were separately checked for \(2\le m\le8\) and \(2m\le n\le4m\). Integer arithmetic is exact. The finite checks are not a proof for all orders; the analytic star-forest trichotomy, counting argument and realization construction supply the unrestricted proof. Independent audit status: not performed.
