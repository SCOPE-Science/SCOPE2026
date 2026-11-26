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

Re-derived the direction-fixed smallest disk with translated center. In an edge-midpoint plane the projected vertices are (±a,±1) and (d,0), d=h√(1−a²). Reflection and uniqueness give center (t,0); a negative t cannot improve on zero. The active balance (a+t)²+1=(d−t)² has its unique optimum between 0 and d if d²>1+a², giving (D+1/D)/2 for D=d+a; otherwise t=0 and the radius is √(1+a²). The inactive branch increases with a, whereas the active branch is a strictly increasing function of the strictly concave D; only a=0 and a₀²=(h²−1)/(h²+1) can minimize for h>1. Verified (h²+1)³−8h⁴=(h²−1)(h⁴−4h²−1), the sole crossing for h>1, and both unequal derivatives at H. At a₀, D′=1−√((h²−1)/2), so the second strict minimum is present for h>√2, not at equality; √2 is its onset threshold. The fixed diagonal chord forces R≥√2 in diagonal planes, strictly exceeding the globally chosen radius. For clarity, the explicit local landscape in the proof is for the edge-midpoint tilt branch. Independently, a diagonal-plane projection gives (0,±√2), (±√2a,0), (d,0): its radius is √2 if d≤√2, (d+2/d)/2 if d>√2 and d√2a≤2, or (d+√2a)/2 if d√2a≥2 and d>√2. This decreases on the active parts (the last region implies h a/√(1−a²)>√2) and becomes flat, introducing no other strict local minima in the permitted union. Horizontal apex contact starts at h=1 (when h<1 it is interior); both claimed coexistence configurations have all five vertices in contact. Checker was read, not executed; the independent exact derivation establishes the continuum result without the grid. Unrestricted axes are excluded.

## originality

PASS

Best-of-knowledge pass for the explicit all-height constrained profile, not for the minimum enclosing disk reduction, the definition of an outer two-radius, or a general cylinder-fitting method.

## value

PASS

The natural five-vertex fitting family has two distinct transition heights, coexistence of distinct exact axis families, and a genuine radius derivative jump, not merely a fixed-direction circle calculation. The exact constrained law is a useful minimax benchmark with a geometric, non-ad-hoc orientation constraint. This value does not depend on an unrestricted result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
