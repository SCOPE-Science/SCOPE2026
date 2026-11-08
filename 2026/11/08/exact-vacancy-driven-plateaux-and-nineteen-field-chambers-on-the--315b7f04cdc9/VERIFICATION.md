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

The bundle specifies the labelled icosahedral graph in `edges.csv`, the complete sector minima in `sector_minima.csv`, the nineteen open-sector energies in `open_chambers.csv`, thirty exact convex-dominance witnesses in `domination_certificates.json`, and nineteen strict rational exposure witnesses in `open_chamber_witnesses.json`.

Run `python3 verify_direct.py` and `python3 verify_transfer.py` from this directory using only the Python 3 standard library. The first check exhausts \(3^{12}=531441\) classical assignments and verifies exact rational comparisons. The second performs a separate upper/lower pentagon-shell contraction and reproduces all forty-nine sector minima and multiplicities. Both were executed successfully against the complete bundled data and printed `VERIFY_OK`.

The coverage is exact for the stated finite classical model at zero temperature and any real crystal field or longitudinal magnetic field. No quantum spectral or positive-temperature property is checked. No independent external audit has been performed.
