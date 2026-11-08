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

# Verification and reproducibility

The analytic proof classifies recurrent states by Dhar burning, constructs explicit reduced-Laplacian odometers, invokes uniqueness of recurrent representatives and counts the nine gate/local-state types. Its validity for all integer \(k\ge2\) does not depend on finite enumeration.

Two standalone, standard-library Python scripts provide independent finite corroboration. Run `python check_exhaustive.py` to enumerate all stable sandpiles, apply a direct burning test, and stabilize by sequential greedy topplings. It checks the complete joint \((T,L)\) histogram for \(1\le k\le7\), including \(30{,}618\) additions at \(k=7\). Run `python check_templates.py` to enumerate only the analytic product states and perform parallel-wave topplings against the theorem's individual gate/local-state cases for \(1\le k\le8\), including \(104{,}976\) additions at \(k=8\). Both were executed successfully from the source package.

The programs are finite independent computational checks, not formal certificates for arbitrary \(k\) or external validation. Verification does not prove priority in sources not inspected. The joint polynomial uses total individual topplings and number of grains absorbed, not number of toppled vertices or wave counts.
