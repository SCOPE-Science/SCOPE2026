---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Independent exact diagonalization verifies the whole open parameter domain. The Ritz gap is au+δ(1−u)>0 and the positive Nyström eigenvalues are the squared norms of Aq_i divided by the respective Ritz values: 1−δ_c and 1−δ. Their eigenvectors are orthogonal, giving the two branches, a two-dimensional top eigenspace at equality, and the stated errors (uniqueness means up to sign). Since b_1>a, 0<δ_c<(1−a)u<1−a, so both branches actually occur. The cross-Gram with span(e_1,e_3) is √(1−u)I. For a=1/2 and δ=u/8 the errors are u/8 and u/2 for the extracted leading eigenvalues, while the two vector sine errors are 1 and √u. The true top gap closes in the limit; the toy family is not a fixed-gap counterexample. Frozen verify.py was inspected, not executed; its finite rational checks are supplementary, not the basis of the verdict.

## originality

PASS

The qualitative caveat about individual vectors and the ordered eigenvalue improvement are prior. What survives is the explicit two-leakage family, the exact crossing surface and tie, and a simultaneous strict quantitative advantage in eigenvalue error with maximal individual-vector error. No equivalent exact comparison or stronger covering result was found in the inspected material; priority is provisional.

## value

PASS

A simple exact witness answers a live extraction question that the known subspace comparisons leave open. The crossing occurs on a sharp squared-angle eigengap scale, can produce maximal vector error at arbitrarily small trial-space error, and accompanies a strictly better eigenvalue on the very same examples. The threshold and tie are useful for interpreting ordered eigenpairs near clustered spectra; no general or fixed-gap instability is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
