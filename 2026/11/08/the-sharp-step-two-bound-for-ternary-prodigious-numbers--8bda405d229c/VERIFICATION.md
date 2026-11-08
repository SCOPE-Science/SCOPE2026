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

# Verification and limits

The theorem is an exact modular statement. The three-digit suffix list \(\{8,17,20,23,24,25,26\}\pmod{27}\), together with \(n\equiv2\pmod4\), gives the seven forbidden classes modulo \(108\). The forbidden positions in a step-\(2\) cycle of even residues are \(13,25,31,37,39,49,53\) modulo \(54\). Their cyclic gaps have maximum \(14\), so no \(14\) consecutive even terms are all valid. For odd terms, the two-digit residue set \(\{0,1,3,4\}\pmod9\) has no three-step-\(2\) run. Both arguments cover all positive starting values.

To reproduce the finite calculations from the local extracted package, run `python3 check_prodigious.py` and compare its stdout with `check_output.json`. No libraries beyond the Python standard library are required. The script checks the exact seven-class residue list, every one of the \(54\) cyclic even starts, the \(9\) possible odd residues, the witness, and a finite selection of the infinite family. A scan up to \(200000\) is corroborative only and is not used to prove the universal upper bound. No independent scientific audit has been performed.
