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
# Reproducibility and scope

Run `python3 verify_q7.py` with a standard Python interpreter; the script has no dependencies beyond the standard library. It regenerates all four kernel arrays from fixed SHA-256 counter streams, constructs the exact \(2401\times2499\) differential in \(\mathbb F_8\), checks the full orbit coverage and independently compares selected entries to direct polynomial finite differences, and obtains full rank \(2401\) with nonzero residues \(1,6,6,1\). The stored pivot-column and parameter hashes disambiguate the witness points and minors. Computational outputs are exact; no real or complex floating-point approximations occur.

The significance of the finite-field calculations is nonvanishing of four minors in the cyclotomic coefficient ring \(\mathbb Z[\zeta_7]\). The ring map \(\zeta_7\mapsto\alpha\in\mathbb F_8\) and complex embedding lift nonzero residues to nonzero characteristic-zero determinants. Full Jacobian rank implies dominance; the independent scaling dimension bound makes seventeen minimal. Any repeat run with a failed assertion invalidates this certificate.

This check does not certify all individual decompositions, any worst-case bound at seventeen, the geometry over characteristic two, or numerical stability. Independent mathematical audit has not been performed.
