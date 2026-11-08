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

# Exact finite verification

Run `python3 verify.py` in the directory containing `morse_pairs.json`. This requires only Python's standard library. The embedded `verification_output.txt` records a successful execution.

The verifier reconstructs the ten-vertex, fifteen-edge Kneser graph \(KG(5,2)\); enumerates its 210 four-vertex subsets into 70 connected and 140 disconnected ones; independently compares two complete face-membership procedures across all 1,024 vertex subsets; and checks the 766 faces and the exact face vector.

It checks that twelve missing five-vertex faces are exactly complements of induced pentagons. It compares the complete ordered 369-pair Morse matching and the 27 critical cells with the literal masks in `morse_pairs.json`. It independently constructs the 3,330 directed Hasse incidences and confirms acyclicity by visiting all 765 nonempty faces. A reversed vertex-order construction is separately checked for acyclicity and the same critical-cell dimensions.

A separate mod-two simplicial boundary calculation gives ranks \((9,36,84,126,114)\) in dimensions one through five, agreeing with the integral Morse homotopy result. Exact signed oriented-simplex traces over each of the 120 natural graph automorphisms produce a seven-class character, and rational irreducible multiplicities are computed using a finite Frobenius coefficient formula.

The integral homotopy classification relies on the acyclic Morse matching and Forman's CW theorem; finite mod-two ranks alone would not prove the torsion-free or integral homotopy conclusions. The character calculation is a rational statement only. These checks are exhaustive for the specified finite complex, not a proof of the behavior of larger graphs. No independent external audit has been performed.
