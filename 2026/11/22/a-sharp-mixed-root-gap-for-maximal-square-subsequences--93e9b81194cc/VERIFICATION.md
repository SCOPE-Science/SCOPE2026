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

# Verification record

Run with standard Python 3 in a directory containing the four checker and output files:

```bash
python3 check_exhaustive.py
python3 check_extension.py
```

`check_exhaustive.py` enumerates every binary host of length zero through seven and all binary candidate root words of allowable length, tests literal ordered-square membership by greedy embedding, and uses root subsequence containment to test maximality. Its complete census gives zero qualifying hosts for lengths zero through six, exactly eight at seven, and two four-element reversal/complementation orbits. The complete observed stdout is `check_exhaustive.txt`.

`check_extension.py` independently constructs square roots as common subsequences across every host split, then tests maximality by adding one symbol in all possible root positions, relying on the elementary one-letter extension criterion. Its complete length-two-through-seven census agrees exactly. For \(3\le m\le40\) it verifies `1010` embeds in \(W_m\), that `10` has no valid one-letter extension, and that \(0^{2m}\) embeds; for \(3\le m\le8\), it exhaustively enumerates all square roots and verifies that maximum root length is \(m\). The complete observed stdout is `check_extension.txt`.

Both programs were executed from their actual source files, with their output files produced afresh and compared to independent expected values. The all-integer family is justified by the central-gap proof, not by extrapolating from finite tests. No external independent audit has been performed.
