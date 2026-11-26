---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The denominator is bounded away from zero and real analyticity follows in local real coordinates. Expanding the geometric series, a zero Gram form forces both sets of feature moments to vanish. Grouping by distinct u values, each moment system for k=0,...,r-1 is an invertible Vandermonde system. The sum and height-weighted sum force all coefficients in a fiber to be zero, including the poles as a two-point fiber and equatorial singleton fibers. The two features in degree ell>=1 are nonzero homogeneous harmonic restrictions of distinct azimuthal order and all other degrees are orthogonal. Each therefore has a positive eigenvalue and the orthogonal complement is null. Taking real parts gives the claimed cos/sin directions, with the azimuthal-order-zero v contributing only one in degree one; the real Gram form is positive on real vectors, hence also on complex vectors. The signed measure (3v^2-1)dσ annihilates every feature (and its conjugate), so integration against it kills kernel sections and, by uniform continuity of the functional and the bounded RKHS embedding, the entire RKHS. The proof's phrase 'oddness of h' should read 'oddness of v h'; h is even with mean zero. Removing the height features identifies the two poles, and removing the other features kills every equatorial diagonal. The formal rank and positivity arguments do not depend on check.py; that script was inspected, not run, and its cutoff assertions check dimension inequalities, not spectral ranks.

## originality

PASS

Credit the existing operator and finite-atomic criteria and the material same-day one-mode overlap. The bounded originality decision concerns the specific rational rotation-invariant-under-common-axial-rotation kernel, the two specified complex harmonic directions, and the associated exact real-part comparison, not the existence of a sparse strictly positive definite nonuniversal sphere kernel in general or a sparsity optimum.

## value

PASS

The rational formula gives an elementary, directly evaluable axially symmetric covariance whose exact complex and real harmonic ranks can both be read off and whose finite interpolation and non-universality are explicit. This remains useful as a closed-form witness, not as a claim to outperform the same-day one-mode construction on rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.
