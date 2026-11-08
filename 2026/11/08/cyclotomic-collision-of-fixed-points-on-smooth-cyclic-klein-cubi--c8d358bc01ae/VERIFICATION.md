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

# Verification and limits

The self-contained mathematical proof in `RESULT.md` establishes the integral fixed-scheme identity and smoothness for every prime \(p\ge5\). The decisive equalizer calculation reduces all projective fixed points to the chart \(X_0=1\), where the coordinate cycle imposes \(X_i=\lambda^i\), \(\lambda^p=1\). Substituting into the cubic gives \(\Phi_p(\lambda)\); this equality is checked in the quotient by \(\lambda^p-1\), and is not an inference from a finite sample.

The supplied file `verify_klein_cyclic.py` is an optional Python 3 standard-library regression program. It was run for primes \(5,7,11,13,17,19\). The accompanying `verify_klein_cyclic.out` records checks of the residue-permutation identity, Eisenstein coefficient divisibility, special-fiber local polynomial, nonzero special gradient, and powers of the cyclic Jordan operator; the final line is `VERIFY_OK`. Reproduction command: `python3 verify_klein_cyclic.py`.

No exhaustive computational classification over all primes is claimed. In particular, sampled finite-field identities cannot by themselves establish an infinite-prime theorem, and rank checks of the ambient permutation operator do not by themselves certify the projective tangent quotient. Both general claims are proved symbolically in `RESULT.md`.

The complete automorphism-group scheme and quotient geometry are not assessed. Independent validation is not performed.
