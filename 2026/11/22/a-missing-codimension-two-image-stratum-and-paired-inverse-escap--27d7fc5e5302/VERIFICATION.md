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

For a,b,c>0, the square first coordinate rules out X<0; at X=0 it forces y=0 and precisely an affine line if Y=0, otherwise nothing. At X>0 the two signs of y are disjoint. Setting x=1-Z/c and w=W-y leaves exactly Y=b y(1-w^2/2)(1-z). The nonzero coefficient gives one point; a zero coefficient gives a line for Y=0 and no point otherwise. At r=sqrt(X/a)>0 simultaneous vanishing means (W-r)^2=(W+r)^2=2; subtraction forces W=0 and then X=2a. Thus only the specified stratum is missing inside X>0, and X>0 off the stratum is dense in X>=0. Expanding the determinant using the first and third rows gives abc y^2(2-w^2); its critical locus is y=0 or w=+/-sqrt(2), with the listed images, all in Y=0. Along X=2a, fixed nonzero Y and fixed Z, the two denominators are b W(2-sigma W/sqrt(2)), giving regular inverse points and lim W z_sigma=-Y/(2b) on both branches. The conclusion about a common pole is restricted to that specified approach, not claimed along arbitrary paths. The frozen symbolic checker was inspected, not executed; exhaustive scalar elimination, not numerical tests, establishes the classification.

## originality

PASS

The 2023 paper supplies the exact map and computes fixed-point linearization, rather than answering the global target-space inverse problem. The structural result is the simultaneous loss of both finite sheets on a noncritical interior stratum, with a common signed inverse residue on a specified slice; neither the map definition, a local Jacobian nor a positive forward-rate theorem classifies this geometry.

## value

PASS

The natural inverse question for this recurrent map is where a real target has no, finite, or positive-dimensional antecedents. The classification includes all targets and parameters in scope, locates an interior hole not due to finite criticality, and gives quantitative loss of both regular antecedents at infinity on a natural fixed-X slice. This distinguishes nonproper backward state loss from finite merging and supplies an exact domain and branching description for backward reconstruction. Elementary proof length does not remove that structural distinction; the result makes no claims about practical inversion, bounded physical domains or forward chaos.

The dated certificate retains the supplied scientific assessment, sources and limitations.
