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

# Reproducible verification

Run `python3 CHECKER.py` using Python 3.8 or newer. The checker uses only the Python standard library, creates the exact colored independent-set faces, reduces them to simultaneous three-color-rotation orbits, verifies that every nonempty face orbit has three distinct representatives, and constructs oriented integer quotient boundary matrices. It verifies the integer chain identities \(\partial^2=0\), computes boundary ranks by exact modular Gaussian elimination for the primes \(2\), \(3\), and \(5\), and compares each resulting reduced Betti vector with the integer-homology theorem and the universal coefficient theorem.

The checked values are every \(m=4,5,6,7,8,9\); the accompanying `VERIFICATION_OUTPUT.txt` records the exact observed orbit counts and mod-three Betti vectors. Each mod-two and mod-five check also passed. The final program line is `ALL_CHECKS_PASS m=4..9: free simplex orbits, integer d^2=0, finite field ranks`.

The all-length proof is mathematical and uses the known homotopy type of the cover, freeness, the integral cyclic-group spectral sequence, and the exact transgression argument. The finite checker does not compute integral Smith forms in all degrees and cannot independently certify exact orders of all torsion groups or the unrestricted range. The formula and the order-three assertion are proved using the spectral sequence, not inferred from finite computations or from modular ranks alone. Independent mathematical audit has not been performed.
