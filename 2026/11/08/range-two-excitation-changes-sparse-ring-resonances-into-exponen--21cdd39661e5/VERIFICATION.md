---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Every vertex of a 3-periodic GHM trajectory is either always zero or advances through 0,1,2 once; a connected graph cannot mix both types because a cycling neighbor would excite a stationary zero. Hence nonfixed 3-periodic colorings are exactly those where every i has a successor-colored neighbor at offsets ±1,±2. The 81-state length-four-word transfer T tests the central vertex, and closed walks of length n biject to labelled period-three states for n>=5. An independently built exact integer 81×81 matrix has characteristic polynomial X^69(X+1)(X³−3X²+2X−2)(X⁴+X³+2X²+3X+4)^2; Newton/trace identity yields the all-n formula. Independent direct GHM simulations gave P5..P8=150,270,588,1548. The cubic has unique root rho≈2.52138 and other roots modulus sqrt(2/rho)<1; scaled Eneström–Kakeya bounds quartic roots by 2, so P_n=rho^n+O(2^n). For nearest-neighbor cycles every directed successor edge must be used, forcing cyclic ±1 color increments and six states iff 3|n. Exact polynomial matrix identity is a finite certificate proving all n jointly with the transfer bijection, not an extrapolated enumeration.

## originality

PASS

Published November 8 open range-two chain result has the same dominant cubic f but different open boundary and generating function; it cannot directly yield periodic closure, extra −1 term, or doubled quartic g spectrum. Another November 8 squared-cycle contact-threshold theorem counts theta=2 (six/zero) and only gives theta=1 lower bound 3·2^(n/3); its finite sample theta=1 counts agree for n<=11 but do not establish the all-n exact theta=1 transfer factorization. The arbitrary-graph activity theorem does not give period-three population numbers. Thus the exact periodic-boundary family and spectral correction survive, with historic original-paper access limitations stated.

## value

PASS

Changing nearest-neighbor to range-two on a labelled cycle is a standard local-interaction perturbation of excitable media. The exact all-length census and exponential entropy rho quantify a real structural transition from bounded arithmetic resonance to extensive primitive-period-three states. The precise quartic spectral correction distinguishes periodic from open boundary, and is a useful finite-dynamics invariant, not a fitted finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
