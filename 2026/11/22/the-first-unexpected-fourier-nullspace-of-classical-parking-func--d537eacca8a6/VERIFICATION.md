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

# Exact reproducibility

From this package directory execute `python3 verify.py`. The program requires only Python 3's standard library. It independently simulates all preference words with one through five car slots where tested, checks the Pollak transversal property for lengths 2 through 5, and enumerates all 252 unordered frequency multisets at length 5. For each multiset, residue counts of 1296 parking functions are computed directly, then divided by the integer polynomial \(\Phi_6(X)=1-X+X^2\). The zero test is exact and weighted by character-orbit multiplicities.

The output is reproduced verbatim in `verification_output.txt`. Expected five-car figures: 46 vanishing multiset orbits, 1295 forced zero characters, 360 unexpected zero characters in five coordinate-multiset classes, 6121 nonzero Fourier characters. The proof for all sizes of the forced-zero lower bound uses Pollak's lemma, not a computational extrapolation. The complete Fourier classification is limited to at most five cars.

The supplied verifier provides an exhaustive finite certificate for the stated cutoff; it is not an external audit.
