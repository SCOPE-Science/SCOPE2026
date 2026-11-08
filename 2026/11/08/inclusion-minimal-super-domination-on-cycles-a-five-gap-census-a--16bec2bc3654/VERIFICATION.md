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

# Reproduction and scope

Run `python3 verify.py` using the standard library. The program independently tests the private-neighbor graph definition on every vertex subset of every cycle of order \(3\) through \(19\). It compares those complete cardinality distributions with (i) coefficients of the rational formal series and (ii) an independent rooted-gap transfer enumeration through order \(45\). It also checks exact upper cardinalities through order \(154\), including the seven rotations when \(7\mid n\).

An observed successful execution printed:

`VERIFY_OK direct_graph_n=3..19 subsets=1048568 minimal_sets=3874 rational_coefficients_n=3..154 upper_quasiperiodic=PASS extremal_seven=PASS`

The statement for arbitrary order is justified by the cyclic-gap proof and nonnegative deficit decomposition in `RESULT.md`, not by extrapolation from finite checks. The package includes no independent mathematical audit or infinite machine-generated certification.
