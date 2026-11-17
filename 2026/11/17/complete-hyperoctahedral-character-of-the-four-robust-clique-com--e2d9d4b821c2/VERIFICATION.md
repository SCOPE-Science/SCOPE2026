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

# Exact verification procedure

Run `python3 verify.py` with Python 3 and the adjacent file `certificate.json`. No nonstandard libraries, network services or externally generated certificates are required. The script reconstructs all 16-vertex subsets and independently checks robust-clique face membership via both forbidden independent quadruples and an induced-independence-number recurrence. It then constructs the complete sequential face matching, reverses its matched Hasse covers and topologically sorts all 6,864 nodes and 33,152 covers. It verifies a critical-cell census of one vertex and 529 five-cells.

Next it constructs all 384 cube automorphisms, performs the exact signed orbit-face Lefschetz sums, repeats every trace through the complementary total four-cut face test and groups the answers into all 20 signed-cycle classes. Finally it computes the 16 translation Fourier multiplicities, verifies their five weight values, checks the 529-dimensional total and calculates invariant ranks 27, 24 and 0 for translations, coordinate permutations and the full group. It compares every recorded value and the full matched-pair digest against `certificate.json`, then prints `VERIFY_OK`. The observed output is in `VERIFIER_OUTPUT.txt`.

The main homotopy assertion is justified by a finite exhaustive discrete-Morse construction. The character is a rational homology character; the program does not compute an integral group-module isomorphism or the homology torsion of quotient spaces. The verifier is reproducibility evidence, not an independent external audit.
