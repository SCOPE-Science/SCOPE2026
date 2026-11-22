---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The frozen RESULT.md defines the open two-leg uniform-adjacency graph P2 square Pn for every n>=2, H_gamma=A-i gamma |a,1><a,1| with gamma>0, and input |b,n>. Product path/rung eigenvalues are 2cos(pi k/(n+1)) +/-1; each simple level is visible at the sink. The cyclotomic trace lemma correctly restricts the cross-band difference 2 to path eigenvalues +/-1 (indices (n+1)/3 and 2(n+1)/3), only if 3 divides n+1, giving exactly one zero-energy dark direction. The sink-cancellation vector (phi_{+,2t}-phi_{-,t})/sqrt2 with t=(n+1)/3 has source amplitude -c(1+(-1)^t)/sqrt2, c=sqrt3/(2sqrt(n+1)), giving 3/[2(n+1)] for n=5 mod 6 and zero otherwise. Bright complement has strictly negative imaginary spectrum by the dissipative quadratic form; finite Jordan blocks decay and the long-time norm is the dark projection, independent of gamma. Independently written check performed 59 exact Chebyshev-polynomial gcd tests for n=2..60 and 39 direct symmetric-adjacency projector tests for n=2..40 (98 passing checks). A first test-script comparison raised a spurious SymPy Poly domain-equality assertion despite identical expressions; corrected by comparing expressions, not by changing any result. Finite checks corroborate rather than prove the universal assertion. No contradiction found, including n=2, n=5, n=8, n=11, n=17 boundary examples.

## originality

FAIL

FAIL: October 26 published prior same-model all-vertex ladder theorem gives the exact normalized dark eigenmode and final survival at each (x,y). At diagonally opposite x=n, row 2, its sitewise modular table reduces exactly to the assigned November 8 claim. Both use the unweighted path-times-rung adjacency Hamiltonian and a single lossy corner for all positive sink rates; factor 1/2 in the earlier definition of gamma has no mathematical effect. The prior theorem also proves the same energy-zero degeneracy and all-length classification. Four structured comparisons and full earlier proof checked. No novelty remains in a mere source-position restriction.

## value

FAIL

FAIL as a distinct research result: exact eventual corner survival is a natural physically motivated invariant, but this submitted final claim only evaluates at a single already-covered source site in an earlier fully tabulated all-site theorem. It introduces no new model, invariant, sharp limit, motivated boundary, or non-implied lemma. A separate proof/checker is useful as corroboration, not a scientifically new substantive contribution to warrant independent acceptance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
