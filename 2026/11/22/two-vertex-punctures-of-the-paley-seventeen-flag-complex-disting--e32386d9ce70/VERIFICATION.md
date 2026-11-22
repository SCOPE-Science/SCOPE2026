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

# Verification
Run the included Python 3 standard-library program from the directory containing its companion expected-output file:

```
python3 verify_paley17_pair.py > observed.json
cmp observed.json expected_output.json
```

The expected output is a one-line JSON object followed by one LF. The program reconstructs the graph from its square-residue rule. It verifies all two-point deletion faces and both full directed-Hasse matching acyclicity certificates, with no sampling, timeout-based inference or floating-point computation. It also checks the once-punctured and full-complex certificates required for the inclusion, verifies the two links are connected with cycle ranks three and five, and maps each of the 136 unordered vertex pairs to an adjacency-class representative under a verified graph automorphism.

The verified finite theorem depends on the accuracy of the specified graph and the standard discrete Morse and relative homology theorems. The checker is not an externally certified independent audit. The complete proof and its scope are in `RESULT.md`; the output records exact finite premises, not independent priority verification.
