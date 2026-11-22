---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Reflection-fixed finite subsets of the unit circle consist uniquely of endpoint flags a,b in {0,1} plus j interior conjugate pairs, a+b+2j<=k. The closed ordered interior-point simplex gives each open CW cell E_ab^j; its j+1 alternating boundary faces are correct, including collisions and endpoint absorptions. Unit-coefficient algebraic pairs E10^(j-1)<->E00^j and E11^(j-1)<->E01^j yield a unique high-dimensional homology generator plus a connectedness base, with the predicted degree floor((k-1)/2). The explicit 3- and 4-stage loops and the degree-one 2-cell in Y5 kill pi1; subsequent new cells are >=2 dimensional, so Hurewicz and homological Whitehead upgrade to homotopy spheres. For odd k=2q+1, the new E00^(q+1) cell bounds a primitive old class; for even-to-odd, degrees differ, so every reduced persistence map is zero. Independently built exact cellular boundary matrices for all k<=16 satisfied boundary-square-zero and had the predicted integral-free ranks (rank calculations plus unit pivots); finite checks do not establish the all-k homotopy assertion.

## originality

PASS

Tuffley proves ambient exp_k(S1) sphere homotopy and nonzero degree-two map for odd-to-even ambient inclusions. These are different spaces and maps from conjugation-fixed subspaces; the new explicit endpoint/paired-orbit CW and primitive-boundary persistence test is not a corollary of Tuffley’s ambient result. Mostovoy supplies a special k=3 lattice model, not the all-k reflection-fixed filtered classification. No direct prior identity found in bounded searches.

## value

PASS

The result gives both all-stage integral homotopy types and exact zero persistence for a canonical involution of a classical configuration-space filtration, sharply contrasting the already known ambient map multiplication by two. This is meaningful equivariant/persistent topological information rather than a routine zero computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
