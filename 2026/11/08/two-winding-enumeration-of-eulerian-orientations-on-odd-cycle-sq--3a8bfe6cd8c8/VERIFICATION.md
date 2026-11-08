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

# Reproduction and limitations

The mathematical claim is the odd-order, two-variable enumeration in `RESULT.md`. It is proved there by a bijection from balanced orientations to closed eight-state walks, exact decomposition of that automaton, a three-by-three characteristic-polynomial computation in each nonconstant sector, and the standard second-order power-sum identity. The proof covers every odd integer \(n\ge5\) without using empirical extrapolation.

Run from the directory containing the extracted files:
```
python3 -S verify_direct.py
python3 -S verify_transfer.py
```
Both scripts use only Python's standard library. `verify_direct.py` constructs every edge of each squared cycle and exhaustively tests every orientation for \(n=5,6,7,8,9\); for each balanced orientation it records counts of forward one-step and two-step edges and compares the complete coefficient dictionary to the exact formula. `verify_transfer.py` reconstructs the local eight-state transition system independently and compares the complete weighted trace polynomials with the formula for \(n=5,\ldots,15\). Recorded outputs are in `verify_direct.out` and `verify_transfer.out`, and both programs returned status zero when run on the packaged source contents.

These are finite verification tests only. Their rigor for the infinite odd family depends on the symbolic automaton proof, not the list of tested \(n\). The theorem does not assert novelty of the even-case scalar count or necessarily the odd-case scalar specialization. An inaccessible 2007 circulant-orientation article and a cited extended 2004 technical report remain literature-priority risks; no independent scholarly audit has been performed.
