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

# Verification scope
Two independent standalone standard-library Python programs accompany this result. Run `python3 direct_dynamics.py` and `python3 cycle_and_transfer.py` in a directory containing the extracted files. The outputs are embedded as `direct_dynamics_output.txt` and `cycle_and_transfer_output.txt`.

The first program constructs each full labelled state transition graph implicitly, follows trajectories to their recurrent cycles, and computes the exact rational per-vertex CCA and GHM long-run activity. The second enumerates all graph simple cycles independently of the update implementation and obtains the maximum signed CCA contour mean, then independently computes the finite transfer-matrix counts. Both check all stated populations for rim sizes 5–8. This is corroborative finite evidence only. The proof of the all-size claim relies on the cited cycle-mean theorem, the stated fundamental-cycle reduction, and the transfer calculation.

Direct model enumeration: 29,160 labelled configurations for each of CCA and GHM, rim sizes 5–8. Independent simple-cycle enumeration: 57,591 labelled configurations across both edge-placement families, with transfer recurrence checked through rim size 30. Exact arithmetic is used for cycle means and population formulas. There is no third-party certification or independent scientific audit.
