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

Independently write g=H_c x=(z,r+d,r−d), k=1−2c², D=3+2c−3c². The input energy is (z²+4czr+2r²)/k+2d². The gain of (i,j) is g_i²+(g_j−H_ji g_i)², including repeats. The average gains for uniform leaf-to-center (B) and for opposite leaves (C) are respectively r²+(z+cr)²+(1+c²)d² and 2(r²+d²). At (z,r,d)=(1−c,1,0), both families give 2, center-to-leaf gives 2−c³(2−c)<2, and repeats give less. The witness bounds every law by 2k/D. At p=2(1+c)/D the mixture pB+(1−p)C minus (2k/D) times input energy is exactly (2c/D)[(z−(1−c)r)²+(1+c)²d²], certifying attainment when p≤1, i.e. c≤1/√3. For B the symmetric generalized determinant has factor 2t²+(3c²−3)t+k. The contrast eigenvalue is (1+c²)/2; the symmetric witness z=−c,r=1 gives k/(2−3c²), strictly less. The symmetric Rayleigh quotient at r=1 has derivative with sign cz²+(1−c²)z−2c³, so its positive root z_c is the smaller symmetric eigenmode. It satisfies 0<z_c<1, and z_c≥1−c exactly when c≥1/√3 (substitution gives 1−3c²). At this root the leaf-to-center gain beats the center-to-leaf gain by c²(1−z_c²) and beats the opposite-leaf gain strictly if c>1/√3; repeats also lose. This certifies optimality and the strong support requirement, and at equality the formulas meet. In the weak regime an edge-only optimizer would have to use B pairs by tightness of the first witness. Leaf symmetrization cannot hurt, but uniform B has strictly smaller gain in its worst mode z_c<1−c; hence nonedges are mandatory. The c=1/4 fractions and B-only radical check exactly. Frozen verification files were inspected, not run; the numerical loop checks the candidate spectrum and symmetry of the nine matrices, not global optimality. The positive-definiteness wording is understood in the stipulated positive-c domain (without that stipulation the condition is |c|<1/√2).

## originality

PASS

The closest Resultary results use the exact same ordered update type on regular graphs, the same star with a simultaneous block solve, a rank-two planar ordered-projection problem, or iid draws at a finite horizon. Their hypotheses do not give the sharp three-dimensional path minimax threshold with an arbitrary ordered joint law. General sampling or SDP tools formulate the problem but do not already resolve it. Historical priority remains qualified.

## value

PASS

The smallest connected nonregular graph gives a natural test of whether the regular-graph edge rule generalizes. The answer is no for an entire coupling interval, and the proof produces exact optimal values and an implementable policy on both sides. This is a structural result about a fixed two-solve minimax budget, not evidence of an asymptotic or runtime advantage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
