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

# Reproduction and evidence

Run `python3 verify.py` with Python 3 and the standard library. The checker enumerates all \(\sum_{n=2}^{7}n^{n-2}=18248\) labelled trees via a bijective Prüfer-sequence decoder. It computes distance-pair polynomials for every possible vaccinated vertex; for each tree it finds a maximum-degree vertex whose pair-count polynomial is no larger than every competitor in the exact Bernstein coefficient order on \([0,1]\). It verifies the explicit eight-vertex polynomial comparisons as well.

An independent exact `fractions.Fraction` route enumerates each of the \(2^7\) bond states, computes surviving open-component squared-size sums, and compares the resulting mean outbreak size with the distance method for all eight targets at \(p\in\{1/5,1/2,3/4,9/10,1\}\), totalling 40 comparisons. The finite state tests corroborate but are not used as proof of the continuum in \(p\); that continuum follows from the explicit polynomial identity, monotonic root equation, and nonnegative Bernstein representations. The solver uses no downloaded paper, network service, unrecorded input, randomness, or third-party package.

Scientific limits: no classification of all eight-vertex trees, no assertion about the optimal locations on general graphs with cycles, no multi-vaccine/heterogeneous-edge result, and no assertion of historically certified priority. The independent scientific audit channel has not been performed.
