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

The implicit relation x_n=h_j(x_(n+1)) gives H0=h0∘h1 and H1=h1∘h0, not the forward composition. Completed squares yield H0=[2(z+b/4)²-(b²-4a)/8]²-a²/4 and H1=2[(z+a/2)²-(a²-b)/4]²-b²/8. A positive inner negative offset is equivalent to two minima separated by central maximum: regular inverse valence four precisely at b²>4a or a²>b, respectively, and windows (-a²/4,-a²/4+(b²-4a)²/64), (-b²/8,-b²/8+(a²-b)²/8). Nonpositive offsets yield at most two regular real roots. At a=-ε,b=ε,0<ε<1/16, phase0 H0(z)=0 splits into four distinct roots 0,-ε/2,(-ε±sqrt(ε²+8ε))/4; phase1 H1(z)=0 has only 0,ε because remaining quadratic discriminant ε²-2ε<0. Along the stationary zero orbit derivatives are 1/a and 1/b; cyclic products both -ε^-2. At a=b=0 inverse branches grow as x^(1/4), exponent optimal. Independently sympy-expanded H0,H1 and factorizations and exact rational witness; global universal root-count reasoning analytical.

## originality

PASS

Best-of-knowledge phase-resolved global inverse valence counterexample, not a new quartic root theorem or regular Floquet cyclic invariance; primary implicit-system literature treats local singular markers under different maps.

## value

PASS

A motivated exact minimal counterexample to equating cyclic Floquet spectra with global inverse-sheet branching in implicit dynamics, including independent sharp phase caustics, explicit four-branch windows and a regular shared zero orbit; more than a bare quartic exercise because it identifies precise failure of a natural inference.

The dated certificate retains the supplied scientific assessment, sources and limitations.
