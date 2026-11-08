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

# Verification evidence and limits

Run the standalone verification programs with Python 3 from this directory:

```text
python3 verify_morse.py
python3 verify_mod2.py
```

The recorded complete outputs are `morse_output.txt` and `mod2_output.txt`. The first program checks the cube-edge definition, every edge subset against two matching-number algorithms, face counts, fixed pivot pairings, exactly enumerated Hasse covers, critical cell dimensions, and directed acyclicity. The second uses an independent vertex-based recurrence and full simplicial boundary reduction over \(\mathbb F_2\). The terminal markers `ALL_CHECKS_PASS` and `INDEPENDENT_MOD2_CHECKS_PASS` are emitted only on successful completion of all assertions. Every attempted finite computation is exhaustive over its stated finite domain.

The integral sphere-wedge conclusion uses the discrete-Morse acyclic matching and unique remaining critical cell dimensions. Finite-field ranks alone would not prove integral homotopy or rule out torsion. This proof does not classify other hypercubes, all crown graphs, or graph-automorphism actions; no external independent audit has been performed.
