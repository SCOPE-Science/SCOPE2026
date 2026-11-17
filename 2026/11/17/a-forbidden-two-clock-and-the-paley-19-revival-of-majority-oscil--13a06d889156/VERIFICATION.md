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
# Reproducible checks

The finite claims are determined by the explicitly given complete Boolean state space, rather than extrapolating from sampled trajectories.

To reproduce the full orbit census and natural geometric equivalence classes with Python 3, run:

```sh
python3 verify_functional.py
```

The output is a single JSON line and should agree with `output_functional.json`, containing each order's residue set, complete temporal cycle counts, primitive entry-time distribution, sharp transient bound and affine-complement-time classes.

For a second, separately written implementation using individual C bit tests and iterate identities, run:

```sh
cc -std=c11 -O2 -Wall -Wextra -pedantic verify_iterates.c -o verify_iterates
./verify_iterates
```

Its output should agree with `output_iterates.txt`. The C program checks every one of \(8+128+2048+524288=526472\) initial labelled configurations, separately computes minimal temporal periods and first-periodic-entry times, and verifies global iterate identities and their sharpness. The Python verifier independently traverses each functional graph, classifying paths and cycles. Both reconstruct the Paley arcs from quadratic residues instead of reading precomputed transition tables. Together they check that no omitted periods or transient branches remain in the four finite systems.

The general fixed-point and no-two-cycle lemmas are verified through their explicit tournament arc-count proofs in RESULT.md. Finite computational checks are not a replacement for those general arguments. The calculations certify only the specified finite Paley orders, not other prime powers, generic directed networks or an all-order asymptotic theorem.
