---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Fourfold pedal theorem gives sigma=∏_sides dist(P,line)/∏_vertices |P-v|, strictly positive over open rectangle. For a>=b>0, one long-side denominator factor increases with y² and the other satisfies R_h(y)^2-(1-y²/b²)^2 R_h(0)^2=b^4 Ht[2H+6-(H+2)t]>0 for y≠0, yielding strict axial reduction. There f(s)=B(A-s)/[s²+2(B-A)s+(A+B)²], s=x², derivative sign (s-A)²-B(4A+B). The optimum shifts from s=0 to s=A-sqrt[B(4A+B)] exactly when (a/b)^2>2+sqrt(5). At equality s=0 is unique. Explicit pedal feet and the symmetry of intermediate polygons ensure axial maximizing points are admissible, so the global upper bound is attained. Independently reproduced the polynomial y-elimination and f derivative identities by exact symbolic algebra; source finite checker inspected, not assumed sufficient as infinite proof.

## originality

PASS

Zwierzyński's general four-step similarity and product-of-distances formula are prior inputs. The interior rectangular global optimization, unique equality set and sharp one-to-two optimizer aspect threshold are not present in the inspected general theorem or first-step quadrilateral literature, and are not obtained by its incircle-center corollary because a nonsquare rectangle is not tangential.

## value

PASS

The aspect threshold sqrt(2+sqrt5) determines a genuine symmetry-breaking geometry of an iterated pedal map, with exact optimal points and scale. This natural shape family tests where a widely applicable similarity formula has nontrivial optimized geometry; far more than simply reprinting the formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
