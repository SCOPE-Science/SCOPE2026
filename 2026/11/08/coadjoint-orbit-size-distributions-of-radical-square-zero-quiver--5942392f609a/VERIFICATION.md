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

# Reproduction and limits

Run the three included standalone Python scripts from the same directory, without external packages:

```
python verify_orbits.py
python verify_gf4.py
python verify_tutte.py
```

The first script independently builds coadjoint orbits under explicit group generators over the prime fields of orders two and three for loops, parallel arrows, chains, cycles, and disconnected/empty graphs. The second constructs arithmetic in the degree-two extension field of order four and repeats independent orbit enumeration. The third uses a deletion--contraction Tutte recurrence that is separate from its spanning-subgraph enumeration. Full recorded standard outputs appear in `verification_output.txt`; each script ends with an `ALL_..._PASS` marker when its assertions succeed.

These are finite cross-checks. The proof of the general formula rests on the exact semidirect coadjoint action, incidence matrix rank for spanning subgraphs, torus orbit-stabilizer and the Tutte rank expansion. No finite case establishes historical novelty, general-field correctness, a character-theoretic orbit method or an independent audit. Results involving \(\mathbb F_4\) in `verify_tutte.py` are only polynomial evaluations; the extension-field coadjoint action itself is tested by `verify_gf4.py`.
