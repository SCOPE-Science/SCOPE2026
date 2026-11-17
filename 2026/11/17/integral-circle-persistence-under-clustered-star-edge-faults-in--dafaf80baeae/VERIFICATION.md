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

# Verification details

Run the accompanying standalone Python 3 program from a directory containing `verify.py`:

```sh
python3 verify.py
```

The accompanying `verification_output.txt` was produced by that command. It reports the exact marker `STAR_DELETION_2_INDEPENDENCE_PASS cases= 72` and selected complete parameter profiles.

For every \(2\le a,b\le5\), \(0\le t\le b\), the program constructs the graph from the deleted-star edge set, evaluates all \(2^{a+b}\) vertex subsets by the *original induced-degree definition*, independently classifies the faces by shoreline cases, and verifies that the two resulting face sets coincide. It then checks the unique-coface condition for all \((a-1)t\) explicit elementary collapse pairs, checks the exact residual core-edge decomposition, constructs the entire mod-two simplicial chain boundary in every degree, and calculates reduced Betti ranks over \(\mathbb F_2\). Each checked case agrees with the claimed circle multiplicity and has zero other reduced Betti ranks.

All-parameter integral correctness rests on the complete face classification, the explicit elementary collapses, the contractible-core gluing argument, and the integral one-cycle basis proved in `RESULT.md`. Mod-two computations cannot rule out integral torsion and are not used as the only proof. The displayed homotopy classification proves torsion-freeness independently. The script does not check an infinite domain or establish bibliographic priority. Independent audit remains unperformed.
