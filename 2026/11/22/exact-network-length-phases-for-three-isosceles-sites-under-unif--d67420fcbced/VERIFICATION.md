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

# Reproducibility and exact scope

Run `python3 verify_mdm.py` from the directory containing the packaged files. This standalone Python 3 program uses only the standard library. A successful run prints `THREE_SITE_MDM_OK 644 formula_and_disk_projection_cases; 20 two_dimensional_grid_checks`.

The checker evaluates both the interval-clamped formula and the piecewise phase diagram for specified height-radius boundary cases and 500 seeded continuous parameter pairs, tests that the proposed disk-projection spokes attain the sum of point-to-disk distances, and independently samples two-dimensional junction locations for 20 further cases. An exploratory independent SciPy differential-evolution check previously matched 200 random cases to within \(8\times10^{-11}\), but that optional external optimizer is not needed to replay the packaged verifier.

These are finite computational checks, not a proof for all real parameters. The analytic certificate is the unrestricted three-terminal network-to-disks reduction; convexity plus reflection; a sign-controlled one-dimensional derivative; and the exact minimum-enclosing-disk threshold. Critical hypotheses are the Euclidean plane, three sites, equal tolerance \(r\), and target height \(h>0\).

The computations do not establish uniqueness of every optimal connected set and do not search all prior literature. Independent mathematical review has not been performed.
