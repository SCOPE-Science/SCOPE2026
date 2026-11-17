---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

On chart with columns 2,4 independent, use invertible row operations to matrix N=[[-a,1,-(1+c),0],[-b,0,-d,1],[y,0,-x,0]]. Its signed maximal minors (x, a x+(1+c)y, y, b x+d y) satisfy Np=0 and Segre equation p0p3-p1p2=b x²+(d-a)xy-(1+c)y² exactly. In char2 derivatives with respect to a,b,c,d,x,y give xy,x²,y²,xy,(d-a)y,(d-a)x; as H belongs to (x²,xy,y²), singular Jacobian ideal is J=(x²,xy,y²,(d-a)x,(d-a)y). Localizing t=d-a invertible yields reduced (x,y). Holding tangency base t=0 gives three-dimensional Artin quotient k[x,y]/(x,y)², while odd characteristic tangent quadratic with nonzero square coefficient gives k[x]/(x²), length 2. At generic char2 t=0 with b and 1+c units, contact square root (1+c)/b is not a rational square since b has odd discrete valuation, so a purely inseparable degree-two field extension. Independent SymPy determinant/partial derivative rederivation matches identity; algebra/valuation, not finite random tests, covers the chart.

## originality

PASS

Best-of-knowledge PASS specifically for the characteristic-two full Jacobian ideal, tangent Artin-length jump and radicial generic contact field. The degree-six boundary-format polynomial and reduced singular-locus framework are prior work, not novelty.

## value

PASS

The exact nonreduced local fiber and inseparable incidence at a natural tangency divisor refine reduced hyperdeterminant singularity classification in bad characteristic. The length jump 2 to 3 is a structural geometric boundary likely useful in modular tensor-degeneracy and singular-scheme computations, not an arbitrary isolated numerical check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
