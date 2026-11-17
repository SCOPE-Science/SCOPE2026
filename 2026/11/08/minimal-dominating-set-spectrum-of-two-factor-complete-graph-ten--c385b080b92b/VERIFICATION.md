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

For K_m x K_n with categorical adjacency iff both coordinates differ, a selected set S fails to dominate iff an unselected cell (i,j) meets every selected edge through row i or column j. A three-edge incidence matching already dominates, giving inclusion-minimal size-three matchings. If matching number<=2, Koenig gives a cover by <=2 row/column vertices. Case analysis gives complete lines, three-corner rectangles for m,n>=3, and exact two-row/two-column two-plus-two disjoint-column four-cell types. Each is inclusion-minimal by a missing private cell after deletion, and the families are disjoint. Their labeled counts give n z^m +m z^n+ 4I_(m,n>=3)bin(m,2)bin(n,2) z^3 +6bin(m,3)bin(n,3)z^3 +6(bin(m,2)bin(n,4)+bin(n,2)bin(m,4))z^4, including K2xK2 disconnected boundary. Exact independent enumeration for K2x2,K2x3,K3x3,K3x4 agrees with all coefficients; infinite result follows from matchings and cover proof.

## originality

PASS

PASS (best-of-knowledge): Defant–Iyer 2017 prove ordinary domination extrema/upper bounds for categorical complete products; Burcroff–O’Brien 2021 concerns the polynomial counting ALL ordinary dominating sets, while the earlier exact October 26 published same-product theorem classifies TOTAL domination (open neighborhoods) and has different families and counts. Neither provides this complete five-family ordinary inclusion-minimal polynomial. Residual risk: another name such as unitary Cayley graph or a stronger all-set formula may hide an equivalent exact minimal classification.

## value

PASS

PASS: the exact all-parameter labeled minimal-domination polynomial, five minimal family structure and unbounded missing-size interval {3,4,n} for K3xKn n>=6 are natural complete combinatorial invariants relevant to domination reconfiguration and extremal structure. The known min/upper values alone and ordinary all-domination polynomial do not mechanically enumerate the minimal family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
