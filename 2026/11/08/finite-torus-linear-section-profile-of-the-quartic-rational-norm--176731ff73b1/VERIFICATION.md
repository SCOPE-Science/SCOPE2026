---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For q>=5, every torus evaluation section is A(x)+yB(x), deg A<=3, deg B<=1; evaluation is injective since q-1>3. One equation has at most 3t zeros. For two independent equations, gcd/factor classification of vertical factors and elimination A1B2-A2B1 (degree<=4) yields <=2t; witnesses are two vertical fibers. For three-dimensional systems, a common vertical x-r factor reduces to a three-dimensional subspace of span{1,x,x^2,y}, whose annihilator picks at most one off-fiber point; otherwise generic coprime pair implies <=4<=t+1. Four-dimensional common-zero points are on a projective line; three distinct torus points on a line necessarily share x, giving <=t. Five/six forms give <=1/0. Independently exhaustively checked all 2^16 torus point subsets at q=5 using exact modular Gaussian elimination: common-zero maxima (12,8,5,4,1,0). This is finite corroboration only.

## originality

PASS

The complete six-position torus section/Hamming weight hierarchy for the trapezoidal S(1,3) six-monomial support is different from earlier cubic scroll S(1,2), ordinary affine Cartesian full-degree Reed–Muller codes and projective-scroll evaluations including boundary. Inspected primary weighted Reed–Muller and affine Cartesian sources provide constructions and bounds/single distances but not this six-position hierarchy. Best-of-knowledge PASS with potential obscure geometry/coding tables as residual risk.

## value

PASS

The six generalized Hamming weights are natural exact invariants of a specific six-dimensional rational normal scroll toric evaluation code. They govern all subcode support thresholds, not just minimum distance; the third extremal t+1 fiber-plus-point phenomenon is a useful geometric structural boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
