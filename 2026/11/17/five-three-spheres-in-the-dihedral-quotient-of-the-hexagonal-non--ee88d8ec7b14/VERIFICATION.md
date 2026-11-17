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

# Reproducible verification

The package includes `verify_nc6.py` and requires no extra mathematical software. Running `python3 verify_nc6.py` produces a successful `PASS` only after checking all \(132\) noncrossing partitions, \(130\) proper partitions, \(4621\) original chains and the full \(12\)-element dihedral action. It checks the \((22,114,204,116)\) quotient cell numbers both by canonicalized orbits and by Burnside sums. It constructs signed integral boundary maps directly from oriented orbit chains, asserts \(\partial^2=0\) in all degrees, and performs \((21,93,111)\) unit cancellations to reach residual chain ranks \((1,0,0,5)\) with no nonzero differential.

The code does not assert that chain cancellations are simplicial collapses; its output establishes integral homology. The stated homotopy type additionally follows from the shellability theorem for the labeled complex, Armstrong's orbit-space fundamental-group theorem, and Hurewicz–Whitehead, with the fixed-reflection witnesses described in the proof. These steps are susceptible to ordinary mathematical review and have not been independently audited. No computations or deductions for other polygon sizes are asserted.
