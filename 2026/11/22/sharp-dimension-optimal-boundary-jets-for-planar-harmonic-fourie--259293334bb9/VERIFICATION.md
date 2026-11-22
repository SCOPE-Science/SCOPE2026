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

# Reproducibility and verification

The local self-contained Python checker uses standard-library `fractions.Fraction` elimination for exact integer Fourier-alias block ranks and separate numerical complex-matrix elimination for the full unreduced circle-jet matrix. Execute `python checker.py` next to the other embedded files. The output was `PASS 10514 exact-block/complex-matrix assertions`.

The checked finite ranges are \(0\le k\le4\), \(0\le L\le16\), \(1\le M\le14\) for exact block ranks and the sharp threshold, and \(0\le k\le3\), \(0\le L\le8\), \(1\le M\le11\) for independent unreduced complex jet ranks. The full mathematical proof does not depend on this finite coverage: it uses root-of-unity Fourier orthogonality, falling-factorial Vandermonde ranks, and arithmetic bounds on residue-class counts.

The stated rank and minimal-node properties are exact but do not provide uniform singular-value lower bounds or numerical conditioning. The sampling data are complete noiseless harmonic jets at points on a nonzero-radius circle.
